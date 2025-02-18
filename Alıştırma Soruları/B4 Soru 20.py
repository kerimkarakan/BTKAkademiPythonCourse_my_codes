# armstrong sayısı

sayi = int(input("Bir sayı giriniz: "))

str_sayi = str(sayi)

rakam_toplam = 0

for rakam in str_sayi:
    üss = int(rakam)**len(str_sayi)
    rakam_toplam += üss

if rakam_toplam == sayi:
    print(f"{sayi} bir armstrong sayısıdır.")

else:
     print(f"{sayi} bir armstrong sayısı değildir.")

