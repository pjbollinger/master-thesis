from . import MultiplierCell
from . import MultiplierCellHalfadder
from . import gates

class SemiPrimeFactorization:
    def __init__(self, semiprime=6):
        self.output = "{0:b}".format(semiprime)
        if len(self.output) % 2 == 1:
            self.output = '0' + self.output
        # self.output = ('0' * ((len(self.output)-1)*2-len(self.output))) + self.output
        self.output = self.output[::-1]
        self.number_of_multiplier_cells_in_row = len(self.output) // 2
        self.input_a = ["Z" for i in range(self.number_of_multiplier_cells_in_row)]
        self.input_b = ["Z" for i in range(self.number_of_multiplier_cells_in_row)]
        self.carry = [["Z" for j in range(self.number_of_multiplier_cells_in_row)] for i in range(self.number_of_multiplier_cells_in_row)]
        self.sum = [["Z" for j in range(self.number_of_multiplier_cells_in_row)] for i in range(self.number_of_multiplier_cells_in_row)]
    
    def __str__(self):
        return(
            "Output: " + self.output[::-1] + "\n" +
            "Input A: " + "".join(self.input_a)[::-1] + "\n" +
            "Input B: " + "".join(self.input_b)[::-1] + "\n" +
            "Sum: " + str(self.sum) + "\n" +
            "Carry: " + str(self.carry)
        )
    
    def dump(self):
        return({
            "input_a": self.input_a,
            "input_b": self.input_b,
            "sum": self.sum,
            "carry": self.carry,
            "output": self.output
        })

    def solve(self, change='0'):
        # Default "ZZZZZZZ"
        #          ||||||└ 6 output Carry Out
        #          |||||└- 5 output Sum Out
        #          ||||└-- 4 signal AND_Z to FA_A
        #          |||└--- 3 input Carry In
        #          ||└---- 2 input Sum In
        #          |└----- 1 inout Y
        #          └------ 0 inout X
        error = '0'
        for i in range(len(self.input_b)):
            for j in range(len(self.input_a)):
                if (i == 0 and j == 0):
                    # Top Right Corner
                    # print("Top Right Corner", "Row:", str(i), "Column:", str(j))
                    # print([self.input_a[j], self.input_b[i], '0', '0', self.output[0], self.carry[i][j]])
                    result = MultiplierCell.MultiplierCell([self.input_a[j], self.input_b[i], '0', '0', self.output[i+j], self.carry[i][j]]).solve()
                    if (result["error"] == '0' and self.output[i+j] == result["bits"][4]):
                        if (result["change"] == '1'):
                            self.input_a[j] = result["bits"][0]
                            self.input_b[i] = result["bits"][1]
                            self.carry[i][j] = result["bits"][5]
                            change = '1'
                    else:
                        error = '1'
                    self.sum[i][j] = None
                elif (i > 0 and j == 0):
                    # Firt Column
                    # print("First Column", "Row:", str(i), "Column:", str(j))
                    # print([self.input_a[j], self.input_b[i], self.sum[i-1][j+1], '0', self.output[i], self.carry[i][j]])
                    result = MultiplierCell.MultiplierCell([self.input_a[j], self.input_b[i], self.sum[i-1][j+1], '0', self.output[i+j], self.carry[i][j]]).solve()
                    if (result["error"] == '0' and self.output[i+j] == result["bits"][4]):
                        if (result["change"] == '1'):
                            self.input_a[j] = result["bits"][0]
                            self.input_b[i] = result["bits"][1]
                            self.sum[i-1][j+1] = result["bits"][2]
                            self.carry[i][j] = result["bits"][5]
                            change = '1'
                    else:
                        error = '1'
                    self.sum[i][j] = None
                elif (i == 0 and j > 0):
                    # Top Row
                    # print("Top Row", "Row:", str(i), "Column:", str(j))
                    # print([self.input_a[j], self.input_b[i], '0', '0', self.sum[i][j], self.carry[i][j]])
                    result = MultiplierCell.MultiplierCell([self.input_a[j], self.input_b[i], '0', self.carry[i][j-1], self.sum[i][j], self.carry[i][j]]).solve()
                    if (result["error"] == '0'):
                        if (result["change"] == '1'):
                            self.input_a[j] = result["bits"][0]
                            self.input_b[i] = result["bits"][1]
                            self.carry[i][j-1] = result["bits"][3]
                            self.sum[i][j] = result["bits"][4]
                            self.carry[i][j] = result["bits"][5]
                            change = '1'
                    else:
                        error = '1'
                elif (i == len(self.input_b)-1 and j == len(self.input_a)-1):
                    # Bottom Left Corner
                    # print("Bottom Left Corner", "Row:", str(i), "Column:", str(j))
                    # print([self.input_a[j], self.input_b[i], '0', self.carry[i-1][j], self.output[i+j], self.output[i+j+1]])
                    result = MultiplierCell.MultiplierCell([self.input_a[j], self.input_b[i], self.carry[i-1][j], self.carry[i][j-1], self.output[i+j], self.output[i+j+1]]).solve()
                    if (result["error"] == '0' and self.output[i+j] == result["bits"][4] and self.output[i+j+1] == result["bits"][5]):
                        if (result["change"] == '1'):
                            self.input_a[j] = result["bits"][0]
                            self.input_b[i] = result["bits"][1]
                            self.carry[i-1][j] = result["bits"][2]
                            self.carry[i][j-1] = result["bits"][3]
                            change = '1'
                    else:
                        error = '1'
                    self.sum[i][j] = None
                    self.carry[i][j] = None
                elif (i == len(self.input_a)-1):
                    # Bottom Row
                    # print("Bottom Row", "Row:", str(i), "Column:", str(j))
                    # print([self.input_a[j], self.input_b[i], self.sum[i-1][j+1], self.carry[i-1][j], self.output[i+j], self.carry[i][j]])
                    result = MultiplierCell.MultiplierCell([self.input_a[j], self.input_b[i], self.sum[i-1][j+1], self.carry[i][j-1], self.output[i+j], self.carry[i][j]]).solve()
                    if (result["error"] == '0' and self.output[i+j] == result["bits"][4]):
                        if (result["change"] == '1'):
                            self.input_a[j] = result["bits"][0]
                            self.input_b[i] = result["bits"][1]
                            self.sum[i-1][j+1] = result["bits"][2]
                            self.carry[i][j-1] = result["bits"][3]
                            self.carry[i][j] = result["bits"][5]
                            change = '1'
                    else:
                        error = '1'
                    self.sum[i][j] = None
                elif (j == len(self.input_b)-1):
                    # Last column
                    # print("Last Column", "Row:", str(i), "Column:", str(j))
                    # print([self.input_a[j], self.input_b[i], '0', self.carry[i-1][j], self.sum[i][j], self.carry[i][j]])
                    result = MultiplierCell.MultiplierCell([self.input_a[j], self.input_b[i], self.carry[i-1][j], self.carry[i][j-1], self.sum[i][j], self.carry[i][j]]).solve()
                    if (result["error"] == '0'):
                        if (result["change"] == '1'):
                            self.input_a[j] = result["bits"][0]
                            self.input_b[i] = result["bits"][1]
                            self.carry[i-1][j] = result["bits"][2]
                            self.carry[i][j-1] = result["bits"][3]
                            self.sum[i][j] = result["bits"][4]
                            self.carry[i][j] = result["bits"][5]
                            change = '1'
                    else:
                        error = '1'
                else:
                    # Interior
                    # print("Interior", "Row:", str(i), "Column:", str(j))
                    # print([self.input_a[j], self.input_b[i], self.sum[i-1][j+1], self.carry[i-1][j], self.sum[i][j], self.carry[i][j]])
                    result = MultiplierCell.MultiplierCell([self.input_a[j], self.input_b[i], self.sum[i-1][j+1], self.carry[i][j-1], self.sum[i][j], self.carry[i][j]]).solve()
                    if (result["error"] == '0'):
                        if (result["change"] == '1'):
                            self.input_a[j] = result["bits"][0]
                            self.input_b[i] = result["bits"][1]
                            self.sum[i-1][j+1] = result["bits"][2]
                            self.carry[i][j-1] = result["bits"][3]
                            self.sum[i][j] = result["bits"][4]
                            self.carry[i][j] = result["bits"][5]
                            change = '1'
                    else:
                        error = '1'
                if error == '1':
                    break
            if error == '1':
                break
        if error == '1':
            print(error)
            return({"input_a": ''.join(self.input_a)[::-1], "input_b": ''.join(self.input_b)[::-1], "error": error})
        if change == '1':
            return(self.solve())
        return({"input_a": ''.join(self.input_a)[::-1], "input_b": ''.join(self.input_b)[::-1], "error": error})

    def information_count(self):
        total_count = 0
        resolved_count = total_count
        for row in self.carry:
            for entry in row:
                if (entry is not None):
                    total_count = total_count + 1
                if (entry == '1') or (entry == '0'):
                    resolved_count = resolved_count + 1
        for row in self.sum:
            for entry in row:
                if (entry is not None):
                    total_count = total_count + 1
                if (entry == '1') or (entry == '0'):
                    resolved_count = resolved_count + 1
        for entry in self.input_a:
            if (entry is not None):
                total_count = total_count + 1
            if (entry == '1') or (entry == '0'):
                resolved_count = resolved_count + 1
        for entry in self.input_b:
            if (entry is not None):
                total_count = total_count + 1
            if (entry == '1') or (entry == '0'):
                resolved_count = resolved_count + 1
        return({"total_count": total_count, "resolved_count": resolved_count})

    def solve_optimized(self, change='0'):
        # Default "ZZZZZZZ"
        #          ||||||└ 6 output Carry Out
        #          |||||└- 5 output Sum Out
        #          ||||└-- 4 signal AND_Z to FA_A
        #          |||└--- 3 input Carry In
        #          ||└---- 2 input Sum In
        #          |└----- 1 inout Y
        #          └------ 0 inout X
        error = '0'
        for i in range(len(self.input_b)):
            for j in range(len(self.input_a)):
                if (i == 0 and j == 0):
                    # Top Right Corner
                    # print("Top Right Corner", "Row:", str(i), "Column:", str(j))
                    # print([self.input_a[j], self.input_b[i], '0', '0', self.output[0], self.carry[i][j]])
                    result = gates.and_gate(self.input_a[j], self.input_b[i], self.output[i+j])
                    if (result["error"] == '0' and self.output[i+j] == result["gates"][2]):
                        if (result["change"] == '1'):
                            self.input_a[j] = result["gates"][0]
                            self.input_b[i] = result["gates"][1]
                            change = '1'
                    else:
                        error = '1'
                    self.sum[i][j] = None
                    self.carry[i][j] = None
                elif (i > 0 and j == 0):
                    # Firt Column
                    # print("First Column", "Row:", str(i), "Column:", str(j))
                    # print([self.input_a[j], self.input_b[i], self.sum[i-1][j+1], '0', self.output[i], self.carry[i][j]])
                    result = MultiplierCellHalfadder.MultiplierCellHalfadder([self.input_a[j], self.input_b[i], self.sum[i-1][j+1], self.output[i+j], self.carry[i][j]]).solve()
                    if (result["error"] == '0' and self.output[i+j] == result["bits"][3]):
                        if (result["change"] == '1'):
                            self.input_a[j] = result["bits"][0]
                            self.input_b[i] = result["bits"][1]
                            self.sum[i-1][j+1] = result["bits"][2]
                            self.carry[i][j] = result["bits"][4]
                            change = '1'
                    else:
                        error = '1'
                    self.sum[i][j] = None
                elif (i == 0 and j == len(self.input_a)-1):
                    # Top Left column
                    # print("Top Row", "Row:", str(i), "Column:", str(j))
                    # print([self.input_a[j], self.input_b[i], '0', '0', self.sum[i][j], self.carry[i][j]])
                    result = gates.and_gate(self.input_a[j], self.input_b[i], self.sum[i][j])
                    if (result["error"] == '0'):
                        if (result["change"] == '1'):
                            self.input_a[j] = result["gates"][0]
                            self.input_b[i] = result["gates"][1]
                            self.sum[i][j] = result["gates"][2]
                            change = '1'
                    else:
                        error = '1'
                    self.carry[i][j] = '0'
                elif (i == 0 and j > 0):
                    # Top Row
                    # print("Top Row", "Row:", str(i), "Column:", str(j))
                    # print([self.input_a[j], self.input_b[i], '0', '0', self.sum[i][j], self.carry[i][j]])
                    result = gates.and_gate(self.input_a[j], self.input_b[i], self.sum[i][j])
                    if (result["error"] == '0'):
                        if (result["change"] == '1'):
                            self.input_a[j] = result["gates"][0]
                            self.input_b[i] = result["gates"][1]
                            self.sum[i][j] = result["gates"][2]
                            change = '1'
                    else:
                        error = '1'
                    self.carry[i][j] = None
                elif (i == len(self.input_b)-1 and j == len(self.input_a)-1):
                    # Bottom Left Corner
                    # print("Bottom Left Corner", "Row:", str(i), "Column:", str(j))
                    # print([self.input_a[j], self.input_b[i], '0', self.carry[i-1][j], self.output[i+j], self.output[i+j+1]])
                    result = MultiplierCell.MultiplierCell([self.input_a[j], self.input_b[i], self.carry[i-1][j], self.carry[i][j-1], self.output[i+j], self.output[i+j+1]]).solve()
                    if (result["error"] == '0' and self.output[i+j] == result["bits"][4] and self.output[i+j+1] == result["bits"][5]):
                        if (result["change"] == '1'):
                            self.input_a[j] = result["bits"][0]
                            self.input_b[i] = result["bits"][1]
                            self.carry[i-1][j] = result["bits"][2]
                            self.carry[i][j-1] = result["bits"][3]
                            change = '1'
                    else:
                        error = '1'
                    self.sum[i][j] = None
                    self.carry[i][j] = None
                elif (i == len(self.input_a)-1):
                    # Bottom Row
                    # print("Bottom Row", "Row:", str(i), "Column:", str(j))
                    # print([self.input_a[j], self.input_b[i], self.sum[i-1][j+1], self.carry[i-1][j], self.output[i+j], self.carry[i][j]])
                    result = MultiplierCell.MultiplierCell([self.input_a[j], self.input_b[i], self.sum[i-1][j+1], self.carry[i][j-1], self.output[i+j], self.carry[i][j]]).solve()
                    if (result["error"] == '0' and self.output[i+j] == result["bits"][4]):
                        if (result["change"] == '1'):
                            self.input_a[j] = result["bits"][0]
                            self.input_b[i] = result["bits"][1]
                            self.sum[i-1][j+1] = result["bits"][2]
                            self.carry[i][j-1] = result["bits"][3]
                            self.carry[i][j] = result["bits"][5]
                            change = '1'
                    else:
                        error = '1'
                    self.sum[i][j] = None
                elif (j == len(self.input_b)-1):
                    # Last column
                    # print("Last Column", "Row:", str(i), "Column:", str(j))
                    # print([self.input_a[j], self.input_b[i], '0', self.carry[i-1][j], self.sum[i][j], self.carry[i][j]])
                    result = MultiplierCell.MultiplierCell([self.input_a[j], self.input_b[i], self.carry[i-1][j], self.carry[i][j-1], self.sum[i][j], self.carry[i][j]]).solve()
                    if (result["error"] == '0'):
                        if (result["change"] == '1'):
                            self.input_a[j] = result["bits"][0]
                            self.input_b[i] = result["bits"][1]
                            self.carry[i-1][j] = result["bits"][2]
                            self.carry[i][j-1] = result["bits"][3]
                            self.sum[i][j] = result["bits"][4]
                            self.carry[i][j] = result["bits"][5]
                            change = '1'
                    else:
                        error = '1'
                else:
                    # Interior
                    # print("Interior", "Row:", str(i), "Column:", str(j))
                    # print([self.input_a[j], self.input_b[i], self.sum[i-1][j+1], self.carry[i-1][j], self.sum[i][j], self.carry[i][j]])
                    result = MultiplierCell.MultiplierCell([self.input_a[j], self.input_b[i], self.sum[i-1][j+1], self.carry[i][j-1], self.sum[i][j], self.carry[i][j]]).solve()
                    if (result["error"] == '0'):
                        if (result["change"] == '1'):
                            self.input_a[j] = result["bits"][0]
                            self.input_b[i] = result["bits"][1]
                            self.sum[i-1][j+1] = result["bits"][2]
                            self.carry[i][j-1] = result["bits"][3]
                            self.sum[i][j] = result["bits"][4]
                            self.carry[i][j] = result["bits"][5]
                            change = '1'
                    else:
                        error = '1'
                if error == '1':
                    break
            if error == '1':
                break
        if error == '1':
            print(error)
            return({"input_a": ''.join(self.input_a)[::-1], "input_b": ''.join(self.input_b)[::-1], "error": error})
        if change == '1':
            return(self.solve_optimized())
        return({"input_a": ''.join(self.input_a)[::-1], "input_b": ''.join(self.input_b)[::-1], "error": error})
