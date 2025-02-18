sebze = ['domates' , 'biber']
meyve = ['domates' , 'çilek' , 'kivi' , 'karpuz' , 'incir' , 'ayva' , 'armut']
sark = ["peynir" , "helva" , "bal"]
yesillik = ["roka" , "maydanoz" , "tere"]

#pazar_listesi = sebze + meyve + sark + yesillik
#print(pazar_listesi)
#print(len(pazar_listesi))

pazar_listesi = [sebze, meyve , sark , yesillik]
#print(len(pazar_listesi))
#print(pazar_listesi[0])
#print(pazar_listesi[0][0]) # [0] [0] dediğimizde 1 inci grubun içindeki 1 inci sebzenin ismini verir
#print(pazar_listesi[3][1])

for x in range(len(pazar_listesi)) : 
    print(x+1 , ". kategorisi : " , pazar_listesi[x])
    #for y in range(len(pazar_listesi[x])) :
        #print(x+1 , y+1 , "ürünü\t" , pazar_listesi[x][y])
    for index, urun in enumerate(pazar_listesi[x]):
        print(index+1, urun)

    


