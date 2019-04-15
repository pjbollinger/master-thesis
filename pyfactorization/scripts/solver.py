import sympy
import math
import pprint
import copy
import itertools

from pyfactorization.RippleCarryArrayMultiplier import RippleCarryArrayMultiplier

pp = pprint.PrettyPrinter(indent=4)

# Semiprimes 1 digit to 10 digits
ranges = [
    (2**x, 2**(x+1))
    for x in range(1, 100+1)
]
print("a, b, resolved_count, total_count, error")
for entry in ranges:
    a = sympy.randprime(entry[0], entry[1])
    b = sympy.nextprime(a) if sympy.nextprime(a) <= entry[1] else sympy.prevprime(a)
    original = RippleCarryArrayMultiplier(a * b)
    result = original.solve()
    information_count = original.information_count()
    print("{}, {}, {}, {}, {}".format(a, b, information_count['resolved_count'], information_count['total_count'], result['error']))
    # unknown_input_a = [{"index": index, "test_1": {"result": None, "information_count": None, "ok": None}, "test_0": {"result": None, "information_count": None, "ok": None}} for (index, value) in enumerate(original.input_a) if value == 'Z']
    # possible_input_a = []
    # for unknown in unknown_input_a:
    #     for value in ['0', '1']:
    #         test = copy.deepcopy(original)
    #         test.input_a[unknown["index"]] = value
    #         unknown["test_" + value]["result"] = test.solve()
    #         unknown["test_" + value]["information_count"] = test.information_count()
    #         if unknown["test_" + value]["result"]["error"] == '0':
    #             unknown["test_" + value]["ok"] = True
    #             possible_input_a.append(test.input_a.copy())
    # print(possible_input_a)
    # for possible_input in possible_input_a:
    #     if 'Z' not in possible_input:
    #         print("SOLUTION:", possible_input)
    #     else:
    #         print("Next Choice:", possible_input)
    # next_possible_input_a = []
    # for possible_input in possible_input_a:
    #     unknown_input_a = [{"index": index, "test_1": {"result": None, "information_count": None, "ok": None}, "test_0": {"result": None, "information_count": None, "ok": None}} for (index, value) in enumerate(possible_input) if value == 'Z']
    #     for unknown in unknown_input_a:
    #         for value in ['0', '1']:
    #             test = copy.deepcopy(original)
    #             test.input_a = possible_input[:]
    #             test.input_a[unknown["index"]] = value
    #             unknown["test_" + value]["result"] = test.solve()
    #             unknown["test_" + value]["information_count"] = test.information_count()
    #             if unknown["test_" + value]["result"]["error"] == '0':
    #                 unknown["test_" + value]["ok"] = True
    #                 next_possible_input_a.append(test.input_a.copy())
    # next_possible_input_a = [list(x) for x in set(tuple(x) for x in next_possible_input_a)]
    # pp.pprint(next_possible_input_a)
