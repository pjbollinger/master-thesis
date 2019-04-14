from . import gates
from . import FullAdder

class MultiplierCell:
    def __init__(self, bits=list("ZZZZZZ")):
        self.bits = [bits[0], bits[1], bits[2], bits[3], 'Z', bits[4], bits[5]]
        # Default "ZZZZZZZ"
        #          ||||||└ 6 output Carry Out
        #          |||||└- 5 output Sum Out
        #          ||||└-- 4 signal AND_Z to FA_A
        #          |||└--- 3 input Carry In
        #          ||└---- 2 input Sum In
        #          |└----- 1 inout Y
        #          └------ 0 inout X

    def solve(self, change='0'):
        if change == '0':
            self.old_bits = self.bits[0] + self.bits[1] + self.bits[2] + self.bits[3] + self.bits[5] + self.bits[6]
        error = '0'

        # AND
        result = gates.and_gate(self.bits[0], self.bits[1], self.bits[4])
        if (result["error"] == '0'):
            if (result["change"] == '1'):
                self.bits[0] = result["gates"][0]
                self.bits[1] = result["gates"][1]
                self.bits[4] = result["gates"][2]
                # print('AND Change:', self.bits)
                change = '1'
        else:
            error = '1'

        # Full Adder
        result = FullAdder.FullAdder([self.bits[4], self.bits[2], self.bits[3], self.bits[5], self.bits[6]]).solve()
        if (result["error"] == '0' and error == '0'):
            if (result["change"] == '1'):
                self.bits[4] = result["bits"][0]
                self.bits[2] = result["bits"][1]
                self.bits[3] = result["bits"][2]
                self.bits[5] = result["bits"][3]
                self.bits[6] = result["bits"][4]
                # print('FA Change:', self.bits)
                return(self.solve('1'))
        else:
            self.bits = list("ZZZZZZZ")
            error = '1'
            change = '1'

        if error == '0':
            change = '1' if self.old_bits != self.bits[0] + self.bits[1] + self.bits[2] + self.bits[3] + self.bits[5] + self.bits[6] else '0'

        return({"bits": (self.bits[0], self.bits[1], self.bits[2], self.bits[3], self.bits[5], self.bits[6]), "error": error, "change": change})
