from calculator.calculator import Calculator

class TestCalculator:
    def test_add(self):
        # arrange
        a = 4321
        b = 1234
        cal = Calculator()

        # act
        result = cal.add(a, b)

        # assert
        expected = 5555
        assert result == expected
    
    def test_subtract(self):
        # arrange
        a = 900
        b = 400
        cal = Calculator()

        # act
        result = cal.subtract(a, b)

        # assert
        expected = 500
        assert result == expected

    def test_multiply(self):
        # arrange
        a = 8
        b = 4
        cal = Calculator()

        # act
        result = cal.multiply(a, b)

        # assert
        expected = 32
        assert result == expected

    def test_divide(self):
        # arrange
        a = 100
        b = 2
        cal = Calculator()

        # act
        result = cal.divide(a, b)

        # assert
        expected = 50
        assert result == expected
