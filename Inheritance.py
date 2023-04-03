from employee import Employee
from person import Person
from customer import Customer


fred = Employee("Fred Bloggs", 'm', '130268')
wilma = Employee("Wilma", 'f', '130266')
pebbles = Customer("Pebbles", 'f', 'c2324')
barney = Person("Barney", 'm')
betty = Person("Betty", 'f')
bambam = Customer("Bam-Bam", 'm', 'c2325')

print(fred)
print(wilma)
print(pebbles)
print(barney)
print(betty)
print(bambam)