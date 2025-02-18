# tuple - demet işareti = (,) 
#tuple değiştirilemez (içine eleman eklenemez veya çıkarılamaz)

demet = (24, 8, 2.5, True, "Kerim", ["Kerim", "Karakan", "Sotware Eng."])
print(demet)
print(type(demet))
pazar = ["marul", "salatalık", "elma", "armut"]
pazardemeti = tuple(pazar)
print(pazardemeti)
print(demet.count(8))
print(demet.index("Kerim"))
for eleman in demet :
    print(eleman)

#eğer tuple da bir şey değiştirmek istersek onu önce listeye çevirip sonra değiştirebilirz ancak (sonra da geri tuple a çeviririz)

dlist = list(demet)
dlist[1] = "ahmet"
demet = tuple(dlist)
print(demet)

print(pazardemeti[0])
print(pazardemeti[-1])
print(pazardemeti[::-1])

# bunu kendim ekstra yazdım
print(pazardemeti[0:3:2])

