
import pytest


@pytest.mark.parametrize("a,b,c",[(1,2,3),(2,2,4),(3,3,6),(8,8,16)])
def test_add(a,b,c):
    assert c==a+b

