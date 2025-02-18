sayi1 = int(input("1. sayıyı giriniz: "))
sayi2 = int(input("2. sayıyı giriniz: "))

if sayi1 > sayi2:
    print(f"Büyük olan sayı: {sayi1} \nKüçük olan sayi: {sayi2}")
elif sayi2 > sayi1:
    print(f"Büyük olan sayı: {sayi2} \nKüçük olan sayi: {sayi1}")

else:
    print("Sayılar birbirinden küçük veya büyük olmalıdır.")


