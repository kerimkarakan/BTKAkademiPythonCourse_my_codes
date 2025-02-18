def selamla(): #def bir fonksiyon tanımlamamızı sağlar
    isim = input("adınız nedir")
    print("selamlar" , isim)
    return isim

selamla()
a = selamla()  # a = selamla() dediğimizde bize kimi selamladığını da söylüyor burda
print(a , "selamlandı")

