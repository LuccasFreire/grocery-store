import sys
sys.path.insert(0, 'C:\\Users\\Lucas Freire\\Documents\\Coding\\Python\\grocery-store\\')
sys.path.insert(0, 'C:\\Users\\Lucas Freire\\Documents\\Coding\\Python\\grocery-store\\Model')
sys.path.insert(0, 'C:\\Users\\Lucas Freire\\Documents\\Coding\\Python\\grocery-store\\DAO')

# from Model.Category import Category
from DAO.CategoryDAO import CategoryDAO
from Model.Category import Category


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
    
    
    def deleteCategory(self, categoryToRemove):
        x = CategoryDAO.read()
        cat = list(filter(lambda x: x.category == categoryToRemove, x))

        if len(cat) <= 0:
            print('The category doesnt exists in the System')
        else:
            for i in range(len(x)):
                if x[i].category == categoryToRemove:
                    del x[i]
                    break
            print("Category removed successfully!")
        
        with open('categoryRegistry.txt', 'w') as categoryRegistry:
            for i in x:
                categoryRegistry.writelines(i.category)
                categoryRegistry.writelines('\n')

    def changeCategory(self, categoryToChange, newCategory):
        x = CategoryDAO.read()
        cat = list(filter(lambda x: x.category == categoryToChange, x))

        if len(cat) > 0:
            cat1 = list(filter(lambda x: x.category == newCategory, x))
            if len(cat1) == 0:
                x = list(map(lambda x: Category(newCategory) if(x.category == categoryToChange) else(x), x))
                print("The changement was made with success")
            else:
                print("Category you want to change already exists")
        else:
            print("Category doesnt exist in the System")

        with open('categoryRegistry.txt', 'w') as categoryRegistry:
            for i in x:
                categoryRegistry.writelines(i.category)
                categoryRegistry.writelines('\n')

    def showCategories(self):
        categories = CategoryDAO.read()
        if len(categories) == 0:
            print("There are 0 categories")
        else:
            for i in categories:
                print(f'Categorie:  {i.categorie}')

# a = CategoryController()
# a.registerCategory('Meat')
# a.changeCategory("Pasta", "Lemon")
# a.deleteCategory('Meat')