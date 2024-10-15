from Ejercicio01 import *

def test_caracter_a():
    assert encriptacion('a', 1) == 'b'

def test_caracter_b():
    assert encriptacion('b', 1) == 'c'

def test_caracter_c():
    assert encriptacion('c', 1) == 'd'

def test_caracter_d():
    assert encriptacion('d', 1) == 'e'

def test_caracter_x():
    assert encriptacion('x', 1) == 'y'

def test_caracter_y():
    assert encriptacion('y', 1) == 'z'

def test_caracter_z():
    assert encriptacion('z', 1) == 'a'

def test_caracter_ab():
    assert encriptacion('ab', 1) == 'bc'

def test_caracter_bc():
    assert encriptacion('bc', 1) == 'cd'

def test_caracter_cd():
    assert encriptacion('cd', 1) == 'de'

def test_caracter_xy():
    assert encriptacion('xy', 1) == 'yz'

def test_caracter_yz():
    assert encriptacion('yz', 1) == 'za'

def test_caracter_za():
    assert encriptacion('za', 1) == 'ab'

def test_caracter_espacio():
    assert encriptacion('ab c', 1) == 'bc d'

def test_caracter_frases():
    assert encriptacion('hola que tal', 1) == 'ipmb rvf ubm'