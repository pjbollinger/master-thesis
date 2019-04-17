import pytest
from pyfactorization.CarrySaveArrayMultiplier import CarrySaveArrayMultiplier
from pyfactorization.RippleCarryArrayMultiplier import OptimizedRippleCarryArrayMultiplier, RippleCarryArrayMultiplier

# Nonsquare Semiprime numbers, compatible for RSA
# 6, 10, 14, 15, 21, 22, 26, 33, 34, 35, 38, 39, 46, 51, 55, 57, 58, 62, 65, 69, 74, 77, 82, 85, 86, 87, 91, 93, 94, 95

def test_6():
    # 2 - '10'
    # 3 - '11'
    test = RippleCarryArrayMultiplier(6)
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
    expected_information = {
        'total_count': 8,
        'resolved_count': 5
    }
    actual_result = test.solve()
    actual_dump = test.dump()
    actual_information = test.information_count()
    assert expected_result == actual_result
    assert expected_dump == actual_dump
    assert expected_information == actual_information

def test_6_carry_save():
    # TODO: Verify this test
    # 2 - '10'
    # 3 - '11'
    test = CarrySaveArrayMultiplier(6)
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
            [None, None],
            ['0', None]
        ],
        "output": "0110"
    }
    actual_result = test.solve()
    actual_dump = test.dump()
    assert expected_result == actual_result
    assert expected_dump == actual_dump

def test_6_optimized():
    # 2 - '10'
    # 3 - '11'
    test = OptimizedRippleCarryArrayMultiplier(6)
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
    actual_result = test.solve()
    actual_dump = test.dump()
    assert expected_result == actual_result
    assert expected_dump == actual_dump

def test_35():
    # 7 - '111'
    # 5 - '101'
    test = RippleCarryArrayMultiplier(35)
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
    expected_information = {
        'total_count': 18,
        'resolved_count': 6
    }
    actual_result = test.solve()
    actual_dump = test.dump()
    actual_information = test.information_count()
    assert expected_result == actual_result
    assert expected_dump == actual_dump
    assert expected_information == actual_information

@pytest.mark.skip("Need to implment carry save")
def test_35_carry_save():
    # 7 - '111'
    # 5 - '101'
    test = CarrySaveArrayMultiplier(35)
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

def test_35_optimized():
    # 7 - '111'
    # 5 - '101'
    test = OptimizedRippleCarryArrayMultiplier(35)
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
    actual_result = test.solve()
    actual_dump = test.dump()
    assert expected_result == actual_result
    assert expected_dump == actual_dump

def test_143():
    # 13 - '1101'
    # 11 - '1011'
    test = RippleCarryArrayMultiplier(143)
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
    expected_information = {
        'total_count': 32,
        'resolved_count': 9,
    }
    actual_result = test.solve()
    actual_dump = test.dump()
    actual_information = test.information_count()
    assert expected_result == actual_result
    assert expected_dump == actual_dump
    assert expected_information == actual_information

@pytest.mark.skip("Need to implment carry save")
def test_143_carry_save():
    # 13 - '1101'
    # 11 - '1011'
    test = CarrySaveArrayMultiplier(143)
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

def test_143_optimized():
    # 13 - '1101'
    # 11 - '1011'
    test = OptimizedRippleCarryArrayMultiplier(143)
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
    actual_result = test.solve()
    actual_dump = test.dump()
    assert expected_result == actual_result
    assert expected_dump == actual_dump

@pytest.mark.skip("Too big")
def test_generic():
    num = 1522605027922533360535618378132637429718068114961380688657908494580122963258952897654000350692006139
    test = RippleCarryArrayMultiplier(num)
    test.input_a[len(test.input_a) - 1] = '1'
    test.input_b[len(test.input_b) - 1] = '1'
    print(test.solve())
    print(test.information_count())
    for index in range(1, 140):
        test.input_a[index] = '0'
    print(test.solve())
    print(test.information_count())
    assert False

@pytest.mark.skip("Too big")
def test_rsa_100():
    test = RippleCarryArrayMultiplier(1522605027922533360535618378132637429718068114961380688657908494580122963258952897654000350692006139)
    print(test.solve())
    print(test.information_count())
    assert False

@pytest.mark.skip("Too big")
def test_rsa_768():
    test = RippleCarryArrayMultiplier(1230186684530117755130494958384962720772853569595334792197322452151726400507263657518745202199786469389956474942774063845925192557326303453731548268507917026122142913461670429214311602221240479274737794080665351419597459856902143413)
    print(test.solve())
    print(test.information_count())
    assert False

@pytest.mark.skip("Too big")
def test_rsa_2048():
    test = RippleCarryArrayMultiplier(25195908475657893494027183240048398571429282126204032027777137836043662020707595556264018525880784406918290641249515082189298559149176184502808489120072844992687392807287776735971418347270261896375014971824691165077613379859095700097330459748808428401797429100642458691817195118746121515172654632282216869987549182422433637259085141865462043576798423387184774447920739934236584823824281198163815010674810451660377306056201619676256133844143603833904414952634432190114657544454178424020924616515723350778707749817125772467962926386356373289912154831438167899885040445364023527381951378636564391212010397122822120720357)
    print(test.solve())
    print(test.information_count())
    assert False
