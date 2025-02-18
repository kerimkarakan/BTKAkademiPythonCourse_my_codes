import random

kazanma_durumu = [random.randint(0,9) for sayi in range(3)]

tahmin_sayisi = 5

print("Tahmin edeceğiniz sayılar 0 ile 9 arasındadır \nToplamda 5 hakkınız vardır.")

while tahmin_sayisi > 0 :
    print(f"{tahmin_sayisi} hakkınız kaldı.")
    tahmin_sayisi -= 1
    kullanici_tahmini = [int(input(f"{i+1} . sayıyı giriniz: ")) for i in range(3)]

    if kullanici_tahmini == kazanma_durumu:
      print("Tebrikler oyunu kazandınız!")
      break

else:
    print("Tekrar deneyiniz.")
    print(f"Şanslı sayılar bunlardı : {kazanma_durumu}")

