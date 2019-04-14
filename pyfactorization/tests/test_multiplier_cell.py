from pyfactorization.MultiplierCell import MultiplierCell

def test_mc_case_ZZZZZZ():
    assert MultiplierCell(['Z', 'Z', 'Z', 'Z', 'Z', 'Z']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_ZZZZZ0():
    assert MultiplierCell(['Z', 'Z', 'Z', 'Z', 'Z', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', '0'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_ZZZZZ1():
    assert MultiplierCell(['Z', 'Z', 'Z', 'Z', 'Z', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', '1'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_ZZZZ0Z():
    assert MultiplierCell(['Z', 'Z', 'Z', 'Z', '0', 'Z']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', '0', 'Z'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_ZZZZ00():
    assert MultiplierCell(['Z', 'Z', 'Z', 'Z', '0', '0']).solve() == ({"bits": ('Z', 'Z', '0', '0', '0', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_ZZZZ01():
    assert MultiplierCell(['Z', 'Z', 'Z', 'Z', '0', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', '0', '1'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_ZZZZ1Z():
    assert MultiplierCell(['Z', 'Z', 'Z', 'Z', '1', 'Z']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', '1', 'Z'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_ZZZZ10():
    assert MultiplierCell(['Z', 'Z', 'Z', 'Z', '1', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', '1', '0'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_ZZZZ11():
    assert MultiplierCell(['Z', 'Z', 'Z', 'Z', '1', '1']).solve() == ({"bits": ('1', '1', '1', '1', '1', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_ZZZ0ZZ():
    assert MultiplierCell(['Z', 'Z', 'Z', '0', 'Z', 'Z']).solve() == ({"bits": ('Z', 'Z', 'Z', '0', 'Z', 'Z'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_ZZZ0Z0():
    assert MultiplierCell(['Z', 'Z', 'Z', '0', 'Z', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', '0', 'Z', '0'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_ZZZ0Z1():
    assert MultiplierCell(['Z', 'Z', 'Z', '0', 'Z', '1']).solve() == ({"bits": ('1', '1', '1', '0', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_ZZZ00Z():
    assert MultiplierCell(['Z', 'Z', 'Z', '0', '0', 'Z']).solve() == ({"bits": ('Z', 'Z', 'Z', '0', '0', 'Z'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_ZZZ000():
    assert MultiplierCell(['Z', 'Z', 'Z', '0', '0', '0']).solve() == ({"bits": ('Z', 'Z', '0', '0', '0', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_ZZZ001():
    assert MultiplierCell(['Z', 'Z', 'Z', '0', '0', '1']).solve() == ({"bits": ('1', '1', '1', '0', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_ZZZ01Z():
    assert MultiplierCell(['Z', 'Z', 'Z', '0', '1', 'Z']).solve() == ({"bits": ('Z', 'Z', 'Z', '0', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_ZZZ010():
    assert MultiplierCell(['Z', 'Z', 'Z', '0', '1', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', '0', '1', '0'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_ZZZ011():
    assert MultiplierCell(['Z', 'Z', 'Z', '0', '1', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_ZZZ1ZZ():
    assert MultiplierCell(['Z', 'Z', 'Z', '1', 'Z', 'Z']).solve() == ({"bits": ('Z', 'Z', 'Z', '1', 'Z', 'Z'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_ZZZ1Z0():
    assert MultiplierCell(['Z', 'Z', 'Z', '1', 'Z', '0']).solve() == ({"bits": ('Z', 'Z', '0', '1', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_ZZZ1Z1():
    assert MultiplierCell(['Z', 'Z', 'Z', '1', 'Z', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', '1', 'Z', '1'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_ZZZ10Z():
    assert MultiplierCell(['Z', 'Z', 'Z', '1', '0', 'Z']).solve() == ({"bits": ('Z', 'Z', 'Z', '1', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_ZZZ100():
    assert MultiplierCell(['Z', 'Z', 'Z', '1', '0', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_ZZZ101():
    assert MultiplierCell(['Z', 'Z', 'Z', '1', '0', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', '1', '0', '1'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_ZZZ11Z():
    assert MultiplierCell(['Z', 'Z', 'Z', '1', '1', 'Z']).solve() == ({"bits": ('Z', 'Z', 'Z', '1', '1', 'Z'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_ZZZ110():
    assert MultiplierCell(['Z', 'Z', 'Z', '1', '1', '0']).solve() == ({"bits": ('Z', 'Z', '0', '1', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_ZZZ111():
    assert MultiplierCell(['Z', 'Z', 'Z', '1', '1', '1']).solve() == ({"bits": ('1', '1', '1', '1', '1', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_ZZ0ZZZ():
    assert MultiplierCell(['Z', 'Z', '0', 'Z', 'Z', 'Z']).solve() == ({"bits": ('Z', 'Z', '0', 'Z', 'Z', 'Z'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_ZZ0ZZ0():
    assert MultiplierCell(['Z', 'Z', '0', 'Z', 'Z', '0']).solve() == ({"bits": ('Z', 'Z', '0', 'Z', 'Z', '0'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_ZZ0ZZ1():
    assert MultiplierCell(['Z', 'Z', '0', 'Z', 'Z', '1']).solve() == ({"bits": ('1', '1', '0', '1', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_ZZ0Z0Z():
    assert MultiplierCell(['Z', 'Z', '0', 'Z', '0', 'Z']).solve() == ({"bits": ('Z', 'Z', '0', 'Z', '0', 'Z'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_ZZ0Z00():
    assert MultiplierCell(['Z', 'Z', '0', 'Z', '0', '0']).solve() == ({"bits": ('Z', 'Z', '0', '0', '0', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_ZZ0Z01():
    assert MultiplierCell(['Z', 'Z', '0', 'Z', '0', '1']).solve() == ({"bits": ('1', '1', '0', '1', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_ZZ0Z1Z():
    assert MultiplierCell(['Z', 'Z', '0', 'Z', '1', 'Z']).solve() == ({"bits": ('Z', 'Z', '0', 'Z', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_ZZ0Z10():
    assert MultiplierCell(['Z', 'Z', '0', 'Z', '1', '0']).solve() == ({"bits": ('Z', 'Z', '0', 'Z', '1', '0'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_ZZ0Z11():
    assert MultiplierCell(['Z', 'Z', '0', 'Z', '1', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_ZZ00ZZ():
    assert MultiplierCell(['Z', 'Z', '0', '0', 'Z', 'Z']).solve() == ({"bits": ('Z', 'Z', '0', '0', 'Z', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_ZZ00Z0():
    assert MultiplierCell(['Z', 'Z', '0', '0', 'Z', '0']).solve() == ({"bits": ('Z', 'Z', '0', '0', 'Z', '0'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_ZZ00Z1():
    assert MultiplierCell(['Z', 'Z', '0', '0', 'Z', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_ZZ000Z():
    assert MultiplierCell(['Z', 'Z', '0', '0', '0', 'Z']).solve() == ({"bits": ('Z', 'Z', '0', '0', '0', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_ZZ0000():
    assert MultiplierCell(['Z', 'Z', '0', '0', '0', '0']).solve() == ({"bits": ('Z', 'Z', '0', '0', '0', '0'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_ZZ0001():
    assert MultiplierCell(['Z', 'Z', '0', '0', '0', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_ZZ001Z():
    assert MultiplierCell(['Z', 'Z', '0', '0', '1', 'Z']).solve() == ({"bits": ('1', '1', '0', '0', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_ZZ0010():
    assert MultiplierCell(['Z', 'Z', '0', '0', '1', '0']).solve() == ({"bits": ('1', '1', '0', '0', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_ZZ0011():
    assert MultiplierCell(['Z', 'Z', '0', '0', '1', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_ZZ01ZZ():
    assert MultiplierCell(['Z', 'Z', '0', '1', 'Z', 'Z']).solve() == ({"bits": ('Z', 'Z', '0', '1', 'Z', 'Z'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_ZZ01Z0():
    assert MultiplierCell(['Z', 'Z', '0', '1', 'Z', '0']).solve() == ({"bits": ('Z', 'Z', '0', '1', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_ZZ01Z1():
    assert MultiplierCell(['Z', 'Z', '0', '1', 'Z', '1']).solve() == ({"bits": ('1', '1', '0', '1', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_ZZ010Z():
    assert MultiplierCell(['Z', 'Z', '0', '1', '0', 'Z']).solve() == ({"bits": ('1', '1', '0', '1', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_ZZ0100():
    assert MultiplierCell(['Z', 'Z', '0', '1', '0', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_ZZ0101():
    assert MultiplierCell(['Z', 'Z', '0', '1', '0', '1']).solve() == ({"bits": ('1', '1', '0', '1', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_ZZ011Z():
    assert MultiplierCell(['Z', 'Z', '0', '1', '1', 'Z']).solve() == ({"bits": ('Z', 'Z', '0', '1', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_ZZ0110():
    assert MultiplierCell(['Z', 'Z', '0', '1', '1', '0']).solve() == ({"bits": ('Z', 'Z', '0', '1', '1', '0'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_ZZ0111():
    assert MultiplierCell(['Z', 'Z', '0', '1', '1', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_ZZ1ZZZ():
    assert MultiplierCell(['Z', 'Z', '1', 'Z', 'Z', 'Z']).solve() == ({"bits": ('Z', 'Z', '1', 'Z', 'Z', 'Z'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_ZZ1ZZ0():
    assert MultiplierCell(['Z', 'Z', '1', 'Z', 'Z', '0']).solve() == ({"bits": ('Z', 'Z', '1', '0', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_ZZ1ZZ1():
    assert MultiplierCell(['Z', 'Z', '1', 'Z', 'Z', '1']).solve() == ({"bits": ('Z', 'Z', '1', 'Z', 'Z', '1'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_ZZ1Z0Z():
    assert MultiplierCell(['Z', 'Z', '1', 'Z', '0', 'Z']).solve() == ({"bits": ('Z', 'Z', '1', 'Z', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_ZZ1Z00():
    assert MultiplierCell(['Z', 'Z', '1', 'Z', '0', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_ZZ1Z01():
    assert MultiplierCell(['Z', 'Z', '1', 'Z', '0', '1']).solve() == ({"bits": ('Z', 'Z', '1', 'Z', '0', '1'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_ZZ1Z1Z():
    assert MultiplierCell(['Z', 'Z', '1', 'Z', '1', 'Z']).solve() == ({"bits": ('Z', 'Z', '1', 'Z', '1', 'Z'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_ZZ1Z10():
    assert MultiplierCell(['Z', 'Z', '1', 'Z', '1', '0']).solve() == ({"bits": ('Z', 'Z', '1', '0', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_ZZ1Z11():
    assert MultiplierCell(['Z', 'Z', '1', 'Z', '1', '1']).solve() == ({"bits": ('1', '1', '1', '1', '1', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_ZZ10ZZ():
    assert MultiplierCell(['Z', 'Z', '1', '0', 'Z', 'Z']).solve() == ({"bits": ('Z', 'Z', '1', '0', 'Z', 'Z'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_ZZ10Z0():
    assert MultiplierCell(['Z', 'Z', '1', '0', 'Z', '0']).solve() == ({"bits": ('Z', 'Z', '1', '0', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_ZZ10Z1():
    assert MultiplierCell(['Z', 'Z', '1', '0', 'Z', '1']).solve() == ({"bits": ('1', '1', '1', '0', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_ZZ100Z():
    assert MultiplierCell(['Z', 'Z', '1', '0', '0', 'Z']).solve() == ({"bits": ('1', '1', '1', '0', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_ZZ1000():
    assert MultiplierCell(['Z', 'Z', '1', '0', '0', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_ZZ1001():
    assert MultiplierCell(['Z', 'Z', '1', '0', '0', '1']).solve() == ({"bits": ('1', '1', '1', '0', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_ZZ101Z():
    assert MultiplierCell(['Z', 'Z', '1', '0', '1', 'Z']).solve() == ({"bits": ('Z', 'Z', '1', '0', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_ZZ1010():
    assert MultiplierCell(['Z', 'Z', '1', '0', '1', '0']).solve() == ({"bits": ('Z', 'Z', '1', '0', '1', '0'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_ZZ1011():
    assert MultiplierCell(['Z', 'Z', '1', '0', '1', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_ZZ11ZZ():
    assert MultiplierCell(['Z', 'Z', '1', '1', 'Z', 'Z']).solve() == ({"bits": ('Z', 'Z', '1', '1', 'Z', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_ZZ11Z0():
    assert MultiplierCell(['Z', 'Z', '1', '1', 'Z', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_ZZ11Z1():
    assert MultiplierCell(['Z', 'Z', '1', '1', 'Z', '1']).solve() == ({"bits": ('Z', 'Z', '1', '1', 'Z', '1'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_ZZ110Z():
    assert MultiplierCell(['Z', 'Z', '1', '1', '0', 'Z']).solve() == ({"bits": ('Z', 'Z', '1', '1', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_ZZ1100():
    assert MultiplierCell(['Z', 'Z', '1', '1', '0', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_ZZ1101():
    assert MultiplierCell(['Z', 'Z', '1', '1', '0', '1']).solve() == ({"bits": ('Z', 'Z', '1', '1', '0', '1'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_ZZ111Z():
    assert MultiplierCell(['Z', 'Z', '1', '1', '1', 'Z']).solve() == ({"bits": ('1', '1', '1', '1', '1', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_ZZ1110():
    assert MultiplierCell(['Z', 'Z', '1', '1', '1', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_ZZ1111():
    assert MultiplierCell(['Z', 'Z', '1', '1', '1', '1']).solve() == ({"bits": ('1', '1', '1', '1', '1', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_Z0ZZZZ():
    assert MultiplierCell(['Z', '0', 'Z', 'Z', 'Z', 'Z']).solve() == ({"bits": ('Z', '0', 'Z', 'Z', 'Z', 'Z'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_Z0ZZZ0():
    assert MultiplierCell(['Z', '0', 'Z', 'Z', 'Z', '0']).solve() == ({"bits": ('Z', '0', 'Z', 'Z', 'Z', '0'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_Z0ZZZ1():
    assert MultiplierCell(['Z', '0', 'Z', 'Z', 'Z', '1']).solve() == ({"bits": ('Z', '0', '1', '1', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_Z0ZZ0Z():
    assert MultiplierCell(['Z', '0', 'Z', 'Z', '0', 'Z']).solve() == ({"bits": ('Z', '0', 'Z', 'Z', '0', 'Z'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_Z0ZZ00():
    assert MultiplierCell(['Z', '0', 'Z', 'Z', '0', '0']).solve() == ({"bits": ('Z', '0', '0', '0', '0', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_Z0ZZ01():
    assert MultiplierCell(['Z', '0', 'Z', 'Z', '0', '1']).solve() == ({"bits": ('Z', '0', '1', '1', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_Z0ZZ1Z():
    assert MultiplierCell(['Z', '0', 'Z', 'Z', '1', 'Z']).solve() == ({"bits": ('Z', '0', 'Z', 'Z', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_Z0ZZ10():
    assert MultiplierCell(['Z', '0', 'Z', 'Z', '1', '0']).solve() == ({"bits": ('Z', '0', 'Z', 'Z', '1', '0'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_Z0ZZ11():
    assert MultiplierCell(['Z', '0', 'Z', 'Z', '1', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_Z0Z0ZZ():
    assert MultiplierCell(['Z', '0', 'Z', '0', 'Z', 'Z']).solve() == ({"bits": ('Z', '0', 'Z', '0', 'Z', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_Z0Z0Z0():
    assert MultiplierCell(['Z', '0', 'Z', '0', 'Z', '0']).solve() == ({"bits": ('Z', '0', 'Z', '0', 'Z', '0'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_Z0Z0Z1():
    assert MultiplierCell(['Z', '0', 'Z', '0', 'Z', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_Z0Z00Z():
    assert MultiplierCell(['Z', '0', 'Z', '0', '0', 'Z']).solve() == ({"bits": ('Z', '0', '0', '0', '0', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_Z0Z000():
    assert MultiplierCell(['Z', '0', 'Z', '0', '0', '0']).solve() == ({"bits": ('Z', '0', '0', '0', '0', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_Z0Z001():
    assert MultiplierCell(['Z', '0', 'Z', '0', '0', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_Z0Z01Z():
    assert MultiplierCell(['Z', '0', 'Z', '0', '1', 'Z']).solve() == ({"bits": ('Z', '0', '1', '0', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_Z0Z010():
    assert MultiplierCell(['Z', '0', 'Z', '0', '1', '0']).solve() == ({"bits": ('Z', '0', '1', '0', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_Z0Z011():
    assert MultiplierCell(['Z', '0', 'Z', '0', '1', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_Z0Z1ZZ():
    assert MultiplierCell(['Z', '0', 'Z', '1', 'Z', 'Z']).solve() == ({"bits": ('Z', '0', 'Z', '1', 'Z', 'Z'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_Z0Z1Z0():
    assert MultiplierCell(['Z', '0', 'Z', '1', 'Z', '0']).solve() == ({"bits": ('Z', '0', '0', '1', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_Z0Z1Z1():
    assert MultiplierCell(['Z', '0', 'Z', '1', 'Z', '1']).solve() == ({"bits": ('Z', '0', '1', '1', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_Z0Z10Z():
    assert MultiplierCell(['Z', '0', 'Z', '1', '0', 'Z']).solve() == ({"bits": ('Z', '0', '1', '1', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_Z0Z100():
    assert MultiplierCell(['Z', '0', 'Z', '1', '0', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_Z0Z101():
    assert MultiplierCell(['Z', '0', 'Z', '1', '0', '1']).solve() == ({"bits": ('Z', '0', '1', '1', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_Z0Z11Z():
    assert MultiplierCell(['Z', '0', 'Z', '1', '1', 'Z']).solve() == ({"bits": ('Z', '0', '0', '1', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_Z0Z110():
    assert MultiplierCell(['Z', '0', 'Z', '1', '1', '0']).solve() == ({"bits": ('Z', '0', '0', '1', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_Z0Z111():
    assert MultiplierCell(['Z', '0', 'Z', '1', '1', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_Z00ZZZ():
    assert MultiplierCell(['Z', '0', '0', 'Z', 'Z', 'Z']).solve() == ({"bits": ('Z', '0', '0', 'Z', 'Z', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_Z00ZZ0():
    assert MultiplierCell(['Z', '0', '0', 'Z', 'Z', '0']).solve() == ({"bits": ('Z', '0', '0', 'Z', 'Z', '0'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_Z00ZZ1():
    assert MultiplierCell(['Z', '0', '0', 'Z', 'Z', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_Z00Z0Z():
    assert MultiplierCell(['Z', '0', '0', 'Z', '0', 'Z']).solve() == ({"bits": ('Z', '0', '0', '0', '0', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_Z00Z00():
    assert MultiplierCell(['Z', '0', '0', 'Z', '0', '0']).solve() == ({"bits": ('Z', '0', '0', '0', '0', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_Z00Z01():
    assert MultiplierCell(['Z', '0', '0', 'Z', '0', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_Z00Z1Z():
    assert MultiplierCell(['Z', '0', '0', 'Z', '1', 'Z']).solve() == ({"bits": ('Z', '0', '0', '1', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_Z00Z10():
    assert MultiplierCell(['Z', '0', '0', 'Z', '1', '0']).solve() == ({"bits": ('Z', '0', '0', '1', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_Z00Z11():
    assert MultiplierCell(['Z', '0', '0', 'Z', '1', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_Z000ZZ():
    assert MultiplierCell(['Z', '0', '0', '0', 'Z', 'Z']).solve() == ({"bits": ('Z', '0', '0', '0', '0', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_Z000Z0():
    assert MultiplierCell(['Z', '0', '0', '0', 'Z', '0']).solve() == ({"bits": ('Z', '0', '0', '0', '0', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_Z000Z1():
    assert MultiplierCell(['Z', '0', '0', '0', 'Z', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_Z0000Z():
    assert MultiplierCell(['Z', '0', '0', '0', '0', 'Z']).solve() == ({"bits": ('Z', '0', '0', '0', '0', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_Z00000():
    assert MultiplierCell(['Z', '0', '0', '0', '0', '0']).solve() == ({"bits": ('Z', '0', '0', '0', '0', '0'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_Z00001():
    assert MultiplierCell(['Z', '0', '0', '0', '0', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_Z0001Z():
    assert MultiplierCell(['Z', '0', '0', '0', '1', 'Z']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_Z00010():
    assert MultiplierCell(['Z', '0', '0', '0', '1', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_Z00011():
    assert MultiplierCell(['Z', '0', '0', '0', '1', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_Z001ZZ():
    assert MultiplierCell(['Z', '0', '0', '1', 'Z', 'Z']).solve() == ({"bits": ('Z', '0', '0', '1', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_Z001Z0():
    assert MultiplierCell(['Z', '0', '0', '1', 'Z', '0']).solve() == ({"bits": ('Z', '0', '0', '1', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_Z001Z1():
    assert MultiplierCell(['Z', '0', '0', '1', 'Z', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_Z0010Z():
    assert MultiplierCell(['Z', '0', '0', '1', '0', 'Z']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_Z00100():
    assert MultiplierCell(['Z', '0', '0', '1', '0', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_Z00101():
    assert MultiplierCell(['Z', '0', '0', '1', '0', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_Z0011Z():
    assert MultiplierCell(['Z', '0', '0', '1', '1', 'Z']).solve() == ({"bits": ('Z', '0', '0', '1', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_Z00110():
    assert MultiplierCell(['Z', '0', '0', '1', '1', '0']).solve() == ({"bits": ('Z', '0', '0', '1', '1', '0'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_Z00111():
    assert MultiplierCell(['Z', '0', '0', '1', '1', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_Z01ZZZ():
    assert MultiplierCell(['Z', '0', '1', 'Z', 'Z', 'Z']).solve() == ({"bits": ('Z', '0', '1', 'Z', 'Z', 'Z'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_Z01ZZ0():
    assert MultiplierCell(['Z', '0', '1', 'Z', 'Z', '0']).solve() == ({"bits": ('Z', '0', '1', '0', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_Z01ZZ1():
    assert MultiplierCell(['Z', '0', '1', 'Z', 'Z', '1']).solve() == ({"bits": ('Z', '0', '1', '1', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_Z01Z0Z():
    assert MultiplierCell(['Z', '0', '1', 'Z', '0', 'Z']).solve() == ({"bits": ('Z', '0', '1', '1', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_Z01Z00():
    assert MultiplierCell(['Z', '0', '1', 'Z', '0', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_Z01Z01():
    assert MultiplierCell(['Z', '0', '1', 'Z', '0', '1']).solve() == ({"bits": ('Z', '0', '1', '1', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_Z01Z1Z():
    assert MultiplierCell(['Z', '0', '1', 'Z', '1', 'Z']).solve() == ({"bits": ('Z', '0', '1', '0', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_Z01Z10():
    assert MultiplierCell(['Z', '0', '1', 'Z', '1', '0']).solve() == ({"bits": ('Z', '0', '1', '0', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_Z01Z11():
    assert MultiplierCell(['Z', '0', '1', 'Z', '1', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_Z010ZZ():
    assert MultiplierCell(['Z', '0', '1', '0', 'Z', 'Z']).solve() == ({"bits": ('Z', '0', '1', '0', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_Z010Z0():
    assert MultiplierCell(['Z', '0', '1', '0', 'Z', '0']).solve() == ({"bits": ('Z', '0', '1', '0', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_Z010Z1():
    assert MultiplierCell(['Z', '0', '1', '0', 'Z', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_Z0100Z():
    assert MultiplierCell(['Z', '0', '1', '0', '0', 'Z']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_Z01000():
    assert MultiplierCell(['Z', '0', '1', '0', '0', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_Z01001():
    assert MultiplierCell(['Z', '0', '1', '0', '0', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_Z0101Z():
    assert MultiplierCell(['Z', '0', '1', '0', '1', 'Z']).solve() == ({"bits": ('Z', '0', '1', '0', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_Z01010():
    assert MultiplierCell(['Z', '0', '1', '0', '1', '0']).solve() == ({"bits": ('Z', '0', '1', '0', '1', '0'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_Z01011():
    assert MultiplierCell(['Z', '0', '1', '0', '1', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_Z011ZZ():
    assert MultiplierCell(['Z', '0', '1', '1', 'Z', 'Z']).solve() == ({"bits": ('Z', '0', '1', '1', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_Z011Z0():
    assert MultiplierCell(['Z', '0', '1', '1', 'Z', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_Z011Z1():
    assert MultiplierCell(['Z', '0', '1', '1', 'Z', '1']).solve() == ({"bits": ('Z', '0', '1', '1', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_Z0110Z():
    assert MultiplierCell(['Z', '0', '1', '1', '0', 'Z']).solve() == ({"bits": ('Z', '0', '1', '1', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_Z01100():
    assert MultiplierCell(['Z', '0', '1', '1', '0', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_Z01101():
    assert MultiplierCell(['Z', '0', '1', '1', '0', '1']).solve() == ({"bits": ('Z', '0', '1', '1', '0', '1'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_Z0111Z():
    assert MultiplierCell(['Z', '0', '1', '1', '1', 'Z']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_Z01110():
    assert MultiplierCell(['Z', '0', '1', '1', '1', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_Z01111():
    assert MultiplierCell(['Z', '0', '1', '1', '1', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_Z1ZZZZ():
    assert MultiplierCell(['Z', '1', 'Z', 'Z', 'Z', 'Z']).solve() == ({"bits": ('Z', '1', 'Z', 'Z', 'Z', 'Z'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_Z1ZZZ0():
    assert MultiplierCell(['Z', '1', 'Z', 'Z', 'Z', '0']).solve() == ({"bits": ('Z', '1', 'Z', 'Z', 'Z', '0'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_Z1ZZZ1():
    assert MultiplierCell(['Z', '1', 'Z', 'Z', 'Z', '1']).solve() == ({"bits": ('Z', '1', 'Z', 'Z', 'Z', '1'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_Z1ZZ0Z():
    assert MultiplierCell(['Z', '1', 'Z', 'Z', '0', 'Z']).solve() == ({"bits": ('Z', '1', 'Z', 'Z', '0', 'Z'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_Z1ZZ00():
    assert MultiplierCell(['Z', '1', 'Z', 'Z', '0', '0']).solve() == ({"bits": ('0', '1', '0', '0', '0', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_Z1ZZ01():
    assert MultiplierCell(['Z', '1', 'Z', 'Z', '0', '1']).solve() == ({"bits": ('Z', '1', 'Z', 'Z', '0', '1'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_Z1ZZ1Z():
    assert MultiplierCell(['Z', '1', 'Z', 'Z', '1', 'Z']).solve() == ({"bits": ('Z', '1', 'Z', 'Z', '1', 'Z'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_Z1ZZ10():
    assert MultiplierCell(['Z', '1', 'Z', 'Z', '1', '0']).solve() == ({"bits": ('Z', '1', 'Z', 'Z', '1', '0'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_Z1ZZ11():
    assert MultiplierCell(['Z', '1', 'Z', 'Z', '1', '1']).solve() == ({"bits": ('1', '1', '1', '1', '1', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_Z1Z0ZZ():
    assert MultiplierCell(['Z', '1', 'Z', '0', 'Z', 'Z']).solve() == ({"bits": ('Z', '1', 'Z', '0', 'Z', 'Z'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_Z1Z0Z0():
    assert MultiplierCell(['Z', '1', 'Z', '0', 'Z', '0']).solve() == ({"bits": ('Z', '1', 'Z', '0', 'Z', '0'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_Z1Z0Z1():
    assert MultiplierCell(['Z', '1', 'Z', '0', 'Z', '1']).solve() == ({"bits": ('1', '1', '1', '0', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_Z1Z00Z():
    assert MultiplierCell(['Z', '1', 'Z', '0', '0', 'Z']).solve() == ({"bits": ('Z', '1', 'Z', '0', '0', 'Z'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_Z1Z000():
    assert MultiplierCell(['Z', '1', 'Z', '0', '0', '0']).solve() == ({"bits": ('0', '1', '0', '0', '0', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_Z1Z001():
    assert MultiplierCell(['Z', '1', 'Z', '0', '0', '1']).solve() == ({"bits": ('1', '1', '1', '0', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_Z1Z01Z():
    assert MultiplierCell(['Z', '1', 'Z', '0', '1', 'Z']).solve() == ({"bits": ('Z', '1', 'Z', '0', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_Z1Z010():
    assert MultiplierCell(['Z', '1', 'Z', '0', '1', '0']).solve() == ({"bits": ('Z', '1', 'Z', '0', '1', '0'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_Z1Z011():
    assert MultiplierCell(['Z', '1', 'Z', '0', '1', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_Z1Z1ZZ():
    assert MultiplierCell(['Z', '1', 'Z', '1', 'Z', 'Z']).solve() == ({"bits": ('Z', '1', 'Z', '1', 'Z', 'Z'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_Z1Z1Z0():
    assert MultiplierCell(['Z', '1', 'Z', '1', 'Z', '0']).solve() == ({"bits": ('0', '1', '0', '1', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_Z1Z1Z1():
    assert MultiplierCell(['Z', '1', 'Z', '1', 'Z', '1']).solve() == ({"bits": ('Z', '1', 'Z', '1', 'Z', '1'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_Z1Z10Z():
    assert MultiplierCell(['Z', '1', 'Z', '1', '0', 'Z']).solve() == ({"bits": ('Z', '1', 'Z', '1', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_Z1Z100():
    assert MultiplierCell(['Z', '1', 'Z', '1', '0', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_Z1Z101():
    assert MultiplierCell(['Z', '1', 'Z', '1', '0', '1']).solve() == ({"bits": ('Z', '1', 'Z', '1', '0', '1'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_Z1Z11Z():
    assert MultiplierCell(['Z', '1', 'Z', '1', '1', 'Z']).solve() == ({"bits": ('Z', '1', 'Z', '1', '1', 'Z'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_Z1Z110():
    assert MultiplierCell(['Z', '1', 'Z', '1', '1', '0']).solve() == ({"bits": ('0', '1', '0', '1', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_Z1Z111():
    assert MultiplierCell(['Z', '1', 'Z', '1', '1', '1']).solve() == ({"bits": ('1', '1', '1', '1', '1', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_Z10ZZZ():
    assert MultiplierCell(['Z', '1', '0', 'Z', 'Z', 'Z']).solve() == ({"bits": ('Z', '1', '0', 'Z', 'Z', 'Z'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_Z10ZZ0():
    assert MultiplierCell(['Z', '1', '0', 'Z', 'Z', '0']).solve() == ({"bits": ('Z', '1', '0', 'Z', 'Z', '0'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_Z10ZZ1():
    assert MultiplierCell(['Z', '1', '0', 'Z', 'Z', '1']).solve() == ({"bits": ('1', '1', '0', '1', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_Z10Z0Z():
    assert MultiplierCell(['Z', '1', '0', 'Z', '0', 'Z']).solve() == ({"bits": ('Z', '1', '0', 'Z', '0', 'Z'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_Z10Z00():
    assert MultiplierCell(['Z', '1', '0', 'Z', '0', '0']).solve() == ({"bits": ('0', '1', '0', '0', '0', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_Z10Z01():
    assert MultiplierCell(['Z', '1', '0', 'Z', '0', '1']).solve() == ({"bits": ('1', '1', '0', '1', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_Z10Z1Z():
    assert MultiplierCell(['Z', '1', '0', 'Z', '1', 'Z']).solve() == ({"bits": ('Z', '1', '0', 'Z', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_Z10Z10():
    assert MultiplierCell(['Z', '1', '0', 'Z', '1', '0']).solve() == ({"bits": ('Z', '1', '0', 'Z', '1', '0'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_Z10Z11():
    assert MultiplierCell(['Z', '1', '0', 'Z', '1', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_Z100ZZ():
    assert MultiplierCell(['Z', '1', '0', '0', 'Z', 'Z']).solve() == ({"bits": ('Z', '1', '0', '0', 'Z', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_Z100Z0():
    assert MultiplierCell(['Z', '1', '0', '0', 'Z', '0']).solve() == ({"bits": ('Z', '1', '0', '0', 'Z', '0'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_Z100Z1():
    assert MultiplierCell(['Z', '1', '0', '0', 'Z', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_Z1000Z():
    assert MultiplierCell(['Z', '1', '0', '0', '0', 'Z']).solve() == ({"bits": ('0', '1', '0', '0', '0', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_Z10000():
    assert MultiplierCell(['Z', '1', '0', '0', '0', '0']).solve() == ({"bits": ('0', '1', '0', '0', '0', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_Z10001():
    assert MultiplierCell(['Z', '1', '0', '0', '0', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_Z1001Z():
    assert MultiplierCell(['Z', '1', '0', '0', '1', 'Z']).solve() == ({"bits": ('1', '1', '0', '0', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_Z10010():
    assert MultiplierCell(['Z', '1', '0', '0', '1', '0']).solve() == ({"bits": ('1', '1', '0', '0', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_Z10011():
    assert MultiplierCell(['Z', '1', '0', '0', '1', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_Z101ZZ():
    assert MultiplierCell(['Z', '1', '0', '1', 'Z', 'Z']).solve() == ({"bits": ('Z', '1', '0', '1', 'Z', 'Z'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_Z101Z0():
    assert MultiplierCell(['Z', '1', '0', '1', 'Z', '0']).solve() == ({"bits": ('0', '1', '0', '1', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_Z101Z1():
    assert MultiplierCell(['Z', '1', '0', '1', 'Z', '1']).solve() == ({"bits": ('1', '1', '0', '1', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_Z1010Z():
    assert MultiplierCell(['Z', '1', '0', '1', '0', 'Z']).solve() == ({"bits": ('1', '1', '0', '1', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_Z10100():
    assert MultiplierCell(['Z', '1', '0', '1', '0', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_Z10101():
    assert MultiplierCell(['Z', '1', '0', '1', '0', '1']).solve() == ({"bits": ('1', '1', '0', '1', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_Z1011Z():
    assert MultiplierCell(['Z', '1', '0', '1', '1', 'Z']).solve() == ({"bits": ('0', '1', '0', '1', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_Z10110():
    assert MultiplierCell(['Z', '1', '0', '1', '1', '0']).solve() == ({"bits": ('0', '1', '0', '1', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_Z10111():
    assert MultiplierCell(['Z', '1', '0', '1', '1', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_Z11ZZZ():
    assert MultiplierCell(['Z', '1', '1', 'Z', 'Z', 'Z']).solve() == ({"bits": ('Z', '1', '1', 'Z', 'Z', 'Z'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_Z11ZZ0():
    assert MultiplierCell(['Z', '1', '1', 'Z', 'Z', '0']).solve() == ({"bits": ('0', '1', '1', '0', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_Z11ZZ1():
    assert MultiplierCell(['Z', '1', '1', 'Z', 'Z', '1']).solve() == ({"bits": ('Z', '1', '1', 'Z', 'Z', '1'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_Z11Z0Z():
    assert MultiplierCell(['Z', '1', '1', 'Z', '0', 'Z']).solve() == ({"bits": ('Z', '1', '1', 'Z', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_Z11Z00():
    assert MultiplierCell(['Z', '1', '1', 'Z', '0', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_Z11Z01():
    assert MultiplierCell(['Z', '1', '1', 'Z', '0', '1']).solve() == ({"bits": ('Z', '1', '1', 'Z', '0', '1'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_Z11Z1Z():
    assert MultiplierCell(['Z', '1', '1', 'Z', '1', 'Z']).solve() == ({"bits": ('Z', '1', '1', 'Z', '1', 'Z'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_Z11Z10():
    assert MultiplierCell(['Z', '1', '1', 'Z', '1', '0']).solve() == ({"bits": ('0', '1', '1', '0', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_Z11Z11():
    assert MultiplierCell(['Z', '1', '1', 'Z', '1', '1']).solve() == ({"bits": ('1', '1', '1', '1', '1', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_Z110ZZ():
    assert MultiplierCell(['Z', '1', '1', '0', 'Z', 'Z']).solve() == ({"bits": ('Z', '1', '1', '0', 'Z', 'Z'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_Z110Z0():
    assert MultiplierCell(['Z', '1', '1', '0', 'Z', '0']).solve() == ({"bits": ('0', '1', '1', '0', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_Z110Z1():
    assert MultiplierCell(['Z', '1', '1', '0', 'Z', '1']).solve() == ({"bits": ('1', '1', '1', '0', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_Z1100Z():
    assert MultiplierCell(['Z', '1', '1', '0', '0', 'Z']).solve() == ({"bits": ('1', '1', '1', '0', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_Z11000():
    assert MultiplierCell(['Z', '1', '1', '0', '0', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_Z11001():
    assert MultiplierCell(['Z', '1', '1', '0', '0', '1']).solve() == ({"bits": ('1', '1', '1', '0', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_Z1101Z():
    assert MultiplierCell(['Z', '1', '1', '0', '1', 'Z']).solve() == ({"bits": ('0', '1', '1', '0', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_Z11010():
    assert MultiplierCell(['Z', '1', '1', '0', '1', '0']).solve() == ({"bits": ('0', '1', '1', '0', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_Z11011():
    assert MultiplierCell(['Z', '1', '1', '0', '1', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_Z111ZZ():
    assert MultiplierCell(['Z', '1', '1', '1', 'Z', 'Z']).solve() == ({"bits": ('Z', '1', '1', '1', 'Z', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_Z111Z0():
    assert MultiplierCell(['Z', '1', '1', '1', 'Z', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_Z111Z1():
    assert MultiplierCell(['Z', '1', '1', '1', 'Z', '1']).solve() == ({"bits": ('Z', '1', '1', '1', 'Z', '1'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_Z1110Z():
    assert MultiplierCell(['Z', '1', '1', '1', '0', 'Z']).solve() == ({"bits": ('0', '1', '1', '1', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_Z11100():
    assert MultiplierCell(['Z', '1', '1', '1', '0', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_Z11101():
    assert MultiplierCell(['Z', '1', '1', '1', '0', '1']).solve() == ({"bits": ('0', '1', '1', '1', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_Z1111Z():
    assert MultiplierCell(['Z', '1', '1', '1', '1', 'Z']).solve() == ({"bits": ('1', '1', '1', '1', '1', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_Z11110():
    assert MultiplierCell(['Z', '1', '1', '1', '1', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_Z11111():
    assert MultiplierCell(['Z', '1', '1', '1', '1', '1']).solve() == ({"bits": ('1', '1', '1', '1', '1', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_0ZZZZZ():
    assert MultiplierCell(['0', 'Z', 'Z', 'Z', 'Z', 'Z']).solve() == ({"bits": ('0', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_0ZZZZ0():
    assert MultiplierCell(['0', 'Z', 'Z', 'Z', 'Z', '0']).solve() == ({"bits": ('0', 'Z', 'Z', 'Z', 'Z', '0'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_0ZZZZ1():
    assert MultiplierCell(['0', 'Z', 'Z', 'Z', 'Z', '1']).solve() == ({"bits": ('0', 'Z', '1', '1', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_0ZZZ0Z():
    assert MultiplierCell(['0', 'Z', 'Z', 'Z', '0', 'Z']).solve() == ({"bits": ('0', 'Z', 'Z', 'Z', '0', 'Z'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_0ZZZ00():
    assert MultiplierCell(['0', 'Z', 'Z', 'Z', '0', '0']).solve() == ({"bits": ('0', 'Z', '0', '0', '0', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_0ZZZ01():
    assert MultiplierCell(['0', 'Z', 'Z', 'Z', '0', '1']).solve() == ({"bits": ('0', 'Z', '1', '1', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_0ZZZ1Z():
    assert MultiplierCell(['0', 'Z', 'Z', 'Z', '1', 'Z']).solve() == ({"bits": ('0', 'Z', 'Z', 'Z', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_0ZZZ10():
    assert MultiplierCell(['0', 'Z', 'Z', 'Z', '1', '0']).solve() == ({"bits": ('0', 'Z', 'Z', 'Z', '1', '0'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_0ZZZ11():
    assert MultiplierCell(['0', 'Z', 'Z', 'Z', '1', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_0ZZ0ZZ():
    assert MultiplierCell(['0', 'Z', 'Z', '0', 'Z', 'Z']).solve() == ({"bits": ('0', 'Z', 'Z', '0', 'Z', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_0ZZ0Z0():
    assert MultiplierCell(['0', 'Z', 'Z', '0', 'Z', '0']).solve() == ({"bits": ('0', 'Z', 'Z', '0', 'Z', '0'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_0ZZ0Z1():
    assert MultiplierCell(['0', 'Z', 'Z', '0', 'Z', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_0ZZ00Z():
    assert MultiplierCell(['0', 'Z', 'Z', '0', '0', 'Z']).solve() == ({"bits": ('0', 'Z', '0', '0', '0', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_0ZZ000():
    assert MultiplierCell(['0', 'Z', 'Z', '0', '0', '0']).solve() == ({"bits": ('0', 'Z', '0', '0', '0', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_0ZZ001():
    assert MultiplierCell(['0', 'Z', 'Z', '0', '0', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_0ZZ01Z():
    assert MultiplierCell(['0', 'Z', 'Z', '0', '1', 'Z']).solve() == ({"bits": ('0', 'Z', '1', '0', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_0ZZ010():
    assert MultiplierCell(['0', 'Z', 'Z', '0', '1', '0']).solve() == ({"bits": ('0', 'Z', '1', '0', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_0ZZ011():
    assert MultiplierCell(['0', 'Z', 'Z', '0', '1', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_0ZZ1ZZ():
    assert MultiplierCell(['0', 'Z', 'Z', '1', 'Z', 'Z']).solve() == ({"bits": ('0', 'Z', 'Z', '1', 'Z', 'Z'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_0ZZ1Z0():
    assert MultiplierCell(['0', 'Z', 'Z', '1', 'Z', '0']).solve() == ({"bits": ('0', 'Z', '0', '1', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_0ZZ1Z1():
    assert MultiplierCell(['0', 'Z', 'Z', '1', 'Z', '1']).solve() == ({"bits": ('0', 'Z', '1', '1', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_0ZZ10Z():
    assert MultiplierCell(['0', 'Z', 'Z', '1', '0', 'Z']).solve() == ({"bits": ('0', 'Z', '1', '1', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_0ZZ100():
    assert MultiplierCell(['0', 'Z', 'Z', '1', '0', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_0ZZ101():
    assert MultiplierCell(['0', 'Z', 'Z', '1', '0', '1']).solve() == ({"bits": ('0', 'Z', '1', '1', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_0ZZ11Z():
    assert MultiplierCell(['0', 'Z', 'Z', '1', '1', 'Z']).solve() == ({"bits": ('0', 'Z', '0', '1', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_0ZZ110():
    assert MultiplierCell(['0', 'Z', 'Z', '1', '1', '0']).solve() == ({"bits": ('0', 'Z', '0', '1', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_0ZZ111():
    assert MultiplierCell(['0', 'Z', 'Z', '1', '1', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_0Z0ZZZ():
    assert MultiplierCell(['0', 'Z', '0', 'Z', 'Z', 'Z']).solve() == ({"bits": ('0', 'Z', '0', 'Z', 'Z', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_0Z0ZZ0():
    assert MultiplierCell(['0', 'Z', '0', 'Z', 'Z', '0']).solve() == ({"bits": ('0', 'Z', '0', 'Z', 'Z', '0'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_0Z0ZZ1():
    assert MultiplierCell(['0', 'Z', '0', 'Z', 'Z', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_0Z0Z0Z():
    assert MultiplierCell(['0', 'Z', '0', 'Z', '0', 'Z']).solve() == ({"bits": ('0', 'Z', '0', '0', '0', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_0Z0Z00():
    assert MultiplierCell(['0', 'Z', '0', 'Z', '0', '0']).solve() == ({"bits": ('0', 'Z', '0', '0', '0', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_0Z0Z01():
    assert MultiplierCell(['0', 'Z', '0', 'Z', '0', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_0Z0Z1Z():
    assert MultiplierCell(['0', 'Z', '0', 'Z', '1', 'Z']).solve() == ({"bits": ('0', 'Z', '0', '1', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_0Z0Z10():
    assert MultiplierCell(['0', 'Z', '0', 'Z', '1', '0']).solve() == ({"bits": ('0', 'Z', '0', '1', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_0Z0Z11():
    assert MultiplierCell(['0', 'Z', '0', 'Z', '1', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_0Z00ZZ():
    assert MultiplierCell(['0', 'Z', '0', '0', 'Z', 'Z']).solve() == ({"bits": ('0', 'Z', '0', '0', '0', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_0Z00Z0():
    assert MultiplierCell(['0', 'Z', '0', '0', 'Z', '0']).solve() == ({"bits": ('0', 'Z', '0', '0', '0', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_0Z00Z1():
    assert MultiplierCell(['0', 'Z', '0', '0', 'Z', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_0Z000Z():
    assert MultiplierCell(['0', 'Z', '0', '0', '0', 'Z']).solve() == ({"bits": ('0', 'Z', '0', '0', '0', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_0Z0000():
    assert MultiplierCell(['0', 'Z', '0', '0', '0', '0']).solve() == ({"bits": ('0', 'Z', '0', '0', '0', '0'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_0Z0001():
    assert MultiplierCell(['0', 'Z', '0', '0', '0', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_0Z001Z():
    assert MultiplierCell(['0', 'Z', '0', '0', '1', 'Z']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_0Z0010():
    assert MultiplierCell(['0', 'Z', '0', '0', '1', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_0Z0011():
    assert MultiplierCell(['0', 'Z', '0', '0', '1', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_0Z01ZZ():
    assert MultiplierCell(['0', 'Z', '0', '1', 'Z', 'Z']).solve() == ({"bits": ('0', 'Z', '0', '1', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_0Z01Z0():
    assert MultiplierCell(['0', 'Z', '0', '1', 'Z', '0']).solve() == ({"bits": ('0', 'Z', '0', '1', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_0Z01Z1():
    assert MultiplierCell(['0', 'Z', '0', '1', 'Z', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_0Z010Z():
    assert MultiplierCell(['0', 'Z', '0', '1', '0', 'Z']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_0Z0100():
    assert MultiplierCell(['0', 'Z', '0', '1', '0', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_0Z0101():
    assert MultiplierCell(['0', 'Z', '0', '1', '0', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_0Z011Z():
    assert MultiplierCell(['0', 'Z', '0', '1', '1', 'Z']).solve() == ({"bits": ('0', 'Z', '0', '1', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_0Z0110():
    assert MultiplierCell(['0', 'Z', '0', '1', '1', '0']).solve() == ({"bits": ('0', 'Z', '0', '1', '1', '0'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_0Z0111():
    assert MultiplierCell(['0', 'Z', '0', '1', '1', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_0Z1ZZZ():
    assert MultiplierCell(['0', 'Z', '1', 'Z', 'Z', 'Z']).solve() == ({"bits": ('0', 'Z', '1', 'Z', 'Z', 'Z'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_0Z1ZZ0():
    assert MultiplierCell(['0', 'Z', '1', 'Z', 'Z', '0']).solve() == ({"bits": ('0', 'Z', '1', '0', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_0Z1ZZ1():
    assert MultiplierCell(['0', 'Z', '1', 'Z', 'Z', '1']).solve() == ({"bits": ('0', 'Z', '1', '1', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_0Z1Z0Z():
    assert MultiplierCell(['0', 'Z', '1', 'Z', '0', 'Z']).solve() == ({"bits": ('0', 'Z', '1', '1', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_0Z1Z00():
    assert MultiplierCell(['0', 'Z', '1', 'Z', '0', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_0Z1Z01():
    assert MultiplierCell(['0', 'Z', '1', 'Z', '0', '1']).solve() == ({"bits": ('0', 'Z', '1', '1', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_0Z1Z1Z():
    assert MultiplierCell(['0', 'Z', '1', 'Z', '1', 'Z']).solve() == ({"bits": ('0', 'Z', '1', '0', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_0Z1Z10():
    assert MultiplierCell(['0', 'Z', '1', 'Z', '1', '0']).solve() == ({"bits": ('0', 'Z', '1', '0', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_0Z1Z11():
    assert MultiplierCell(['0', 'Z', '1', 'Z', '1', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_0Z10ZZ():
    assert MultiplierCell(['0', 'Z', '1', '0', 'Z', 'Z']).solve() == ({"bits": ('0', 'Z', '1', '0', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_0Z10Z0():
    assert MultiplierCell(['0', 'Z', '1', '0', 'Z', '0']).solve() == ({"bits": ('0', 'Z', '1', '0', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_0Z10Z1():
    assert MultiplierCell(['0', 'Z', '1', '0', 'Z', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_0Z100Z():
    assert MultiplierCell(['0', 'Z', '1', '0', '0', 'Z']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_0Z1000():
    assert MultiplierCell(['0', 'Z', '1', '0', '0', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_0Z1001():
    assert MultiplierCell(['0', 'Z', '1', '0', '0', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_0Z101Z():
    assert MultiplierCell(['0', 'Z', '1', '0', '1', 'Z']).solve() == ({"bits": ('0', 'Z', '1', '0', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_0Z1010():
    assert MultiplierCell(['0', 'Z', '1', '0', '1', '0']).solve() == ({"bits": ('0', 'Z', '1', '0', '1', '0'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_0Z1011():
    assert MultiplierCell(['0', 'Z', '1', '0', '1', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_0Z11ZZ():
    assert MultiplierCell(['0', 'Z', '1', '1', 'Z', 'Z']).solve() == ({"bits": ('0', 'Z', '1', '1', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_0Z11Z0():
    assert MultiplierCell(['0', 'Z', '1', '1', 'Z', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_0Z11Z1():
    assert MultiplierCell(['0', 'Z', '1', '1', 'Z', '1']).solve() == ({"bits": ('0', 'Z', '1', '1', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_0Z110Z():
    assert MultiplierCell(['0', 'Z', '1', '1', '0', 'Z']).solve() == ({"bits": ('0', 'Z', '1', '1', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_0Z1100():
    assert MultiplierCell(['0', 'Z', '1', '1', '0', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_0Z1101():
    assert MultiplierCell(['0', 'Z', '1', '1', '0', '1']).solve() == ({"bits": ('0', 'Z', '1', '1', '0', '1'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_0Z111Z():
    assert MultiplierCell(['0', 'Z', '1', '1', '1', 'Z']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_0Z1110():
    assert MultiplierCell(['0', 'Z', '1', '1', '1', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_0Z1111():
    assert MultiplierCell(['0', 'Z', '1', '1', '1', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_00ZZZZ():
    assert MultiplierCell(['0', '0', 'Z', 'Z', 'Z', 'Z']).solve() == ({"bits": ('0', '0', 'Z', 'Z', 'Z', 'Z'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_00ZZZ0():
    assert MultiplierCell(['0', '0', 'Z', 'Z', 'Z', '0']).solve() == ({"bits": ('0', '0', 'Z', 'Z', 'Z', '0'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_00ZZZ1():
    assert MultiplierCell(['0', '0', 'Z', 'Z', 'Z', '1']).solve() == ({"bits": ('0', '0', '1', '1', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_00ZZ0Z():
    assert MultiplierCell(['0', '0', 'Z', 'Z', '0', 'Z']).solve() == ({"bits": ('0', '0', 'Z', 'Z', '0', 'Z'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_00ZZ00():
    assert MultiplierCell(['0', '0', 'Z', 'Z', '0', '0']).solve() == ({"bits": ('0', '0', '0', '0', '0', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_00ZZ01():
    assert MultiplierCell(['0', '0', 'Z', 'Z', '0', '1']).solve() == ({"bits": ('0', '0', '1', '1', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_00ZZ1Z():
    assert MultiplierCell(['0', '0', 'Z', 'Z', '1', 'Z']).solve() == ({"bits": ('0', '0', 'Z', 'Z', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_00ZZ10():
    assert MultiplierCell(['0', '0', 'Z', 'Z', '1', '0']).solve() == ({"bits": ('0', '0', 'Z', 'Z', '1', '0'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_00ZZ11():
    assert MultiplierCell(['0', '0', 'Z', 'Z', '1', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_00Z0ZZ():
    assert MultiplierCell(['0', '0', 'Z', '0', 'Z', 'Z']).solve() == ({"bits": ('0', '0', 'Z', '0', 'Z', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_00Z0Z0():
    assert MultiplierCell(['0', '0', 'Z', '0', 'Z', '0']).solve() == ({"bits": ('0', '0', 'Z', '0', 'Z', '0'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_00Z0Z1():
    assert MultiplierCell(['0', '0', 'Z', '0', 'Z', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_00Z00Z():
    assert MultiplierCell(['0', '0', 'Z', '0', '0', 'Z']).solve() == ({"bits": ('0', '0', '0', '0', '0', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_00Z000():
    assert MultiplierCell(['0', '0', 'Z', '0', '0', '0']).solve() == ({"bits": ('0', '0', '0', '0', '0', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_00Z001():
    assert MultiplierCell(['0', '0', 'Z', '0', '0', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_00Z01Z():
    assert MultiplierCell(['0', '0', 'Z', '0', '1', 'Z']).solve() == ({"bits": ('0', '0', '1', '0', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_00Z010():
    assert MultiplierCell(['0', '0', 'Z', '0', '1', '0']).solve() == ({"bits": ('0', '0', '1', '0', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_00Z011():
    assert MultiplierCell(['0', '0', 'Z', '0', '1', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_00Z1ZZ():
    assert MultiplierCell(['0', '0', 'Z', '1', 'Z', 'Z']).solve() == ({"bits": ('0', '0', 'Z', '1', 'Z', 'Z'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_00Z1Z0():
    assert MultiplierCell(['0', '0', 'Z', '1', 'Z', '0']).solve() == ({"bits": ('0', '0', '0', '1', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_00Z1Z1():
    assert MultiplierCell(['0', '0', 'Z', '1', 'Z', '1']).solve() == ({"bits": ('0', '0', '1', '1', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_00Z10Z():
    assert MultiplierCell(['0', '0', 'Z', '1', '0', 'Z']).solve() == ({"bits": ('0', '0', '1', '1', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_00Z100():
    assert MultiplierCell(['0', '0', 'Z', '1', '0', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_00Z101():
    assert MultiplierCell(['0', '0', 'Z', '1', '0', '1']).solve() == ({"bits": ('0', '0', '1', '1', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_00Z11Z():
    assert MultiplierCell(['0', '0', 'Z', '1', '1', 'Z']).solve() == ({"bits": ('0', '0', '0', '1', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_00Z110():
    assert MultiplierCell(['0', '0', 'Z', '1', '1', '0']).solve() == ({"bits": ('0', '0', '0', '1', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_00Z111():
    assert MultiplierCell(['0', '0', 'Z', '1', '1', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_000ZZZ():
    assert MultiplierCell(['0', '0', '0', 'Z', 'Z', 'Z']).solve() == ({"bits": ('0', '0', '0', 'Z', 'Z', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_000ZZ0():
    assert MultiplierCell(['0', '0', '0', 'Z', 'Z', '0']).solve() == ({"bits": ('0', '0', '0', 'Z', 'Z', '0'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_000ZZ1():
    assert MultiplierCell(['0', '0', '0', 'Z', 'Z', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_000Z0Z():
    assert MultiplierCell(['0', '0', '0', 'Z', '0', 'Z']).solve() == ({"bits": ('0', '0', '0', '0', '0', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_000Z00():
    assert MultiplierCell(['0', '0', '0', 'Z', '0', '0']).solve() == ({"bits": ('0', '0', '0', '0', '0', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_000Z01():
    assert MultiplierCell(['0', '0', '0', 'Z', '0', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_000Z1Z():
    assert MultiplierCell(['0', '0', '0', 'Z', '1', 'Z']).solve() == ({"bits": ('0', '0', '0', '1', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_000Z10():
    assert MultiplierCell(['0', '0', '0', 'Z', '1', '0']).solve() == ({"bits": ('0', '0', '0', '1', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_000Z11():
    assert MultiplierCell(['0', '0', '0', 'Z', '1', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_0000ZZ():
    assert MultiplierCell(['0', '0', '0', '0', 'Z', 'Z']).solve() == ({"bits": ('0', '0', '0', '0', '0', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_0000Z0():
    assert MultiplierCell(['0', '0', '0', '0', 'Z', '0']).solve() == ({"bits": ('0', '0', '0', '0', '0', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_0000Z1():
    assert MultiplierCell(['0', '0', '0', '0', 'Z', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_00000Z():
    assert MultiplierCell(['0', '0', '0', '0', '0', 'Z']).solve() == ({"bits": ('0', '0', '0', '0', '0', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_000000():
    assert MultiplierCell(['0', '0', '0', '0', '0', '0']).solve() == ({"bits": ('0', '0', '0', '0', '0', '0'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_000001():
    assert MultiplierCell(['0', '0', '0', '0', '0', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_00001Z():
    assert MultiplierCell(['0', '0', '0', '0', '1', 'Z']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_000010():
    assert MultiplierCell(['0', '0', '0', '0', '1', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_000011():
    assert MultiplierCell(['0', '0', '0', '0', '1', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_0001ZZ():
    assert MultiplierCell(['0', '0', '0', '1', 'Z', 'Z']).solve() == ({"bits": ('0', '0', '0', '1', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_0001Z0():
    assert MultiplierCell(['0', '0', '0', '1', 'Z', '0']).solve() == ({"bits": ('0', '0', '0', '1', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_0001Z1():
    assert MultiplierCell(['0', '0', '0', '1', 'Z', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_00010Z():
    assert MultiplierCell(['0', '0', '0', '1', '0', 'Z']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_000100():
    assert MultiplierCell(['0', '0', '0', '1', '0', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_000101():
    assert MultiplierCell(['0', '0', '0', '1', '0', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_00011Z():
    assert MultiplierCell(['0', '0', '0', '1', '1', 'Z']).solve() == ({"bits": ('0', '0', '0', '1', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_000110():
    assert MultiplierCell(['0', '0', '0', '1', '1', '0']).solve() == ({"bits": ('0', '0', '0', '1', '1', '0'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_000111():
    assert MultiplierCell(['0', '0', '0', '1', '1', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_001ZZZ():
    assert MultiplierCell(['0', '0', '1', 'Z', 'Z', 'Z']).solve() == ({"bits": ('0', '0', '1', 'Z', 'Z', 'Z'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_001ZZ0():
    assert MultiplierCell(['0', '0', '1', 'Z', 'Z', '0']).solve() == ({"bits": ('0', '0', '1', '0', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_001ZZ1():
    assert MultiplierCell(['0', '0', '1', 'Z', 'Z', '1']).solve() == ({"bits": ('0', '0', '1', '1', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_001Z0Z():
    assert MultiplierCell(['0', '0', '1', 'Z', '0', 'Z']).solve() == ({"bits": ('0', '0', '1', '1', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_001Z00():
    assert MultiplierCell(['0', '0', '1', 'Z', '0', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_001Z01():
    assert MultiplierCell(['0', '0', '1', 'Z', '0', '1']).solve() == ({"bits": ('0', '0', '1', '1', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_001Z1Z():
    assert MultiplierCell(['0', '0', '1', 'Z', '1', 'Z']).solve() == ({"bits": ('0', '0', '1', '0', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_001Z10():
    assert MultiplierCell(['0', '0', '1', 'Z', '1', '0']).solve() == ({"bits": ('0', '0', '1', '0', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_001Z11():
    assert MultiplierCell(['0', '0', '1', 'Z', '1', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_0010ZZ():
    assert MultiplierCell(['0', '0', '1', '0', 'Z', 'Z']).solve() == ({"bits": ('0', '0', '1', '0', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_0010Z0():
    assert MultiplierCell(['0', '0', '1', '0', 'Z', '0']).solve() == ({"bits": ('0', '0', '1', '0', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_0010Z1():
    assert MultiplierCell(['0', '0', '1', '0', 'Z', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_00100Z():
    assert MultiplierCell(['0', '0', '1', '0', '0', 'Z']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_001000():
    assert MultiplierCell(['0', '0', '1', '0', '0', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_001001():
    assert MultiplierCell(['0', '0', '1', '0', '0', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_00101Z():
    assert MultiplierCell(['0', '0', '1', '0', '1', 'Z']).solve() == ({"bits": ('0', '0', '1', '0', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_001010():
    assert MultiplierCell(['0', '0', '1', '0', '1', '0']).solve() == ({"bits": ('0', '0', '1', '0', '1', '0'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_001011():
    assert MultiplierCell(['0', '0', '1', '0', '1', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_0011ZZ():
    assert MultiplierCell(['0', '0', '1', '1', 'Z', 'Z']).solve() == ({"bits": ('0', '0', '1', '1', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_0011Z0():
    assert MultiplierCell(['0', '0', '1', '1', 'Z', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_0011Z1():
    assert MultiplierCell(['0', '0', '1', '1', 'Z', '1']).solve() == ({"bits": ('0', '0', '1', '1', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_00110Z():
    assert MultiplierCell(['0', '0', '1', '1', '0', 'Z']).solve() == ({"bits": ('0', '0', '1', '1', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_001100():
    assert MultiplierCell(['0', '0', '1', '1', '0', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_001101():
    assert MultiplierCell(['0', '0', '1', '1', '0', '1']).solve() == ({"bits": ('0', '0', '1', '1', '0', '1'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_00111Z():
    assert MultiplierCell(['0', '0', '1', '1', '1', 'Z']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_001110():
    assert MultiplierCell(['0', '0', '1', '1', '1', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_001111():
    assert MultiplierCell(['0', '0', '1', '1', '1', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_01ZZZZ():
    assert MultiplierCell(['0', '1', 'Z', 'Z', 'Z', 'Z']).solve() == ({"bits": ('0', '1', 'Z', 'Z', 'Z', 'Z'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_01ZZZ0():
    assert MultiplierCell(['0', '1', 'Z', 'Z', 'Z', '0']).solve() == ({"bits": ('0', '1', 'Z', 'Z', 'Z', '0'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_01ZZZ1():
    assert MultiplierCell(['0', '1', 'Z', 'Z', 'Z', '1']).solve() == ({"bits": ('0', '1', '1', '1', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_01ZZ0Z():
    assert MultiplierCell(['0', '1', 'Z', 'Z', '0', 'Z']).solve() == ({"bits": ('0', '1', 'Z', 'Z', '0', 'Z'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_01ZZ00():
    assert MultiplierCell(['0', '1', 'Z', 'Z', '0', '0']).solve() == ({"bits": ('0', '1', '0', '0', '0', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_01ZZ01():
    assert MultiplierCell(['0', '1', 'Z', 'Z', '0', '1']).solve() == ({"bits": ('0', '1', '1', '1', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_01ZZ1Z():
    assert MultiplierCell(['0', '1', 'Z', 'Z', '1', 'Z']).solve() == ({"bits": ('0', '1', 'Z', 'Z', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_01ZZ10():
    assert MultiplierCell(['0', '1', 'Z', 'Z', '1', '0']).solve() == ({"bits": ('0', '1', 'Z', 'Z', '1', '0'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_01ZZ11():
    assert MultiplierCell(['0', '1', 'Z', 'Z', '1', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_01Z0ZZ():
    assert MultiplierCell(['0', '1', 'Z', '0', 'Z', 'Z']).solve() == ({"bits": ('0', '1', 'Z', '0', 'Z', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_01Z0Z0():
    assert MultiplierCell(['0', '1', 'Z', '0', 'Z', '0']).solve() == ({"bits": ('0', '1', 'Z', '0', 'Z', '0'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_01Z0Z1():
    assert MultiplierCell(['0', '1', 'Z', '0', 'Z', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_01Z00Z():
    assert MultiplierCell(['0', '1', 'Z', '0', '0', 'Z']).solve() == ({"bits": ('0', '1', '0', '0', '0', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_01Z000():
    assert MultiplierCell(['0', '1', 'Z', '0', '0', '0']).solve() == ({"bits": ('0', '1', '0', '0', '0', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_01Z001():
    assert MultiplierCell(['0', '1', 'Z', '0', '0', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_01Z01Z():
    assert MultiplierCell(['0', '1', 'Z', '0', '1', 'Z']).solve() == ({"bits": ('0', '1', '1', '0', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_01Z010():
    assert MultiplierCell(['0', '1', 'Z', '0', '1', '0']).solve() == ({"bits": ('0', '1', '1', '0', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_01Z011():
    assert MultiplierCell(['0', '1', 'Z', '0', '1', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_01Z1ZZ():
    assert MultiplierCell(['0', '1', 'Z', '1', 'Z', 'Z']).solve() == ({"bits": ('0', '1', 'Z', '1', 'Z', 'Z'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_01Z1Z0():
    assert MultiplierCell(['0', '1', 'Z', '1', 'Z', '0']).solve() == ({"bits": ('0', '1', '0', '1', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_01Z1Z1():
    assert MultiplierCell(['0', '1', 'Z', '1', 'Z', '1']).solve() == ({"bits": ('0', '1', '1', '1', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_01Z10Z():
    assert MultiplierCell(['0', '1', 'Z', '1', '0', 'Z']).solve() == ({"bits": ('0', '1', '1', '1', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_01Z100():
    assert MultiplierCell(['0', '1', 'Z', '1', '0', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_01Z101():
    assert MultiplierCell(['0', '1', 'Z', '1', '0', '1']).solve() == ({"bits": ('0', '1', '1', '1', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_01Z11Z():
    assert MultiplierCell(['0', '1', 'Z', '1', '1', 'Z']).solve() == ({"bits": ('0', '1', '0', '1', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_01Z110():
    assert MultiplierCell(['0', '1', 'Z', '1', '1', '0']).solve() == ({"bits": ('0', '1', '0', '1', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_01Z111():
    assert MultiplierCell(['0', '1', 'Z', '1', '1', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_010ZZZ():
    assert MultiplierCell(['0', '1', '0', 'Z', 'Z', 'Z']).solve() == ({"bits": ('0', '1', '0', 'Z', 'Z', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_010ZZ0():
    assert MultiplierCell(['0', '1', '0', 'Z', 'Z', '0']).solve() == ({"bits": ('0', '1', '0', 'Z', 'Z', '0'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_010ZZ1():
    assert MultiplierCell(['0', '1', '0', 'Z', 'Z', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_010Z0Z():
    assert MultiplierCell(['0', '1', '0', 'Z', '0', 'Z']).solve() == ({"bits": ('0', '1', '0', '0', '0', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_010Z00():
    assert MultiplierCell(['0', '1', '0', 'Z', '0', '0']).solve() == ({"bits": ('0', '1', '0', '0', '0', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_010Z01():
    assert MultiplierCell(['0', '1', '0', 'Z', '0', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_010Z1Z():
    assert MultiplierCell(['0', '1', '0', 'Z', '1', 'Z']).solve() == ({"bits": ('0', '1', '0', '1', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_010Z10():
    assert MultiplierCell(['0', '1', '0', 'Z', '1', '0']).solve() == ({"bits": ('0', '1', '0', '1', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_010Z11():
    assert MultiplierCell(['0', '1', '0', 'Z', '1', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_0100ZZ():
    assert MultiplierCell(['0', '1', '0', '0', 'Z', 'Z']).solve() == ({"bits": ('0', '1', '0', '0', '0', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_0100Z0():
    assert MultiplierCell(['0', '1', '0', '0', 'Z', '0']).solve() == ({"bits": ('0', '1', '0', '0', '0', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_0100Z1():
    assert MultiplierCell(['0', '1', '0', '0', 'Z', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_01000Z():
    assert MultiplierCell(['0', '1', '0', '0', '0', 'Z']).solve() == ({"bits": ('0', '1', '0', '0', '0', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_010000():
    assert MultiplierCell(['0', '1', '0', '0', '0', '0']).solve() == ({"bits": ('0', '1', '0', '0', '0', '0'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_010001():
    assert MultiplierCell(['0', '1', '0', '0', '0', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_01001Z():
    assert MultiplierCell(['0', '1', '0', '0', '1', 'Z']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_010010():
    assert MultiplierCell(['0', '1', '0', '0', '1', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_010011():
    assert MultiplierCell(['0', '1', '0', '0', '1', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_0101ZZ():
    assert MultiplierCell(['0', '1', '0', '1', 'Z', 'Z']).solve() == ({"bits": ('0', '1', '0', '1', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_0101Z0():
    assert MultiplierCell(['0', '1', '0', '1', 'Z', '0']).solve() == ({"bits": ('0', '1', '0', '1', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_0101Z1():
    assert MultiplierCell(['0', '1', '0', '1', 'Z', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_01010Z():
    assert MultiplierCell(['0', '1', '0', '1', '0', 'Z']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_010100():
    assert MultiplierCell(['0', '1', '0', '1', '0', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_010101():
    assert MultiplierCell(['0', '1', '0', '1', '0', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_01011Z():
    assert MultiplierCell(['0', '1', '0', '1', '1', 'Z']).solve() == ({"bits": ('0', '1', '0', '1', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_010110():
    assert MultiplierCell(['0', '1', '0', '1', '1', '0']).solve() == ({"bits": ('0', '1', '0', '1', '1', '0'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_010111():
    assert MultiplierCell(['0', '1', '0', '1', '1', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_011ZZZ():
    assert MultiplierCell(['0', '1', '1', 'Z', 'Z', 'Z']).solve() == ({"bits": ('0', '1', '1', 'Z', 'Z', 'Z'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_011ZZ0():
    assert MultiplierCell(['0', '1', '1', 'Z', 'Z', '0']).solve() == ({"bits": ('0', '1', '1', '0', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_011ZZ1():
    assert MultiplierCell(['0', '1', '1', 'Z', 'Z', '1']).solve() == ({"bits": ('0', '1', '1', '1', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_011Z0Z():
    assert MultiplierCell(['0', '1', '1', 'Z', '0', 'Z']).solve() == ({"bits": ('0', '1', '1', '1', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_011Z00():
    assert MultiplierCell(['0', '1', '1', 'Z', '0', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_011Z01():
    assert MultiplierCell(['0', '1', '1', 'Z', '0', '1']).solve() == ({"bits": ('0', '1', '1', '1', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_011Z1Z():
    assert MultiplierCell(['0', '1', '1', 'Z', '1', 'Z']).solve() == ({"bits": ('0', '1', '1', '0', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_011Z10():
    assert MultiplierCell(['0', '1', '1', 'Z', '1', '0']).solve() == ({"bits": ('0', '1', '1', '0', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_011Z11():
    assert MultiplierCell(['0', '1', '1', 'Z', '1', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_0110ZZ():
    assert MultiplierCell(['0', '1', '1', '0', 'Z', 'Z']).solve() == ({"bits": ('0', '1', '1', '0', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_0110Z0():
    assert MultiplierCell(['0', '1', '1', '0', 'Z', '0']).solve() == ({"bits": ('0', '1', '1', '0', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_0110Z1():
    assert MultiplierCell(['0', '1', '1', '0', 'Z', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_01100Z():
    assert MultiplierCell(['0', '1', '1', '0', '0', 'Z']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_011000():
    assert MultiplierCell(['0', '1', '1', '0', '0', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_011001():
    assert MultiplierCell(['0', '1', '1', '0', '0', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_01101Z():
    assert MultiplierCell(['0', '1', '1', '0', '1', 'Z']).solve() == ({"bits": ('0', '1', '1', '0', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_011010():
    assert MultiplierCell(['0', '1', '1', '0', '1', '0']).solve() == ({"bits": ('0', '1', '1', '0', '1', '0'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_011011():
    assert MultiplierCell(['0', '1', '1', '0', '1', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_0111ZZ():
    assert MultiplierCell(['0', '1', '1', '1', 'Z', 'Z']).solve() == ({"bits": ('0', '1', '1', '1', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_0111Z0():
    assert MultiplierCell(['0', '1', '1', '1', 'Z', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_0111Z1():
    assert MultiplierCell(['0', '1', '1', '1', 'Z', '1']).solve() == ({"bits": ('0', '1', '1', '1', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_01110Z():
    assert MultiplierCell(['0', '1', '1', '1', '0', 'Z']).solve() == ({"bits": ('0', '1', '1', '1', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_011100():
    assert MultiplierCell(['0', '1', '1', '1', '0', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_011101():
    assert MultiplierCell(['0', '1', '1', '1', '0', '1']).solve() == ({"bits": ('0', '1', '1', '1', '0', '1'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_01111Z():
    assert MultiplierCell(['0', '1', '1', '1', '1', 'Z']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_011110():
    assert MultiplierCell(['0', '1', '1', '1', '1', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_011111():
    assert MultiplierCell(['0', '1', '1', '1', '1', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_1ZZZZZ():
    assert MultiplierCell(['1', 'Z', 'Z', 'Z', 'Z', 'Z']).solve() == ({"bits": ('1', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_1ZZZZ0():
    assert MultiplierCell(['1', 'Z', 'Z', 'Z', 'Z', '0']).solve() == ({"bits": ('1', 'Z', 'Z', 'Z', 'Z', '0'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_1ZZZZ1():
    assert MultiplierCell(['1', 'Z', 'Z', 'Z', 'Z', '1']).solve() == ({"bits": ('1', 'Z', 'Z', 'Z', 'Z', '1'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_1ZZZ0Z():
    assert MultiplierCell(['1', 'Z', 'Z', 'Z', '0', 'Z']).solve() == ({"bits": ('1', 'Z', 'Z', 'Z', '0', 'Z'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_1ZZZ00():
    assert MultiplierCell(['1', 'Z', 'Z', 'Z', '0', '0']).solve() == ({"bits": ('1', '0', '0', '0', '0', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_1ZZZ01():
    assert MultiplierCell(['1', 'Z', 'Z', 'Z', '0', '1']).solve() == ({"bits": ('1', 'Z', 'Z', 'Z', '0', '1'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_1ZZZ1Z():
    assert MultiplierCell(['1', 'Z', 'Z', 'Z', '1', 'Z']).solve() == ({"bits": ('1', 'Z', 'Z', 'Z', '1', 'Z'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_1ZZZ10():
    assert MultiplierCell(['1', 'Z', 'Z', 'Z', '1', '0']).solve() == ({"bits": ('1', 'Z', 'Z', 'Z', '1', '0'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_1ZZZ11():
    assert MultiplierCell(['1', 'Z', 'Z', 'Z', '1', '1']).solve() == ({"bits": ('1', '1', '1', '1', '1', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_1ZZ0ZZ():
    assert MultiplierCell(['1', 'Z', 'Z', '0', 'Z', 'Z']).solve() == ({"bits": ('1', 'Z', 'Z', '0', 'Z', 'Z'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_1ZZ0Z0():
    assert MultiplierCell(['1', 'Z', 'Z', '0', 'Z', '0']).solve() == ({"bits": ('1', 'Z', 'Z', '0', 'Z', '0'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_1ZZ0Z1():
    assert MultiplierCell(['1', 'Z', 'Z', '0', 'Z', '1']).solve() == ({"bits": ('1', '1', '1', '0', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_1ZZ00Z():
    assert MultiplierCell(['1', 'Z', 'Z', '0', '0', 'Z']).solve() == ({"bits": ('1', 'Z', 'Z', '0', '0', 'Z'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_1ZZ000():
    assert MultiplierCell(['1', 'Z', 'Z', '0', '0', '0']).solve() == ({"bits": ('1', '0', '0', '0', '0', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_1ZZ001():
    assert MultiplierCell(['1', 'Z', 'Z', '0', '0', '1']).solve() == ({"bits": ('1', '1', '1', '0', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_1ZZ01Z():
    assert MultiplierCell(['1', 'Z', 'Z', '0', '1', 'Z']).solve() == ({"bits": ('1', 'Z', 'Z', '0', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_1ZZ010():
    assert MultiplierCell(['1', 'Z', 'Z', '0', '1', '0']).solve() == ({"bits": ('1', 'Z', 'Z', '0', '1', '0'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_1ZZ011():
    assert MultiplierCell(['1', 'Z', 'Z', '0', '1', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_1ZZ1ZZ():
    assert MultiplierCell(['1', 'Z', 'Z', '1', 'Z', 'Z']).solve() == ({"bits": ('1', 'Z', 'Z', '1', 'Z', 'Z'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_1ZZ1Z0():
    assert MultiplierCell(['1', 'Z', 'Z', '1', 'Z', '0']).solve() == ({"bits": ('1', '0', '0', '1', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_1ZZ1Z1():
    assert MultiplierCell(['1', 'Z', 'Z', '1', 'Z', '1']).solve() == ({"bits": ('1', 'Z', 'Z', '1', 'Z', '1'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_1ZZ10Z():
    assert MultiplierCell(['1', 'Z', 'Z', '1', '0', 'Z']).solve() == ({"bits": ('1', 'Z', 'Z', '1', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_1ZZ100():
    assert MultiplierCell(['1', 'Z', 'Z', '1', '0', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_1ZZ101():
    assert MultiplierCell(['1', 'Z', 'Z', '1', '0', '1']).solve() == ({"bits": ('1', 'Z', 'Z', '1', '0', '1'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_1ZZ11Z():
    assert MultiplierCell(['1', 'Z', 'Z', '1', '1', 'Z']).solve() == ({"bits": ('1', 'Z', 'Z', '1', '1', 'Z'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_1ZZ110():
    assert MultiplierCell(['1', 'Z', 'Z', '1', '1', '0']).solve() == ({"bits": ('1', '0', '0', '1', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_1ZZ111():
    assert MultiplierCell(['1', 'Z', 'Z', '1', '1', '1']).solve() == ({"bits": ('1', '1', '1', '1', '1', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_1Z0ZZZ():
    assert MultiplierCell(['1', 'Z', '0', 'Z', 'Z', 'Z']).solve() == ({"bits": ('1', 'Z', '0', 'Z', 'Z', 'Z'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_1Z0ZZ0():
    assert MultiplierCell(['1', 'Z', '0', 'Z', 'Z', '0']).solve() == ({"bits": ('1', 'Z', '0', 'Z', 'Z', '0'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_1Z0ZZ1():
    assert MultiplierCell(['1', 'Z', '0', 'Z', 'Z', '1']).solve() == ({"bits": ('1', '1', '0', '1', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_1Z0Z0Z():
    assert MultiplierCell(['1', 'Z', '0', 'Z', '0', 'Z']).solve() == ({"bits": ('1', 'Z', '0', 'Z', '0', 'Z'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_1Z0Z00():
    assert MultiplierCell(['1', 'Z', '0', 'Z', '0', '0']).solve() == ({"bits": ('1', '0', '0', '0', '0', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_1Z0Z01():
    assert MultiplierCell(['1', 'Z', '0', 'Z', '0', '1']).solve() == ({"bits": ('1', '1', '0', '1', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_1Z0Z1Z():
    assert MultiplierCell(['1', 'Z', '0', 'Z', '1', 'Z']).solve() == ({"bits": ('1', 'Z', '0', 'Z', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_1Z0Z10():
    assert MultiplierCell(['1', 'Z', '0', 'Z', '1', '0']).solve() == ({"bits": ('1', 'Z', '0', 'Z', '1', '0'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_1Z0Z11():
    assert MultiplierCell(['1', 'Z', '0', 'Z', '1', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_1Z00ZZ():
    assert MultiplierCell(['1', 'Z', '0', '0', 'Z', 'Z']).solve() == ({"bits": ('1', 'Z', '0', '0', 'Z', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_1Z00Z0():
    assert MultiplierCell(['1', 'Z', '0', '0', 'Z', '0']).solve() == ({"bits": ('1', 'Z', '0', '0', 'Z', '0'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_1Z00Z1():
    assert MultiplierCell(['1', 'Z', '0', '0', 'Z', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_1Z000Z():
    assert MultiplierCell(['1', 'Z', '0', '0', '0', 'Z']).solve() == ({"bits": ('1', '0', '0', '0', '0', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_1Z0000():
    assert MultiplierCell(['1', 'Z', '0', '0', '0', '0']).solve() == ({"bits": ('1', '0', '0', '0', '0', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_1Z0001():
    assert MultiplierCell(['1', 'Z', '0', '0', '0', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_1Z001Z():
    assert MultiplierCell(['1', 'Z', '0', '0', '1', 'Z']).solve() == ({"bits": ('1', '1', '0', '0', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_1Z0010():
    assert MultiplierCell(['1', 'Z', '0', '0', '1', '0']).solve() == ({"bits": ('1', '1', '0', '0', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_1Z0011():
    assert MultiplierCell(['1', 'Z', '0', '0', '1', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_1Z01ZZ():
    assert MultiplierCell(['1', 'Z', '0', '1', 'Z', 'Z']).solve() == ({"bits": ('1', 'Z', '0', '1', 'Z', 'Z'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_1Z01Z0():
    assert MultiplierCell(['1', 'Z', '0', '1', 'Z', '0']).solve() == ({"bits": ('1', '0', '0', '1', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_1Z01Z1():
    assert MultiplierCell(['1', 'Z', '0', '1', 'Z', '1']).solve() == ({"bits": ('1', '1', '0', '1', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_1Z010Z():
    assert MultiplierCell(['1', 'Z', '0', '1', '0', 'Z']).solve() == ({"bits": ('1', '1', '0', '1', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_1Z0100():
    assert MultiplierCell(['1', 'Z', '0', '1', '0', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_1Z0101():
    assert MultiplierCell(['1', 'Z', '0', '1', '0', '1']).solve() == ({"bits": ('1', '1', '0', '1', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_1Z011Z():
    assert MultiplierCell(['1', 'Z', '0', '1', '1', 'Z']).solve() == ({"bits": ('1', '0', '0', '1', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_1Z0110():
    assert MultiplierCell(['1', 'Z', '0', '1', '1', '0']).solve() == ({"bits": ('1', '0', '0', '1', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_1Z0111():
    assert MultiplierCell(['1', 'Z', '0', '1', '1', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_1Z1ZZZ():
    assert MultiplierCell(['1', 'Z', '1', 'Z', 'Z', 'Z']).solve() == ({"bits": ('1', 'Z', '1', 'Z', 'Z', 'Z'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_1Z1ZZ0():
    assert MultiplierCell(['1', 'Z', '1', 'Z', 'Z', '0']).solve() == ({"bits": ('1', '0', '1', '0', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_1Z1ZZ1():
    assert MultiplierCell(['1', 'Z', '1', 'Z', 'Z', '1']).solve() == ({"bits": ('1', 'Z', '1', 'Z', 'Z', '1'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_1Z1Z0Z():
    assert MultiplierCell(['1', 'Z', '1', 'Z', '0', 'Z']).solve() == ({"bits": ('1', 'Z', '1', 'Z', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_1Z1Z00():
    assert MultiplierCell(['1', 'Z', '1', 'Z', '0', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_1Z1Z01():
    assert MultiplierCell(['1', 'Z', '1', 'Z', '0', '1']).solve() == ({"bits": ('1', 'Z', '1', 'Z', '0', '1'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_1Z1Z1Z():
    assert MultiplierCell(['1', 'Z', '1', 'Z', '1', 'Z']).solve() == ({"bits": ('1', 'Z', '1', 'Z', '1', 'Z'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_1Z1Z10():
    assert MultiplierCell(['1', 'Z', '1', 'Z', '1', '0']).solve() == ({"bits": ('1', '0', '1', '0', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_1Z1Z11():
    assert MultiplierCell(['1', 'Z', '1', 'Z', '1', '1']).solve() == ({"bits": ('1', '1', '1', '1', '1', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_1Z10ZZ():
    assert MultiplierCell(['1', 'Z', '1', '0', 'Z', 'Z']).solve() == ({"bits": ('1', 'Z', '1', '0', 'Z', 'Z'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_1Z10Z0():
    assert MultiplierCell(['1', 'Z', '1', '0', 'Z', '0']).solve() == ({"bits": ('1', '0', '1', '0', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_1Z10Z1():
    assert MultiplierCell(['1', 'Z', '1', '0', 'Z', '1']).solve() == ({"bits": ('1', '1', '1', '0', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_1Z100Z():
    assert MultiplierCell(['1', 'Z', '1', '0', '0', 'Z']).solve() == ({"bits": ('1', '1', '1', '0', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_1Z1000():
    assert MultiplierCell(['1', 'Z', '1', '0', '0', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_1Z1001():
    assert MultiplierCell(['1', 'Z', '1', '0', '0', '1']).solve() == ({"bits": ('1', '1', '1', '0', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_1Z101Z():
    assert MultiplierCell(['1', 'Z', '1', '0', '1', 'Z']).solve() == ({"bits": ('1', '0', '1', '0', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_1Z1010():
    assert MultiplierCell(['1', 'Z', '1', '0', '1', '0']).solve() == ({"bits": ('1', '0', '1', '0', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_1Z1011():
    assert MultiplierCell(['1', 'Z', '1', '0', '1', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_1Z11ZZ():
    assert MultiplierCell(['1', 'Z', '1', '1', 'Z', 'Z']).solve() == ({"bits": ('1', 'Z', '1', '1', 'Z', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_1Z11Z0():
    assert MultiplierCell(['1', 'Z', '1', '1', 'Z', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_1Z11Z1():
    assert MultiplierCell(['1', 'Z', '1', '1', 'Z', '1']).solve() == ({"bits": ('1', 'Z', '1', '1', 'Z', '1'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_1Z110Z():
    assert MultiplierCell(['1', 'Z', '1', '1', '0', 'Z']).solve() == ({"bits": ('1', '0', '1', '1', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_1Z1100():
    assert MultiplierCell(['1', 'Z', '1', '1', '0', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_1Z1101():
    assert MultiplierCell(['1', 'Z', '1', '1', '0', '1']).solve() == ({"bits": ('1', '0', '1', '1', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_1Z111Z():
    assert MultiplierCell(['1', 'Z', '1', '1', '1', 'Z']).solve() == ({"bits": ('1', '1', '1', '1', '1', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_1Z1110():
    assert MultiplierCell(['1', 'Z', '1', '1', '1', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_1Z1111():
    assert MultiplierCell(['1', 'Z', '1', '1', '1', '1']).solve() == ({"bits": ('1', '1', '1', '1', '1', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_10ZZZZ():
    assert MultiplierCell(['1', '0', 'Z', 'Z', 'Z', 'Z']).solve() == ({"bits": ('1', '0', 'Z', 'Z', 'Z', 'Z'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_10ZZZ0():
    assert MultiplierCell(['1', '0', 'Z', 'Z', 'Z', '0']).solve() == ({"bits": ('1', '0', 'Z', 'Z', 'Z', '0'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_10ZZZ1():
    assert MultiplierCell(['1', '0', 'Z', 'Z', 'Z', '1']).solve() == ({"bits": ('1', '0', '1', '1', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_10ZZ0Z():
    assert MultiplierCell(['1', '0', 'Z', 'Z', '0', 'Z']).solve() == ({"bits": ('1', '0', 'Z', 'Z', '0', 'Z'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_10ZZ00():
    assert MultiplierCell(['1', '0', 'Z', 'Z', '0', '0']).solve() == ({"bits": ('1', '0', '0', '0', '0', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_10ZZ01():
    assert MultiplierCell(['1', '0', 'Z', 'Z', '0', '1']).solve() == ({"bits": ('1', '0', '1', '1', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_10ZZ1Z():
    assert MultiplierCell(['1', '0', 'Z', 'Z', '1', 'Z']).solve() == ({"bits": ('1', '0', 'Z', 'Z', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_10ZZ10():
    assert MultiplierCell(['1', '0', 'Z', 'Z', '1', '0']).solve() == ({"bits": ('1', '0', 'Z', 'Z', '1', '0'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_10ZZ11():
    assert MultiplierCell(['1', '0', 'Z', 'Z', '1', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_10Z0ZZ():
    assert MultiplierCell(['1', '0', 'Z', '0', 'Z', 'Z']).solve() == ({"bits": ('1', '0', 'Z', '0', 'Z', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_10Z0Z0():
    assert MultiplierCell(['1', '0', 'Z', '0', 'Z', '0']).solve() == ({"bits": ('1', '0', 'Z', '0', 'Z', '0'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_10Z0Z1():
    assert MultiplierCell(['1', '0', 'Z', '0', 'Z', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_10Z00Z():
    assert MultiplierCell(['1', '0', 'Z', '0', '0', 'Z']).solve() == ({"bits": ('1', '0', '0', '0', '0', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_10Z000():
    assert MultiplierCell(['1', '0', 'Z', '0', '0', '0']).solve() == ({"bits": ('1', '0', '0', '0', '0', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_10Z001():
    assert MultiplierCell(['1', '0', 'Z', '0', '0', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_10Z01Z():
    assert MultiplierCell(['1', '0', 'Z', '0', '1', 'Z']).solve() == ({"bits": ('1', '0', '1', '0', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_10Z010():
    assert MultiplierCell(['1', '0', 'Z', '0', '1', '0']).solve() == ({"bits": ('1', '0', '1', '0', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_10Z011():
    assert MultiplierCell(['1', '0', 'Z', '0', '1', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_10Z1ZZ():
    assert MultiplierCell(['1', '0', 'Z', '1', 'Z', 'Z']).solve() == ({"bits": ('1', '0', 'Z', '1', 'Z', 'Z'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_10Z1Z0():
    assert MultiplierCell(['1', '0', 'Z', '1', 'Z', '0']).solve() == ({"bits": ('1', '0', '0', '1', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_10Z1Z1():
    assert MultiplierCell(['1', '0', 'Z', '1', 'Z', '1']).solve() == ({"bits": ('1', '0', '1', '1', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_10Z10Z():
    assert MultiplierCell(['1', '0', 'Z', '1', '0', 'Z']).solve() == ({"bits": ('1', '0', '1', '1', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_10Z100():
    assert MultiplierCell(['1', '0', 'Z', '1', '0', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_10Z101():
    assert MultiplierCell(['1', '0', 'Z', '1', '0', '1']).solve() == ({"bits": ('1', '0', '1', '1', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_10Z11Z():
    assert MultiplierCell(['1', '0', 'Z', '1', '1', 'Z']).solve() == ({"bits": ('1', '0', '0', '1', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_10Z110():
    assert MultiplierCell(['1', '0', 'Z', '1', '1', '0']).solve() == ({"bits": ('1', '0', '0', '1', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_10Z111():
    assert MultiplierCell(['1', '0', 'Z', '1', '1', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_100ZZZ():
    assert MultiplierCell(['1', '0', '0', 'Z', 'Z', 'Z']).solve() == ({"bits": ('1', '0', '0', 'Z', 'Z', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_100ZZ0():
    assert MultiplierCell(['1', '0', '0', 'Z', 'Z', '0']).solve() == ({"bits": ('1', '0', '0', 'Z', 'Z', '0'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_100ZZ1():
    assert MultiplierCell(['1', '0', '0', 'Z', 'Z', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_100Z0Z():
    assert MultiplierCell(['1', '0', '0', 'Z', '0', 'Z']).solve() == ({"bits": ('1', '0', '0', '0', '0', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_100Z00():
    assert MultiplierCell(['1', '0', '0', 'Z', '0', '0']).solve() == ({"bits": ('1', '0', '0', '0', '0', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_100Z01():
    assert MultiplierCell(['1', '0', '0', 'Z', '0', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_100Z1Z():
    assert MultiplierCell(['1', '0', '0', 'Z', '1', 'Z']).solve() == ({"bits": ('1', '0', '0', '1', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_100Z10():
    assert MultiplierCell(['1', '0', '0', 'Z', '1', '0']).solve() == ({"bits": ('1', '0', '0', '1', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_100Z11():
    assert MultiplierCell(['1', '0', '0', 'Z', '1', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_1000ZZ():
    assert MultiplierCell(['1', '0', '0', '0', 'Z', 'Z']).solve() == ({"bits": ('1', '0', '0', '0', '0', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_1000Z0():
    assert MultiplierCell(['1', '0', '0', '0', 'Z', '0']).solve() == ({"bits": ('1', '0', '0', '0', '0', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_1000Z1():
    assert MultiplierCell(['1', '0', '0', '0', 'Z', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_10000Z():
    assert MultiplierCell(['1', '0', '0', '0', '0', 'Z']).solve() == ({"bits": ('1', '0', '0', '0', '0', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_100000():
    assert MultiplierCell(['1', '0', '0', '0', '0', '0']).solve() == ({"bits": ('1', '0', '0', '0', '0', '0'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_100001():
    assert MultiplierCell(['1', '0', '0', '0', '0', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_10001Z():
    assert MultiplierCell(['1', '0', '0', '0', '1', 'Z']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_100010():
    assert MultiplierCell(['1', '0', '0', '0', '1', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_100011():
    assert MultiplierCell(['1', '0', '0', '0', '1', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_1001ZZ():
    assert MultiplierCell(['1', '0', '0', '1', 'Z', 'Z']).solve() == ({"bits": ('1', '0', '0', '1', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_1001Z0():
    assert MultiplierCell(['1', '0', '0', '1', 'Z', '0']).solve() == ({"bits": ('1', '0', '0', '1', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_1001Z1():
    assert MultiplierCell(['1', '0', '0', '1', 'Z', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_10010Z():
    assert MultiplierCell(['1', '0', '0', '1', '0', 'Z']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_100100():
    assert MultiplierCell(['1', '0', '0', '1', '0', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_100101():
    assert MultiplierCell(['1', '0', '0', '1', '0', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_10011Z():
    assert MultiplierCell(['1', '0', '0', '1', '1', 'Z']).solve() == ({"bits": ('1', '0', '0', '1', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_100110():
    assert MultiplierCell(['1', '0', '0', '1', '1', '0']).solve() == ({"bits": ('1', '0', '0', '1', '1', '0'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_100111():
    assert MultiplierCell(['1', '0', '0', '1', '1', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_101ZZZ():
    assert MultiplierCell(['1', '0', '1', 'Z', 'Z', 'Z']).solve() == ({"bits": ('1', '0', '1', 'Z', 'Z', 'Z'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_101ZZ0():
    assert MultiplierCell(['1', '0', '1', 'Z', 'Z', '0']).solve() == ({"bits": ('1', '0', '1', '0', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_101ZZ1():
    assert MultiplierCell(['1', '0', '1', 'Z', 'Z', '1']).solve() == ({"bits": ('1', '0', '1', '1', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_101Z0Z():
    assert MultiplierCell(['1', '0', '1', 'Z', '0', 'Z']).solve() == ({"bits": ('1', '0', '1', '1', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_101Z00():
    assert MultiplierCell(['1', '0', '1', 'Z', '0', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_101Z01():
    assert MultiplierCell(['1', '0', '1', 'Z', '0', '1']).solve() == ({"bits": ('1', '0', '1', '1', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_101Z1Z():
    assert MultiplierCell(['1', '0', '1', 'Z', '1', 'Z']).solve() == ({"bits": ('1', '0', '1', '0', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_101Z10():
    assert MultiplierCell(['1', '0', '1', 'Z', '1', '0']).solve() == ({"bits": ('1', '0', '1', '0', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_101Z11():
    assert MultiplierCell(['1', '0', '1', 'Z', '1', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_1010ZZ():
    assert MultiplierCell(['1', '0', '1', '0', 'Z', 'Z']).solve() == ({"bits": ('1', '0', '1', '0', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_1010Z0():
    assert MultiplierCell(['1', '0', '1', '0', 'Z', '0']).solve() == ({"bits": ('1', '0', '1', '0', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_1010Z1():
    assert MultiplierCell(['1', '0', '1', '0', 'Z', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_10100Z():
    assert MultiplierCell(['1', '0', '1', '0', '0', 'Z']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_101000():
    assert MultiplierCell(['1', '0', '1', '0', '0', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_101001():
    assert MultiplierCell(['1', '0', '1', '0', '0', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_10101Z():
    assert MultiplierCell(['1', '0', '1', '0', '1', 'Z']).solve() == ({"bits": ('1', '0', '1', '0', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_101010():
    assert MultiplierCell(['1', '0', '1', '0', '1', '0']).solve() == ({"bits": ('1', '0', '1', '0', '1', '0'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_101011():
    assert MultiplierCell(['1', '0', '1', '0', '1', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_1011ZZ():
    assert MultiplierCell(['1', '0', '1', '1', 'Z', 'Z']).solve() == ({"bits": ('1', '0', '1', '1', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_1011Z0():
    assert MultiplierCell(['1', '0', '1', '1', 'Z', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_1011Z1():
    assert MultiplierCell(['1', '0', '1', '1', 'Z', '1']).solve() == ({"bits": ('1', '0', '1', '1', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_10110Z():
    assert MultiplierCell(['1', '0', '1', '1', '0', 'Z']).solve() == ({"bits": ('1', '0', '1', '1', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_101100():
    assert MultiplierCell(['1', '0', '1', '1', '0', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_101101():
    assert MultiplierCell(['1', '0', '1', '1', '0', '1']).solve() == ({"bits": ('1', '0', '1', '1', '0', '1'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_10111Z():
    assert MultiplierCell(['1', '0', '1', '1', '1', 'Z']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_101110():
    assert MultiplierCell(['1', '0', '1', '1', '1', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_101111():
    assert MultiplierCell(['1', '0', '1', '1', '1', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_11ZZZZ():
    assert MultiplierCell(['1', '1', 'Z', 'Z', 'Z', 'Z']).solve() == ({"bits": ('1', '1', 'Z', 'Z', 'Z', 'Z'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_11ZZZ0():
    assert MultiplierCell(['1', '1', 'Z', 'Z', 'Z', '0']).solve() == ({"bits": ('1', '1', '0', '0', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_11ZZZ1():
    assert MultiplierCell(['1', '1', 'Z', 'Z', 'Z', '1']).solve() == ({"bits": ('1', '1', 'Z', 'Z', 'Z', '1'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_11ZZ0Z():
    assert MultiplierCell(['1', '1', 'Z', 'Z', '0', 'Z']).solve() == ({"bits": ('1', '1', 'Z', 'Z', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_11ZZ00():
    assert MultiplierCell(['1', '1', 'Z', 'Z', '0', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_11ZZ01():
    assert MultiplierCell(['1', '1', 'Z', 'Z', '0', '1']).solve() == ({"bits": ('1', '1', 'Z', 'Z', '0', '1'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_11ZZ1Z():
    assert MultiplierCell(['1', '1', 'Z', 'Z', '1', 'Z']).solve() == ({"bits": ('1', '1', 'Z', 'Z', '1', 'Z'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_11ZZ10():
    assert MultiplierCell(['1', '1', 'Z', 'Z', '1', '0']).solve() == ({"bits": ('1', '1', '0', '0', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_11ZZ11():
    assert MultiplierCell(['1', '1', 'Z', 'Z', '1', '1']).solve() == ({"bits": ('1', '1', '1', '1', '1', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_11Z0ZZ():
    assert MultiplierCell(['1', '1', 'Z', '0', 'Z', 'Z']).solve() == ({"bits": ('1', '1', 'Z', '0', 'Z', 'Z'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_11Z0Z0():
    assert MultiplierCell(['1', '1', 'Z', '0', 'Z', '0']).solve() == ({"bits": ('1', '1', '0', '0', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_11Z0Z1():
    assert MultiplierCell(['1', '1', 'Z', '0', 'Z', '1']).solve() == ({"bits": ('1', '1', '1', '0', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_11Z00Z():
    assert MultiplierCell(['1', '1', 'Z', '0', '0', 'Z']).solve() == ({"bits": ('1', '1', '1', '0', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_11Z000():
    assert MultiplierCell(['1', '1', 'Z', '0', '0', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_11Z001():
    assert MultiplierCell(['1', '1', 'Z', '0', '0', '1']).solve() == ({"bits": ('1', '1', '1', '0', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_11Z01Z():
    assert MultiplierCell(['1', '1', 'Z', '0', '1', 'Z']).solve() == ({"bits": ('1', '1', '0', '0', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_11Z010():
    assert MultiplierCell(['1', '1', 'Z', '0', '1', '0']).solve() == ({"bits": ('1', '1', '0', '0', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_11Z011():
    assert MultiplierCell(['1', '1', 'Z', '0', '1', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_11Z1ZZ():
    assert MultiplierCell(['1', '1', 'Z', '1', 'Z', 'Z']).solve() == ({"bits": ('1', '1', 'Z', '1', 'Z', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_11Z1Z0():
    assert MultiplierCell(['1', '1', 'Z', '1', 'Z', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_11Z1Z1():
    assert MultiplierCell(['1', '1', 'Z', '1', 'Z', '1']).solve() == ({"bits": ('1', '1', 'Z', '1', 'Z', '1'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_11Z10Z():
    assert MultiplierCell(['1', '1', 'Z', '1', '0', 'Z']).solve() == ({"bits": ('1', '1', '0', '1', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_11Z100():
    assert MultiplierCell(['1', '1', 'Z', '1', '0', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_11Z101():
    assert MultiplierCell(['1', '1', 'Z', '1', '0', '1']).solve() == ({"bits": ('1', '1', '0', '1', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_11Z11Z():
    assert MultiplierCell(['1', '1', 'Z', '1', '1', 'Z']).solve() == ({"bits": ('1', '1', '1', '1', '1', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_11Z110():
    assert MultiplierCell(['1', '1', 'Z', '1', '1', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_11Z111():
    assert MultiplierCell(['1', '1', 'Z', '1', '1', '1']).solve() == ({"bits": ('1', '1', '1', '1', '1', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_110ZZZ():
    assert MultiplierCell(['1', '1', '0', 'Z', 'Z', 'Z']).solve() == ({"bits": ('1', '1', '0', 'Z', 'Z', 'Z'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_110ZZ0():
    assert MultiplierCell(['1', '1', '0', 'Z', 'Z', '0']).solve() == ({"bits": ('1', '1', '0', '0', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_110ZZ1():
    assert MultiplierCell(['1', '1', '0', 'Z', 'Z', '1']).solve() == ({"bits": ('1', '1', '0', '1', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_110Z0Z():
    assert MultiplierCell(['1', '1', '0', 'Z', '0', 'Z']).solve() == ({"bits": ('1', '1', '0', '1', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_110Z00():
    assert MultiplierCell(['1', '1', '0', 'Z', '0', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_110Z01():
    assert MultiplierCell(['1', '1', '0', 'Z', '0', '1']).solve() == ({"bits": ('1', '1', '0', '1', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_110Z1Z():
    assert MultiplierCell(['1', '1', '0', 'Z', '1', 'Z']).solve() == ({"bits": ('1', '1', '0', '0', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_110Z10():
    assert MultiplierCell(['1', '1', '0', 'Z', '1', '0']).solve() == ({"bits": ('1', '1', '0', '0', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_110Z11():
    assert MultiplierCell(['1', '1', '0', 'Z', '1', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_1100ZZ():
    assert MultiplierCell(['1', '1', '0', '0', 'Z', 'Z']).solve() == ({"bits": ('1', '1', '0', '0', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_1100Z0():
    assert MultiplierCell(['1', '1', '0', '0', 'Z', '0']).solve() == ({"bits": ('1', '1', '0', '0', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_1100Z1():
    assert MultiplierCell(['1', '1', '0', '0', 'Z', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_11000Z():
    assert MultiplierCell(['1', '1', '0', '0', '0', 'Z']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_110000():
    assert MultiplierCell(['1', '1', '0', '0', '0', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_110001():
    assert MultiplierCell(['1', '1', '0', '0', '0', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_11001Z():
    assert MultiplierCell(['1', '1', '0', '0', '1', 'Z']).solve() == ({"bits": ('1', '1', '0', '0', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_110010():
    assert MultiplierCell(['1', '1', '0', '0', '1', '0']).solve() == ({"bits": ('1', '1', '0', '0', '1', '0'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_110011():
    assert MultiplierCell(['1', '1', '0', '0', '1', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_1101ZZ():
    assert MultiplierCell(['1', '1', '0', '1', 'Z', 'Z']).solve() == ({"bits": ('1', '1', '0', '1', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_1101Z0():
    assert MultiplierCell(['1', '1', '0', '1', 'Z', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_1101Z1():
    assert MultiplierCell(['1', '1', '0', '1', 'Z', '1']).solve() == ({"bits": ('1', '1', '0', '1', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_11010Z():
    assert MultiplierCell(['1', '1', '0', '1', '0', 'Z']).solve() == ({"bits": ('1', '1', '0', '1', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_110100():
    assert MultiplierCell(['1', '1', '0', '1', '0', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_110101():
    assert MultiplierCell(['1', '1', '0', '1', '0', '1']).solve() == ({"bits": ('1', '1', '0', '1', '0', '1'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_11011Z():
    assert MultiplierCell(['1', '1', '0', '1', '1', 'Z']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_110110():
    assert MultiplierCell(['1', '1', '0', '1', '1', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_110111():
    assert MultiplierCell(['1', '1', '0', '1', '1', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_111ZZZ():
    assert MultiplierCell(['1', '1', '1', 'Z', 'Z', 'Z']).solve() == ({"bits": ('1', '1', '1', 'Z', 'Z', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_111ZZ0():
    assert MultiplierCell(['1', '1', '1', 'Z', 'Z', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_111ZZ1():
    assert MultiplierCell(['1', '1', '1', 'Z', 'Z', '1']).solve() == ({"bits": ('1', '1', '1', 'Z', 'Z', '1'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_111Z0Z():
    assert MultiplierCell(['1', '1', '1', 'Z', '0', 'Z']).solve() == ({"bits": ('1', '1', '1', '0', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_111Z00():
    assert MultiplierCell(['1', '1', '1', 'Z', '0', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_111Z01():
    assert MultiplierCell(['1', '1', '1', 'Z', '0', '1']).solve() == ({"bits": ('1', '1', '1', '0', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_111Z1Z():
    assert MultiplierCell(['1', '1', '1', 'Z', '1', 'Z']).solve() == ({"bits": ('1', '1', '1', '1', '1', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_111Z10():
    assert MultiplierCell(['1', '1', '1', 'Z', '1', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_111Z11():
    assert MultiplierCell(['1', '1', '1', 'Z', '1', '1']).solve() == ({"bits": ('1', '1', '1', '1', '1', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_1110ZZ():
    assert MultiplierCell(['1', '1', '1', '0', 'Z', 'Z']).solve() == ({"bits": ('1', '1', '1', '0', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_1110Z0():
    assert MultiplierCell(['1', '1', '1', '0', 'Z', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_1110Z1():
    assert MultiplierCell(['1', '1', '1', '0', 'Z', '1']).solve() == ({"bits": ('1', '1', '1', '0', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_11100Z():
    assert MultiplierCell(['1', '1', '1', '0', '0', 'Z']).solve() == ({"bits": ('1', '1', '1', '0', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_111000():
    assert MultiplierCell(['1', '1', '1', '0', '0', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_111001():
    assert MultiplierCell(['1', '1', '1', '0', '0', '1']).solve() == ({"bits": ('1', '1', '1', '0', '0', '1'), "error": '0', "change": '0'}) # NO MOD
def test_mc_case_11101Z():
    assert MultiplierCell(['1', '1', '1', '0', '1', 'Z']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_111010():
    assert MultiplierCell(['1', '1', '1', '0', '1', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_111011():
    assert MultiplierCell(['1', '1', '1', '0', '1', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_1111ZZ():
    assert MultiplierCell(['1', '1', '1', '1', 'Z', 'Z']).solve() == ({"bits": ('1', '1', '1', '1', '1', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_1111Z0():
    assert MultiplierCell(['1', '1', '1', '1', 'Z', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_1111Z1():
    assert MultiplierCell(['1', '1', '1', '1', 'Z', '1']).solve() == ({"bits": ('1', '1', '1', '1', '1', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_11110Z():
    assert MultiplierCell(['1', '1', '1', '1', '0', 'Z']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_111100():
    assert MultiplierCell(['1', '1', '1', '1', '0', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_111101():
    assert MultiplierCell(['1', '1', '1', '1', '0', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_11111Z():
    assert MultiplierCell(['1', '1', '1', '1', '1', 'Z']).solve() == ({"bits": ('1', '1', '1', '1', '1', '1'), "error": '0', "change": '1'}) # NO MOD
def test_mc_case_111110():
    assert MultiplierCell(['1', '1', '1', '1', '1', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_mc_case_111111():
    assert MultiplierCell(['1', '1', '1', '1', '1', '1']).solve() == ({"bits": ('1', '1', '1', '1', '1', '1'), "error": '0', "change": '0'}) # NO MOD
