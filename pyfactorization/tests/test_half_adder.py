from pyfactorization.HalfAdder import HalfAdder

def test_ha_case_ZZZZ():
    assert HalfAdder(['Z', 'Z', 'Z', 'Z']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z'), "error": '0', "change": "0"}) # NO MOD

def test_ha_case_ZZZ0():
    assert HalfAdder(['Z', 'Z', 'Z', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', '0'), "error": '0', "change": "0"}) # NO MOD

def test_ha_case_ZZZ1():
    assert HalfAdder(['Z', 'Z', 'Z', '1']).solve() == ({"bits": ('1', '1', '0', '1'), "error": '0', "change": "1"}) # NO MOD

def test_ha_case_ZZ0Z():
    assert HalfAdder(['Z', 'Z', '0', 'Z']).solve() == ({"bits": ('Z', 'Z', '0', 'Z'), "error": '0', "change": "0"}) # NO MOD

def test_ha_case_ZZ00():
    assert HalfAdder(['Z', 'Z', '0', '0']).solve() == ({"bits": ('0', '0', '0', '0'), "error": '0', "change": "1"}) #    MOD

def test_ha_case_ZZ01():
    assert HalfAdder(['Z', 'Z', '0', '1']).solve() == ({"bits": ('1', '1', '0', '1'), "error": '0', "change": "1"}) # NO MOD

def test_ha_case_ZZ1Z():
    assert HalfAdder(['Z', 'Z', '1', 'Z']).solve() == ({"bits": ('Z', 'Z', '1', '0'), "error": '0', "change": "1"}) #    MOD

def test_ha_case_ZZ10():
    assert HalfAdder(['Z', 'Z', '1', '0']).solve() == ({"bits": ('Z', 'Z', '1', '0'), "error": '0', "change": "0"}) # NO MOD

def test_ha_case_ZZ11():
    assert HalfAdder(['Z', 'Z', '1', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z'), "error": '1', "change": "1"}) # NO MOD

def test_ha_case_Z0ZZ():
    assert HalfAdder(['Z', '0', 'Z', 'Z']).solve() == ({"bits": ('Z', '0', 'Z', '0'), "error": '0', "change": "1"}) # NO MOD

def test_ha_case_Z0Z0():
    assert HalfAdder(['Z', '0', 'Z', '0']).solve() == ({"bits": ('Z', '0', 'Z', '0'), "error": '0', "change": "0"}) # NO MOD

def test_ha_case_Z0Z1():
    assert HalfAdder(['Z', '0', 'Z', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z'), "error": '1', "change": "1"}) # NO MOD

def test_ha_case_Z00Z():
    assert HalfAdder(['Z', '0', '0', 'Z']).solve() == ({"bits": ('0', '0', '0', '0'), "error": '0', "change": "1"}) # NO MOD

def test_ha_case_Z000():
    assert HalfAdder(['Z', '0', '0', '0']).solve() == ({"bits": ('0', '0', '0', '0'), "error": '0', "change": "1"}) # NO MOD

def test_ha_case_Z001():
    assert HalfAdder(['Z', '0', '0', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z'), "error": '1', "change": "1"}) # NO MOD

def test_ha_case_Z01Z():
    assert HalfAdder(['Z', '0', '1', 'Z']).solve() == ({"bits": ('1', '0', '1', '0'), "error": '0', "change": "1"}) # NO MOD

def test_ha_case_Z010():
    assert HalfAdder(['Z', '0', '1', '0']).solve() == ({"bits": ('1', '0', '1', '0'), "error": '0', "change": "1"}) # NO MOD

def test_ha_case_Z011():
    assert HalfAdder(['Z', '0', '1', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z'), "error": '1', "change": "1"}) # NO MOD

def test_ha_case_Z1ZZ():
    assert HalfAdder(['Z', '1', 'Z', 'Z']).solve() == ({"bits": ('Z', '1', 'Z', 'Z'), "error": '0', "change": "0"}) # NO MOD

def test_ha_case_Z1Z0():
    assert HalfAdder(['Z', '1', 'Z', '0']).solve() == ({"bits": ('0', '1', '1', '0'), "error": '0', "change": "1"}) # NO MOD

def test_ha_case_Z1Z1():
    assert HalfAdder(['Z', '1', 'Z', '1']).solve() == ({"bits": ('1', '1', '0', '1'), "error": '0', "change": "1"}) # NO MOD

def test_ha_case_Z10Z():
    assert HalfAdder(['Z', '1', '0', 'Z']).solve() == ({"bits": ('1', '1', '0', '1'), "error": '0', "change": "1"}) # NO MOD

def test_ha_case_Z100():
    assert HalfAdder(['Z', '1', '0', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z'), "error": '1', "change": "1"}) # NO MOD

def test_ha_case_Z101():
    assert HalfAdder(['Z', '1', '0', '1']).solve() == ({"bits": ('1', '1', '0', '1'), "error": '0', "change": "1"}) # NO MOD

def test_ha_case_Z11Z():
    assert HalfAdder(['Z', '1', '1', 'Z']).solve() == ({"bits": ('0', '1', '1', '0'), "error": '0', "change": "1"}) # NO MOD

def test_ha_case_Z110():
    assert HalfAdder(['Z', '1', '1', '0']).solve() == ({"bits": ('0', '1', '1', '0'), "error": '0', "change": "1"}) # NO MOD

def test_ha_case_Z111():
    assert HalfAdder(['Z', '1', '1', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z'), "error": '1', "change": "1"}) # NO MOD

def test_ha_case_0ZZZ():
    assert HalfAdder(['0', 'Z', 'Z', 'Z']).solve() == ({"bits": ('0', 'Z', 'Z', '0'), "error": '0', "change": "1"}) # NO MOD

def test_ha_case_0ZZ0():
    assert HalfAdder(['0', 'Z', 'Z', '0']).solve() == ({"bits": ('0', 'Z', 'Z', '0'), "error": '0', "change": "0"}) # NO MOD

def test_ha_case_0ZZ1():
    assert HalfAdder(['0', 'Z', 'Z', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z'), "error": '1', "change": "1"}) # NO MOD

def test_ha_case_0Z0Z():
    assert HalfAdder(['0', 'Z', '0', 'Z']).solve() == ({"bits": ('0', '0', '0', '0'), "error": '0', "change": "1"}) # NO MOD

def test_ha_case_0Z00():
    assert HalfAdder(['0', 'Z', '0', '0']).solve() == ({"bits": ('0', '0', '0', '0'), "error": '0', "change": "1"}) # NO MOD

def test_ha_case_0Z01():
    assert HalfAdder(['0', 'Z', '0', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z'), "error": '1', "change": "1"}) # NO MOD

def test_ha_case_0Z1Z():
    assert HalfAdder(['0', 'Z', '1', 'Z']).solve() == ({"bits": ('0', '1', '1', '0'), "error": '0', "change": "1"}) # NO MOD

def test_ha_case_0Z10():
    assert HalfAdder(['0', 'Z', '1', '0']).solve() == ({"bits": ('0', '1', '1', '0'), "error": '0', "change": "1"}) # NO MOD

def test_ha_case_0Z11():
    assert HalfAdder(['0', 'Z', '1', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z'), "error": '1', "change": "1"}) # NO MOD

def test_ha_case_00ZZ():
    assert HalfAdder(['0', '0', 'Z', 'Z']).solve() == ({"bits": ('0', '0', '0', '0'), "error": '0', "change": "1"}) # NO MOD

def test_ha_case_00Z0():
    assert HalfAdder(['0', '0', 'Z', '0']).solve() == ({"bits": ('0', '0', '0', '0'), "error": '0', "change": "1"}) # NO MOD

def test_ha_case_00Z1():
    assert HalfAdder(['0', '0', 'Z', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z'), "error": '1', "change": "1"}) # NO MOD

def test_ha_case_000Z():
    assert HalfAdder(['0', '0', '0', 'Z']).solve() == ({"bits": ('0', '0', '0', '0'), "error": '0', "change": "1"}) # NO MOD

def test_ha_case_0000():
    assert HalfAdder(['0', '0', '0', '0']).solve() == ({"bits": ('0', '0', '0', '0'), "error": '0', "change": "0"}) # NO MOD

def test_ha_case_0001():
    assert HalfAdder(['0', '0', '0', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z'), "error": '1', "change": "1"}) # NO MOD

def test_ha_case_001Z():
    assert HalfAdder(['0', '0', '1', 'Z']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z'), "error": '1', "change": "1"}) # NO MOD

def test_ha_case_0010():
    assert HalfAdder(['0', '0', '1', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z'), "error": '1', "change": "1"}) # NO MOD

def test_ha_case_0011():
    assert HalfAdder(['0', '0', '1', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z'), "error": '1', "change": "1"}) # NO MOD

def test_ha_case_01ZZ():
    assert HalfAdder(['0', '1', 'Z', 'Z']).solve() == ({"bits": ('0', '1', '1', '0'), "error": '0', "change": "1"}) # NO MOD

def test_ha_case_01Z0():
    assert HalfAdder(['0', '1', 'Z', '0']).solve() == ({"bits": ('0', '1', '1', '0'), "error": '0', "change": "1"}) # NO MOD

def test_ha_case_01Z1():
    assert HalfAdder(['0', '1', 'Z', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z'), "error": '1', "change": "1"}) # NO MOD

def test_ha_case_010Z():
    assert HalfAdder(['0', '1', '0', 'Z']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z'), "error": '1', "change": "1"}) # NO MOD

def test_ha_case_0100():
    assert HalfAdder(['0', '1', '0', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z'), "error": '1', "change": "1"}) # NO MOD

def test_ha_case_0101():
    assert HalfAdder(['0', '1', '0', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z'), "error": '1', "change": "1"}) # NO MOD

def test_ha_case_011Z():
    assert HalfAdder(['0', '1', '1', 'Z']).solve() == ({"bits": ('0', '1', '1', '0'), "error": '0', "change": "1"}) # NO MOD

def test_ha_case_0110():
    assert HalfAdder(['0', '1', '1', '0']).solve() == ({"bits": ('0', '1', '1', '0'), "error": '0', "change": "0"}) # NO MOD

def test_ha_case_0111():
    assert HalfAdder(['0', '1', '1', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z'), "error": '1', "change": "1"}) # NO MOD

def test_ha_case_1ZZZ():
    assert HalfAdder(['1', 'Z', 'Z', 'Z']).solve() == ({"bits": ('1', 'Z', 'Z', 'Z'), "error": '0', "change": "0"}) # NO MOD

def test_ha_case_1ZZ0():
    assert HalfAdder(['1', 'Z', 'Z', '0']).solve() == ({"bits": ('1', '0', '1', '0'), "error": '0', "change": "1"}) # NO MOD

def test_ha_case_1ZZ1():
    assert HalfAdder(['1', 'Z', 'Z', '1']).solve() == ({"bits": ('1', '1', '0', '1'), "error": '0', "change": "1"}) # NO MOD

def test_ha_case_1Z0Z():
    assert HalfAdder(['1', 'Z', '0', 'Z']).solve() == ({"bits": ('1', '1', '0', '1'), "error": '0', "change": "1"}) # NO MOD

def test_ha_case_1Z00():
    assert HalfAdder(['1', 'Z', '0', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z'), "error": '1', "change": "1"}) # NO MOD

def test_ha_case_1Z01():
    assert HalfAdder(['1', 'Z', '0', '1']).solve() == ({"bits": ('1', '1', '0', '1'), "error": '0', "change": "1"}) # NO MOD

def test_ha_case_1Z1Z():
    assert HalfAdder(['1', 'Z', '1', 'Z']).solve() == ({"bits": ('1', '0', '1', '0'), "error": '0', "change": "1"}) # NO MOD

def test_ha_case_1Z10():
    assert HalfAdder(['1', 'Z', '1', '0']).solve() == ({"bits": ('1', '0', '1', '0'), "error": '0', "change": "1"}) # NO MOD

def test_ha_case_1Z11():
    assert HalfAdder(['1', 'Z', '1', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z'), "error": '1', "change": "1"}) # NO MOD

def test_ha_case_10ZZ():
    assert HalfAdder(['1', '0', 'Z', 'Z']).solve() == ({"bits": ('1', '0', '1', '0'), "error": '0', "change": "1"}) # NO MOD

def test_ha_case_10Z0():
    assert HalfAdder(['1', '0', 'Z', '0']).solve() == ({"bits": ('1', '0', '1', '0'), "error": '0', "change": "1"}) # NO MOD

def test_ha_case_10Z1():
    assert HalfAdder(['1', '0', 'Z', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z'), "error": '1', "change": "1"}) # NO MOD

def test_ha_case_100Z():
    assert HalfAdder(['1', '0', '0', 'Z']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z'), "error": '1', "change": "1"}) # NO MOD

def test_ha_case_1000():
    assert HalfAdder(['1', '0', '0', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z'), "error": '1', "change": "1"}) # NO MOD

def test_ha_case_1001():
    assert HalfAdder(['1', '0', '0', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z'), "error": '1', "change": "1"}) # NO MOD

def test_ha_case_101Z():
    assert HalfAdder(['1', '0', '1', 'Z']).solve() == ({"bits": ('1', '0', '1', '0'), "error": '0', "change": "1"}) # NO MOD

def test_ha_case_1010():
    assert HalfAdder(['1', '0', '1', '0']).solve() == ({"bits": ('1', '0', '1', '0'), "error": '0', "change": "0"}) # NO MOD

def test_ha_case_1011():
    assert HalfAdder(['1', '0', '1', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z'), "error": '1', "change": "1"}) # NO MOD

def test_ha_case_11ZZ():
    assert HalfAdder(['1', '1', 'Z', 'Z']).solve() == ({"bits": ('1', '1', '0', '1'), "error": '0', "change": "1"}) # NO MOD

def test_ha_case_11Z0():
    assert HalfAdder(['1', '1', 'Z', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z'), "error": '1', "change": "1"}) # NO MOD

def test_ha_case_11Z1():
    assert HalfAdder(['1', '1', 'Z', '1']).solve() == ({"bits": ('1', '1', '0', '1'), "error": '0', "change": "1"}) # NO MOD

def test_ha_case_110Z():
    assert HalfAdder(['1', '1', '0', 'Z']).solve() == ({"bits": ('1', '1', '0', '1'), "error": '0', "change": "1"}) # NO MOD

def test_ha_case_1100():
    assert HalfAdder(['1', '1', '0', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z'), "error": '1', "change": "1"}) # NO MOD

def test_ha_case_1101():
    assert HalfAdder(['1', '1', '0', '1']).solve() == ({"bits": ('1', '1', '0', '1'), "error": '0', "change": "0"}) # NO MOD

def test_ha_case_111Z():
    assert HalfAdder(['1', '1', '1', 'Z']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z'), "error": '1', "change": "1"}) # NO MOD

def test_ha_case_1110():
    assert HalfAdder(['1', '1', '1', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z'), "error": '1', "change": "1"}) # NO MOD

def test_ha_case_1111():
    assert HalfAdder(['1', '1', '1', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z'), "error": '1', "change": "1"}) # NO MOD
