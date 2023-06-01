import unittest

from eval_postfix import eval_postfix
from operators import Operators
from adt import Stack
from infix_to_postfix import infix_to_postfix


class TestEvalPostix(unittest.TestCase):
    def test_single_operator(self):
        # 3 + 1 = 4
        s = Stack.from_list([3, 1, Operators.ADD])
        self.assertEqual(eval_postfix(s), 4)

        # 5 - 19 = -14
        s = Stack.from_list([5, 19, Operators.SUB])
        self.assertEqual(eval_postfix(s), -14)

        # 2 * -4 = -8
        s = Stack.from_list([2, -4, Operators.MUL])
        self.assertEqual(eval_postfix(s), -8)

        # 9 / 2 = 4.5
        s = Stack.from_list([9, 2, Operators.DIV])
        self.assertEqual(eval_postfix(s), 4.5)

        # 2 ^ 3 = 8
        s = Stack.from_list([2, 3, Operators.EXP])
        self.assertEqual(eval_postfix(s), 8)

    def test_complex_postfix(self):
        #  2 + (3 * 1) – 9 = -4
        s = Stack.from_list([2, 3, 1, Operators.MUL, Operators.ADD, 9, Operators.SUB])
        self.assertEqual(eval_postfix(s), -4)

        # 5 * ((100 + 200) / 2) + 7 = 757
        s = Stack.from_list(
            [
                100,
                200,
                Operators.ADD,
                2,
                Operators.DIV,
                5,
                Operators.MUL,
                7,
                Operators.ADD,
            ]
        )
        self.assertEqual(eval_postfix(s), 757)


class TestInfixToPostfix(unittest.TestCase):
    def test_infix_to_postfix_order(self):
        self.assertEqual(
            infix_to_postfix("3*2+6/4").get_data(),
            [3.0, 2.0, Operators.MUL, 6.0, 4.0, Operators.DIV, Operators.ADD],
        )
        self.assertEqual(
            infix_to_postfix("1+2*3").get_data(),
            [1.0, 2.0, 3.0, Operators.MUL, Operators.ADD],
        )
        self.assertEqual(
            infix_to_postfix("1+2+3+4").get_data(),
            [1.0, 2.0, Operators.ADD, 3.0, Operators.ADD, 4.0, Operators.ADD],
        )
        self.assertEqual(
            infix_to_postfix("1.5*2.5+3.5/4.5").get_data(),
            [1.5, 2.5, Operators.MUL, 3.5, 4.5, Operators.DIV, Operators.ADD],
        )

    def test_infix_to_postfix_parentheses(self):
        self.assertEqual(
            infix_to_postfix("(1+2)*3").get_data(),
            [1.0, 2.0, Operators.ADD, 3, Operators.MUL],
        )
        self.assertEqual(
            infix_to_postfix("6/(1+2)*3").get_data(),
            [6.0, 1.0, 2.0, Operators.ADD, Operators.DIV, 3.0, Operators.MUL],
        )

    def test_infix_to_postfix_negative(self):
        self.assertEqual(
            infix_to_postfix("8*-2").get_data(), [8.0, -2.0, Operators.MUL]
        )
        self.assertEqual(
            infix_to_postfix("8*(-2)").get_data(), [8.0, -2.0, Operators.MUL]
        )
        self.assertEqual(
            infix_to_postfix("-2--3").get_data(), [-2.0, -3.0, Operators.SUB]
        )
        self.assertEqual(
            infix_to_postfix("-2*(9-6)").get_data(),
            [-2.0, 9.0, 6.0, Operators.SUB, Operators.MUL],
        )

    def test_infix_to_infix_decimals(self):
        self.assertEqual(
            infix_to_postfix("-2.5*(9-6.2)").get_data(),
            [-2.5, 9.0, 6.2, Operators.SUB, Operators.MUL],
        )


if __name__ == "__main__":
    unittest.main()
