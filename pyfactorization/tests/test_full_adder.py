from pyfactorization.FullAdder import FullAdder

def test_fa_case_ZZZZZ():
    assert FullAdder(['Z', 'Z', 'Z', 'Z', 'Z']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z'), "error": '0', "change": '0'}) # NO MOD
def test_fa_case_ZZZZ0():
    assert FullAdder(['Z', 'Z', 'Z', 'Z', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', '0'), "error": '0', "change": '0'}) # NO MOD
def test_fa_case_ZZZZ1():
    assert FullAdder(['Z', 'Z', 'Z', 'Z', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', '1'), "error": '0', "change": '0'}) # NO MOD
def test_fa_case_ZZZ0Z():
    assert FullAdder(['Z', 'Z', 'Z', '0', 'Z']).solve() == ({"bits": ('Z', 'Z', 'Z', '0', 'Z'), "error": '0', "change": '0'}) # NO MOD
def test_fa_case_ZZZ00():
    assert FullAdder(['Z', 'Z', 'Z', '0', '0']).solve() == ({"bits": ('0', '0', '0', '0', '0'), "error": '0', "change": '1'}) # NO MOD
def test_fa_case_ZZZ01():
    assert FullAdder(['Z', 'Z', 'Z', '0', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', '0', '1'), "error": '0', "change": '0'}) # NO MOD
def test_fa_case_ZZZ1Z():
    assert FullAdder(['Z', 'Z', 'Z', '1', 'Z']).solve() == ({"bits": ('Z', 'Z', 'Z', '1', 'Z'), "error": '0', "change": '0'}) # NO MOD
def test_fa_case_ZZZ10():
    assert FullAdder(['Z', 'Z', 'Z', '1', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', '1', '0'), "error": '0', "change": '0'}) # NO MOD
def test_fa_case_ZZZ11():
    assert FullAdder(['Z', 'Z', 'Z', '1', '1']).solve() == ({"bits": ('1', '1', '1', '1', '1'), "error": '0', "change": '1'}) # NO MOD
def test_fa_case_ZZ0ZZ():
    assert FullAdder(['Z', 'Z', '0', 'Z', 'Z']).solve() == ({"bits": ('Z', 'Z', '0', 'Z', 'Z'), "error": '0', "change": '0'}) # NO MOD
def test_fa_case_ZZ0Z0():
    assert FullAdder(['Z', 'Z', '0', 'Z', '0']).solve() == ({"bits": ('Z', 'Z', '0', 'Z', '0'), "error": '0', "change": '0'}) # NO MOD
def test_fa_case_ZZ0Z1():
    assert FullAdder(['Z', 'Z', '0', 'Z', '1']).solve() == ({"bits": ('1', '1', '0', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_fa_case_ZZ00Z():
    assert FullAdder(['Z', 'Z', '0', '0', 'Z']).solve() == ({"bits": ('Z', 'Z', '0', '0', 'Z'), "error": '0', "change": '0'}) # NO MOD
def test_fa_case_ZZ000():
    assert FullAdder(['Z', 'Z', '0', '0', '0']).solve() == ({"bits": ('0', '0', '0', '0', '0'), "error": '0', "change": '1'}) # NO MOD
def test_fa_case_ZZ001():
    assert FullAdder(['Z', 'Z', '0', '0', '1']).solve() == ({"bits": ('1', '1', '0', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_fa_case_ZZ01Z():
    assert FullAdder(['Z', 'Z', '0', '1', 'Z']).solve() == ({"bits": ('Z', 'Z', '0', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_fa_case_ZZ010():
    assert FullAdder(['Z', 'Z', '0', '1', '0']).solve() == ({"bits": ('Z', 'Z', '0', '1', '0'), "error": '0', "change": '0'}) # NO MOD
def test_fa_case_ZZ011():
    assert FullAdder(['Z', 'Z', '0', '1', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_fa_case_ZZ1ZZ():
    assert FullAdder(['Z', 'Z', '1', 'Z', 'Z']).solve() == ({"bits": ('Z', 'Z', '1', 'Z', 'Z'), "error": '0', "change": '0'}) # NO MOD
def test_fa_case_ZZ1Z0():
    assert FullAdder(['Z', 'Z', '1', 'Z', '0']).solve() == ({"bits": ('0', '0', '1', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_fa_case_ZZ1Z1():
    assert FullAdder(['Z', 'Z', '1', 'Z', '1']).solve() == ({"bits": ('Z', 'Z', '1', 'Z', '1'), "error": '0', "change": '0'}) # NO MOD
def test_fa_case_ZZ10Z():
    assert FullAdder(['Z', 'Z', '1', '0', 'Z']).solve() == ({"bits": ('Z', 'Z', '1', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_fa_case_ZZ100():
    assert FullAdder(['Z', 'Z', '1', '0', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_fa_case_ZZ101():
    assert FullAdder(['Z', 'Z', '1', '0', '1']).solve() == ({"bits": ('Z', 'Z', '1', '0', '1'), "error": '0', "change": '0'}) # NO MOD
def test_fa_case_ZZ11Z():
    assert FullAdder(['Z', 'Z', '1', '1', 'Z']).solve() == ({"bits": ('Z', 'Z', '1', '1', 'Z'), "error": '0', "change": '0'}) # NO MOD
def test_fa_case_ZZ110():
    assert FullAdder(['Z', 'Z', '1', '1', '0']).solve() == ({"bits": ('0', '0', '1', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_fa_case_ZZ111():
    assert FullAdder(['Z', 'Z', '1', '1', '1']).solve() == ({"bits": ('1', '1', '1', '1', '1'), "error": '0', "change": '1'}) # NO MOD
def test_fa_case_Z0ZZZ():
    assert FullAdder(['Z', '0', 'Z', 'Z', 'Z']).solve() == ({"bits": ('Z', '0', 'Z', 'Z', 'Z'), "error": '0', "change": '0'}) # NO MOD
def test_fa_case_Z0ZZ0():
    assert FullAdder(['Z', '0', 'Z', 'Z', '0']).solve() == ({"bits": ('Z', '0', 'Z', 'Z', '0'), "error": '0', "change": '0'}) # NO MOD
def test_fa_case_Z0ZZ1():
    assert FullAdder(['Z', '0', 'Z', 'Z', '1']).solve() == ({"bits": ('1', '0', '1', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_fa_case_Z0Z0Z():
    assert FullAdder(['Z', '0', 'Z', '0', 'Z']).solve() == ({"bits": ('Z', '0', 'Z', '0', 'Z'), "error": '0', "change": '0'}) # NO MOD
def test_fa_case_Z0Z00():
    assert FullAdder(['Z', '0', 'Z', '0', '0']).solve() == ({"bits": ('0', '0', '0', '0', '0'), "error": '0', "change": '1'}) # NO MOD
def test_fa_case_Z0Z01():
    assert FullAdder(['Z', '0', 'Z', '0', '1']).solve() == ({"bits": ('1', '0', '1', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_fa_case_Z0Z1Z():
    assert FullAdder(['Z', '0', 'Z', '1', 'Z']).solve() == ({"bits": ('Z', '0', 'Z', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_fa_case_Z0Z10():
    assert FullAdder(['Z', '0', 'Z', '1', '0']).solve() == ({"bits": ('Z', '0', 'Z', '1', '0'), "error": '0', "change": '0'}) # NO MOD
def test_fa_case_Z0Z11():
    assert FullAdder(['Z', '0', 'Z', '1', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_fa_case_Z00ZZ():
    assert FullAdder(['Z', '0', '0', 'Z', 'Z']).solve() == ({"bits": ('Z', '0', '0', 'Z', '0'), "error": '0', "change": '1'}) # NO MOD
def test_fa_case_Z00Z0():
    assert FullAdder(['Z', '0', '0', 'Z', '0']).solve() == ({"bits": ('Z', '0', '0', 'Z', '0'), "error": '0', "change": '0'}) # NO MOD
def test_fa_case_Z00Z1():
    assert FullAdder(['Z', '0', '0', 'Z', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_fa_case_Z000Z():
    assert FullAdder(['Z', '0', '0', '0', 'Z']).solve() == ({"bits": ('0', '0', '0', '0', '0'), "error": '0', "change": '1'}) # NO MOD
def test_fa_case_Z0000():
    assert FullAdder(['Z', '0', '0', '0', '0']).solve() == ({"bits": ('0', '0', '0', '0', '0'), "error": '0', "change": '1'}) # NO MOD
def test_fa_case_Z0001():
    assert FullAdder(['Z', '0', '0', '0', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_fa_case_Z001Z():
    assert FullAdder(['Z', '0', '0', '1', 'Z']).solve() == ({"bits": ('1', '0', '0', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_fa_case_Z0010():
    assert FullAdder(['Z', '0', '0', '1', '0']).solve() == ({"bits": ('1', '0', '0', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_fa_case_Z0011():
    assert FullAdder(['Z', '0', '0', '1', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_fa_case_Z01ZZ():
    assert FullAdder(['Z', '0', '1', 'Z', 'Z']).solve() == ({"bits": ('Z', '0', '1', 'Z', 'Z'), "error": '0', "change": '0'}) # NO MOD
def test_fa_case_Z01Z0():
    assert FullAdder(['Z', '0', '1', 'Z', '0']).solve() == ({"bits": ('0', '0', '1', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_fa_case_Z01Z1():
    assert FullAdder(['Z', '0', '1', 'Z', '1']).solve() == ({"bits": ('1', '0', '1', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_fa_case_Z010Z():
    assert FullAdder(['Z', '0', '1', '0', 'Z']).solve() == ({"bits": ('1', '0', '1', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_fa_case_Z0100():
    assert FullAdder(['Z', '0', '1', '0', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_fa_case_Z0101():
    assert FullAdder(['Z', '0', '1', '0', '1']).solve() == ({"bits": ('1', '0', '1', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_fa_case_Z011Z():
    assert FullAdder(['Z', '0', '1', '1', 'Z']).solve() == ({"bits": ('0', '0', '1', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_fa_case_Z0110():
    assert FullAdder(['Z', '0', '1', '1', '0']).solve() == ({"bits": ('0', '0', '1', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_fa_case_Z0111():
    assert FullAdder(['Z', '0', '1', '1', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_fa_case_Z1ZZZ():
    assert FullAdder(['Z', '1', 'Z', 'Z', 'Z']).solve() == ({"bits": ('Z', '1', 'Z', 'Z', 'Z'), "error": '0', "change": '0'}) # NO MOD
def test_fa_case_Z1ZZ0():
    assert FullAdder(['Z', '1', 'Z', 'Z', '0']).solve() == ({"bits": ('0', '1', '0', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_fa_case_Z1ZZ1():
    assert FullAdder(['Z', '1', 'Z', 'Z', '1']).solve() == ({"bits": ('Z', '1', 'Z', 'Z', '1'), "error": '0', "change": '0'}) # NO MOD
def test_fa_case_Z1Z0Z():
    assert FullAdder(['Z', '1', 'Z', '0', 'Z']).solve() == ({"bits": ('Z', '1', 'Z', '0', '1'), "error": '0', "change": '1'}) #    MOD
def test_fa_case_Z1Z00():
    assert FullAdder(['Z', '1', 'Z', '0', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_fa_case_Z1Z01():
    assert FullAdder(['Z', '1', 'Z', '0', '1']).solve() == ({"bits": ('Z', '1', 'Z', '0', '1'), "error": '0', "change": '0'}) # NO MOD
def test_fa_case_Z1Z1Z():
    assert FullAdder(['Z', '1', 'Z', '1', 'Z']).solve() == ({"bits": ('Z', '1', 'Z', '1', 'Z'), "error": '0', "change": '0'}) # NO MOD
def test_fa_case_Z1Z10():
    assert FullAdder(['Z', '1', 'Z', '1', '0']).solve() == ({"bits": ('0', '1', '0', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_fa_case_Z1Z11():
    assert FullAdder(['Z', '1', 'Z', '1', '1']).solve() == ({"bits": ('1', '1', '1', '1', '1'), "error": '0', "change": '1'}) # NO MOD
def test_fa_case_Z10ZZ():
    assert FullAdder(['Z', '1', '0', 'Z', 'Z']).solve() == ({"bits": ('Z', '1', '0', 'Z', 'Z'), "error": '0', "change": '0'}) # NO MOD
def test_fa_case_Z10Z0():
    assert FullAdder(['Z', '1', '0', 'Z', '0']).solve() == ({"bits": ('0', '1', '0', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_fa_case_Z10Z1():
    assert FullAdder(['Z', '1', '0', 'Z', '1']).solve() == ({"bits": ('1', '1', '0', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_fa_case_Z100Z():
    assert FullAdder(['Z', '1', '0', '0', 'Z']).solve() == ({"bits": ('1', '1', '0', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_fa_case_Z1000():
    assert FullAdder(['Z', '1', '0', '0', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_fa_case_Z1001():
    assert FullAdder(['Z', '1', '0', '0', '1']).solve() == ({"bits": ('1', '1', '0', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_fa_case_Z101Z():
    assert FullAdder(['Z', '1', '0', '1', 'Z']).solve() == ({"bits": ('0', '1', '0', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_fa_case_Z1010():
    assert FullAdder(['Z', '1', '0', '1', '0']).solve() == ({"bits": ('0', '1', '0', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_fa_case_Z1011():
    assert FullAdder(['Z', '1', '0', '1', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_fa_case_Z11ZZ():
    assert FullAdder(['Z', '1', '1', 'Z', 'Z']).solve() == ({"bits": ('Z', '1', '1', 'Z', '1'), "error": '0', "change": '1'}) #    MOD
def test_fa_case_Z11Z0():
    assert FullAdder(['Z', '1', '1', 'Z', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_fa_case_Z11Z1():
    assert FullAdder(['Z', '1', '1', 'Z', '1']).solve() == ({"bits": ('Z', '1', '1', 'Z', '1'), "error": '0', "change": '0'}) # NO MOD
def test_fa_case_Z110Z():
    assert FullAdder(['Z', '1', '1', '0', 'Z']).solve() == ({"bits": ('0', '1', '1', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_fa_case_Z1100():
    assert FullAdder(['Z', '1', '1', '0', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_fa_case_Z1101():
    assert FullAdder(['Z', '1', '1', '0', '1']).solve() == ({"bits": ('0', '1', '1', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_fa_case_Z111Z():
    assert FullAdder(['Z', '1', '1', '1', 'Z']).solve() == ({"bits": ('1', '1', '1', '1', '1'), "error": '0', "change": '1'}) # NO MOD
def test_fa_case_Z1110():
    assert FullAdder(['Z', '1', '1', '1', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_fa_case_Z1111():
    assert FullAdder(['Z', '1', '1', '1', '1']).solve() == ({"bits": ('1', '1', '1', '1', '1'), "error": '0', "change": '1'}) # NO MOD
def test_fa_case_0ZZZZ():
    assert FullAdder(['0', 'Z', 'Z', 'Z', 'Z']).solve() == ({"bits": ('0', 'Z', 'Z', 'Z', 'Z'), "error": '0', "change": '0'}) # NO MOD
def test_fa_case_0ZZZ0():
    assert FullAdder(['0', 'Z', 'Z', 'Z', '0']).solve() == ({"bits": ('0', 'Z', 'Z', 'Z', '0'), "error": '0', "change": '0'}) # NO MOD
def test_fa_case_0ZZZ1():
    assert FullAdder(['0', 'Z', 'Z', 'Z', '1']).solve() == ({"bits": ('0', '1', '1', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_fa_case_0ZZ0Z():
    assert FullAdder(['0', 'Z', 'Z', '0', 'Z']).solve() == ({"bits": ('0', 'Z', 'Z', '0', 'Z'), "error": '0', "change": '0'}) # NO MOD
def test_fa_case_0ZZ00():
    assert FullAdder(['0', 'Z', 'Z', '0', '0']).solve() == ({"bits": ('0', '0', '0', '0', '0'), "error": '0', "change": '1'}) # NO MOD
def test_fa_case_0ZZ01():
    assert FullAdder(['0', 'Z', 'Z', '0', '1']).solve() == ({"bits": ('0', '1', '1', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_fa_case_0ZZ1Z():
    assert FullAdder(['0', 'Z', 'Z', '1', 'Z']).solve() == ({"bits": ('0', 'Z', 'Z', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_fa_case_0ZZ10():
    assert FullAdder(['0', 'Z', 'Z', '1', '0']).solve() == ({"bits": ('0', 'Z', 'Z', '1', '0'), "error": '0', "change": '0'}) # NO MOD
def test_fa_case_0ZZ11():
    assert FullAdder(['0', 'Z', 'Z', '1', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_fa_case_0Z0ZZ():
    assert FullAdder(['0', 'Z', '0', 'Z', 'Z']).solve() == ({"bits": ('0', 'Z', '0', 'Z', '0'), "error": '0', "change": '1'}) # NO MOD
def test_fa_case_0Z0Z0():
    assert FullAdder(['0', 'Z', '0', 'Z', '0']).solve() == ({"bits": ('0', 'Z', '0', 'Z', '0'), "error": '0', "change": '0'}) # NO MOD
def test_fa_case_0Z0Z1():
    assert FullAdder(['0', 'Z', '0', 'Z', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_fa_case_0Z00Z():
    assert FullAdder(['0', 'Z', '0', '0', 'Z']).solve() == ({"bits": ('0', '0', '0', '0', '0'), "error": '0', "change": '1'}) # NO MOD
def test_fa_case_0Z000():
    assert FullAdder(['0', 'Z', '0', '0', '0']).solve() == ({"bits": ('0', '0', '0', '0', '0'), "error": '0', "change": '1'}) # NO MOD
def test_fa_case_0Z001():
    assert FullAdder(['0', 'Z', '0', '0', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_fa_case_0Z01Z():
    assert FullAdder(['0', 'Z', '0', '1', 'Z']).solve() == ({"bits": ('0', '1', '0', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_fa_case_0Z010():
    assert FullAdder(['0', 'Z', '0', '1', '0']).solve() == ({"bits": ('0', '1', '0', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_fa_case_0Z011():
    assert FullAdder(['0', 'Z', '0', '1', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_fa_case_0Z1ZZ():
    assert FullAdder(['0', 'Z', '1', 'Z', 'Z']).solve() == ({"bits": ('0', 'Z', '1', 'Z', 'Z'), "error": '0', "change": '0'}) # NO MOD
def test_fa_case_0Z1Z0():
    assert FullAdder(['0', 'Z', '1', 'Z', '0']).solve() == ({"bits": ('0', '0', '1', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_fa_case_0Z1Z1():
    assert FullAdder(['0', 'Z', '1', 'Z', '1']).solve() == ({"bits": ('0', '1', '1', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_fa_case_0Z10Z():
    assert FullAdder(['0', 'Z', '1', '0', 'Z']).solve() == ({"bits": ('0', '1', '1', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_fa_case_0Z100():
    assert FullAdder(['0', 'Z', '1', '0', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_fa_case_0Z101():
    assert FullAdder(['0', 'Z', '1', '0', '1']).solve() == ({"bits": ('0', '1', '1', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_fa_case_0Z11Z():
    assert FullAdder(['0', 'Z', '1', '1', 'Z']).solve() == ({"bits": ('0', '0', '1', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_fa_case_0Z110():
    assert FullAdder(['0', 'Z', '1', '1', '0']).solve() == ({"bits": ('0', '0', '1', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_fa_case_0Z111():
    assert FullAdder(['0', 'Z', '1', '1', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_fa_case_00ZZZ():
    assert FullAdder(['0', '0', 'Z', 'Z', 'Z']).solve() == ({"bits": ('0', '0', 'Z', 'Z', '0'), "error": '0', "change": '1'}) # NO MOD
def test_fa_case_00ZZ0():
    assert FullAdder(['0', '0', 'Z', 'Z', '0']).solve() == ({"bits": ('0', '0', 'Z', 'Z', '0'), "error": '0', "change": '0'}) # NO MOD
def test_fa_case_00ZZ1():
    assert FullAdder(['0', '0', 'Z', 'Z', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_fa_case_00Z0Z():
    assert FullAdder(['0', '0', 'Z', '0', 'Z']).solve() == ({"bits": ('0', '0', '0', '0', '0'), "error": '0', "change": '1'}) # NO MOD
def test_fa_case_00Z00():
    assert FullAdder(['0', '0', 'Z', '0', '0']).solve() == ({"bits": ('0', '0', '0', '0', '0'), "error": '0', "change": '1'}) # NO MOD
def test_fa_case_00Z01():
    assert FullAdder(['0', '0', 'Z', '0', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_fa_case_00Z1Z():
    assert FullAdder(['0', '0', 'Z', '1', 'Z']).solve() == ({"bits": ('0', '0', '1', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_fa_case_00Z10():
    assert FullAdder(['0', '0', 'Z', '1', '0']).solve() == ({"bits": ('0', '0', '1', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_fa_case_00Z11():
    assert FullAdder(['0', '0', 'Z', '1', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_fa_case_000ZZ():
    assert FullAdder(['0', '0', '0', 'Z', 'Z']).solve() == ({"bits": ('0', '0', '0', '0', '0'), "error": '0', "change": '1'}) # NO MOD
def test_fa_case_000Z0():
    assert FullAdder(['0', '0', '0', 'Z', '0']).solve() == ({"bits": ('0', '0', '0', '0', '0'), "error": '0', "change": '1'}) # NO MOD
def test_fa_case_000Z1():
    assert FullAdder(['0', '0', '0', 'Z', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_fa_case_0000Z():
    assert FullAdder(['0', '0', '0', '0', 'Z']).solve() == ({"bits": ('0', '0', '0', '0', '0'), "error": '0', "change": '1'}) # NO MOD
def test_fa_case_00000():
    assert FullAdder(['0', '0', '0', '0', '0']).solve() == ({"bits": ('0', '0', '0', '0', '0'), "error": '0', "change": '0'}) # NO MOD
def test_fa_case_00001():
    assert FullAdder(['0', '0', '0', '0', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_fa_case_0001Z():
    assert FullAdder(['0', '0', '0', '1', 'Z']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_fa_case_00010():
    assert FullAdder(['0', '0', '0', '1', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_fa_case_00011():
    assert FullAdder(['0', '0', '0', '1', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_fa_case_001ZZ():
    assert FullAdder(['0', '0', '1', 'Z', 'Z']).solve() == ({"bits": ('0', '0', '1', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_fa_case_001Z0():
    assert FullAdder(['0', '0', '1', 'Z', '0']).solve() == ({"bits": ('0', '0', '1', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_fa_case_001Z1():
    assert FullAdder(['0', '0', '1', 'Z', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_fa_case_0010Z():
    assert FullAdder(['0', '0', '1', '0', 'Z']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_fa_case_00100():
    assert FullAdder(['0', '0', '1', '0', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_fa_case_00101():
    assert FullAdder(['0', '0', '1', '0', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_fa_case_0011Z():
    assert FullAdder(['0', '0', '1', '1', 'Z']).solve() == ({"bits": ('0', '0', '1', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_fa_case_00110():
    assert FullAdder(['0', '0', '1', '1', '0']).solve() == ({"bits": ('0', '0', '1', '1', '0'), "error": '0', "change": '0'}) # NO MOD
def test_fa_case_00111():
    assert FullAdder(['0', '0', '1', '1', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_fa_case_01ZZZ():
    assert FullAdder(['0', '1', 'Z', 'Z', 'Z']).solve() == ({"bits": ('0', '1', 'Z', 'Z', 'Z'), "error": '0', "change": '0'}) # NO MOD
def test_fa_case_01ZZ0():
    assert FullAdder(['0', '1', 'Z', 'Z', '0']).solve() == ({"bits": ('0', '1', '0', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_fa_case_01ZZ1():
    assert FullAdder(['0', '1', 'Z', 'Z', '1']).solve() == ({"bits": ('0', '1', '1', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_fa_case_01Z0Z():
    assert FullAdder(['0', '1', 'Z', '0', 'Z']).solve() == ({"bits": ('0', '1', '1', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_fa_case_01Z00():
    assert FullAdder(['0', '1', 'Z', '0', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_fa_case_01Z01():
    assert FullAdder(['0', '1', 'Z', '0', '1']).solve() == ({"bits": ('0', '1', '1', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_fa_case_01Z1Z():
    assert FullAdder(['0', '1', 'Z', '1', 'Z']).solve() == ({"bits": ('0', '1', '0', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_fa_case_01Z10():
    assert FullAdder(['0', '1', 'Z', '1', '0']).solve() == ({"bits": ('0', '1', '0', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_fa_case_01Z11():
    assert FullAdder(['0', '1', 'Z', '1', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_fa_case_010ZZ():
    assert FullAdder(['0', '1', '0', 'Z', 'Z']).solve() == ({"bits": ('0', '1', '0', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_fa_case_010Z0():
    assert FullAdder(['0', '1', '0', 'Z', '0']).solve() == ({"bits": ('0', '1', '0', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_fa_case_010Z1():
    assert FullAdder(['0', '1', '0', 'Z', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_fa_case_0100Z():
    assert FullAdder(['0', '1', '0', '0', 'Z']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_fa_case_01000():
    assert FullAdder(['0', '1', '0', '0', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_fa_case_01001():
    assert FullAdder(['0', '1', '0', '0', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_fa_case_0101Z():
    assert FullAdder(['0', '1', '0', '1', 'Z']).solve() == ({"bits": ('0', '1', '0', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_fa_case_01010():
    assert FullAdder(['0', '1', '0', '1', '0']).solve() == ({"bits": ('0', '1', '0', '1', '0'), "error": '0', "change": '0'}) # NO MOD
def test_fa_case_01011():
    assert FullAdder(['0', '1', '0', '1', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_fa_case_011ZZ():
    assert FullAdder(['0', '1', '1', 'Z', 'Z']).solve() == ({"bits": ('0', '1', '1', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_fa_case_011Z0():
    assert FullAdder(['0', '1', '1', 'Z', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_fa_case_011Z1():
    assert FullAdder(['0', '1', '1', 'Z', '1']).solve() == ({"bits": ('0', '1', '1', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_fa_case_0110Z():
    assert FullAdder(['0', '1', '1', '0', 'Z']).solve() == ({"bits": ('0', '1', '1', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_fa_case_01100():
    assert FullAdder(['0', '1', '1', '0', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_fa_case_01101():
    assert FullAdder(['0', '1', '1', '0', '1']).solve() == ({"bits": ('0', '1', '1', '0', '1'), "error": '0', "change": '0'}) # NO MOD
def test_fa_case_0111Z():
    assert FullAdder(['0', '1', '1', '1', 'Z']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_fa_case_01110():
    assert FullAdder(['0', '1', '1', '1', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_fa_case_01111():
    assert FullAdder(['0', '1', '1', '1', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_fa_case_1ZZZZ():
    assert FullAdder(['1', 'Z', 'Z', 'Z', 'Z']).solve() == ({"bits": ('1', 'Z', 'Z', 'Z', 'Z'), "error": '0', "change": '0'}) # NO MOD
def test_fa_case_1ZZZ0():
    assert FullAdder(['1', 'Z', 'Z', 'Z', '0']).solve() == ({"bits": ('1', '0', '0', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_fa_case_1ZZZ1():
    assert FullAdder(['1', 'Z', 'Z', 'Z', '1']).solve() == ({"bits": ('1', 'Z', 'Z', 'Z', '1'), "error": '0', "change": '0'}) # NO MOD
def test_fa_case_1ZZ0Z():
    assert FullAdder(['1', 'Z', 'Z', '0', 'Z']).solve() == ({"bits": ('1', 'Z', 'Z', '0', '1'), "error": '0', "change": '1'}) #    MOD
def test_fa_case_1ZZ00():
    assert FullAdder(['1', 'Z', 'Z', '0', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_fa_case_1ZZ01():
    assert FullAdder(['1', 'Z', 'Z', '0', '1']).solve() == ({"bits": ('1', 'Z', 'Z', '0', '1'), "error": '0', "change": '0'}) # NO MOD
def test_fa_case_1ZZ1Z():
    assert FullAdder(['1', 'Z', 'Z', '1', 'Z']).solve() == ({"bits": ('1', 'Z', 'Z', '1', 'Z'), "error": '0', "change": '0'}) # NO MOD
def test_fa_case_1ZZ10():
    assert FullAdder(['1', 'Z', 'Z', '1', '0']).solve() == ({"bits": ('1', '0', '0', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_fa_case_1ZZ11():
    assert FullAdder(['1', 'Z', 'Z', '1', '1']).solve() == ({"bits": ('1', '1', '1', '1', '1'), "error": '0', "change": '1'}) # NO MOD
def test_fa_case_1Z0ZZ():
    assert FullAdder(['1', 'Z', '0', 'Z', 'Z']).solve() == ({"bits": ('1', 'Z', '0', 'Z', 'Z'), "error": '0', "change": '0'}) # NO MOD
def test_fa_case_1Z0Z0():
    assert FullAdder(['1', 'Z', '0', 'Z', '0']).solve() == ({"bits": ('1', '0', '0', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_fa_case_1Z0Z1():
    assert FullAdder(['1', 'Z', '0', 'Z', '1']).solve() == ({"bits": ('1', '1', '0', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_fa_case_1Z00Z():
    assert FullAdder(['1', 'Z', '0', '0', 'Z']).solve() == ({"bits": ('1', '1', '0', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_fa_case_1Z000():
    assert FullAdder(['1', 'Z', '0', '0', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_fa_case_1Z001():
    assert FullAdder(['1', 'Z', '0', '0', '1']).solve() == ({"bits": ('1', '1', '0', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_fa_case_1Z01Z():
    assert FullAdder(['1', 'Z', '0', '1', 'Z']).solve() == ({"bits": ('1', '0', '0', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_fa_case_1Z010():
    assert FullAdder(['1', 'Z', '0', '1', '0']).solve() == ({"bits": ('1', '0', '0', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_fa_case_1Z011():
    assert FullAdder(['1', 'Z', '0', '1', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_fa_case_1Z1ZZ():
    assert FullAdder(['1', 'Z', '1', 'Z', 'Z']).solve() == ({"bits": ('1', 'Z', '1', 'Z', '1'), "error": '0', "change": '1'}) #    MOD
def test_fa_case_1Z1Z0():
    assert FullAdder(['1', 'Z', '1', 'Z', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_fa_case_1Z1Z1():
    assert FullAdder(['1', 'Z', '1', 'Z', '1']).solve() == ({"bits": ('1', 'Z', '1', 'Z', '1'), "error": '0', "change": '0'}) # NO MOD
def test_fa_case_1Z10Z():
    assert FullAdder(['1', 'Z', '1', '0', 'Z']).solve() == ({"bits": ('1', '0', '1', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_fa_case_1Z100():
    assert FullAdder(['1', 'Z', '1', '0', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_fa_case_1Z101():
    assert FullAdder(['1', 'Z', '1', '0', '1']).solve() == ({"bits": ('1', '0', '1', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_fa_case_1Z11Z():
    assert FullAdder(['1', 'Z', '1', '1', 'Z']).solve() == ({"bits": ('1', '1', '1', '1', '1'), "error": '0', "change": '1'}) # NO MOD
def test_fa_case_1Z110():
    assert FullAdder(['1', 'Z', '1', '1', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_fa_case_1Z111():
    assert FullAdder(['1', 'Z', '1', '1', '1']).solve() == ({"bits": ('1', '1', '1', '1', '1'), "error": '0', "change": '1'}) # NO MOD
def test_fa_case_10ZZZ():
    assert FullAdder(['1', '0', 'Z', 'Z', 'Z']).solve() == ({"bits": ('1', '0', 'Z', 'Z', 'Z'), "error": '0', "change": '0'}) # NO MOD
def test_fa_case_10ZZ0():
    assert FullAdder(['1', '0', 'Z', 'Z', '0']).solve() == ({"bits": ('1', '0', '0', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_fa_case_10ZZ1():
    assert FullAdder(['1', '0', 'Z', 'Z', '1']).solve() == ({"bits": ('1', '0', '1', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_fa_case_10Z0Z():
    assert FullAdder(['1', '0', 'Z', '0', 'Z']).solve() == ({"bits": ('1', '0', '1', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_fa_case_10Z00():
    assert FullAdder(['1', '0', 'Z', '0', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_fa_case_10Z01():
    assert FullAdder(['1', '0', 'Z', '0', '1']).solve() == ({"bits": ('1', '0', '1', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_fa_case_10Z1Z():
    assert FullAdder(['1', '0', 'Z', '1', 'Z']).solve() == ({"bits": ('1', '0', '0', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_fa_case_10Z10():
    assert FullAdder(['1', '0', 'Z', '1', '0']).solve() == ({"bits": ('1', '0', '0', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_fa_case_10Z11():
    assert FullAdder(['1', '0', 'Z', '1', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_fa_case_100ZZ():
    assert FullAdder(['1', '0', '0', 'Z', 'Z']).solve() == ({"bits": ('1', '0', '0', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_fa_case_100Z0():
    assert FullAdder(['1', '0', '0', 'Z', '0']).solve() == ({"bits": ('1', '0', '0', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_fa_case_100Z1():
    assert FullAdder(['1', '0', '0', 'Z', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_fa_case_1000Z():
    assert FullAdder(['1', '0', '0', '0', 'Z']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_fa_case_10000():
    assert FullAdder(['1', '0', '0', '0', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_fa_case_10001():
    assert FullAdder(['1', '0', '0', '0', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_fa_case_1001Z():
    assert FullAdder(['1', '0', '0', '1', 'Z']).solve() == ({"bits": ('1', '0', '0', '1', '0'), "error": '0', "change": '1'}) # NO MOD
def test_fa_case_10010():
    assert FullAdder(['1', '0', '0', '1', '0']).solve() == ({"bits": ('1', '0', '0', '1', '0'), "error": '0', "change": '0'}) # NO MOD
def test_fa_case_10011():
    assert FullAdder(['1', '0', '0', '1', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_fa_case_101ZZ():
    assert FullAdder(['1', '0', '1', 'Z', 'Z']).solve() == ({"bits": ('1', '0', '1', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_fa_case_101Z0():
    assert FullAdder(['1', '0', '1', 'Z', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_fa_case_101Z1():
    assert FullAdder(['1', '0', '1', 'Z', '1']).solve() == ({"bits": ('1', '0', '1', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_fa_case_1010Z():
    assert FullAdder(['1', '0', '1', '0', 'Z']).solve() == ({"bits": ('1', '0', '1', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_fa_case_10100():
    assert FullAdder(['1', '0', '1', '0', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_fa_case_10101():
    assert FullAdder(['1', '0', '1', '0', '1']).solve() == ({"bits": ('1', '0', '1', '0', '1'), "error": '0', "change": '0'}) # NO MOD
def test_fa_case_1011Z():
    assert FullAdder(['1', '0', '1', '1', 'Z']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_fa_case_10110():
    assert FullAdder(['1', '0', '1', '1', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_fa_case_10111():
    assert FullAdder(['1', '0', '1', '1', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_fa_case_11ZZZ():
    assert FullAdder(['1', '1', 'Z', 'Z', 'Z']).solve() == ({"bits": ('1', '1', 'Z', 'Z', '1'), "error": '0', "change": '1'}) # NO MOD
def test_fa_case_11ZZ0():
    assert FullAdder(['1', '1', 'Z', 'Z', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_fa_case_11ZZ1():
    assert FullAdder(['1', '1', 'Z', 'Z', '1']).solve() == ({"bits": ('1', '1', 'Z', 'Z', '1'), "error": '0', "change": '0'}) # NO MOD
def test_fa_case_11Z0Z():
    assert FullAdder(['1', '1', 'Z', '0', 'Z']).solve() == ({"bits": ('1', '1', '0', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_fa_case_11Z00():
    assert FullAdder(['1', '1', 'Z', '0', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_fa_case_11Z01():
    assert FullAdder(['1', '1', 'Z', '0', '1']).solve() == ({"bits": ('1', '1', '0', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_fa_case_11Z1Z():
    assert FullAdder(['1', '1', 'Z', '1', 'Z']).solve() == ({"bits": ('1', '1', '1', '1', '1'), "error": '0', "change": '1'}) # NO MOD
def test_fa_case_11Z10():
    assert FullAdder(['1', '1', 'Z', '1', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_fa_case_11Z11():
    assert FullAdder(['1', '1', 'Z', '1', '1']).solve() == ({"bits": ('1', '1', '1', '1', '1'), "error": '0', "change": '1'}) # NO MOD
def test_fa_case_110ZZ():
    assert FullAdder(['1', '1', '0', 'Z', 'Z']).solve() == ({"bits": ('1', '1', '0', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_fa_case_110Z0():
    assert FullAdder(['1', '1', '0', 'Z', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_fa_case_110Z1():
    assert FullAdder(['1', '1', '0', 'Z', '1']).solve() == ({"bits": ('1', '1', '0', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_fa_case_1100Z():
    assert FullAdder(['1', '1', '0', '0', 'Z']).solve() == ({"bits": ('1', '1', '0', '0', '1'), "error": '0', "change": '1'}) # NO MOD
def test_fa_case_11000():
    assert FullAdder(['1', '1', '0', '0', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_fa_case_11001():
    assert FullAdder(['1', '1', '0', '0', '1']).solve() == ({"bits": ('1', '1', '0', '0', '1'), "error": '0', "change": '0'}) # NO MOD
def test_fa_case_1101Z():
    assert FullAdder(['1', '1', '0', '1', 'Z']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_fa_case_11010():
    assert FullAdder(['1', '1', '0', '1', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_fa_case_11011():
    assert FullAdder(['1', '1', '0', '1', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_fa_case_111ZZ():
    assert FullAdder(['1', '1', '1', 'Z', 'Z']).solve() == ({"bits": ('1', '1', '1', '1', '1'), "error": '0', "change": '1'}) # NO MOD
def test_fa_case_111Z0():
    assert FullAdder(['1', '1', '1', 'Z', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_fa_case_111Z1():
    assert FullAdder(['1', '1', '1', 'Z', '1']).solve() == ({"bits": ('1', '1', '1', '1', '1'), "error": '0', "change": '1'}) # NO MOD
def test_fa_case_1110Z():
    assert FullAdder(['1', '1', '1', '0', 'Z']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_fa_case_11100():
    assert FullAdder(['1', '1', '1', '0', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_fa_case_11101():
    assert FullAdder(['1', '1', '1', '0', '1']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_fa_case_1111Z():
    assert FullAdder(['1', '1', '1', '1', 'Z']).solve() == ({"bits": ('1', '1', '1', '1', '1'), "error": '0', "change": '1'}) # NO MOD
def test_fa_case_11110():
    assert FullAdder(['1', '1', '1', '1', '0']).solve() == ({"bits": ('Z', 'Z', 'Z', 'Z', 'Z'), "error": '1', "change": '1'}) # NO MOD
def test_fa_case_11111():
    assert FullAdder(['1', '1', '1', '1', '1']).solve() == ({"bits": ('1', '1', '1', '1', '1'), "error": '0', "change": '0'}) # NO MOD
