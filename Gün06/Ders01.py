class Calisan():
    sirket = "BTK"
    def __init__(self, ad, soyad, maas):
        self.ad = ad
        self.soyad = soyad
        self.maas = maas
        self.eposta = self.fEpostaOlustur()
    
    def fEpostaOlustur(self):
        return self.soyad + self.ad + "@sirket.com"
    
    @classmethod
    def fSirketDegis(cls):
        cls.sirket = input("Yeni şirket adını giriniz: ")
        return cls.sirket 
    def __str__(self):
        return self.soyad + self.ad
    
print(Calisan.sirket)
calisan1 = Calisan("hamza", "can", 20000)

print(calisan1.eposta)
print(calisan1.sirket)

calisan1.sirket =  "IBM"
calisan1.maas *= 33
Calisan.fSirketDegis()
print(calisan1.sirket)

calisan2 = Calisan("sakir", "can", 43355)
print(calisan2.sirket)


