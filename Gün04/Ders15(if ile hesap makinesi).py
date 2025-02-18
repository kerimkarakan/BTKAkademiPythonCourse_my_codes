# bunu ben kendim if e çevirdim match case ile yaptığımız kısımları (burda bir hata var ama bir bak ona)
# 2 basamaklı bir sayıyla işlem yaptığımda (yanlış işlem girdiniz...) mesajını da veriyor

def toplama(a,b):
    return a+b

def cikartma(a,b):
    return a-b

def carpma(a,b):
    return a*b

def karsilama():
    islem = input("Yapmak istediğiniz işlemi giriniz(+, -, *): ")
    sayi1 = int(input("1. sayı: "))
    sayi2 = int(input("2. sayı: "))
    if islem == "+":
        print(toplama(sayi1,sayi2))
    if islem == "-":
        print(cikartma(sayi1,sayi2))
    if islem == "*":
        print(carpma(sayi1,sayi2))
    else:
        print("Yanlış işlem girdiniz. Lütfen doğru bir işlem giriniz.")
     


if __name__=="__main__":
    karsilama()