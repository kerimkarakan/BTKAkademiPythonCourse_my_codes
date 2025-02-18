# kullanıcının sayısı 0 ile 100 arasında değilse bunu tahmin edip hatayı söyleyebiliriz ama k_ sayi not in range(100) ile olmadı bu
sayimiz = 78

while True:
    k_sayi = int(input("0 ile 100 arasında bir sayı giriniz: "))
    if k_sayi < sayimiz:
        print("Daha büyük bir sayı giriniz")
        continue
    elif k_sayi > sayimiz:
        print("Daha küçük bir sayı giriniz.")
        continue
    elif k_sayi not in range(100):
        print("Girdiğiniz sayı 0 ile 100 arasında değildir. Lütfen doğru bir sayı girip tekrar deneyiniz.")
        continue
    elif k_sayi == sayimiz:
        print("Tebrikler oyunu kazandınız.")
        break

