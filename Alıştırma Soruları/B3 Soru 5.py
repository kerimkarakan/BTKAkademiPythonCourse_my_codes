katilma_kosulu1 = "erkek"
katilma_kosulu2 = 1.8
katilma_kosulu3 = 60

cevap1 = input("Cinsiyetinizi giriniz: ")
cevap2 = float(input("Boyunuzu metre cinsinden giriniz: : "))
cevap3 = int(input("Kilonuzu kilogram cinsinden giriniz: "))

if cevap1 == katilma_kosulu1 and cevap2 >= katilma_kosulu2 and cevap3 >= katilma_kosulu3:
    print("Turnuvaya katılmaya uygunsunuz.")

else:
    print("Turnuvaya katılmaya uygun değilsiniz.")