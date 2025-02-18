# Hata ayıklama (try,except,else,finally)
# bunları hata olabileceğini düşündüğümüz yerlerde kullanırız (özellikle kullanıcıdan bir veri alıyorsak)
try:
    a = int(input("Enter a number: "))
except:
    print("Hata var.")
else:
    print("Değer atama işlemi başarılı.")
finally:
    print("Ben de çalıştım.")