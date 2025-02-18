ogrenci_not1 = float(input("1. notunuzu giriniz: "))
ogrenci_not2 = float(input("2. notunuzu giriniz: "))
ogrenci_not3 = float(input("3. notunuzu giriniz: "))

not_ortalamasi = (ogrenci_not1 + ogrenci_not2 + ogrenci_not3) / 3

if 100.0 > not_ortalamasi >=50.0:
    print(f"Not ortalamaniz: {not_ortalamasi} \nTebrikler dersi geçtinz!")
elif 0 < not_ortalamasi < 50.0:
    print(f"Not ortalamaniz {not_ortalamasi} olduğundan dolayı dersten kaldınız.")
else:
    print("Geçerli bir not girdiğinizden emin olunuz.")


