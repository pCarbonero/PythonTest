from Ejercicio03 import *

def test_1():
    assert codigoCorrecto('1') == False

def test_12345678():
    assert codigoCorrecto('12345678') == False

def test_12345678910111213():
    assert codigoCorrecto('12345678910111213') == False

def test_1234567891011121314():
    assert codigoCorrecto('1234567891011121314') == False 

def test_65839522():
    assert codigoCorrecto('65839522') == True 

def test_65839521():
    assert codigoCorrecto('65839521') == False 

def test_8414533043847():
    assert codigoCorrecto('8414533043847') == True 

def test_6583952():
    assert codigoCorrecto('6583952') == False 

def test_5029365779425():
    assert codigoCorrecto('5029365779425') == True 

def test_5129365779425():
    assert codigoCorrecto('5129365779425') == False 



