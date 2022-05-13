class Fraction:

    def __init__(self, num, den):
        self.num = num
        self.den = den

    def __add__(self, other):
        self.num += other
        self.den += other
        print(f"Its method 'add' {self.num}/{self.den}")

    def __sub__(self, other):
        self.num -= other
        self.den -= other
        print(f"Its method 'sub' {self.num}/{self.den}")

    def __str__(self):
        return f"{self.num}/{self.den}"

    def __mul__(self, other):
        self.num *= other
        self.den *= other
        print(f"Its method 'mul' {self.num}/{self.den}")

    def __floordiv__(self, other):
        self.num //= other
        self.den //= other
        print(f"Its method 'floordiv' {self.num}/{self.den}")


num1 = Fraction(10, 5)

print(f'Its fraction {num1}')

num_add = num1 + 20
num_mul = num1 * 2
num_sub = num1 - 30
num_floordiv = num1 // 5
