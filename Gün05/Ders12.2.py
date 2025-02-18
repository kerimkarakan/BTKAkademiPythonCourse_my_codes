class Ogrenci():
    bolum = "Bilişim"
    kurs = "Btk Akademi"
    ogrenci_sayisi = 0
    orenci_listesi = []
    
    def __init__(self, ad, soyad, tc):
        self.ad = ad
        self.soyad = soyad
        self.tcno = tc
        Ogrenci.ogrenci_sayisi += 1
        print(self.ogrenci_sayisi , "Ogrenci oluşturuldu")

    def tamAd(self):
        return self.ad + self.soyad
    
    def kacHarf(self):
        return len(self.ad)
    
    def __str__(self): 
        return f"{self.ad} {self.soyad} adında bir öğrenci."
    

ogr1 = Ogrenci("kerim","karakan",123)
ogr2 = Ogrenci("ege","canan",456)

# bu şekilde print yapmak istediğimizde direk (print(ogr1)) olmayacak çünkü içindeki elemanları ver diye belirtmemiz lazım yani print(vars(ogr1)) dememiz gerekiyor 
# veya yukarıdaki gibi def __str__(self) deriz ve ogr1 i çağırdığımızda bunları bunları getir diyebiliriz (mesela örnekte biz ogr1 in ad ve soyadını istedik sadece)

print(ogr1) 
print(ogr2)
print("Tanımlanan öğrenci sayisi: " , Ogrenci.ogrenci_sayisi)
print("Tanımlanan öğrenci sayisi: " , ogr1.ogrenci_sayisi)
print("Tanımlanan öğrenci sayisi: " , ogr2.ogrenci_sayisi)

print(ogr1.bolum)
print(ogr1.kurs)
print(vars(ogr1))
print(ogr1.tamAd())
harf_sayisi = ogr1.kacHarf()
print(harf_sayisi)