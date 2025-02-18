def selamla(isim): #def bir fonksiyon tanımlamamızı sağlar
    print("selamlar" , isim)
    return True # burda True ya da False yazmak zorunda değiliz istediğimizi döndürebiliriz

isim = input("adınız nedir")
a = selamla(isim)  # a = selamla() dediğimizde bize kimi selamladığını da söylüyor burda
print("selamlama işlemi", a)