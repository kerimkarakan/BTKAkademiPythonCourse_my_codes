class Ogrenci():
    kurs = "BTK Python"
    fakulte = ""

print(Ogrenci.kurs)
print(Ogrenci.fakulte)
# print(Ogrenci.bolum)

ogr1 = Ogrenci()
print(ogr1.kurs)

ogr1.fakulte = "Muhendislik" # burada sadece bir kişinin fakültesini tanımlıyoruz gruptaki herkesin değil (oluşturduğumuz Ogrenci() tipindeki))
print(ogr1.fakulte)
ogr1.bolum = "Yazılım" # burda da yine aynı şekilde sadece 1 kişiye bölüm tanımladık
print(ogr1.bolum)



