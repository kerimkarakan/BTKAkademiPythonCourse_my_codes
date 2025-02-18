class Ogrenci():
    def __init__(self,ad,soyad):
        self.ad = ad
        self.soyad = soyad

class FOgrenci(Ogrenci): #bu şekilde class içinde class tanımlayabiliyoruz
    def __init__(self,ad,soyad,fakulte):
        #Ogrenci.__init__(self,ad,soyad)
        super().__init__(ad,soyad)
        self.fakulte = fakulte

class BOgrenci(FOgrenci):
    def __init__(self,ad,soyad,fakulte,bolum):
        #FOgrenci.__init__(self,ad,soyad,fakulte)
        super().__init__(ad,soyad,fakulte)
        self.bolum = bolum

ogr1 = Ogrenci("ali", "veli")
fogr1 = FOgrenci("ali", "veli", "muhendislik")
bogr1 = BOgrenci("ali", "veli", "muhendislik", "yazılım")

print(vars(bogr1))