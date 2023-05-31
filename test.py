import unittest

from eval_postfix import eval_postfix
from operators import Operators
from stack import Stack



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
        s = Stack.from_list([100, 200, Operators.ADD, 2, Operators.DIV, 5, Operators.MUL, 7, Operators.ADD])
        self.assertEqual(eval_postfix(s), 757)
        


if __name__ == '__main__':
    unittest.main()