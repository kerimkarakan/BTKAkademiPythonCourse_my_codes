# iç içe listeler, çok boyutlu listeler

sebze = ['domates' , 'biber']
meyve = ['domates' , 'çilek' , 'kivi' , 'karpuz' , 'incir' , 'ayva' , 'armut']
sark = ["peynir" , "helva" , "bal"]
yesillik = ["roka" , "maydanoz" , "tere"]

#pazar_listesi = sebze + meyve + sark + yesillik
#print(pazar_listesi)
#print(len(pazar_listesi))

pazar_listesi = [sebze, meyve , sark , yesillik , "baklava"]
print(len(pazar_listesi))
print(pazar_listesi[0])
print(pazar_listesi[0][0]) # [0] [0] dediğimizde 1 inci grubun içindeki 1 inci sebzenin ismini verir
print(pazar_listesi[3][1])

for kategori in pazar_listesi : 
    print(kategori)
    if type(kategori) == list: # burda eğer tipi kategoriyse alttakine geç diyoruz bu sayede listeye istediğimizi ekleyebiliriz(baklava gibi)
    #üsttekinin yerine şöyle de yazarız : if type(kategori) != list
     for urun in kategori :
        print(urun)



