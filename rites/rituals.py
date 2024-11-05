import math


class Math:
    """Usefull math operations that I couldn't find in the stdlib operations
    """
    @staticmethod
    def split_into_primes(number):
        primes = []

        def __iterate(number):
            for i in range(2, number + 1):
                if number % i == 0:
                    return i

        while number != 1:
            i = __iterate(number)
            number = number // i
            primes.append(i)

        return primes

    class ComplexNumber:
        """A class to represent Complex Numbers
        Attributes:
            real (int): The real part of the complex number
            imaginary (int): The imaginary part of the complex number

        Methods:
            __init__(self, real=0, imaginary=0): Constructor for the class
            add(self, other: CN): Adds the complex number with another complex number
            subtract(self, other: CN): Subtracts the complex number with another complex number
            multiply(self, other: CN): Multiplies the complex number with another complex number

        Static Methods:
            add_s(*args: CN) -> CN: Adds multiple complex numbers
            subtract_s(*args: CN) -> CN: Subtracts multiple complex numbers
            multiply_s(*args: CN) -> CN: Multiplies multiple complex numbers
            
            *CN = rites.rituals.Math.ComplexNumber
        """

        def __init__(self, real=0, imaginary=0, complex_letter="i"):
            self.real = real
            self.imaginary = imaginary
            self.complex_letter = complex_letter

        def __add__(self, other):
            if self.complex_letter != other.complex_letter:
                print("[!] Complex Letters are different, defaulted to i")
                return Math.ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)
            return Math.ComplexNumber(self.real + other.real, self.imaginary + other.imaginary, self.complex_letter)

        def __sub__(self, other):
            if self.complex_letter != other.complex_letter:
                print("[!] Complex Letters are different, defaulted to i")
                return Math.ComplexNumber(self.real - other.real, self.imaginary - other.imaginary)
            return Math.ComplexNumber(self.real - other.real, self.imaginary - other.imaginary, self.complex_letter)

        def __mul__(self, other):
            if self.complex_letter != other.complex_letter:
                print("[!] Complex Letters are different, defaulted to i")
                return Math.ComplexNumber(self.real * other.real - self.imaginary * other.imaginary, self.real * other.imaginary + self.imaginary * other.real)
            return Math.ComplexNumber(self.real * other.real - self.imaginary * other.imaginary, self.real * other.imaginary + self.imaginary * other.real, self.complex_letter)

        def __str__(self):
            if self.imaginary == 0:
                return f"{self.real}"
            elif self.imaginary == 1:
                return f"{self.real} + {self.complex_letter}"
            elif self.imaginary == -1:
                return f"{self.real} - {self.complex_letter}"
            elif self.real == 0:
                return f"{self.imaginary}{self.complex_letter}"

            if self.imaginary < 0:
                return f"{self.real} - {abs(self.imaginary)}{self.complex_letter}"
            return f"{self.real} + {self.imaginary}{self.complex_letter}"

        def add(self, other):
            self.real = self.real + other.real
            self.imaginary = self.imaginary + other.imaginary

        def subtract(self, other):
            self.real = self.real - other.real
            self.imaginary = self.imaginary - other.imaginary

        def multiply(self, other):
            self.real = self.real * other.real - self.imaginary * other.imaginary
            self.imaginary = self.real * other.imaginary + self.imaginary * other.real

        @staticmethod
        def add_s(*args: 'Math.ComplexNumber') -> 'Math.ComplexNumber':
            result = Math.ComplexNumber()
            for arg in args:
                result += arg
            return result

        @staticmethod
        def subtract_s(*args: 'Math.ComplexNumber') -> 'Math.ComplexNumber':
            result = Math.ComplexNumber()
            for arg in args:
                result -= arg
            return result

        @staticmethod
        def multiply_s(*args: 'Math.ComplexNumber') -> 'Math.ComplexNumber':
            result = Math.ComplexNumber(1, 0)
            for arg in args:
                result *= arg
            return result
        
        @staticmethod
        def fromString(string: str):
            if "+" in string:
                real, imaginary = string.split("+")
                return Math.ComplexNumber(int(real), int(imaginary.replace("i", "")))
            elif "-" in string:
                real, imaginary = string.split("-")
                return Math.ComplexNumber(int(real), -int(imaginary.replace("i", "")))
            if len(string.split(" ")) == 2:
                real, imaginary = string.split(" ")
                if "i" in imaginary:
                    return Math.ComplexNumber(int(real), int(imaginary.replace("i", "")))
                else:
                    return Math.ComplexNumber(int(real), int(imaginary))
            
            raise ValueError("Invalid Complex Number String")

    class Sqrt:
        """A class to represent Square Roots of Integers
        Attributes:
            number (int): The number to find the square root of
            composites (dict): Array of the composite primes of the number

        Methods:
            __init__(self, number=0): Constructor for the class
        """

        def __init__(self, number: int = 0):
            self.number = int(number)
            self.whole = 1
            self.remainder = 1
            self.composites = {}

            arr = Math.split_into_primes(self.number)

            for i in arr:
                if i in self.composites:
                    self.composites[i] += 1
                else:
                    self.composites[i] = 1
            for nr, power in self.composites.items():
                if power >= 2:
                    if power % 2 == 0:
                        self.whole *= nr ** (power // 2)
                    else:
                        self.whole *= nr ** (power // 2)
                        self.remainder *= nr
                elif power == 1:
                    self.remainder *= nr

        def __str__(self):
            if self.whole == 0 or self.whole == 1:
                return f"√{self.remainder}"
            elif self.remainder == 0 or self.remainder == 1:
                return f"{self.whole}"
            return f"{self.whole}√{self.remainder}"

        def __mul__(self, other):
            return Math.Sqrt(self.number * other.number)

        def __truediv__(self, other):
            if (self.number / other.number != self.number // other.number):
                raise ValueError("The division doesn't return an integer")
            return Math.Sqrt(self.number / other.number)

        @staticmethod
        def aprox(number) -> float:
            return math.sqrt(number)
