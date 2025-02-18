# bir kitaplığımız olacak, biz bir kitap ile ilgili bilgileri bir doyaya kaydedicez kitapların üstünde silme güncelleme işlemlerini yapalım
# kitap adı , yazarı , sayfası ,basım yılı

# Tam bitmedi!!!

kitap_listesi = []

class Kitap():
    def __init__(self , ad , yazar , sayfa , basimYili):
        self.ad = ad
        self.yazar = yazar
        self.sayfa = sayfa
        self.basimYili = basimYili

def kitapekle():
    kitap_adi = input("Kitap adını giriniz: ")
    kitap_yazari = input("Kitabın yazarını giriniz: ")
    kitap_sayfasi = int(input("Kitabın sayfa sayısını giriniz: "))
    kitap_basimYili = int(input("Kitabın basım yılını giriniz: "))
    kitap = (kitap_adi , kitap_yazari , kitap_sayfasi , kitap_basimYili)
    kitap_listesi.append(kitap)

def kitapCikar():
    kitap_adi = input("Çıkartmak istediğiniz kitabın adını giriniz: ")
    kitap_yazari = input("Çıkartmak istediğiniz kitabın azarını giriniz: ")
    kitap_sayfasi = int(input("Çıkartmak istediğiniz kitabın sayfa sayısını giriniz: "))
    kitap_basimYili = int(input("Çıkartmak istediğiniz kitabın basım yılını giriniz: "))
    kitap = (kitap_adi , kitap_yazari , kitap_sayfasi , kitap_basimYili)

    if kitap in kitap_listesi:
      kitap_listesi.pop(kitap)
    else:
        print("Silmek istediğiniz kitap listede bulunmamaktadır.")

def kitapGuncelle():
    kitap_adi = input("Güncellemek istediğiniz kitabın adını giriniz: ")
    kitap_yazari = input("Güncellemek istediğiniz kitabın  yazarını giriniz: ")
    kitap_sayfasi = int(input("Güncellemek istediğiniz kitabın  sayfa sayısını giriniz: "))
    kitap_basimYili = int(input("Güncellemek istediğiniz kitabın basım yılını giriniz: "))
    kitap = (kitap_adi , kitap_yazari , kitap_sayfasi , kitap_basimYili)

    if kitap in kitap_listesi:
      index = kitap_listesi.index(kitap)
      kitap_listesi.pop(kitap[index])

    else:
        print("Güncellemek istediğiniz kitap listede bulunmamaktadır.")

    ykitap_adi = input("Eklemek istediğiniz kitabın adını giriniz: ")
    ykitap_yazari = input("Eklemek istediğiniz kitabın  yazarını giriniz: ")
    ykitap_sayfasi = int(input("Eklemek istediğiniz kitabın  sayfa sayısını giriniz: "))
    ykitap_basimYili = int(input("Eklemek istediğiniz kitabın basım yılını giriniz: "))
    ykitap = (ykitap_adi , ykitap_yazari , ykitap_sayfasi , ykitap_basimYili)
    kitap_listesi.append(ykitap)
    print("Kitap başarıyla güncellendi.")


kitapekle()
print(kitap_listesi)
kitapGuncelle()
print(kitap_listesi)