import pytest
from app.calculator import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator

    # позитивный тест умножение
    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(self, 2, 2) == 4

    # позитивный тест деление
    def test_division_calculate_correctly(self):
        assert self.calc.division(self, 4, 2) == 2

    # позитивный тест вычитание
    def test_subtraction_calculate_correctly(self):
        assert self.calc.subtraction(self, 8, 2) == 6

    # позитивный тест сложение
    def test_adding_calculate_correctly(self):
        assert self.calc.adding(self, 5, 2) == 7



