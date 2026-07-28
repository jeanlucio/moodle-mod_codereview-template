"""Testes das operações da calculadora."""

import pytest

from exercicio.calculadora import multiplicar, somar, subtrair


def test_somar():
    assert somar(2, 3) == 5
    assert somar(-1, 1) == 0


def test_subtrair():
    assert subtrair(5, 3) == 2
    assert subtrair(0, 4) == -4


def test_multiplicar():
    assert multiplicar(3, 4) == 12
    assert multiplicar(0, 9) == 0
