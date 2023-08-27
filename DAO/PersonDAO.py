import sys
sys.path.insert(0, 'C:\\Users\\Lucas Freire\\Documents\\Coding\\Python\\grocery-store\\')
from Model.Person import Person

class PersonDAO:
    @classmethod
    def save(cls, person: Person):
        with open("personRegistry.txt", "a") as personRegistry:
          personRegistry.writelines(person.name + "-" + person.phone +"-"+ person.cpf + "-" + person.email + "-" + person.address)
          personRegistry.writelines("\n")
    
    @classmethod
    def read(cls):
        with open("personRegistry.txt", "r") as personRegistry:
            cls.reg = personRegistry.readlines()
            cls.reg = list(map(lambda x: x.replace('\n', ''), cls.reg))
            cls.reg = list(map(lambda x: x.split('-'), cls.reg))

            pers = []
            for i in cls.reg:
              pers.append(Person(i[0], i[1], i[2], i[3], i[4]))
            return pers
        
# x = Person('Lucas', '8383828381', '12312312312312', 'teste@gmail.com', 'Rua Augusto de Lima')
# PersonDAO.read()
