from Model import Product


class Estoque:
    def __init__(self, product: Product, quantity):
        self.product = product
        self.quantity = quantity