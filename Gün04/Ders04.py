#sayı tahmin oyunumuzu bilgisayarın veridiği random bir değere göre yeniden düzenleyelim

# benim yaptığım (hepsi değil) :

import random
sayi = random.randint(0,100)
taban = 0
tavan = 100
gecerli = []
gecersiz = []
tahminler = {"gecerli":gecerli,"gecersiz":gecersiz}
print(f"Tahmin edeceğiniz sayı {taban} - {tavan} aralığındadır")
tahmin = int(input("Bir sayı giriniz"))
while True:
    if taban <= tahmin <= tavan:
        print(f"Tahmin geçerli aralıkta")
        gecerli.append(tahmin)
        break
    else:
        print(f"Tahmin aralığı dışında geçersiz tahmin")
        print(f"Tahmin edeceğiniz sayı {taban} - {tavan} aralığındadır")
        gecersiz.append(tahmin)
        tahmin = int(input("Bir sayı giriniz"))
while tahmin != sayi:
    if tahmin > sayi:
        print("Tahmin Başarısız Keşke küçük bir sayı söyleseydin")
        tavan = tahmin
    elif tahmin < sayi:
        print("Tahmin Başarısız Keşke büyük bir sayı söyleseydin")
        taban = tahmin
    while True:
        if taban < tahmin < tavan:
            print(f"Tahmin geçerli aralıkta")
            gecerli.append(tahmin)
            break
        else:
            print(f"Tahmin aralığı dışında geçersiz tahmin")
            print(f"Tahmin edeceğiniz sayı {taban} - {tavan} aralığındadır")
            gecersiz.append(tahmin)
            tahmin = int(input("Bir sayı giriniz"))
else:
    print("Tahmin Başarılı tebrikler")
print(tahminler)
print(len(gecerli+gecersiz)," kerede bildiniz")


#hocanın yaptığı : 

import random
rastgele = random.randrange(1,1000)
# print("tutulan sayı",rastgele)
tahminSayisi = 10
taban = 0
tavan = 1001
while tahminSayisi >= 1:
    tahmin =random.randrange(taban,tavan)
    # tahmin =int(input("sayı giriniz"))
    print(tahmin , end=" ")
    cevap = input("+,-,=")
    if cevap == "=":
        print("Tebrikler")
        break
    elif cevap == "+" :
        print("daha küçük")
        tavan = tahmin
    elif cevap == "-":
        print("daha büyük")
        taban = tahmin
    tahminSayisi -= 1
    print("kalan hakkınız", tahminSayisi)

#versiyon 2
# import random
# rastgele = random.randrange(1,1000)
# print("tutulan sayı",rastgele)
# tahminSayisi = 10
# taban = 0
# tavan = 1001
# while tahminSayisi >= 1:
#     tahmin =random.randrange(taban,tavan)
#     print(tahmin , end=" ")
#     if tahmin == rastgele:
#         print("Tebrikler")
#         break
#     elif tahmin > rastgele:
#         tavan = tahmin
#     elif tahmin < rastgele:
#         taban = tahmin
#     tahminSayisi -= 1
#     print("kalan hakkınız", tahminSayisi)