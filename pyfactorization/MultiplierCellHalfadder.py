from . import gates
from . import HalfAdder

class MultiplierCellHalfadder:
    def __init__(self, bits=list("ZZZZZ")):
        self.bits = [bits[0], bits[1], bits[2], 'Z', bits[3], bits[4]]
        # Default "ZZZZZZ"
        #          |||||└ 5 output Carry Out
        #          ||||└- 4 output Sum Out
        #          |||└-- 3 signal AND_Z to HA_A
        #          ||└--- 2 input W
        #          |└---- 1 inout Y
        #          └----- 0 inout X

    def solve(self, change='0'):
        if change == '0':
            self.old_bits = self.bits[0] + self.bits[1] + self.bits[2] + self.bits[4] + self.bits[5]
        error = '0'

        # AND
        result = gates.and_gate(self.bits[0], self.bits[1], self.bits[3])
        if (result["error"] == '0'):
            if (result["change"] == '1'):
                self.bits[0] = result["gates"][0]
                self.bits[1] = result["gates"][1]
                self.bits[3] = result["gates"][2]
                # print('AND Change:', self.bits)
                change = '1'
        else:
            error = '1'

        # Full Adder
        result = HalfAdder.HalfAdder([self.bits[3], self.bits[2], self.bits[4], self.bits[5]]).solve()
        if (result["error"] == '0' and error == '0'):
            if (result["change"] == '1'):
                self.bits[3] = result["bits"][0]
                self.bits[2] = result["bits"][1]
                self.bits[4] = result["bits"][2]
                self.bits[5] = result["bits"][3]
                # print('FA Change:', self.bits)
                return(self.solve('1'))
        else:
            self.bits = list("ZZZZZZ")
            error = '1'
            change = '1'

        if error == '0':
            change = '1' if self.old_bits != self.bits[0] + self.bits[1] + self.bits[2] + self.bits[4] + self.bits[5] else '0'

        return({"bits": (self.bits[0], self.bits[1], self.bits[2], self.bits[4], self.bits[5]), "error": error, "change": change})
