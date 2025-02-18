# import ornek01 #böyle kendi dosyalarımızı çağırabiliriz
#
# ortalamam = ornek01.sinifOrtalama(8,9,5,6)
# print(ortalamam)
# from ornek01 import sinifOrtalama
from .ornek01 import sinifOrtalama

print(sinifOrtalama(8,5,4,7))
