# bu aşağıdaki kod benim yazdığım kod(hatalı) (kullanıcıdan aldığımız 5 tane kitabı yazdırıyoruz) :
class Kitap():
    ad = ""
    yazar = ""
    basim_yili = ""

kitap_listesi = []

kitap_sayisi = 5

while kitap_sayisi > 0:
    for i in range(5):
     kitap_sayisi -= 1
     kitaplar = [input(f"{i+1} tane kitap ismi giriniz: ")]
     kitaplar = Kitap()
     kitap_listesi.append(kitaplar)

    if len(kitap_listesi) == 5:
        break

print(kitap_listesi)
    

#hocanın yazdığı:

class Kitap():
    ad = ""
    yazar = ""
    basim = ""

kitap_listesi = []
for i in range(5):
    kitap = Kitap()
    kitap.ad = input(f"{i+1}. Kitap adı giriniz")
    kitap_listesi.append(kitap)

for i in kitap_listesi:
    print(i.ad)
# print(Kitap.count)


