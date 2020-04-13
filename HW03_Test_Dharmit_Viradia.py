"""
    Create Test Cases for all the functions and exceptions of Fraction Class 

"""

import unittest
from HW03_Dharmit_Viradia import Fraction

class TestFraction(unittest.TestCase):
    """ test class Fraction """
    def test_init(self) -> None:
        """ verify that the numerator and denominator are set properly """
        f: Fraction = Fraction(3, 4)
        self.assertEqual(f.num, 3)
        self.assertEqual(f.denom, 4)

    def test_init_exception(self) -> None:
        """ verify that ZeroDivisionError is raised when appropriate """
        with self.assertRaises(ZeroDivisionError, msg="Denominator is Zero"):
            f10: Fraction = Fraction(1, 0)
    
    def test_str(self) -> None:
        """verify str function"""
        f: Fraction = Fraction(3, 4)
        self.assertEqual(str(f), "3/4")
        self.assertEqual(str(Fraction(-1,2)), "-1/2")
        self.assertEqual(str(Fraction(1,-2)), "-1/2")
        self.assertEqual(str(Fraction(-1,-2)), "1/2")

    def test_simplify(self) -> None:
        """verify simplified Fraction"""
        f12: Fraction = Fraction(1, 2)
        f24: Fraction = Fraction(2, 4)
        fn12: Fraction = Fraction(-1, 2)
        fn24: Fraction = Fraction(2, -4)
        self.assertTrue((f12.simplify()) == f12)
        self.assertTrue((f24.simplify()) == f12)
        self.assertTrue((fn24.simplify()) == fn12)
        self.assertTrue((Fraction(9, 27).simplify()) == Fraction(1, 3))


    def test_add(self) -> None:
        """ verify Fraction addition """
        f12: Fraction = Fraction(1, 2)
        f34: Fraction = Fraction(3, 4)
        self.assertEqual(f12 + f34, Fraction(10, 8))
        self.assertEqual(f12, Fraction(1, 2))  # f12 should not have changed

    def test_multiple_operands(self) -> None:
        """ verify Fraction addition with more than two operands"""
        f12: Fraction = Fraction(1, 2)
        f34: Fraction = Fraction(3, 4)
        f44: Fraction = Fraction(4, 4)
        self.assertEqual(f12 + f34 + f44, Fraction(72, 32))
        self.assertEqual(f12 + f34 * f44, Fraction(40, 32))


    def test_sub(self) -> None:
        """ verify Fraction subtraction"""
        f12: Fraction = Fraction(1, 2)
        f34: Fraction = Fraction(3, 4)
        self.assertEqual(f12 - f34, Fraction(-2, 8))
        self.assertEqual(f34, Fraction(3, 4))

    def test_mul(self) -> None:
        """ verify Fraction multiplication"""
        f12: Fraction = Fraction(1, 2)
        f34: Fraction = Fraction(3, 4)
        self.assertEqual(f12 * f34, Fraction(3, 8))

    def test_div(self) -> None:
        """ verify Fraction division"""
        f12: Fraction = Fraction(1, 2)
        f34: Fraction = Fraction(3, 4)
        self.assertEqual(f12 / f34, Fraction(4, 6))

    def test_equal(self) -> None:
        """ verify Fraction equal"""
        f12: Fraction = Fraction(1, 2)
        f24: Fraction = Fraction(2, 4)
        f34: Fraction = Fraction(3, 4)
        self.assertTrue(f12 == f24)
        self.assertTrue(f12 == f12)
        self.assertFalse(f12 == f34)

    def test_notequal(self) -> None:
        """ verify Fraction notequal"""
        f12: Fraction = Fraction(1, 2)
        f24: Fraction = Fraction(2, 4)
        f34: Fraction = Fraction(3, 4)
        self.assertFalse(f12 != f24)
        self.assertFalse(f12 != f12)
        self.assertTrue(f12 != f34)

    def test_lessthan(self) -> None:
        """ verify Fraction less than """
        f12: Fraction = Fraction(1, 2)
        f34: Fraction = Fraction(3, 4)
        fn12: Fraction = Fraction(-1, 2)
        fn34: Fraction = Fraction(3, -4)
        self.assertLess(f12, f34)
        self.assertEqual(f12 < f12, False)
        self.assertEqual(f34 < f12, False)
        self.assertEqual(fn12 < f12, True)
        self.assertEqual(f12 < fn34, False)


    
    def test_lessthanequal(self) -> None:
        """ verify Fraction less than equal to """
        f12: Fraction = Fraction(1, 2)
        f34: Fraction = Fraction(3, 4)
        fn12: Fraction = Fraction(-1, 2)
        fn34: Fraction = Fraction(3, -4)
        self.assertLessEqual(f12, f34)
        self.assertEqual(f12 <= f12, True)
        self.assertEqual(f34 <= f12, False)
        self.assertEqual(fn12 <= f12, True)
        self.assertEqual(f12 <= fn34, False)

    def test_greaterthan(self) -> None:
        """ verify Fraction greater than """
        f12: Fraction = Fraction(1, 2)
        f34: Fraction = Fraction(3, 4)
        fn12: Fraction = Fraction(-1, 2)
        fn34: Fraction = Fraction(3, -4)
        self.assertGreater(f34, f12)
        self.assertEqual(f12 > f12, False)
        self.assertEqual(f12 > f34, False)
        self.assertEqual(fn12 > f12, False)
        self.assertEqual(f12 > fn34, True)

    def test_greaterthanequal(self) -> None:
        """ verify Fraction greater than equal to """
        f12: Fraction = Fraction(1, 2)
        f34: Fraction = Fraction(3, 4)
        fn12: Fraction = Fraction(-1, 2)
        fn34: Fraction = Fraction(3, -4)
        self.assertGreaterEqual(f34, f12)
        self.assertEqual(f12 >= f12, True)
        self.assertEqual(f12 >= f34, False)
        self.assertEqual(fn12 >= f12, False)
        self.assertEqual(f12 >= fn34, True)


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)