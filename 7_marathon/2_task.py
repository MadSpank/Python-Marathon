class Goods: 

    def __init__(self, price, discount_strategy = None): 
        self.price = price
        self.discount_strategy = discount_strategy
        self.new_price = price
    
    def price_after_discount(self):
        if self.discount_strategy:
            self.new_price = self.discount_strategy(self.price)
    
    def __str__(self):
        self.price_after_discount()
        return f'Price: {self.price}, price after discount: {self.new_price}'

def on_sale_discount(order): 
      return order * 0.5

def twenty_percent_discount(order):
    return order * 0.8

print(Goods(20000, discount_strategy = twenty_percent_discount))
    
print(Goods(20000, discount_strategy = on_sale_discount))