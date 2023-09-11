"""
  File: employee.py
  Description: Employee classes and stuff

  Student Name: Arham Lodha
  Student UT EID: arl3759

  Partner Name: Tho Lam
  Partner UT EID: tml2532

  Course Name: CS 313E
  Unique Number: 52590
  Date Created: 09/01/2023
  Date Last Modified: 09/01/2023
"""


class Employee:
    """
    Represents an employee with a name, identifier, and salary.

    Attributes:
        _name (str): The name of the employee.
        _identifier (str): The unique identifier of the employee.
        _salary (float): The salary of the employee.

    Methods:
        __init__(self, **kwargs): Initializes an Employee object with optional attributes.
        __str__(self): Returns a string representation of the Employee object.
    """

    def __init__(self, **kwargs):
        self._name = kwargs.get("name", 0)
        self._identifier = kwargs.get("identifier", "")
        self._salary = kwargs.get("salary", 0)

    def __str__(self):
        return f'Employee\n{self._name}, {self._identifier}, {self._salary}'


############################################################
############################################################
############################################################

class PermanentEmployee:
    """
    Represents a permanent employee, inheriting attributes and methods from the Employee class.

    Attributes:
        _name (str): The name of the employee.
        _identifier (str): The unique identifier of the employee.
        _salary (float): The salary of the employee.

        _benefits (list): A list of benefits available to the permanent employee.
            Should contain 'health_insurance' and/or 'retirement'.

    Methods:
        __init__(self, **kwargs): Initializes a PermanentEmployee object with optional attributes.
        cal_salary(self): Calculates the salary based on the employee's benefits.
        __str__(self): Returns a string representation of the PermanentEmployee object.
    """

    def __init__(self, **kwargs):

        benefits = kwargs.get("benefits", [])

        if len(benefits) != 1 and len(benefits) != 2:
            raise ValueError(
                "Permanent Employee can only have 1 or 2 benefits")
        if benefits[0] != "health_insurance" and benefits[0] != "retirement":
            raise ValueError(
                "Invalid benefits: should be 'health_insurance' or 'retirement")
        if (len(benefits) == 2
                and (benefits[1] != "health_insurance" or benefits[1] != "retirement")):
            raise ValueError(
                "Invalid benefits: should be 'health_insurance' or 'retirement")

        self._name = kwargs.get("name", 0)
        self._identifier = kwargs.get("identifier", "")
        self._salary = kwargs.get("salary", 0)

        self.benefits = benefits

    def cal_salary(self):
        """
        Calculates the salary for the PermanentEmployee based on their benefits.

        Returns:
            float: The calculated salary.
        """
        if len(self.benefits) == 2:
            return self._salary * 0.7

        if self.benefits[0] == "health_insurance":
            return self._salary * 0.9

        return self._salary * 0.8

    def __str__(self):
        return f"""PermanentEmployee
        {self._name}, {self._identifier}, {self._salary}, {self.benefits}"""


############################################################
############################################################
############################################################

class Manager:
    """
    Represents a manager, inheriting attributes and methods from the Employee class.

    Attributes:
        _name (str): The name of the employee.
        _identifier (str): The unique identifier of the employee.
        _salary (float): The salary of the employee.

        _bonus (float): The bonus amount for the manager.

    Methods:
        __init__(self, **kwargs): Initializes a Manager object with optional attributes.
        cal_salary(self): Calculates the total salary for the manager, including the bonus.
        __str__(self): Returns a string representation of the Manager object.
    """

    def __init__(self, **kwargs):
        self._name = kwargs.get("name", 0)
        self._identifier = kwargs.get("identifier", "")
        self._salary = kwargs.get("salary", 0)

        self._bonus = kwargs.get("bonus", 0)

    def cal_salary(self):
        """
        Calculates the total salary for the Manager, including the bonus.

        Returns:
            float: The calculated total salary.
        """
        return self._salary + self._bonus

    def __str__(self):
        return f"Manager\n{self._name}, {self._identifier}, {self._salary}, {self._bonus}"


############################################################
############################################################
############################################################
class TemporaryEmployee:
    """
    Represents a temporary employee, inheriting attributes and methods from the Employee class.

    Attributes:
        _name (str): The name of the employee.
        _identifier (str): The unique identifier of the employee.
        _salary (float): The salary of the employee.
        _hours (float): The number of hours worked by the temporary employee.

    Methods:
        __init__(self, **kwargs): Initializes a TemporaryEmployee object with optional attributes.
        cal_salary(self): Calculates the salary for the temporary employee based on hours worked.
        __str__(self): Returns a string representation of the TemporaryEmployee object.
    """

    def __init__(self, **kwargs):
        self._hours = kwargs.get("hours", 0)
        self._name = kwargs.get("name", 0)
        self._identifier = kwargs.get("identifier", "")
        self._salary = kwargs.get("salary", 0)

    def cal_salary(self):
        """
        Calculates the salary for the TemporaryEmployee based on the number of hours worked.

        Returns:
            float: The calculated salary.
        """
        return self._salary * self._hours

    def __str__(self):
        return f"TemporaryEmployee\n{self._name}, {self._identifier}, {self._salary}, {self._hours}"


