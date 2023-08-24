from Model import Products
from datetime import datetime
class Sell:
    def __init__(self,soldItems: Products, seller, buyer, quantitySold, date = datetime.now().strftime("%d/%m/%Y")):
        self.soldItems = soldItems
        self.seller = seller
        self.buyer = buyer
        self.quantitySold = quantitySold
        self.date = date
