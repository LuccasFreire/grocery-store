from Model import Product


class Stock:
    def __init__(self, product: Product, quantity):
        self.product = product
        self.quantity = quantity