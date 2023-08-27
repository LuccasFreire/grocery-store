import sys
sys.path.insert(0, 'C:\\Users\\Lucas Freire\\Documents\\Coding\\Python\\grocery-store\\')
# sys.path.insert(0, 'C:\\Users\\Lucas Freire\\Documents\\Coding\\Python\\grocery-store\\DAO')


from Model.Employee import Employee

class PersonDAO:
    @classmethod
    def save(cls, employee: Employee):
        with open("supplierRegistry.txt", "a") as employeeRegistry:
          employeeRegistry.writelines(employee.clt + "-" + employee.name + "-" + employee.phone + "-" + employee.cpf + "-" + employee.email + "-" + employee.address)
          employeeRegistry.writelines("\n")
    
    @classmethod
    def read(cls):
        with open("employeeRegistry.txt", "r") as employeeRegistry:
            cls.reg = employeeRegistry.readlines()
            cls.reg = list(map(lambda x: x.replace('\n', ''), cls.reg))
            cls.reg = list(map(lambda x: x.split('-'), cls.reg))

            empl = []
            for i in cls.reg:
              empl.append(Employee(i[0], i[1], i[2], i[3], i[4], i[5]))
            return empl