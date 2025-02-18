# dosyalar (dosyaları okuma, içine yazma, içine ekleme yapma veya dosya oluşturma)

dosya = open("deneme.txt")
# print(dosya.read())
#print(dosya.read(10)) #kaç karakter okuyacağını belirleyebiliriz böyle
#print(dosya.readline())
#print(dosya.readline())
#satirlar = dosya.readlines()
#print(satirlar)
#for satir in satirlar:
#    print(satir, end="")
okuma1 = dosya.read()
print(okuma1)
okuma2 = dosya.read()
print(okuma2)

#dosyayı kapatmak için :
dosya.close()
