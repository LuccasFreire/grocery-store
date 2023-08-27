import sys
sys.path.insert(0, 'C:\\Users\\Lucas Freire\\Documents\\Coding\\Python\\grocery-store\\')
from Model.Supplier import Supplier

class PersonDAO:
    @classmethod
    def save(cls, supplier: Supplier):
        with open("supplierRegistry.txt", "a") as supplierRegistry:
          supplierRegistry.writelines(supplier.name + "-" + supplier.cnpj + "-" + supplier.phone + "-" + supplier.category)
          supplierRegistry.writelines("\n")
    
    @classmethod
    def read(cls):
        with open("supplierRegistry.txt", "r") as supplierRegistry:
            cls.reg = supplierRegistry.readlines()
            cls.reg = list(map(lambda x: x.replace('\n', ''), cls.reg))
            cls.reg = list(map(lambda x: x.split('-'), cls.reg))

            supp = []
            for i in cls.reg:
              supp.append(Supplier(i[0], i[1], i[2], i[3]))
            return supp