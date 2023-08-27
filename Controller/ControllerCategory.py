import sys
sys.path.insert(0, 'C:\\Users\\Lucas Freire\\Documents\\Coding\\Python\\grocery-store\\')
sys.path.insert(0, 'C:\\Users\\Lucas Freire\\Documents\\Coding\\Python\\grocery-store\\Model')
sys.path.insert(0, 'C:\\Users\\Lucas Freire\\Documents\\Coding\\Python\\grocery-store\\DAO')

# from Model.Category import Category
from DAO.CategoryDAO import CategoryDAO


class CategoryController:
    
    def registerCategory(self, newCategory):
        exists = False
        read = CategoryDAO.read()
        
        for i in read:
            if i.category == newCategory:
                exists = True
        if not exists:
            CategoryDAO.save(newCategory)
            print("Sucessfully registered the category")
        else:
            print("The category already exists in the System!")

# a = CategoryController()
# a.registerCategory('Meat')