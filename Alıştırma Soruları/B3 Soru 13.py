# 2 den fazla yemek olduğunda sorun çıkacaktır bunu bilgisayara nasıl yaptırabiliriz ona bir bakabilitsin
menu = "dürüm" , "kebap"

print(f"Restorantımıza hoşgeldiniz. \nBugünkü menümüz: {menu} ")

durum_fiyat = 200

kebap_fiyat = 300

durum_kebap_toplam = 500

siparis = input("Menüden bir yemek seçiniz (kebap ve dürümü aynı anda istiyorsanız dürüm + kebap yazınız): ")

if siparis in menu and siparis == "dürüm":
    print(f"Sipariş tutarı: {durum_fiyat} TL ")

elif siparis in menu and siparis == "kebap":
    print(f"Sipariş tutarı: {kebap_fiyat} TL")

elif siparis in menu and siparis == "durum + kebap":
    print(f"Sipariş tutarınız: {durum_kebap_toplam} TL ")

else:
    print("Siparişinizi kontrol edip tekrar deneyiniz. Bugünkü menümüzden bir şey söylediğinize emin olunuz.")

