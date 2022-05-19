
"""

Person - its class for Person
attrs - (
    first_name: String
    last_name: String
    age: Integer >= 0 <= 100
    salary: Float !< 0
)

methods - (
    get_info --> return Person Information
    get_salary --> Person.salary_amount += Person.salary and return it
)

"""


class Person:

    salary_amount = 0

    def __init__(self,
                 first_name: str,
                 last_name: str,
                 age: int,
                 salary: float
                 ):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.salary = salary

    def get_info(self):
        print(f"""
        First Name: { self.first_name }
        Last Name: { self.last_name }
        Full Name: { self.first_name } { self.last_name }
        Age: { self.age }
        Salary: { self.salary }
        """)

    def get_salary(self):
        self.salary_amount += self.salary
        print(f"You get Salary! +{self.salary}")
        return self.salary_amount


"""
create_person - function for create new instance of Person - (class)
create_person() return new Instance of Person - (class)
"""


def create_person(
        first_name: str,
        last_name: str,
        age: int,
        salary: float
) -> Person:
    return Person(first_name, last_name, age, salary)
