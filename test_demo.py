
import pytest


@pytest.mark.parametrize("a,b,c",[(1,2,3),(2,2,4),(3,3,6),(8,8,16),(9,9,18)])
def test_add(a,b,c):
    assert c==a+b
def test_mul_practice():
    assert 2 * 3 == 7
def test_conflict():
    return "main version"
