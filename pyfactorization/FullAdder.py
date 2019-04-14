from . import gates
from . import HalfAdder

class FullAdder:
    def __init__(self, bits=list("ZZZZZ")):
        self.bits = [bits[0], bits[1], bits[2], 'Z', 'Z', 'Z', bits[3], bits[4]]
        # Default "ZZZZZZZZ"
        #          |||||||└ 7 output Carry Out
        #          ||||||└- 6 output Sum
        #          |||||└-- 5 signal HA_2_Carry to OR_B
        #          ||||└--- 4 signal HA_1_Carry to OR_A
        #          |||└---- 3 signal HA_1_Sum to HA_2_B
        #          ||└----- 2 input Carry In
        #          |└------ 1 input B
        #          └------- 0 input A

    def solve(self, change='0'):
        if self.bits[0] == 'Z' and self.bits[1] == '1' and self.bits[2] == 'Z' and self.bits[6] == '0' and self.bits[7] == 'Z':
            # Special case 1
            self.bits[7] = '1'
            return({"bits": (self.bits[0], self.bits[1], self.bits[2], self.bits[6], self.bits[7]), "error": '0', "change": '1'})
        elif self.bits[0] == 'Z' and self.bits[1] == '1' and self.bits[2] == '1' and self.bits[6] == 'Z' and self.bits[7] == 'Z':
            # Special case 2
            self.bits[7] = '1'
            return({"bits": (self.bits[0], self.bits[1], self.bits[2], self.bits[6], self.bits[7]), "error": '0', "change": '1'})
        elif self.bits[0] == '1' and self.bits[1] == 'Z' and self.bits[2] == 'Z' and self.bits[6] == '0' and self.bits[7] == 'Z':
            # Special case 3
            self.bits[7] = '1'
            return({"bits": (self.bits[0], self.bits[1], self.bits[2], self.bits[6], self.bits[7]), "error": '0', "change": '1'})
        elif self.bits[0] == '1' and self.bits[1] == 'Z' and self.bits[2] == '1' and self.bits[6] == 'Z' and self.bits[7] == 'Z':
            # Special case 4
            self.bits[7] = '1'
            return({"bits": (self.bits[0], self.bits[1], self.bits[2], self.bits[6], self.bits[7]), "error": '0', "change": '1'})

        if change == '0':
            self.old_bits = self.bits[0] + self.bits[1] + self.bits[2] + self.bits[6] + self.bits[7]
        error = '0'

        # Half Adder 1
        result = HalfAdder.HalfAdder([self.bits[0], self.bits[1], self.bits[3], self.bits[4]]).solve()
        if (result["error"] == '0'):
            if (result["change"] == '1'):
                self.bits[0] = result["bits"][0]
                self.bits[1] = result["bits"][1]
                self.bits[3] = result["bits"][2]
                self.bits[4] = result["bits"][3]
                # print('HA1 Change:', self.bits)
                change = '1'
        else:
            error = '1'

        # Half Adder 2
        result = HalfAdder.HalfAdder([self.bits[2], self.bits[3], self.bits[6], self.bits[5]]).solve()
        if (result["error"] == '0' and error == '0'):
            if (result["change"] == '1'):
                self.bits[2] = result["bits"][0]
                self.bits[3] = result["bits"][1]
                self.bits[6] = result["bits"][2]
                self.bits[5] = result["bits"][3]
                # print('HA2 Change:', self.bits)
                return(self.solve('1'))
        else:
            error = '1'

        # OR
        result = gates.or_gate(self.bits[4], self.bits[5], self.bits[7])
        if (result["error"] == '0' and error == '0'):
            if (result["change"] == '1'):
                self.bits[4] = result["gates"][0]
                self.bits[5] = result["gates"][1]
                self.bits[7] = result["gates"][2]
                # print('OR Change:', self.bits)
                return(self.solve('1'))
        else:
            self.bits = list("ZZZZZZZZ")
            error = '1'
            change = '1'
        
        if error == '0':
            change = '1' if self.old_bits != self.bits[0] + self.bits[1] + self.bits[2] + self.bits[6] + self.bits[7] else '0'

        return({"bits": (self.bits[0], self.bits[1], self.bits[2], self.bits[6], self.bits[7]), "error": error, "change": change})
