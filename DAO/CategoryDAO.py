import sys
sys.path.insert(0, 'C:\\Users\\Lucas Freire\\Documents\\Coding\\Python\\grocery-store\\')
from Model.Category import Category

class CategoryDAO:
    @classmethod
    def save(cls, category):
        with open("categoryRegistry.txt", "a") as categRegistry:
            categRegistry.write(f"{category}\n")
    
    @classmethod
    def read(cls):
        with open("categoryRegistry.txt", "r") as categoryRegistry:
            a = categoryRegistry.readlines()
        
        # a = list(map(lambda x: x.replace('\n', ''), a))
        cls.category = list(a)
        cat = []
        for i in cls.category:
            cat.append(Category(i))
        return cat
    
# cls.category(cat[i])


# CategoryDAO.save("Teste")
# CategoryDAO.read()
