from exceptions import ArithmeticException


class ArithmeticOps:
    @staticmethod
    def add(num1: int, num2: int):
        return num1 + num2

    @staticmethod
    def subtract(num1: int, num2: int):
        return num1 - num2

    @staticmethod
    def multiply(num1: int, num2: int):
        return num1 * num2

    @staticmethod
    def divide(num1: int, num2: int):
        if num2 == 0:
            raise ArithmeticException("Division by zero not allowed", "divide")
        return num1 / num2

    @staticmethod
    def exponent(num: int, power: int):
        if num == power and num == 0:
            raise ArithmeticException("0 ^ 0 is undefined", "exponent")

        return num**power

    @staticmethod
    def factorial(num: int):
        if num < 0:
            raise ArithmeticException("Negative Factorial not allowed", "factorial")

        if num == 0 or num == 1:
            return 1

        res = 1
        for i in range(2, num):
            res *= i
        return res
