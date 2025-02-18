kizlar = ["ayşe" , "fatma", "hayriye"]
erkekler = ["ali", "veli", "can"]
liste1 = [kizlar, erkekler]

#for dd in liste1 :
    #for kişi in dd:
        #print(dd, kişi)
for kiz, erkek in zip(kizlar, erkekler): #zip yaptığımızda eşleştirebiliyoruz
    print(kiz, erkek)
