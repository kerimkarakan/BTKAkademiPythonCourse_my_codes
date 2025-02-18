class Ogrenci():
    bolum = "Bilişim"
    kurs = "Btk Akademi"

    def __init__(self, ad, soyad, tc):
        print("Ogrenci oluşturuldu")
        self.ad = ad
        self.soyad = soyad
        self.tcno = tc
    def tamAd(self):
        return self.ad + self.soyad
    def kacHarf(self):
        return len(self.ad)
    
    def __str__(self): 
        return f"{self.ad} {self.soyad} adında bir öğrenci."
    

ogr1 = Ogrenci("kerim","karakan",123)

# bu şekilde print yapmak istediğimizde olmayacak çünkü içindeki elemanları ver diye belirtmemiz lazım yani print(vars(ogr1)) dememiz gerekiyor 
# veya yukarıdaki gibi def __str__(self) deriz ve ogr1 i çağırdığımızda bunları bunları getir diyebiliriz (mesela örnekte biz ogr1 in ad ve soyadını istedik sadece)

print(ogr1) 

print(ogr1.bolum)
print(ogr1.kurs)
print(vars(ogr1))
print(ogr1.tamAd())
harf_sayisi = ogr1.kacHarf()
print(harf_sayisi)


