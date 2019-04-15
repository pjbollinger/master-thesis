from . import MultiplierCell
from . import MultiplierCellHalfadder
from . import gates

class RippleCarryArrayMultiplier:
    def __init__(self, semiprime=6):
        self.output = "{0:b}".format(semiprime)
        if len(self.output) % 2 == 1:
            self.output = '0' + self.output
        self.output = self.output[::-1]
        self.number_of_multiplier_cells_in_row = len(self.output) // 2
        self.input_a = ["Z" for _ in range(self.number_of_multiplier_cells_in_row)]
        self.input_b = ["Z" for _ in range(self.number_of_multiplier_cells_in_row)]
        self.carry = [["Z" for _ in range(self.number_of_multiplier_cells_in_row)] for _ in range(self.number_of_multiplier_cells_in_row)]
        self.sum = [["Z" for _ in range(self.number_of_multiplier_cells_in_row)] for _ in range(self.number_of_multiplier_cells_in_row)]
    
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

    def information_count(self):
        total_count = 0
        resolved_count = 0

        count_carry = self._information_counter_two_dimensional(self.carry)
        resolved_count += count_carry["resolved_count"]
        total_count += count_carry["total_count"]

        count_sum = self._information_counter_two_dimensional(self.sum)
        resolved_count += count_sum["resolved_count"]
        total_count += count_sum["total_count"]

        count_input_a = self._information_counter_one_dimensional(self.input_a)
        resolved_count += count_input_a["resolved_count"]
        total_count += count_input_a["total_count"]

        count_input_b = self._information_counter_one_dimensional(self.input_b)
        resolved_count += count_input_b["resolved_count"]
        total_count += count_input_b["total_count"]

        return({"total_count": total_count, "resolved_count": resolved_count})
    
    def _information_counter_two_dimensional(self, two_dimensional_list):
        count_knowns = sum(row.count('1') for row in two_dimensional_list) + sum(row.count('0') for row in two_dimensional_list)
        return {
            "resolved_count": count_knowns,
            "total_count": count_knowns + sum(row.count('Z') for row in two_dimensional_list)
        }

    def _information_counter_one_dimensional(self, one_dimensional_list):
        count_knowns = one_dimensional_list.count('1') + one_dimensional_list.count('0')
        return {
            "resolved_count": count_knowns,
            "total_count": count_knowns + one_dimensional_list.count('Z')
        }

    def solve(self):
        raise NotImplementedError


