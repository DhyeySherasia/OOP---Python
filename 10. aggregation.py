# Employee and Salary relation is unidirectional

class Salary:
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus

    def annual_salary(self):
        return (self.pay * 12) + self.bonus


class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age

        # Employee 'has a' Salary object
        self.salary_object = salary

    def total_salary(self):
        return self.salary_object.annual_salary()


# Both classes are given objects independently. Removing one will not affect the other
salary = Salary(1000000, 20000)
e1 = Employee("Elon Musk", 45, salary)
print(e1.total_salary())
