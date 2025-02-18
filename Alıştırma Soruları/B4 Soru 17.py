from math import factorial

sayilar = []

for i in range(10):
    k_sayi = int(input(f"{i+1}. sayıyı giriniz: "))
    sayilar.append(k_sayi)
    if k_sayi <= -1:
        print("Negatif sayıların faktöriyel değerleri hesaplanamaz.")
        break

toplam = 0

for k_sayi in sayilar:

    toplam += factorial(k_sayi)

print(f"Girilen sayıların faktöriyellerinin toplamı: {toplam}")