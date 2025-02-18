tek_sayilar = []
cift_sayilar = []

for i in range(20):
    ksayilar = int(input(f"{i+1}. sayıyı giriniz: "))
    
    if ksayilar % 2 != 0:
        tek_sayilar.append(ksayilar)

    elif ksayilar % 2 == 0:
        cift_sayilar.append(ksayilar)

teksayilar_ortalama = sum(tek_sayilar) / len(tek_sayilar)
ciftsayilar_ortalama = sum(cift_sayilar) / len(cift_sayilar)

print(f"Girdiğiniz tek sayıların ortalaması: {teksayilar_ortalama}")
print(f"Girdiğiniz çift sayıların ortalaması: {ciftsayilar_ortalama}")

