"""
    This program is to iterate through the different
    gates on a one-by-one basis in order to not run
    into synchronous issues that I experience in VHDL.
"""

from . import gates

class HalfAdder:
    def __init__(self, bits=list("ZZZZ")):
        self.bits = bits
        # Default "ZZZZ"
        #          |||└ output Carry
        #          ||└- output Sum
        #          |└-- input B
        #          └--- input A

    def solve(self, change='0'):
        error = '0'

        if self.bits == ['Z', 'Z', '0', '0']:
            # Special Case 1
            return({"bits": ('0', '0', '0', '0'), "error": '0', "change": '1'})
        elif self.bits == ['Z', 'Z', '1', 'Z']:
            # Special Case 2
            return({"bits": ('Z', 'Z', '1', '0'), "error": '0', "change": '1'})

        result = gates.and_gate(self.bits[0], self.bits[1], self.bits[3])
        if (result["error"] == '0'):
            if (result["change"] == '1'):
                self.bits[0] = result["gates"][0]
                self.bits[1] = result["gates"][1]
                self.bits[3] = result["gates"][2]
                change = '1'
        else:
            error = '1'

        result = gates.xor_gate(self.bits[0], self.bits[1], self.bits[2])
        if (result["error"] == '0' and error == '0'):
            if (result["change"] == '1'):
                self.bits[0] = result["gates"][0]
                self.bits[1] = result["gates"][1]
                self.bits[2] = result["gates"][2]
                return(self.solve('1'))
        else:
            self.bits[0] = 'Z'
            self.bits[1] = 'Z'
            self.bits[2] = 'Z'
            self.bits[3] = 'Z'
            error = '1'
            change = '1'

        return({"bits": tuple(self.bits), "error": error, "change": change})
