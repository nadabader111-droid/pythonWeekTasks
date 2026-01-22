from product import Product
from discountProduct import DiscountProduct
from taxProduct import TaxProduct

p1 = Product("Water", 10)
d1 = DiscountProduct("Shoes", 200, 30)
t1 = TaxProduct("Laptop", 3000, 0.15)


print(p1.name, p1.getTotalPrice())
print(d1.name, d1.getTotalPrice())
print(t1.name, t1.getTotalPrice())





#Product
# name , price
# getTotalPrice() → price

#DiscountProduct
# name , price , discount
# getTotalPrice() → price - discount


#TaxProduct
# name , price , taxRate
# getTotalPrice() → price + (price * taxRate)

#test_product
#Product , DiscountProduct , TaxProduct
