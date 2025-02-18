#kullanıcıdan 10 tane sayı isteyelim bu sayılardan en küçüğünü ve en büyüğünü yazdıralım (3. sayı en büyük sayı, 5. sayı en büyük sayı diye)

sayilar = []
for i in range(10):
    sayi = int(input(f"{i+1}. sayıyı giriniz"))
    sayilar.append(sayi)
print(sayilar)

# sayilar2 = sayilar.copy()
# sayilar.sort()
# eb = sayilar[-1]
# ek = sayilar[0]
# print(sayilar2,eb,ek)        #bu soldakilerin hepsi aynı işlemi uyguluyor neredeyse (taa sona kadar bana en kolayı max min yapmak geldi)

# eb = max(sayilar)
# ek = min(sayilar)
# print(sayilar,eb,ek)

eb = ek = sayilar[0]
for sayi in sayilar:
    if sayi > eb:
        eb = sayi
    if sayi < ek:
        ek = sayi
metin1 = "{} en küçük sayı, {} en küçük sırası".format(ek, sayilar.index(ek)+1)
metin2 = "{} en büyük sayı, {} en büyük sırası".format(eb, sayilar.index(eb)+1)
print(sayilar,metin1,metin2,sep="\n")



