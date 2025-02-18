# temel string yani karakter dizisi işlemleri 
# "len" komutu almış olduğu verinin içerisinde kaç eleman olduğunu bize veriyor

ad = "besteakıllılar"
print(len(ad))

print(ad[0]) # ad[x] x index değerini döndürür

print(ad[-1]) # soldan sağa 1,2,3.. sağdan sola-1,-2,-2.. diye gidiyor

print(ad[4] , ad[-2]) 

print(ad[0:5]) # sayıların arasında iki nokta koyduğumzda bize 0 dan 5 e kadar olan karakterleri verir mesela
print(ad[:5])
print(ad[-9:])

print(ad[:])

print(ad[::2]) # ad[baş,bitiş,artış] baştan sona atlayarak verir yazdığımız artışa göre

print(ad[::-1])

print(ad[3:8:2])
print(ad[-8:-3:2])

#bu şekilde de içinde b olup olmaığını kontrol edebiliyoruz : 

print("b" in ad)
print("bes" in ad)
print("besk" in ad)

