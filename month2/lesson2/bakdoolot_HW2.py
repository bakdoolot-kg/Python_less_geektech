class Company:
    company_bank = 20000
    # company_bank = 9000

    def __init__(self, company_name):
        self.company_name = company_name

class Person(Company):

    def __init__(self, company_name, first_name, last_name, salary):
        super().__init__(company_name)
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def get_salary(self):
        if self.company_bank < self.salary : print('У компании не достаточно средств!')
        else:
            self.company_bank -= self.salary
            print('Зарплата оплачена!')
        print(f'Оставшиеся бюджет: {self.company_bank}')

    def person_info(self):
        print(f"""
            Имя: {self.first_name}
            Фамилия: {self.last_name}
            Зарплата: {self.salary}
        """)

person1 = Person('Google', 'Jonathan', 'Jojo', 10000)
person2 = Person('Apple', 'Tom', 'Holland', 9500)

person1.get_salary()
person1.person_info()

# person2.get_salary()
# person2.person_info()