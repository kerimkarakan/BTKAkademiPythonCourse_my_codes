ad= "Kerim"
sifre ="123"

kullanici_adi = input("Kullanıcı adınızı giriniz: ")
kullanici_sifre = input("Şifrenizi giriniz: ")

if kullanici_adi == ad and kullanici_sifre == sifre:
    print(f"Kullanıcı adı ve şifre doğru. \nHoşgeldin {kullanici_adi} ")
else:
    print("Kullanıcı adı veya şifre hatalı. Doğru bilgileri girdiğinizden emin olunuz.")

