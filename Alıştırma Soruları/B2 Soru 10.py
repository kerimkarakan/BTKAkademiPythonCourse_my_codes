gunluk_ucret = 350

calisma_gunu = int(input("Kaç gün çalıştığınızı giriniz : "))

if calisma_gunu < 0 :
    print("Hatalı gün sayısı girdiniz.")
    
else: 
    print("Çalıştığınız güne göre kazancınız : " , gunluk_ucret*calisma_gunu)

