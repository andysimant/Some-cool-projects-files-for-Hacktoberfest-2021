
class Main:
   def __init__(self, price, product):
      self.price = price
      self.product = product
   def return_price(self):
      return self.price
   def return_product(self):
      return self.product

car1 = Main(20000, 'pyla')
car2 = Main(200000, 'pyla+extreampro')
rubics_mute = Main(20, 'CoolLookToy')

print(rubics_mute.return_price())
