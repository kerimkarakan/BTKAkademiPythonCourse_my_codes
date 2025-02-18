print("10 tane sayı giriniz.")

sayilar = []

for i in range(10):
    ksayilar = int(input(f"{i+1}. sayıyı giriniz: "))
    sayilar.append(ksayilar)

sayilarin_toplami = sum(sayilar)
sayilarin_bolumu = sum(sayilar) / len(sayilar)

print(f"Girdiğiniz sayıların toplamı: {sayilarin_toplami}")
print(f"Girdiğiniz sayıların bölümü: {sayilarin_bolumu}")