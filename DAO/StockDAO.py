import sys
sys.path.insert(0, 'C:\\Users\\Lucas Freire\\Documents\\Coding\\Python\\grocery-store\\')

from Model.Stock import Stock
from Model.Products import Product
# from Model.Category import Category




class StockDAO:
    @classmethod 
    def save(cls, stock: Stock):
        with open("stockRegistry.txt", "a") as stockReg:
            stockReg.writelines(stock.product.name + "-" + stock.product.price + "-" + stock.product.category + "-" + str(stock.quantity))
            stockReg.writelines('\n')
    
    @classmethod
    def read(cls):
        with open("stockRegistry.txt", "r") as stockReg:
            cls.stock  = stockReg.readlines()
            cls.stock = list(map(lambda x: x.replace('\n', ''), cls.stock))
            cls.stock = list(map(lambda x: x.split('-'), cls.stock))

            st = []
            if len(cls.stock > 0):
              for i in cls.stock:
                st.append(Stock(Product(i[0],i[1],i[2]), [3]))
            return st

    
