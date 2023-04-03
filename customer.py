from person import Person


class Customer(Person):

    def __init__(self, name, gender, customerid):
        super().__init__(name, gender)
        self._customerid = customerid

    def __str__(self):
        return super().__str__() + " Customer ID: " + self._customerid
