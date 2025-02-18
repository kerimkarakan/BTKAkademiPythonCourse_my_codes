#versiyon 1 pazar listesi oluşturma
adet = int(input("Kaç farklı zerzevat alacaksınız"))
zerzevat = []

for i in range(1, adet+1) :
    urun = int(input(f"{i} . ürün bilgisini giriniz."))
    zerzevat.append(urun)

for urun in zerzevat :
    print(urun, sep="* " , end = "\t")

#versiyon 2 pazar listesi oluşturma
mesaj = """Pazar Listesi Oluşturma Programına Hoşgeldiniz. Programdan çıkmak için x'e basınız."""
print(mesaj)
zerzevat = []
while True:
    urun = input("Ürün girişi yapınız : ")
    if urun.lower() == "x" :
        print("pazar listeniz : " , zerzevat)
        break
    elif urun.lower() == "":
        continue
    else:
        zerzevat.append(urun)


