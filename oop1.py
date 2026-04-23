# class champion:
#     def show(self):
#         print("salom")

# p1=champion()
# p1.show()

# class animal:
#     def __init__(self,animal,type):
#         self.animal=animal
#         self.type=type
    
#     def show(self):
#         print(f"""
# hayvon nomi: {self.animal}
# hayvon turi: {self.type}""")

# hayvon=animal(input("hayvon:"),input("turi:"))
# hayvon.show()

# class car:
#     def __init__(self,name,year,speed,color,country,petrol):
#         self.nomi=name
#         self.yili=year
#         self.tezlik=speed
#         self.rangi=color
#         self.mamlakat=country
#         self.yoqilgi=petrol

#     def year(self,new_year=2020):
#         self.yili=new_year
#     def country(self,new_country="uzbekistan"):
#         self.mamlakat=new_country
#     def tuning(self,new_color="black"):
#         self.rangi=new_color
#     def update_speed(self,new_speed=350):
#         self.tezlik=new_speed
#     def settings(self,new_petrol="dizel"):
#         self.yoqilgi=new_petrol
#     def info(self):
#         print(f"""
# nomi:{self.nomi}
# yili:{self.yili}
# tezligi:{self.tezlik}
# rangi:{self.rangi}
# davlati:{self.mamlakat}
# yoqilgisi:{self.yoqilgi}""")

# m1 = car("audi", "1995","220","oq","germany","benzin")
# m2 = car ("ferrari","2025","300","qizil","italy","salyarka")
# m3 = car ("bugatti","2015","500","kok","UAE","dizel")
# lst=[m1,m2,m3]
# minimum_tezlik=min(lst,key=lambda x:x.tezlik)
# print(minimum_tezlik.nomi)
# m2.info()

# class market:
#     def __init__(self,price,name):
#         self.narxi=price
#         self.nomi=name
# dct={}
# for i in range(3):
#     dct.update()
# for i in dct:
#     print(i)
# ------------------------------------------------

class Market:
    def __init__(self):
        self.products = []

    def addProduct(self, name, price):
        product = {"name": name, "price": price}
        self.products.append(product)

    def removeProduct(self, name):
        self.products = [p for p in self.products if p["name"] != name]

    def get_all_price(self):
        total = sum(p["price"] for p in self.products)
        return total
    
m = Market()
m.addProduct("Olma", 5000)
m.addProduct("Banan", 8000)
m.addProduct("Uzum", 6000)
print("Jami narx:", m.get_all_price())
m.removeProduct("Banan")
print("Yangi jami:", m.get_all_price())

