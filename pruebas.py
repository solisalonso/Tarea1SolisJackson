import pytest
from codigo import *




@pytest.mark.parametrize('ch',[('a'),('b')])
def test(ch):
    assert check_char(ch)=='0'

@pytest.mark.parametrize('ch',[('a'),('b')])
def test(ch):
    assert caps_switch(ch)==ch.swapcase()

