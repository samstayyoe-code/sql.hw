class Apteka:
    def __init__(self):
        self.royxat=[]
        self.kassa=0
    def add_drug(self,name,narx,ogriq,srog,soni):
        dori={
            "name": name,
            "narx": narx,
            "ogriq": ogriq,
            "srog": srog,
            "soni": soni
        }
        self.royxat.append(dori)
    def sotmoq_by_name(self,name):
        for d in self.royxat:
            if d["name"]==name and d["soni"]>0:
                d["soni"]-=1
                self.kassa+=d["narx"]
                print(f"{name} sotildi")
                return
        print("topilmadi yoki qolmagan")
    
    def sotmoq_by_ogriq(self,ogriq):
        for d in self.royxat:
            if d["ogriq"]==ogriq and d["soni"]>0:
                d["soni"]-=1
                self.kassa+=d["narx"]
                print(f"{d["name"]} sotildi {ogriq} uchun")
                return
        print("mos dori aptekamizda yoq boshqa aptekadan sorab koring")

    def utilizatsiya(self):
        yangi=[]
        for d in self.royxat:
            if d["srog"]>0:
                yangi.append(d)
            self.royxat=yangi
        print("muddati otgan dorilar tashlab yuborildi")


apteka = Apteka()

apteka.add_drug("Paracetamol", 2000, "bosh", 5, 3)
apteka.add_drug("ketanol", 3000, "tish", 0, 2)

apteka.sotmoq_by_name("Paracetamol")
apteka.sotmoq_by_ogriq("bosh")

apteka.utilizatsiya()

print("Kassa:", apteka.kassa)
print("Dorilar:", apteka.royxat)