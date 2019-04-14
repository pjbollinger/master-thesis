import pytest
from pyfactorization.SemiPrimeFactorization import SemiPrimeFactorization

# Nonsquare Semiprime numbers, compatible for RSA
# 6, 10, 14, 15, 21, 22, 26, 33, 34, 35, 38, 39, 46, 51, 55, 57, 58, 62, 65, 69, 74, 77, 82, 85, 86, 87, 91, 93, 94, 95

def test_6():
    # 2 - '10'
    # 3 - '11'
    test = SemiPrimeFactorization(6)
    expected_result = {
        "input_a": "1Z",
        "input_b": "1Z",
        "error": '0'
    }
    expected_dump = {
        "input_a": ['Z', '1'],
        "input_b": ['Z', '1'],
        "sum": [
            [None, 'Z'],
            [None, None]
        ],
        "carry": [
            ['0', '0'],
            ['0', None]
        ],
        "output": "0110"
    }
    actual_result = test.solve()
    actual_dump = test.dump()
    assert expected_result == actual_result
    assert expected_dump == actual_dump

@pytest.mark.skip("Need to implment carry save")
def test_6_carry_save():
    # 2 - '10'
    # 3 - '11'
    test = SemiPrimeFactorization(6)
    expected_result = {
        "input_a": "1Z",
        "input_b": "1Z",
        "error": '0'
    }
    expected_dump = {
        "input_a": ['Z', '1'],
        "input_b": ['Z', '1'],
        "sum": [
            [None, 'Z'],
            [None, None]
        ],
        "carry": [
            ['0', '0'],
            ['0', None]
        ],
        "output": "0110"
    }
    actual_result = test.solve_carry_save()
    actual_dump = test.dump()
    assert expected_result == actual_result
    assert expected_dump == actual_dump

def test_6_optimized():
    # 2 - '10'
    # 3 - '11'
    test = SemiPrimeFactorization(6)
    expected_result = {
        "input_a": "1Z",
        "input_b": "1Z",
        "error": '0'
    }
    expected_dump = {
        "input_a": ['Z', '1'],
        "input_b": ['Z', '1'],
        "sum": [
            [None, 'Z'],
            [None, None]
        ],
        "carry": [
            [None, '0'],
            ['0', None]
        ],
        "output": "0110"
    }
    actual_result = test.solve_optimized()
    actual_dump = test.dump()
    assert expected_result == actual_result
    assert expected_dump == actual_dump

def test_35():
    # 7 - '111'
    # 5 - '101'
    test = SemiPrimeFactorization(35)
    expected_result = {
        "input_a": "ZZ1",
        "input_b": "ZZ1",
        "error": '0'
    }
    expected_dump = {
        "input_a": ['1', 'Z', 'Z'],
        "input_b": ['1', 'Z', 'Z'],
        "sum": [
            [None, 'Z', 'Z'],
            [None, 'Z', 'Z'],
            [None, None, None]
        ],
        "carry": [
            ['0', '0', '0'],
            ['0', 'Z', 'Z'],
            ['Z', 'Z', None]
        ],
        "output": "110001"
    }
    actual_result = test.solve()
    actual_dump = test.dump()
    assert expected_result == actual_result
    assert expected_dump == actual_dump

@pytest.mark.skip("Need to implment carry save")
def test_35_carry_save():
    # 7 - '111'
    # 5 - '101'
    test = SemiPrimeFactorization(35)
    expected_result = {
        "input_a": "ZZ1",
        "input_b": "ZZ1",
        "error": '0'
    }
    expected_dump = {
        "input_a": ['1', 'Z', 'Z'],
        "input_b": ['1', 'Z', 'Z'],
        "sum": [
            [None, 'Z', 'Z'],
            [None, 'Z', 'Z'],
            [None, None, None]
        ],
        "carry": [
            ['0', '0', '0'],
            ['0', 'Z', 'Z'],
            ['Z', 'Z', None]
        ],
        "output": "110001"
    }
    actual_result = test.solve_carry_save()
    actual_dump = test.dump()
    assert expected_result == actual_result
    assert expected_dump == actual_dump

def test_35_optimized():
    # 7 - '111'
    # 5 - '101'
    test = SemiPrimeFactorization(35)
    expected_result = {
        "input_a": "ZZ1",
        "input_b": "ZZ1",
        "error": '0'
    }
    expected_dump = {
        "input_a": ['1', 'Z', 'Z'],
        "input_b": ['1', 'Z', 'Z'],
        "sum": [
            [None, 'Z', 'Z'],
            [None, 'Z', 'Z'],
            [None, None, None]
        ],
        "carry": [
            [None, None, '0'],
            ['0', 'Z', 'Z'],
            ['Z', 'Z', None]
        ],
        "output": "110001"
    }
    actual_result = test.solve_optimized()
    actual_dump = test.dump()
    assert expected_result == actual_result
    assert expected_dump == actual_dump

