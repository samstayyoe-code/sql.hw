# class Kitob:
#     def __init__(self, nom, muallif, narx, nashriyot):
#         self.nom = nom
#         self.muallif = muallif
#         self.narx = narx
#         self.nashriyot = nashriyot

#     def info(self):
#         return f"{self.nom} - {self.muallif} - {self.narx} - {self.nashriyot}"
    
# k1=Kitob("Python", "Ali", 100, "Alif")
# k2=Kitob("JS", "Vali", 120, "Beta")
# k3=Kitob("Java", "Sami", 150, "Delta")
# k4=Kitob("C++", "Hasan", 90, "Zeta")
# k5=Kitob("Go", "Husan", 110, "Gamma")

# books=[k1, k2, k3, k4, k5]
# for b in books:
#     if b.nashriyot[0].upper() >= 'A' and b.nashriyot[0].upper() <= 'H':
#         print(b.info())

# --------------------------------------------------

# class Kompyuter:
#     def __init__(self, nom, ram, narx, protsessor):
#         self.nom=nom
#         self.ram=ram
#         self.narx=narx
#         self.protsessor=protsessor

#     def info(self):
#         return f"{self.nom} - {self.ram}GB - {self.narx}$ - {self.protsessor}"


# c1=Kompyuter("HP",8,800,"i5")
# c2=Kompyuter("Dell",16,1000,"i7")
# c3=Kompyuter("Lenovo",6,700,"i3")
# c4=ompyuter("Asus",12,900,"i5")

# computers = [c1,c2,c3,c4]

# for c in computers:
#     if 4<c.ram<16:
#         print(c.info())

# --------------------------------------------------

class User:
    def __init__(self,ism,username,email):
        self.ism=ism
        self.username=username
        self.email=email

    def get_info(self):
        return(f"foydalanuvchi:{self.username}, ismi: {self.ism}, email:{self.email}")

u1=User("Alijon Valiyev","alijon1994","alijon1994@gmail.com")
u2=User("Bekzod Karimov","bekzod01","bekzod@mail.com")
print(u1.get_info())
print(u2.get_info())