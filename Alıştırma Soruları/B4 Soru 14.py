sayimiz = 56

while True:
    k_sayi = int(input("0 ile 100 arasında bir sayı giriniz: "))
    if k_sayi != sayimiz:
        print("Lütfen tekrar deneyiniz.")
        continue
    elif k_sayi == sayimiz:
        print("Tebrikler oyunu kazandınız!")
        break
