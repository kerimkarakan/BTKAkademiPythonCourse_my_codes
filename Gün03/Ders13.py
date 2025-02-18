# dictionary - sözlük  işareti = {key:value}

treng = {"araba" : "car", "kalem" : "pencil" , "cam" : "glass"}
print(treng)
print(type(treng))
print(treng["araba"])
print(treng.keys())
print(treng.values())
print(treng.items())

for k in treng : 
    print(k , end="\t")
    print(treng[k])

for key, value in treng.items():
    print(key, value, sep= " = ")

#yukarıdakini böyle de yapabiliriz :
for dd in treng:
    print(dd, treng[dd])
    print(dd, "*", treng.get(dd))




