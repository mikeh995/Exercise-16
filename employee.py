from person import Person


class Employee(Person):

    def __init__(self, name, gender, employeeid):
        super().__init__(name, gender)
        self._employeeid = employeeid

    def __str__(self):
        return super().__str__() + " Employee ID: " + self._employeeid
