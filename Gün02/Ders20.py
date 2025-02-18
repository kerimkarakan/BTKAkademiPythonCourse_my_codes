baslangic = int(input("Başlangıç sayısını giriniz :"))
bitis = int(input("Bitiş sayısını giriniz :"))
artis = int (input("Artış sayısını giriniz :"))

toplam, carpim = 0,1

for i in range(baslangic,bitis,artis) :
    print(i)
    toplam += i
    carpim *= i

metin = "Sayıların toplamı {} , çarpımı {}"
print(metin.format(toplam,carpim))





