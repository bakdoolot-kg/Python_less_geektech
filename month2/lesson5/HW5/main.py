import re


class ValidCarNumber:
    def __init__(self, number):
        self.number = number

    def is_valid(self):
        self.number.upper()
        valid = re.search(r"0([1-9])KG([0-9]{3})([a-zA-Z]{3})", self.number)

        if not valid:
            print(f"Номер {self.number} не валидный!")
        elif self.number[valid.start():valid.end()] == self.number:
            print(f"Номер {self.number} валидный!")


num1 = ValidCarNumber(input('''
        Пример (09KG777STR)
        Ваш номер машины: '''))
num1.is_valid()

# num2 = ValidCarNumber('06KG333STR')
# num2.is_valid()
