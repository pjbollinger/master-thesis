import pytest
from pyfactorization.HalfAdder import HalfAdder

test_data = [
    (['Z', 'Z', 'Z', 'Z'], {"bits": ('Z', 'Z', 'Z', 'Z'), "error": '0', "change": "0"}), # NO MOD
    (['Z', 'Z', 'Z', '0'], {"bits": ('Z', 'Z', 'Z', '0'), "error": '0', "change": "0"}), # NO MOD
    (['Z', 'Z', 'Z', '1'], {"bits": ('1', '1', '0', '1'), "error": '0', "change": "1"}), # NO MOD
    (['Z', 'Z', '0', 'Z'], {"bits": ('Z', 'Z', '0', 'Z'), "error": '0', "change": "0"}), # NO MOD
    (['Z', 'Z', '0', '0'], {"bits": ('0', '0', '0', '0'), "error": '0', "change": "1"}), #    MOD
    (['Z', 'Z', '0', '1'], {"bits": ('1', '1', '0', '1'), "error": '0', "change": "1"}), # NO MOD
    (['Z', 'Z', '1', 'Z'], {"bits": ('Z', 'Z', '1', '0'), "error": '0', "change": "1"}), #    MOD
    (['Z', 'Z', '1', '0'], {"bits": ('Z', 'Z', '1', '0'), "error": '0', "change": "0"}), # NO MOD
    (['Z', 'Z', '1', '1'], {"bits": ('Z', 'Z', 'Z', 'Z'), "error": '1', "change": "1"}), # NO MOD
    (['Z', '0', 'Z', 'Z'], {"bits": ('Z', '0', 'Z', '0'), "error": '0', "change": "1"}), # NO MOD
    (['Z', '0', 'Z', '0'], {"bits": ('Z', '0', 'Z', '0'), "error": '0', "change": "0"}), # NO MOD
    (['Z', '0', 'Z', '1'], {"bits": ('Z', 'Z', 'Z', 'Z'), "error": '1', "change": "1"}), # NO MOD
    (['Z', '0', '0', 'Z'], {"bits": ('0', '0', '0', '0'), "error": '0', "change": "1"}), # NO MOD
    (['Z', '0', '0', '0'], {"bits": ('0', '0', '0', '0'), "error": '0', "change": "1"}), # NO MOD
    (['Z', '0', '0', '1'], {"bits": ('Z', 'Z', 'Z', 'Z'), "error": '1', "change": "1"}), # NO MOD
    (['Z', '0', '1', 'Z'], {"bits": ('1', '0', '1', '0'), "error": '0', "change": "1"}), # NO MOD
    (['Z', '0', '1', '0'], {"bits": ('1', '0', '1', '0'), "error": '0', "change": "1"}), # NO MOD
    (['Z', '0', '1', '1'], {"bits": ('Z', 'Z', 'Z', 'Z'), "error": '1', "change": "1"}), # NO MOD
    (['Z', '1', 'Z', 'Z'], {"bits": ('Z', '1', 'Z', 'Z'), "error": '0', "change": "0"}), # NO MOD
    (['Z', '1', 'Z', '0'], {"bits": ('0', '1', '1', '0'), "error": '0', "change": "1"}), # NO MOD
    (['Z', '1', 'Z', '1'], {"bits": ('1', '1', '0', '1'), "error": '0', "change": "1"}), # NO MOD
    (['Z', '1', '0', 'Z'], {"bits": ('1', '1', '0', '1'), "error": '0', "change": "1"}), # NO MOD
    (['Z', '1', '0', '0'], {"bits": ('Z', 'Z', 'Z', 'Z'), "error": '1', "change": "1"}), # NO MOD
    (['Z', '1', '0', '1'], {"bits": ('1', '1', '0', '1'), "error": '0', "change": "1"}), # NO MOD
    (['Z', '1', '1', 'Z'], {"bits": ('0', '1', '1', '0'), "error": '0', "change": "1"}), # NO MOD
    (['Z', '1', '1', '0'], {"bits": ('0', '1', '1', '0'), "error": '0', "change": "1"}), # NO MOD
    (['Z', '1', '1', '1'], {"bits": ('Z', 'Z', 'Z', 'Z'), "error": '1', "change": "1"}), # NO MOD
    (['0', 'Z', 'Z', 'Z'], {"bits": ('0', 'Z', 'Z', '0'), "error": '0', "change": "1"}), # NO MOD
    (['0', 'Z', 'Z', '0'], {"bits": ('0', 'Z', 'Z', '0'), "error": '0', "change": "0"}), # NO MOD
    (['0', 'Z', 'Z', '1'], {"bits": ('Z', 'Z', 'Z', 'Z'), "error": '1', "change": "1"}), # NO MOD
    (['0', 'Z', '0', 'Z'], {"bits": ('0', '0', '0', '0'), "error": '0', "change": "1"}), # NO MOD
    (['0', 'Z', '0', '0'], {"bits": ('0', '0', '0', '0'), "error": '0', "change": "1"}), # NO MOD
    (['0', 'Z', '0', '1'], {"bits": ('Z', 'Z', 'Z', 'Z'), "error": '1', "change": "1"}), # NO MOD
    (['0', 'Z', '1', 'Z'], {"bits": ('0', '1', '1', '0'), "error": '0', "change": "1"}), # NO MOD
    (['0', 'Z', '1', '0'], {"bits": ('0', '1', '1', '0'), "error": '0', "change": "1"}), # NO MOD
    (['0', 'Z', '1', '1'], {"bits": ('Z', 'Z', 'Z', 'Z'), "error": '1', "change": "1"}), # NO MOD
    (['0', '0', 'Z', 'Z'], {"bits": ('0', '0', '0', '0'), "error": '0', "change": "1"}), # NO MOD
    (['0', '0', 'Z', '0'], {"bits": ('0', '0', '0', '0'), "error": '0', "change": "1"}), # NO MOD
    (['0', '0', 'Z', '1'], {"bits": ('Z', 'Z', 'Z', 'Z'), "error": '1', "change": "1"}), # NO MOD
    (['0', '0', '0', 'Z'], {"bits": ('0', '0', '0', '0'), "error": '0', "change": "1"}), # NO MOD
    (['0', '0', '0', '0'], {"bits": ('0', '0', '0', '0'), "error": '0', "change": "0"}), # NO MOD
    (['0', '0', '0', '1'], {"bits": ('Z', 'Z', 'Z', 'Z'), "error": '1', "change": "1"}), # NO MOD
    (['0', '0', '1', 'Z'], {"bits": ('Z', 'Z', 'Z', 'Z'), "error": '1', "change": "1"}), # NO MOD
    (['0', '0', '1', '0'], {"bits": ('Z', 'Z', 'Z', 'Z'), "error": '1', "change": "1"}), # NO MOD
    (['0', '0', '1', '1'], {"bits": ('Z', 'Z', 'Z', 'Z'), "error": '1', "change": "1"}), # NO MOD
    (['0', '1', 'Z', 'Z'], {"bits": ('0', '1', '1', '0'), "error": '0', "change": "1"}), # NO MOD
    (['0', '1', 'Z', '0'], {"bits": ('0', '1', '1', '0'), "error": '0', "change": "1"}), # NO MOD
    (['0', '1', 'Z', '1'], {"bits": ('Z', 'Z', 'Z', 'Z'), "error": '1', "change": "1"}), # NO MOD
    (['0', '1', '0', 'Z'], {"bits": ('Z', 'Z', 'Z', 'Z'), "error": '1', "change": "1"}), # NO MOD
    (['0', '1', '0', '0'], {"bits": ('Z', 'Z', 'Z', 'Z'), "error": '1', "change": "1"}), # NO MOD
    (['0', '1', '0', '1'], {"bits": ('Z', 'Z', 'Z', 'Z'), "error": '1', "change": "1"}), # NO MOD
    (['0', '1', '1', 'Z'], {"bits": ('0', '1', '1', '0'), "error": '0', "change": "1"}), # NO MOD
    (['0', '1', '1', '0'], {"bits": ('0', '1', '1', '0'), "error": '0', "change": "0"}), # NO MOD
    (['0', '1', '1', '1'], {"bits": ('Z', 'Z', 'Z', 'Z'), "error": '1', "change": "1"}), # NO MOD
    (['1', 'Z', 'Z', 'Z'], {"bits": ('1', 'Z', 'Z', 'Z'), "error": '0', "change": "0"}), # NO MOD
    (['1', 'Z', 'Z', '0'], {"bits": ('1', '0', '1', '0'), "error": '0', "change": "1"}), # NO MOD
    (['1', 'Z', 'Z', '1'], {"bits": ('1', '1', '0', '1'), "error": '0', "change": "1"}), # NO MOD
    (['1', 'Z', '0', 'Z'], {"bits": ('1', '1', '0', '1'), "error": '0', "change": "1"}), # NO MOD
    (['1', 'Z', '0', '0'], {"bits": ('Z', 'Z', 'Z', 'Z'), "error": '1', "change": "1"}), # NO MOD
    (['1', 'Z', '0', '1'], {"bits": ('1', '1', '0', '1'), "error": '0', "change": "1"}), # NO MOD
    (['1', 'Z', '1', 'Z'], {"bits": ('1', '0', '1', '0'), "error": '0', "change": "1"}), # NO MOD
    (['1', 'Z', '1', '0'], {"bits": ('1', '0', '1', '0'), "error": '0', "change": "1"}), # NO MOD
    (['1', 'Z', '1', '1'], {"bits": ('Z', 'Z', 'Z', 'Z'), "error": '1', "change": "1"}), # NO MOD
    (['1', '0', 'Z', 'Z'], {"bits": ('1', '0', '1', '0'), "error": '0', "change": "1"}), # NO MOD
    (['1', '0', 'Z', '0'], {"bits": ('1', '0', '1', '0'), "error": '0', "change": "1"}), # NO MOD
    (['1', '0', 'Z', '1'], {"bits": ('Z', 'Z', 'Z', 'Z'), "error": '1', "change": "1"}), # NO MOD
    (['1', '0', '0', 'Z'], {"bits": ('Z', 'Z', 'Z', 'Z'), "error": '1', "change": "1"}), # NO MOD
    (['1', '0', '0', '0'], {"bits": ('Z', 'Z', 'Z', 'Z'), "error": '1', "change": "1"}), # NO MOD
    (['1', '0', '0', '1'], {"bits": ('Z', 'Z', 'Z', 'Z'), "error": '1', "change": "1"}), # NO MOD
    (['1', '0', '1', 'Z'], {"bits": ('1', '0', '1', '0'), "error": '0', "change": "1"}), # NO MOD
    (['1', '0', '1', '0'], {"bits": ('1', '0', '1', '0'), "error": '0', "change": "0"}), # NO MOD
    (['1', '0', '1', '1'], {"bits": ('Z', 'Z', 'Z', 'Z'), "error": '1', "change": "1"}), # NO MOD
    (['1', '1', 'Z', 'Z'], {"bits": ('1', '1', '0', '1'), "error": '0', "change": "1"}), # NO MOD
    (['1', '1', 'Z', '0'], {"bits": ('Z', 'Z', 'Z', 'Z'), "error": '1', "change": "1"}), # NO MOD
    (['1', '1', 'Z', '1'], {"bits": ('1', '1', '0', '1'), "error": '0', "change": "1"}), # NO MOD
    (['1', '1', '0', 'Z'], {"bits": ('1', '1', '0', '1'), "error": '0', "change": "1"}), # NO MOD
    (['1', '1', '0', '0'], {"bits": ('Z', 'Z', 'Z', 'Z'), "error": '1', "change": "1"}), # NO MOD
    (['1', '1', '0', '1'], {"bits": ('1', '1', '0', '1'), "error": '0', "change": "0"}), # NO MOD
    (['1', '1', '1', 'Z'], {"bits": ('Z', 'Z', 'Z', 'Z'), "error": '1', "change": "1"}), # NO MOD
    (['1', '1', '1', '0'], {"bits": ('Z', 'Z', 'Z', 'Z'), "error": '1', "change": "1"}), # NO MOD
    (['1', '1', '1', '1'], {"bits": ('Z', 'Z', 'Z', 'Z'), "error": '1', "change": "1"}), # NO MOD
]

@pytest.mark.parametrize("io_bits,expected", test_data)
def test_half_adder_cases(io_bits, expected):
    assert HalfAdder(io_bits).solve() == expected
