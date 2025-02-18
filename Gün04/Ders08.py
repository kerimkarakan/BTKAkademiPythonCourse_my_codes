import os
import time

dosya_adi = "deneme.txt"
with open(dosya_adi, "a") as dosya: # "a" write komutu
    dosya.write("esma")
with open(dosya_adi, "r") as dosya: # "r" read komutu
    print(dosya.read())

dosya_adi2 = "deneme2.txt"
if not(os.path.isfile(dosya_adi2)):
    dosya = open(dosya_adi2, "x") # "x" create komutu
    print("dosya oluşturuldu")
    dosya.close()
else:
    print("oluşturmak istediğiniz dosya mevcut")

# dosyayı silmek veya olup olmadığını kontrol etmek için import os dememiz gerekiyor (yani işletim sistemini kullanmamız lazım)

time.sleep(5)
if os.path.exists(dosya_adi2):
  os.remove(dosya_adi2)
  print("dosya silindi")
else:
  print("The file does not exist")

