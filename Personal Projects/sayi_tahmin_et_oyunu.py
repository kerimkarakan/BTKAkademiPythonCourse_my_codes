import random

sayimiz = random.randint(0,10)
print("5 tahmin hakkınız vardır.")
print("Tahmin edeceğiniz sayı 0 ile 10 arasındadır.")

tahmin_sayisi = 5

while tahmin_sayisi > 0 :
    tahmin_sayisi -= 1
    print(f"{tahmin_sayisi+1} hakkınız kaldı")
    tahmin = int(input("Tahmininizi giriniz: "))

    if tahmin == sayimiz:
        print("Tebrikler oyunu kazandınız!")
        break

else: 
    print("Tekrar deneyiniz.")
    print(f"Şanslı sayı buydu : {sayimiz}")
