from Ejercicio05 import * 

def test_prueba0():
    assert contarRecorrido("0") == 1

def test_prueba1():
    assert contarRecorrido("1") == 1

def test_prueba2():
    assert contarRecorrido("987") == 1

def test_prueba3():
    assert contarRecorrido("10") == 1

def test_prueba4():
    assert contarRecorrido("1 2") == 1

def test_prueba5():
    assert contarRecorrido("2 1") == 1

def test_prueba6():
    assert contarRecorrido("0 3") == 3

def test_prueba7():
    assert contarRecorrido("1 0") == 1

def test_prueba8():
    assert contarRecorrido("1 0 1") == 2

def test_prueba9():
    assert contarRecorrido("1 0 2") == 3

def test_prueba10():
    assert contarRecorrido("1 2 3") == 2

def test_prueba11():
    assert contarRecorrido("0 8 6 7") == 11

def test_prueba12():
    assert contarRecorrido("1 4 6 5 3") == 8

def test_prueba13():
    assert contarRecorrido("1 2 3 4 5") == 4

def test_prueba14():
    assert contarRecorrido("0 1 5 2 0 3 9") == 19

def test_prueba15():
    assert contarRecorrido("5 5 4") == 1

def test_pruebaLetras():
    assert contarRecorrido("5 5 df") == "No se pueden convertir caracteres no numericos al tipo int"


