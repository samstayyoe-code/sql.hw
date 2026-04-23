from datetime import datetime

class Drug:
    def __init__(self, name: str, production_date: str):
        self.name = name
        self.production_date = production_date
    def get_time(self):
        today = datetime.now()
        prod_date = datetime.strptime(self.production_date, "%Y-%m-%d")
        days = (today - prod_date).days
        print(days)
d = Drug("Paracetamol", "2024-01-01")
d.get_time()

# ------------------------------------

# class BookStore:
#     def __init__(self, customer_name: str, age: int, book_name: str, price: float):
#         self.customer_name = customer_name
#         self.age = age
#         self.book_name = book_name
#         self.price = price
#     def get_price(self):
#         if self.age < 18:
#             discount = 0.2
#         elif self.age >= 60:
#             discount = 0.3
#         else:
#             discount = 0.0
#         final_price = self.price * (1 - discount)
#         print(final_price)
# b = BookStore("Ali", 16, "Python Book", 100)
# b.get_price()

# ------------------------------------------------

# class Transport:
#     def __init__(self, fuel: str, model: str, max_speed: int):
#         self.fuel = fuel
#         self.model = model
#         self.max_speed = max_speed

#     def get_info(self):
#         print(f"""TRANSPORT INFO:
# MODEL: {self.model}
# MAX SPEED: {self.max_speed}
# FUEL: {self.fuel}""")
# t = Transport("Petrol", "Malibu", 220)
# t.get_info()

# ------------------------------------------

# class Population:
#     def __init__(self, name: str, age: int, gender: str):
#         self.name = name
#         self.age = age
#         self.gender = gender

#     def get_info(self):
#         if self.age > 50:
#             if self.gender == "male":
#                 prefix = "janob"
#             else:
#                 prefix = "xonim"

#             print(f"{prefix} {self.name} - {self.age}")

# people = [
#     Population("Ali", 55, "male"),
#     Population("Vali", 30, "male"),
#     Population("Nodira", 60, "female"),
#     Population("Aziza", 25, "female"),
#     Population("Karim", 70, "male"),
# ]

# for p in people:
#     p.get_info()