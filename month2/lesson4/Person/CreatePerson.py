
"""

Person - its class for Person
attrs - (
    first_name: String,
    last_name: String,
    age: Integer >= 0 <= 100
    salary: Float !< 0
)

methods - (
    get_info -> return Person all attrs
    get_salary -> return Person salary
)
"""
class Person:
    salary_mount = 0

    def __init__(self,
                 first_name: str,
                 last_name: str,
                 age: int,
                 salary: float):
        self.first_name = first_name,
        self.last_name = last_name,
        self.age = age,
        self.salary = salary

    def get_info(self):
        print(f"""
        First name: {self.first_name}
        Last name: {self.last_name}
        Full name: {self.first_name} {self.last_name}
        Age: {self.age}
        Salary: {self.salary}
        """)

    def get_salary(self):
        self.salary_mount += self.salary
        print(f'You get Salary! +{self.salary}')
        return self.salary_mount


"""
create_person - func for create new Person - (class)
"""

def create_person(
        first_name: str,
        last_name: str,
        age: int,
        salary: float
) -> Person:
    return Person(first_name, last_name, age, salary)