def test_143():
    # 13 - '1101'
    # 11 - '1011'
    test = SemiPrimeFactorization(143)
    expected_result = {
        "input_a": "ZZZ1",
        "input_b": "ZZZ1",
        "error": '0'
    }
    expected_dump = {
        "input_a": ['1', 'Z', 'Z', 'Z'],
        "input_b": ['1', 'Z', 'Z', 'Z'],
        "sum": [
            [None, 'Z', 'Z', 'Z'],
            [None, 'Z', 'Z', 'Z'],
            [None, 'Z', 'Z', 'Z'],
            [None, None, None, None]
        ],
        "carry": [
            ['0', '0', '0', '0'],
            ['0', 'Z', 'Z', 'Z'],
            ['0', 'Z', 'Z', 'Z'],
            ['0', 'Z', 'Z', None]
        ],
        "output": "11110001"
    }
    actual_result = test.solve()
    actual_dump = test.dump()
    assert expected_result == actual_result
    assert expected_dump == actual_dump

@pytest.mark.skip("Need to implment carry save")
def test_143_carry_save():
    # 13 - '1101'
    # 11 - '1011'
    test = SemiPrimeFactorization(143)
    expected_result = {
        "input_a": "ZZZ1",
        "input_b": "ZZZ1",
        "error": '0'
    }
    expected_dump = {
        "input_a": ['1', 'Z', 'Z', 'Z'],
        "input_b": ['1', 'Z', 'Z', 'Z'],
        "sum": [
            [None, 'Z', 'Z', 'Z'],
            [None, 'Z', 'Z', 'Z'],
            [None, 'Z', 'Z', 'Z'],
            [None, None, None, None]
        ],
        "carry": [
            ['0', '0', '0', '0'],
            ['0', 'Z', 'Z', 'Z'],
            ['0', 'Z', 'Z', 'Z'],
            ['0', 'Z', 'Z', None]
        ],
        "output": "11110001"
    }
    actual_result = test.solve_carry_save()
    actual_dump = test.dump()
    assert expected_result == actual_result
    assert expected_dump == actual_dump

def test_143_optimized():
    # 13 - '1101'
    # 11 - '1011'
    test = SemiPrimeFactorization(143)
    expected_result = {
        "input_a": "ZZZ1",
        "input_b": "ZZZ1",
        "error": '0'
    }
    expected_dump = {
        "input_a": ['1', 'Z', 'Z', 'Z'],
        "input_b": ['1', 'Z', 'Z', 'Z'],
        "sum": [
            [None, 'Z', 'Z', 'Z'],
            [None, 'Z', 'Z', 'Z'],
            [None, 'Z', 'Z', 'Z'],
            [None, None, None, None]
        ],
        "carry": [
            [None, None, None, '0'],
            ['0', 'Z', 'Z', 'Z'],
            ['0', 'Z', 'Z', 'Z'],
            ['0', 'Z', 'Z', None]
        ],
        "output": "11110001"
    }
    actual_result = test.solve_optimized()
    actual_dump = test.dump()
    assert expected_result == actual_result
    assert expected_dump == actual_dump

@pytest.mark.skip("Too big")
def test_generic():
    num = 1522605027922533360535618378132637429718068114961380688657908494580122963258952897654000350692006139
    test = SemiPrimeFactorization(num)
    test.input_a[len(test.input_a) - 1] = '1'
    test.input_b[len(test.input_b) - 1] = '1'
    print(test.solve())
    print(test.information_count())
    for index in range(1, 140):
        test.input_a[index] = '0'
    print(test.solve())
    print(test.information_count())
    assert False

# def test_rsa_100():
#     test = SemiPrimeFactorization(1522605027922533360535618378132637429718068114961380688657908494580122963258952897654000350692006139)
#     print(test.solve())
#     print(test.information_count())
#     assert False
# 
# def test_rsa_768():
#     test = SemiPrimeFactorization(1230186684530117755130494958384962720772853569595334792197322452151726400507263657518745202199786469389956474942774063845925192557326303453731548268507917026122142913461670429214311602221240479274737794080665351419597459856902143413)
#     print(test.solve())
#     print(test.information_count())
#     assert False
# 
# def test_rsa_2048():
#     test = SemiPrimeFactorization(25195908475657893494027183240048398571429282126204032027777137836043662020707595556264018525880784406918290641249515082189298559149176184502808489120072844992687392807287776735971418347270261896375014971824691165077613379859095700097330459748808428401797429100642458691817195118746121515172654632282216869987549182422433637259085141865462043576798423387184774447920739934236584823824281198163815010674810451660377306056201619676256133844143603833904414952634432190114657544454178424020924616515723350778707749817125772467962926386356373289912154831438167899885040445364023527381951378636564391212010397122822120720357)
#     print(test.solve())
#     print(test.information_count())
#     assert False

import sympy
import math
import pprint
import copy
import itertools
pp = pprint.PrettyPrinter(indent=4)

@pytest.mark.skip(reason="Don't want to deal with right now")
def test_wow():
    # Semiprimes 1 digit to 10 digits
    ranges = [
        (2**x, 2**(x+1))
        for x in range(1, 100+1)
    ]
    print("a, b, resolved_count, total_count, error")
    for entry in ranges:
        a = sympy.randprime(entry[0], entry[1])
        b = sympy.nextprime(a) if sympy.nextprime(a) <= entry[1] else sympy.prevprime(a)
        original = SemiPrimeFactorization(a * b)
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
    assert False
