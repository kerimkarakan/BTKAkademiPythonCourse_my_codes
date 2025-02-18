def ogrenciKarti(**kwargs): # keyword argümanı yaptık burda da yani dictionary gibi tanımlama yaptık
    print(kwargs)
    o_bilgileri = {**kwargs}
    print(o_bilgileri)
    pass

ogrenciKarti(oAdi="didem", oSoyadi="bozyel", oBolum="ekonometri")
