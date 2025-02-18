# set - küme küme işareti = {}
# her run ettiğimizde farklı sırayla geliyor belli bir sırası yok
# aynı veriden 2 tane olamaz

ogrenciler = {"ali", "veli", "can", "kadir", "kaan",}
print(ogrenciler)
print(ogrenciler.pop())
print(ogrenciler)
for ogrenci in ogrenciler:
    print(ogrenci)

if "can" in ogrenciler:
    ogrenciler.remove("can")
    print(ogrenciler)
