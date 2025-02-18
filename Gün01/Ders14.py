# tip dönüşüm işlemleri

sayi = 15
ssayi = str(sayi)
print(sayi , ssayi) # "ssayi" aslında 1 ve 5 sayısından oluşuyor ama print ettiğimizde "sayi" ile aynı değeri görüyoruz

print(sayi*2, ssayi*2) # ssayi ve sayi değeerinin farkını burda görebiliyoruz

# x değerini stringe çevirmek için str(x) metodunu kullanırız

numara = "782"
inumara= int(numara)
print(inumara, numara)
print(inumara*2, numara*2)

ondalikli = 12.5
osayi = float(ondalikli)
print(ondalikli, osayi)
print(ondalikli*2, osayi*2) # farklı olduklarını kanıtlamak için 2 ile çarptık

iosayi = int(osayi)
ossayi = float(sayi)
print(ossayi, iosayi)

mantik = "dfsfds"
smantik = bool(mantik) # boolean fonksiyonu stringin içinde veri olup olmadığına bakıyor yani parantez içinde bir şey varsa true vericek print(smantik) yazdığımızda
print(smantik) # eğer string içinde (yani yukarıdaki parantez içinde) veri yoksa false çıktısı verir

mantik = 5
imantik = bool(mantik) # burda da mantik değerimize 0 dan farklı bir şey verdğimiz sürece çıktı true olacak 0 olursa false olacak
print(imantik)

bifade = False
bmetin = str(bifade)
print(bmetin)

bsayi= True
isayi= int(bsayi)
print(isayi)
