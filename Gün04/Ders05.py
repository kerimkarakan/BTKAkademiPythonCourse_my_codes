# time kütüphanesi

# import time
# print("Merhaba dünya")
# time.sleep(5) # bu şekilde 5 saniye bekler
# print("Sana da merhaba")

import datetime
a = input("birinci giris")
giris = datetime.datetime.now()
print(giris)
giris2 = datetime.datetime.now()
b = input("ikinci giris")
fark = giris2 - giris
print(fark)
print(fark.total_seconds())

