from product import Product


class TaxProduct(Product):
    def __init__(self, name, price, taxRate):
        Product.__init__(self, name, price)
        self.taxRate = taxRate

    def getTotalPrice(self):
        total = self.price + (self.price * self.taxRate)
        return total

#TaxProduct
# name , price , taxRate
# getTotalPrice() → price + (price * taxRate)