class StandardRippleCarryArrayMultiplier(RippleCarryArrayMultiplier):
    def solve(self, change='0'):
        # Default "ZZZZZZZ"
        #          ||||||└ 6 output Carry Out
        #          |||||└- 5 output Sum Out
        #          ||||└-- 4 signal AND_Z to FA_A
        #          |||└--- 3 input Carry In
        #          ||└---- 2 input Sum In
        #          |└----- 1 inout Y
        #          └------ 0 inout X
        self.change = change
        self.error = '0'
        array_solve_dict = {
            ("i_eq_0", "j_eq_0"): self._solve_top_right_corner,
            ("i_gt_0", "j_eq_0"): self._solve_first_column,
            ("i_eq_last", "j_eq_0"): self._solve_first_column,
            ("i_eq_0", "j_gt_0"): self._solve_top_row,
            ("i_eq_0", "j_eq_last"): self._solve_top_row,
            ("i_eq_last", "j_eq_last"): self._solve_bottom_left_corner,
            ("i_eq_last", "j_gt_0"): self._solve_bottom_row,
            ("i_gt_0", "j_eq_last"): self._solve_last_column,
            ("i_gt_0", "j_gt_0"): self._solve_interior,
        }
        for i in range(len(self.input_b)):
            for j in range(len(self.input_a)):
                i_key = self._index_i_to_key(i)
                j_key = self._index_j_to_key(j)
                array_solve_dict.get((i_key, j_key), self._solve_interior)(i, j)
                if self.error == '1':
                    print(self.error)
                    return({"input_a": ''.join(self.input_a)[::-1], "input_b": ''.join(self.input_b)[::-1], "error": self.error})
        if self.change == '1':
            return(self.solve())
        return({"input_a": ''.join(self.input_a)[::-1], "input_b": ''.join(self.input_b)[::-1], "error": self.error})

    def _solve_top_right_corner(self, i, j):
        result = MultiplierCell.MultiplierCell([self.input_a[j], self.input_b[i], '0', '0', self.output[i+j], self.carry[i][j]]).solve()
        if (result["error"] == '0' and self.output[i+j] == result["bits"][4]):
            if (result["change"] == '1'):
                self.input_a[j] = result["bits"][0]
                self.input_b[i] = result["bits"][1]
                self.carry[i][j] = result["bits"][5]
                self.change = '1'
        else:
            self.error = '1'
        self.sum[i][j] = None

    def _solve_first_column(self, i, j):
        result = MultiplierCell.MultiplierCell([self.input_a[j], self.input_b[i], self.sum[i-1][j+1], '0', self.output[i+j], self.carry[i][j]]).solve()
        if (result["error"] == '0' and self.output[i+j] == result["bits"][4]):
            if (result["change"] == '1'):
                self.input_a[j] = result["bits"][0]
                self.input_b[i] = result["bits"][1]
                self.sum[i-1][j+1] = result["bits"][2]
                self.carry[i][j] = result["bits"][5]
                self.change = '1'
        else:
            self.error = '1'
        self.sum[i][j] = None

    def _solve_top_row(self, i, j):
        result = MultiplierCell.MultiplierCell([self.input_a[j], self.input_b[i], '0', self.carry[i][j-1], self.sum[i][j], self.carry[i][j]]).solve()
        if (result["error"] == '0'):
            if (result["change"] == '1'):
                self.input_a[j] = result["bits"][0]
                self.input_b[i] = result["bits"][1]
                self.carry[i][j-1] = result["bits"][3]
                self.sum[i][j] = result["bits"][4]
                self.carry[i][j] = result["bits"][5]
                self.change = '1'
        else:
            self.error = '1'

    def _solve_bottom_left_corner(self, i, j):
        result = MultiplierCell.MultiplierCell([self.input_a[j], self.input_b[i], self.carry[i-1][j], self.carry[i][j-1], self.output[i+j], self.output[i+j+1]]).solve()
        if (result["error"] == '0' and self.output[i+j] == result["bits"][4] and self.output[i+j+1] == result["bits"][5]):
            if (result["change"] == '1'):
                self.input_a[j] = result["bits"][0]
                self.input_b[i] = result["bits"][1]
                self.carry[i-1][j] = result["bits"][2]
                self.carry[i][j-1] = result["bits"][3]
                self.change = '1'
        else:
            self.error = '1'
        self.sum[i][j] = None
        self.carry[i][j] = None

    def _solve_bottom_row(self, i, j):
        result = MultiplierCell.MultiplierCell([self.input_a[j], self.input_b[i], self.sum[i-1][j+1], self.carry[i][j-1], self.output[i+j], self.carry[i][j]]).solve()
        if (result["error"] == '0' and self.output[i+j] == result["bits"][4]):
            if (result["change"] == '1'):
                self.input_a[j] = result["bits"][0]
                self.input_b[i] = result["bits"][1]
                self.sum[i-1][j+1] = result["bits"][2]
                self.carry[i][j-1] = result["bits"][3]
                self.carry[i][j] = result["bits"][5]
                self.change = '1'
        else:
            self.error = '1'
        self.sum[i][j] = None

    def _solve_last_column(self, i, j):
        result = MultiplierCell.MultiplierCell([self.input_a[j], self.input_b[i], self.carry[i-1][j], self.carry[i][j-1], self.sum[i][j], self.carry[i][j]]).solve()
        if (result["error"] == '0'):
            if (result["change"] == '1'):
                self.input_a[j] = result["bits"][0]
                self.input_b[i] = result["bits"][1]
                self.carry[i-1][j] = result["bits"][2]
                self.carry[i][j-1] = result["bits"][3]
                self.sum[i][j] = result["bits"][4]
                self.carry[i][j] = result["bits"][5]
                self.change = '1'
        else:
            self.error = '1'

    def _solve_interior(self, i, j):
        result = MultiplierCell.MultiplierCell([self.input_a[j], self.input_b[i], self.sum[i-1][j+1], self.carry[i][j-1], self.sum[i][j], self.carry[i][j]]).solve()
        if (result["error"] == '0'):
            if (result["change"] == '1'):
                self.input_a[j] = result["bits"][0]
                self.input_b[i] = result["bits"][1]
                self.sum[i-1][j+1] = result["bits"][2]
                self.carry[i][j-1] = result["bits"][3]
                self.sum[i][j] = result["bits"][4]
                self.carry[i][j] = result["bits"][5]
                self.change = '1'
        else:
            self.error = '1'

    def _index_i_to_key(self, i):
        if i == 0:
            return "i_eq_0"
        elif i == len(self.input_b) - 1:
            return "i_eq_last"
        else:
            return "i_gt_0"

    def _index_j_to_key(self, j):
        if j == 0:
            return "j_eq_0"
        elif j == len(self.input_a) - 1:
            return "j_eq_last"
        else:
            return "j_gt_0"


class OptimizedRippleCarryArrayMultiplier(RippleCarryArrayMultiplier):
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
            return(self.solve())
        return({"input_a": ''.join(self.input_a)[::-1], "input_b": ''.join(self.input_b)[::-1], "error": error})
