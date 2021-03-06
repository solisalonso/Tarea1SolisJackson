import pytest
from codigo import *


@pytest.mark.parametrize('ch', [('a'), ('b'), ('c'), ('d'), ('e'), ('f'), ('g'), ('h'), ('i'), ('j'), ('k'), ('l'), ('m'), ('n'), ('o'), ('p'), ('q'), ('r'), ('s'), ('t'), ('u'), ('v'), ('w'), ('x'), ('y'), ('z')])
def test1(ch):
    assert check_char(ch) == '0'


@pytest.mark.parametrize('ch', [('a')])
def test2(ch):
    assert caps_switch(ch) == 'A'


@pytest.mark.parametrize('ch', [('hh')])
def test3(ch):
    assert check_char(ch) == '0'


@pytest.mark.parametrize('ch', [('55')])
def test4(ch):
    assert check_char(ch) == '0'


@pytest.mark.parametrize('ch', [('/')])
def test5(ch):
    assert check_char(ch) == '0'


"""
para ejecutar pytest se debe escribir:
Para ejecutar los 5 tests juntos: pytest pruebas.py
Para ejecutar cada test por separado: pytest pruebas.py -k (numero del test) -v
Por ejemplo para el primero: pytest pruebas.py -k 1 -v
"""
