
# Salary and Employee are interdependent

class Salary:
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus

    def annual_salary(self):
        return (self.pay * 12) + self.bonus


class Employee:
    def __init__(self, name, age, pay, bonus):
        self.name = name
        self.age = age

        # Salary class is 'part of' Employee
        self.salary_object = Salary(pay, bonus)

    def total_salary(self):
        return self.salary_object.annual_salary()


# Salary class object is defined under Employee class. Removing Employee will remove Salary
e1 = Employee("Elon Musk", 45, 1000000, 20000)
print(e1.total_salary())
