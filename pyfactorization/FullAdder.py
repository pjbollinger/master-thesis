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

    def _current_io(self):
        return (self.bits[0], self.bits[1], self.bits[2], self.bits[6], self.bits[7])

    def solve(self, change='0'):
        self.change = change
        if self.change == '0':
            self.old_bits = "".join(self._current_io())
        self.error = '0'
        if (self.old_bits in ["Z1Z0Z", "Z11ZZ", "1ZZ0Z", "1Z1ZZ"]):
            # Special cases
            self.bits[7] = '1'
            return {
                "bits": self._current_io(),
                "error": '0',
                "change": '1',
            }

        # Half Adder 1
        self._solve_half_adder(0, 1, 3, 4)

        # Half Adder 2
        self._solve_half_adder(2, 3, 6, 5)

        # OR
        result = gates.or_gate(self.bits[4], self.bits[5], self.bits[7])
        if (result["error"] == '0' and self.error == '0'):
            if (result["change"] == '1'):
                self.bits[4] = result["gates"][0]
                self.bits[5] = result["gates"][1]
                self.bits[7] = result["gates"][2]
                return(self.solve('1'))
        else:
            self.bits = list("ZZZZZZZZ")
            self.error = '1'
            self.change = '1'
        
        if self.error == '0':
            self.change = '1' if self.old_bits != "".join(self._current_io()) else '0'

        return({"bits": self._current_io(), "error": self.error, "change": self.change})
    
    def _solve_half_adder(self, a_index, b_index, sum_index, cout_index):
        result = HalfAdder.HalfAdder([self.bits[a_index], self.bits[b_index], self.bits[sum_index], self.bits[cout_index]]).solve()
        if (result["error"] == '0'):
            if (result["change"] == '1'):
                self.bits[a_index] = result["bits"][0]
                self.bits[b_index] = result["bits"][1]
                self.bits[sum_index] = result["bits"][2]
                self.bits[cout_index] = result["bits"][3]
                return self.solve('1')
        else:
            self.error = '1'
