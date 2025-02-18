meyve = ["elma", "armut", "karpuz", "erik", "çilek"]

meyve.append("üzüm") #append listeye sonradan ibr şey ekleme işini görür
print(meyve)
print(meyve.count("üzüm"))#count içine yazdığımız şeyden listede kaç tane var onu söyler
print(meyve.index("armut"))
meyve.insert(1,"kavun")
print(meyve)
meyve[3] = "kara üzüm"
print(meyve)
meyve.sort()
print(meyve)
meyve.reverse()
print(meyve)
liste2 = ["şeftali", "muz"]
meyve.extend(liste2)
print(meyve)
liste3 = ["canerik", "muşmula"]
meyve.append()
print(meyve)
meyve.pop()
print(meyve)
meyve.pop(2)
print(meyve)
meyve.remove("erik")
print(meyve)
meyve.clear()
print(meyve)
del meyve
print(meyve)


