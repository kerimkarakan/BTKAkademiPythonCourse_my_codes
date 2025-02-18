#bir tane sınıfın ortalamasını bulacak fonk yazıyoruz

def sinifOrtalama(*args):
    toplam = 0
    for arg in [*args]:
        toplam += arg
    ortalama = toplam / len(args)
    return ortalama

if __name__ == '__main__': #bunu bu dosya buradan başka yerde çalışmasın diye yaptık
    print(sinifOrtalama(1,5,9,6,7,4))


