import sys
sys.path.insert(0, 'C:\\Users\\Lucas Freire\\Documents\\Coding\\Python\\grocery-store\\')

from Model.Sell import Sell
from Model.Products import Product


class SellDAO:
    @classmethod
    def save(cls, sell: Sell):
      with open("sellsRegistry.txt","a") as sellsRegistry:
        sellsRegistry.writelines(sell.soldItems.name + "-" + sell.soldItems.price + "-" + sell.soldItems.category + "-" + sell.seller + "-" + sell.buyer + "-" + str(sell.quantitySold) + "-" + sell.date)
        sellsRegistry.writelines("\n")
    
    @classmethod
    def read(cls):
       with open("sellsRegistry.txt", "r") as sellsRegistry:
          cls.sell = sellsRegistry.readlines()
          cls.sell = list(map(lambda x: x.replace('\n', ''), cls.sell))
          cls.sell = list(map(lambda x: x.split('-'), cls.sell))

          sel = []
          for i in cls.sell:
             sel.append(Sell(Product(i[0], i[1], [2]), i[3], i[4], i[5], i[6]))
          return sel