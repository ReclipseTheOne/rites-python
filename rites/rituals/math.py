from typing import Union
import math


class Math:
    """Useful math operations that I couldn't find in the stdlib operations
    """
    @staticmethod
    def split_into_primes(number: int) -> list:
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

    @staticmethod
    def equalize_matrix(matrix: list) -> list:
        __temp = len(matrix[0])
        for row in matrix:
            if len(row) > __temp:
                __temp = len(row)

        for row in matrix:
            if len(row) < __temp:
                row += [0] * (__temp - len(row))
        return matrix

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
            add_of(*args: CN) -> CN: Adds multiple complex numbers
            subtract_of(*args: CN) -> CN: Subtracts multiple complex numbers
            multiply_of(*args: CN) -> CN: Multiplies multiple complex numbers
            diagonal_of(matrix: list) -> list: Returns the diagonal of a matrix
            secondary_diagonal_of(matrix: list) -> list: Returns the secondary diagonal of a matrix

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

        def __pow__(self, power):
            if power == 0:
                return Math.ComplexNumber(1, 0)
            result = Math.ComplexNumber(self.real, self.imaginary)
            for i in range(power - 1):
                result *= self
            return result

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
        def add_of(*args: 'Math.ComplexNumber') -> 'Math.ComplexNumber':
            result = Math.ComplexNumber()
            for arg in args:
                result += arg
            return result

        @staticmethod
        def subtract_of(*args: 'Math.ComplexNumber') -> 'Math.ComplexNumber':
            result = Math.ComplexNumber()
            for arg in args:
                result -= arg
            return result

        @staticmethod
        def multiply_of(*args: 'Math.ComplexNumber') -> 'Math.ComplexNumber':
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
            composites (dict): Dictionary of the composite primes of the number

        Methods:
            __init__(self, number: int = 0): Constructor for the class
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

    class Matrix:
        """Matrix representations and operations
        Attributes:
            matrix list: The matrix itself

        Methods:
            __init__(self, matrix: list): Constructor for the class
        """

        def __init__(self, matrix: list = [[]]):
            # <- Just to make sure the matrix is a matrix lol
            self.matrix = Math.equalize_matrix(matrix)
            self.width = len(self.matrix[0])
            self.height = len(self.matrix)

        def __add__(self, other: 'Math.Matrix') -> 'Math.Matrix':
            if self.width != other.width or self.height != other.height:
                raise ValueError("Matrixes have different dimensions")

            result = []
            for i in range(self.height):
                result.append([])
                for j in range(self.width):
                    result[i].append(self.matrix[i][j] + other.matrix[i][j])
            return Math.Matrix(result)

        def __sub__(self, other: 'Math.Matrix') -> 'Math.Matrix':
            if self.width != other.width or self.height != other.height:
                raise ValueError("Matrixes have different dimensions")

            result = []
            for i in range(self.height):
                result.append([])
                for j in range(self.width):
                    result[i].append(self.matrix[i][j] - other.matrix[i][j])
            return Math.Matrix(result)

        def __mul__(self, other: Union['Math.Matrix', int]) -> 'Math.Matrix':
            if isinstance(other, int):
                result = []
                for i in range(self.height):
                    result.append([])
                    for j in range(self.width):
                        result[i].append(self.matrix[i][j] * other)
                return Math.Matrix(result)

            if self.width != other.height:
                raise ValueError("Matrixes have incompatible dimensions")

            result = []
            for i in range(self.height):
                result.append([])
                for j in range(other.width):
                    result[i].append(0)
                    for k in range(self.width):
                        result[i][j] += self.matrix[i][k] * other.matrix[k][j]
            return Math.Matrix(result)

        def __rmul__(self, other: int) -> 'Math.Matrix':
            # int * matrix fix
            return self.__mul__(other)

        def __str__(self):
            # Spaghetti code goes hard <3

            __temp = []
            for i in range(0, self.height):
                __temp.append([])

            # Iterate through the columns
            for i in range(0, self.width):

                # Get longest number in characters used (- included etc.) per column
                __longest = 0
                for j, row in enumerate(self.matrix):
                    row = str(row)
                    numbers = row.split(",")

                    # Sanitizing goes hard
                    for k in range(len(numbers)):
                        if "[" in numbers[k]:
                            numbers[k] = numbers[k].replace("[", "")
                        if "]" in numbers[k]:
                            numbers[k] = numbers[k].replace("]", "")
                        if " " in numbers[k]:
                            numbers[k] = numbers[k].replace(" ", "")

                    if len(numbers[i]) > __longest:
                        __longest = len(numbers[i])

                # Same loop but now stretch the numbers based on the longest number
                for j, row in enumerate(self.matrix):
                    row = str(row)
                    numbers = row.split(",")

                    # Sanitizing goes hard #2
                    for k in range(len(numbers)):
                        if "[" in numbers[k]:
                            numbers[k] = numbers[k].replace("[", "")
                        if "]" in numbers[k]:
                            numbers[k] = numbers[k].replace("]", "")
                        if " " in numbers[k]:
                            numbers[k] = numbers[k].replace(" ", "")

                    # The special case of Nx1 matrices
                    if self.width == 1:
                        __temp[j].append(
                            "[" + " " * (__longest - len(numbers[i])) + numbers[i] + "]")
                        continue

                    '''
                    3 cases:
                        - First number in the row gets a [ and a comma
                        - Last number in the row just gets a ]
                        - Everything in between gets a comma
                    '''
                    if i == 0:
                        __temp[j].append(
                            "[" + " " * (__longest - len(numbers[i])) + numbers[i] + ",")
                    elif i == self.width - 1:
                        __temp[j].append(
                            " " * (__longest - len(numbers[i])) + numbers[i] + "]")
                    else:
                        __temp[j].append(
                            " " * (__longest - len(numbers[i])) + numbers[i] + ",")

            # Print the matrix with numbers stretched to the longest number
            # Please use a monospace font for this :(
            result = ""
            for row in __temp:
                result += " ".join(row) + "\n"

            return result

        def __pow__(self, power: int) -> 'Math.Matrix':
            if self.width != self.height:
                raise ValueError("Matrix is not a square matrix")

            result = Math.Matrix.unit_matrix(self.width)
            for i in range(power):
                result *= self
            return result

        def __len__(self) -> int:
            return self.width * self.height

        def __getitem__(self, key: int) -> list:
            return self.matrix[key]

        def __setitem__(self, key: int, value: list) -> None:
            self.matrix[key] = value

        def __iter__(self):
            return iter(self.matrix)

        def __eq__(self, other: 'Math.Matrix') -> bool:
            return self.matrix == other.matrix

        def __ne__(self, other: 'Math.Matrix') -> bool:
            return self.matrix != other.matrix

        def __hash__(self):
            return hash(self.matrix)

        def transpose(self) -> 'Math.Matrix':
            result = []
            for i in range(self.width):
                result.append([])
                for j in range(self.height):
                    result[i].append(self.matrix[j][i])
            return Math.Matrix(result)

        def diagonal(self) -> list:
            if self.width != self.height:
                raise ValueError("Matrix is not a square matrix")

            result = []
            for i in range(self.width):
                result.append(self.matrix[i][i])
            return result

        def secondary_diagonal(self) -> list:
            if self.width != self.height:
                raise ValueError("Matrix is not a square matrix")

            result = []
            for i in range(self.width):
                result.append(self.matrix[i][self.width - i - 1])
            return result

        def inferior_triangular_matrix(self, offset=0):
            if self.width != self.height:
                raise ValueError("Matrix is not a square matrix")

            result = []

            # Fill the matrix with 0s
            for i in range(self.width):
                line = []
                for j in range(self.height):
                    line.append(0)
                result.append(line)

            for i in range(offset, self.height):
                for j in range(i + 1 - offset):
                    result[i][j] = self.matrix[i][j]
            return Math.Matrix(result)

        def superior_triangular_matrix(self, offset=0):
            if self.width != self.height:
                raise ValueError("Matrix is not a square matrix")

            result = []

            # Fill the matrix with 0s
            for i in range(self.width):
                line = []
                for j in range(self.height):
                    line.append(0)
                result.append(line)

            for i in range(self.height):
                for j in range(i + offset, self.width):
                    result[i][j] = self.matrix[i][j]
            return Math.Matrix(result)

        def elements(self) -> list:
            elements = []
            for row in self.matrix:
                for element in row:
                    elements.append(element)
            return elements

        @staticmethod
        def elements_of(matrix: 'Math.Matrix') -> list:
            elements = []
            for row in matrix.matrix:
                for element in row:
                    elements.append(element)
            return elements

        @staticmethod
        def unit_matrix(size: int) -> 'Math.Matrix':
            matrix = []
            for i in range(size):
                matrix.append([0] * size)
                matrix[i][i] = 1
            return Math.Matrix(matrix)

        @staticmethod
        def diagonal_of(matrix: Union[list, 'Math.Matrix']) -> list:
            if not isinstance(matrix, Math.Matrix):
                matrix = Math.Matrix(matrix)

            if matrix.width != matrix.height:
                raise ValueError("Matrix is not a square matrix")

            result = []
            for i in range(matrix.width):
                result.append(matrix.matrix[i][i])
            return result

        @staticmethod
        def secondary_diagonal_of(matrix: Union[list, 'Math.Matrix']) -> list:
            if not isinstance(matrix, Math.Matrix):
                matrix = Math.Matrix(matrix)

            if matrix.width != matrix.height:
                raise ValueError("Matrix is not a square matrix")

            result = []
            for i in range(matrix.width):
                result.append(matrix.matrix[i][matrix.width - i - 1])
            return result

        @staticmethod
        def transpose_of(matrix: Union[list, 'Math.Matrix']) -> 'Math.Matrix':
            if not isinstance(matrix, Math.Matrix):
                matrix = Math.Matrix(matrix)

            result = []
            for i in range(matrix.width):
                result.append([])
                for j in range(matrix.height):
                    result[i].append(matrix.matrix[j][i])
            return Math.Matrix(result)

        @staticmethod
        def inferior_triangular_matrix_of(matrix: Union[list, 'Math.Matrix'], offset=0) -> 'Math.Matrix':
            if not isinstance(matrix, Math.Matrix):
                matrix = Math.Matrix(matrix)

            if matrix.width != matrix.height:
                raise ValueError("Matrix is not a square matrix")

            result = []

            # Fill the matrix with 0s
            for i in range(matrix.width):
                line = []
                for j in range(matrix.height):
                    line.append(0)
                result.append(line)

            for i in range(offset, matrix.height):
                for j in range(i + 1 - offset):
                    result[i][j] = matrix.matrix[i][j]
            return Math.Matrix(result)

        @staticmethod
        def superior_triangular_matrix_of(matrix: Union[list, 'Math.Matrix'], offset=0) -> 'Math.Matrix':
            if not isinstance(matrix, Math.Matrix):
                matrix = Math.Matrix(matrix)

            if matrix.width != matrix.height:
                raise ValueError("Matrix is not a square matrix")

            result = []

            # Fill the matrix with 0s
            for i in range(matrix.width):
                line = []
                for j in range(matrix.height):
                    line.append(0)
                result.append(line)

            for i in range(matrix.height):
                for j in range(i + offset, matrix.width):
                    result[i][j] = matrix.matrix[i][j]
            return Math.Matrix(result)

        @staticmethod
        def from_terminal(height, width) -> 'Math.Matrix':
            matrix = []
            for i in range(height):
                matrix.append([])
                for j in range(width):
                    matrix[i].append(
                        int(input(f"Enter the value for [{i}][{j}]: ")))
            return Math.Matrix(matrix)
