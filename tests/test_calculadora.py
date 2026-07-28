"""Testes das operações da calculadora."""

from exercicio.calculadora import multiplicar, somar, subtrair


def test_somar():
    """somar() devolve a soma dos dois argumentos."""
    assert somar(2, 3) == 5
    assert somar(-1, 1) == 0


def test_subtrair():
    """subtrair() devolve a diferença entre os dois argumentos."""
    assert subtrair(5, 3) == 2
    assert subtrair(0, 4) == -4


def test_multiplicar():
    """multiplicar() devolve o produto dos dois argumentos."""
    assert multiplicar(3, 4) == 12
    assert multiplicar(0, 9) == 0
