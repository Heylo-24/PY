# fms.py - Food Management System (Beginner)

class Food:
    def __init__(self, food_id, name, price, quantity):
        self.food_id = food_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.food_id} - {self.name} (RM{self.price:.2f}, Stock: {self.quantity})"


# Fungsi asas
food_list = []

def add_food(food):
    food_list.append(food)

def find_food(food_id):
    for f in food_list:
        if f.food_id == food_id:
            return f
    return None

def search_food(name):
    return [f for f in food_list if name.lower() in f.name.lower()]

def calculate_total_price():
    return sum(f.price * f.quantity for f in food_list)

def place_order(food_id, qty):
    food = find_food(food_id)
    if food and food.quantity >= qty:
        food.quantity -= qty
        return True
    return False

def total_available_food():
    return sum(f.quantity for f in food_list)
