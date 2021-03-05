import pytest
from codigo import *




@pytest.mark.parametrize('ch',[('a'),('b'),('c'),('d'),('e'),('f'),('g'),('h'),('i'),('j')])
def test1(ch):
    assert check_char(ch)=='0'

@pytest.mark.parametrize('ch',[('a')])
def test2(ch):
    assert caps_switch(ch)=='A'

@pytest.mark.parametrize('ch',[('55')])
def test3(ch):
    assert check_char(ch)=='0'

@pytest.mark.parametrize('ch',[('hh')])
def test4(ch):
    assert check_char(ch)=='0'