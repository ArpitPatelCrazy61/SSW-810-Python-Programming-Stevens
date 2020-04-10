"""
    Implement a class for fractions that supports addition, subtraction, multiplication, and division.
"""

class Fraction:
    """ Support addition, subtraction, multiplication, and division of fractions
        with a simple algorithm
    """
    def __init__(self, num: float, denom: float) -> None:
        """ store num and denom
            Raise ZeroDivisionError on 0 denominator 
        """
        self.num: float = num
        self.denom: float = denom

        if self.denom == 0:
            raise ZeroDivisionError("Denominator is Zero")
        
    def __str__(self) -> str:
        """ return a String to display fractions """
        # return str(self.num)+"/"+str(self.denom) python 2
        return f"{self.num}/{self.denom}"
       
    def plus(self, other: "Fraction") -> "Fraction":
        """ Add two fractions using simplest approach.
            Calculate new numerator and denominator and return new Fraction
        """
        onum: float = self.num*other.denom+other.num*self.denom
        odenom: float = self.denom*other.denom

        return Fraction(onum,odenom)
        
    def minus(self, other: "Fraction") -> "Fraction":
        """ subtract two fractions using simplest approach 
            Calculate new numerator and denominator and return new Fraction
        """
        onum: float = self.num*other.denom-other.num*self.denom
        odenom: float = self.denom*other.denom

        return Fraction(onum,odenom)
        
    def times(self, other: "Fraction") -> "Fraction":
        """ Multiply two fractions using simplest approach 
            Calculate new numerator and denominator and return new Fraction
        """
        onum: float = self.num*other.num
        odenom: float = self.denom*other.denom

        return Fraction(onum,odenom)
        
    def divide(self, other: "Fraction") -> "Fraction":
        """ Add two fractions using simplest approach.
            Calculate new numerator and denominator and return new Fraction
        """
        onum: float = self.num*other.denom
        odenom: float = self.denom*other.num
        
        return Fraction(onum,odenom)

    def equal(self, other: "Fraction")-> bool:
        """ return True/False if the two fractions are equivalent """

        onum: float = self.num*other.denom
        odenom:float = self.denom*other.num

        if onum == odenom:
            return True
        else:
            return False
        

def test_suite() -> None:
    """ We'll see a better testing approach next week but here's a start.
        Note that each statement includes the result of the computation plus 
        the expected answer to help to quickly identify if everything works properly.
    """
    f12: Fraction = Fraction(1, 2)
    f34: Fraction = Fraction(3, 4)
    f44: Fraction = Fraction(4, 4)
    f68: Fraction = Fraction(6, 8)
    f128: Fraction = Fraction(12, 8)
    f32: Fraction = Fraction(3, 2)
    f912: Fraction = Fraction(9, 12)

    print("Test Cases")
    # test cases 
    print(f"{f12} + {f34} = {f12.plus(f34)} [10/8]")
    print(f"{f12} + {f12} = {f12.plus(f12)} [4/4]")
    print(f"{f44} - {f12} = {f44.minus(f12)} [4/8]")
    print(f"{f12} + {f44} = {f12.plus(f44)} [12/8]")
    print(f"{f128} == {f32} is {f128.equal(f32)} [True]")
    print(f"{f912} * {f12} = {f912.times(f12)} [9/24]")
    print(f"{f128} / {f32} = {f128.divide(f32)} [24/24]")
    
    # include a test with three operands
    print(f"{f12} + {f34} + {f44} = {f12.plus(f34).plus(f44)} [72/32]")
    
    
def get_number(prompt: str) -> int:
    """ read and return a number from the user.
        Loop until the user provides a valid number.
    """
    while True:
        inp: str = input(prompt)
        try:
            return int(inp)
        except ValueError:
            print(f"Error: '{inp}' is not a number. Please try again...")

def get_fraction1() -> Fraction:
    """ Ask the user for a numerator and denominator and return a valid Fraction """
    while True:
        num = get_number("Enter First Fraction Numerator: ")
        denom = get_number("Enter First Fraction Denominator: ")
        f = Fraction(num,denom)
        return f

def get_fraction2() -> Fraction:
    """ Ask the user for a numerator and denominator and return a valid Fraction """
    while True:
        num = get_number("Enter Second Fraction Numerator: ")
        denom = get_number("Enter Second Fraction Denominator: ")
        f = Fraction(num,denom)
        return f
    
def compute(f1: Fraction, operator: str, f2: Fraction) -> None:
    """ Given two fractions and an operator, return the result
        of applying the operator to the two fractions
    """
    result: Fraction  # just define the type of result, don't set a value
    okay: bool = True

    if operator == '+':
        result = f1.plus(f2)
    elif operator == "-":
        result = f1.minus(f2)
    elif operator == "*":
        result = f1.times(f2)
    elif operator == "/":
        result = f1.divide(f2)
    elif operator == "==":
        result = f1.equal(f2)
    else:
        print(f"Error: '{operator}' is an unrecognized operator")
        okay = False

    if okay:
        print(f"{f1} {operator} {f2} = {result}")

def main() -> None:
    """ Fraction calculations """
    print('\nWelcome to the fraction calculator!')
    f1: Fraction = get_fraction1()
    operator: str = input("Operation (+, -, *, /,==): ")
    f2: Fraction = get_fraction2()
    
    try:
        compute(f1, operator, f2)
    except ZeroDivisionError as e:
        print(e)
        
if __name__ == '__main__':
    test_suite()
    main()