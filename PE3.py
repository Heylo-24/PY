def line():
    print("======")

class food:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display_food(self):
        print("Food Name:",self.name)
        print("Food Price:RM{:.2f}".format(self.price))

class Restaurant(food):
    tax_rate = 0.06

    @classmethod
    def show_tax_rate(cls):
        print("Tax Rate:", cls.tax_rate)

    def calculate_total(self):
        tax = self.price * Restaurant.tax_rate
        total = self.price + tax
        return tax,total

    def display_receipt(self):
        tax, total = self.calculate_total()
        print("Food Name:",self.name)
        print("Food Price:RM{:.2f}".format(self.price))
        print("tax:RM{:.2f}".format(tax))
        print("Total:RM{:.2f}".format(total))

#input

name = input("ENTER food name")
price = float(input("ENTER food price"))

order = Restaurant(name,price)


line()
print("Receipt")
line()
order.display_receipt()
line()
              
              
        
