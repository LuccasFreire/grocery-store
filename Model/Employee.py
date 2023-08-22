from Model import Person
class Employee(Person):
    def __init__(self, clt, name, phone, cpf, email, address):
        self.clt = clt
        super(Employee, self).__init__(name, phone, cpf, email, address)
