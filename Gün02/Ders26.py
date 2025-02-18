if True :
    pass
print("hello")

for dd in range(20) :
    if dd == 15:
        break
    print(dd)

for dd in range(20):
    ad = input("adınızı giriniz")
    if ad == "kerim":
        print("kerim bulundu")
        break
    print(dd)

for dd in range(20):
    ad = input("adınızı giriniz:")
    if ad == "can":
        print("can ile kayıt yapamaz.")
        continue
    soyad = input("soyadınızı giriniz:")
    print(ad, soyad, "kaydınız tamamlandı")



