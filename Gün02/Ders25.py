baslangic = int(input("Başlangıç :"))
bitis = int(input("Bitis :"))
artis = int (input("Artış :"))

if baslangic > bitis:
    baslangic , bitis = bitis , baslangic
    
toplam, carpim = 0,1

while baslangic <= bitis :
    toplam += baslangic
    carpim *= baslangic
    baslangic += artis

metin = "Sayıların toplamı {} , çarpımı {}"
print(metin.format(toplam,carpim))