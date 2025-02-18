yol = float(input("Kaç km yol gittiğinizi giriniz : "))
sure = float(input("Bu yolu ne kadar sürede gittiğinizi giriniz :"))
hiz = yol/sure

if hiz > 143.0 :
    print(f"{hiz} km/s hızla gittiğiniz için ceza yediniz.")

else:
    print("Hız kurallarına uygduğunuz için teşekkürler.")



