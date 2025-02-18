# otoyol hız radar sistemi yapıyoruz

yol = float(input("Kaç km yol gittiniz : "))
zaman = float(input("Kaç saat yol gittiniz : "))
hiz = yol/zaman

if hiz > 132 :
    print(f"{hiz-132} km/s kadar hız sınırını aştığınız için ceza yediniz")

else: 
    print("Kurallara uyduğunuz için tebrikler!")
