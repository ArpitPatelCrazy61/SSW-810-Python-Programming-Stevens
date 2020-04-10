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

        if self.denom < 0:
            self.num = -1*self.num
            self.denom = -1*self.denom

    def simplify(self) -> "Fraction":
        """ return a Simplified Fraction"""
        return Fraction(int(self.num/gcd(self.num,self.denom)), int(self.denom/gcd(self.num,self.denom)))
        
    def __str__(self) -> str:
        """ return a String to display fractions """
        # return str(self.num)+"/"+str(self.denom) python 2
        return f"{self.num}/{self.denom}"
       
    def __add__(self, other: "Fraction") -> "Fraction":
        """ Add two fractions using simplest approach.
            Calculate new numerator and denominator and return new Fraction
        """
        onum: float = self.num*other.denom+other.num*self.denom
        odenom: float = self.denom*other.denom

        return Fraction(onum,odenom).simplify()
        
    def __sub__(self, other: "Fraction") -> "Fraction":
        """ subtract two fractions using simplest approach 
            Calculate new numerator and denominator and return new Fraction
        """
        onum: float = self.num*other.denom-other.num*self.denom
        odenom: float = self.denom*other.denom

        return Fraction(onum,odenom).simplify()
        
    def __mul__(self, other: "Fraction") -> "Fraction":
        """ Multiply two fractions using simplest approach 
            Calculate new numerator and denominator and return new Fraction
        """
        onum: float = self.num*other.num
        odenom: float = self.denom*other.denom

        return Fraction(onum,odenom).simplify()
        
    def __truediv__(self, other: "Fraction") -> "Fraction":
        """ Divide two fractions using simplest approach.
            Calculate new numerator and denominator and return new Fraction
        """
        onum: float = self.num*other.denom
        odenom: float = self.denom*other.num

        return Fraction(onum,odenom).simplify()

    def __eq__(self, other: "Fraction")-> bool:
        """ return True/False if the two fractions are equivalent """

        onum: float = self.num*other.denom
        odenom: float = self.denom*other.num

        if onum == odenom:
            return True
        else:
            return False
        
    def __ne__(self, other: "Fraction")-> bool:
        """ return True/False if the two fractions are not equivalent """

        onum: float = self.num*other.denom
        odenom: float = self.denom*other.num

        if onum != odenom:
            return True
        else:
            return False

    def __lt__(self, other: "Fraction")-> bool:
        """ return True/False if the two fractions are less than"""

        onum: float = self.num*other.denom
        odenom: float = self.denom*other.num

        if onum < odenom:
            return True
        else:
            return False

    def __le__(self, other: "Fraction")-> bool:
        """ return True/False if the two fractions are less than equal """

        onum: float = self.num*other.denom
        odenom: float = self.denom*other.num

        if onum <= odenom:
            return True
        else:
            return False

    def __gt__(self, other: "Fraction")-> bool:
        """ return True/False if the two fractions are greater than """

        onum: float = self.num*other.denom
        odenom: float = self.denom*other.num

        if onum > odenom:
            return True
        else:
            return False

    def __ge__(self, other: "Fraction")-> bool:
        """ return True/False if the two fractions are greater tan equal """

        onum: float = self.num*other.denom
        odenom: float = self.denom*other.num

        if onum >= odenom:
            return True
        else:
            return False

def gcd(num, denom) -> int:
     """Calculates the GCD"""
     x = num % denom
     if x == 0 :
        return denom
     else : 
        return gcd(denom, x)

    
def get_number(prompt: str) -> float:
    """ read and return a number from the user.
        Loop until the user provides a valid number.
    """
    while True:
        inp: str = input(prompt)
        try:
            return int(inp)
        except ValueError:
            print(f"Error: '{inp}' is not a number. Please try again...")

def get_fraction(flag: bool) -> "Fraction":
    """ Ask the user for a numerator and denominator and return a valid Fraction """
    while True:
        if flag == True:
            num = get_number("Enter First Fraction Numerator: ")
            denom = get_number("Enter First Fraction Denominator: ")
            f = Fraction(num,denom).simplify()
            return f

        elif flag == False:
            num = get_number("Enter Second Fraction Numerator: ")
            denom = get_number("Enter Second Fraction Denominator: ")
            f = Fraction(num,denom).simplify()
            return f

    
def compute(f1: Fraction, operator: str, f2: Fraction) -> None:
    """ Given two fractions and an operator, return the result
        of applying the operator to the two fractions
    """
    result: Fraction  # just define the type of result, don't set a value
    okay: bool = True

    if operator == '+':
        result = f1 + f2
    elif operator == "-":
        result = f1 - f2
    elif operator == "*":
        result = f1 * f2
    elif operator == "/":
        result = f1 / f2
    elif operator == "==":
        result = f1 == f2
    elif operator == "!=":
        result = f1 != f2
    elif operator == "<":
        result = f1 < f2
    elif operator == "<=":
        result = f1 <= f2
    elif operator == ">":
        result = f1 > f2
    elif operator == ">=":
        result = f1 >= f2
    else:
        print(f"Error: '{operator}' is an unrecognized operator")
        okay = False

    if okay:
        print(f"{f1} {operator} {f2} = {result}")

def main() -> None:
    """ Fraction calculations """
    print('\nWelcome to the fraction calculator!')
    f1: Fraction = get_fraction(True)
    operator: str = input("Operation (+, -, *, /,==, !=, <, <=, >, >=): ")
    f2: Fraction = get_fraction(False)
    
    try:
        compute(f1, operator, f2)
    except ZeroDivisionError as e:
        print(e)
        
if __name__ == '__main__':
    main()