############################################################
############################################################
############################################################


class Consultant:
    """
    Represents a consultant, inheriting attributes and methods from the TemporaryEmployee class.

    Attributes:
        _name (str): The name of the employee.
        _identifier (str): The unique identifier of the employee.
        _salary (float): The salary of the employee.
        _hours (float): Hours of work
        _travel (float): The amount of travel expenses for the consultant.

    Methods:
        __init__(self, **kwargs): Initializes a Consultant object with optional attributes.
        cal_salary(self): Calculates the salary for the consultant, including travel expenses.
        __str__(self): Returns a string representation of the Consultant object.
    """

    def __init__(self, **kwargs):
        self._name = kwargs.get("name", 0)
        self._identifier = kwargs.get("identifier", "")
        self._salary = kwargs.get("salary", 0)
        self._hours = kwargs.get("hours", 0)
        self._travel = kwargs.get("travel", 0)

    def cal_salary(self):
        """Calculate Salary for Consultant



        Returns:
            int: Salary
        """
        return self._salary * self._hours + self._travel*1000

    def __str__(self):
        return f"""Consultant
        {self._name}, {self._identifier}, {self._salary}, {self._hours}, {self._travel}"""
############################################################
############################################################
############################################################


class ConsultantManager:
    """
    Represents a consultant manager, 

    Attributes:
        _name (str): The name of the employee.
        _identifier (str): The unique identifier of the employee.
        _salary (float): The salary of the employee.
        _hours (float): Hours of work
        _travel (float): The amount of travel expenses for the consultant.
        _bonus (float): The bonus amount for the manager.


    Methods:
        cal_salary(self): Calculates the salary for the consultant manager, 
            including bonus and travel expenses.
        __str__(self): Returns a string representation of the ConsultantManager object.
    """

    def __init__(self, **kwargs):
        self._name = kwargs.get("name", 0)
        self._identifier = kwargs.get("identifier", "")
        self._salary = kwargs.get("salary", 0)
        self._hours = kwargs.get("hours", 0)
        self._travel = kwargs.get("travel", 0)
        self._bonus = kwargs.get("bonus", 0)

    def cal_salary(self):
        """Calculate salary for consultant manager

        Returns:
            int: Salary
        """
        return self._salary * self._hours + self._travel*1000 + self._bonus

    def __str__(self):
        return f"""Consultant
        {self._name}, {self._identifier}, {self._salary}, 
        {self._hours}, {self._travel}, {self._bonus}"""


############################################################
############################################################
############################################################


###### DO NOT CHANGE THE MAIN FUNCTION ########

def main():
    """
    A Main function to create some example objects of our classes. 
    """

    chris = Employee(name="Chris", identifier="UT1")
    print(chris, "\n")

    emma = PermanentEmployee(name="Emma", identifier="UT2",
                             salary=100000, benefits=["health_insurance"])
    print(emma, "\n")

    sam = TemporaryEmployee(
        name="Sam", identifier="UT3", salary=100,  hours=40)
    print(sam, "\n")

    john = Consultant(name="John", identifier="UT4",
                      salary=100, hours=40, travel=10)
    print(john, "\n")

    charlotte = Manager(name="Charlotte", identifier="UT5",
                        salary=1000000, bonus=100000)
    print(charlotte, "\n")

    matt = ConsultantManager(name="Matt", identifier="UT6",
                             salary=1000, hours=40, travel=4, bonus=10000)
    print(matt, "\n")

    ###################################
    print("Check Salaries")

    print("Emma's Salary is:", emma.cal_salary(), "\n")
    emma.benefits = ["health_insurance"]

    print("Emma's Salary is:", emma.cal_salary(), "\n")
    emma.benefits = ["retirement", "health_insurance"]

    print("Emma's Salary is:", emma.cal_salary(), "\n")

    print("Sam's Salary is:", sam.cal_salary(), "\n")

    print("John's Salary is:", john.cal_salary(), "\n")

    print("Charlotte's Salary is:", charlotte.cal_salary(), "\n")

    print("Matt's Salary is:",  matt.cal_salary(), "\n")


if __name__ == "__main__":
    main()
