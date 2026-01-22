from  product import Product
class  DiscountProduct(Product):
    def __init__(self,name , price,discount):
        Product.__init__(self,name , price)
        self.discount =discount

    def getTotalPrice(self):
        total =   self.price -self.discount
        return  total


#DiscountProduct
# name , price , discount
# getTotalPrice() → price - discount