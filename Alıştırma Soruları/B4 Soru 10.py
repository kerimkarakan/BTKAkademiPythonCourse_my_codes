kare_olcu1 = int(input("Bir dikdörtgen oluşturmak için 1. kenar değerini giriniz: "))
kare_olcu2 = int(input("Bir dikdörtgen oluşturmak için 2. kenar değerini giriniz: "))

for i in range(kare_olcu1):
    for k in range(kare_olcu2):
        print("*" , end = " ")
    print()