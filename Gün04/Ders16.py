# default parametreli fonksiyonlar

# def kare(a=5):
#    return a*a
#print(kare(4))

# biz a ya definition ederken değer versek bile bizim print ederken verdiğimiz değere göre çalışır

#def daireAlan(r= 1, pi= 3.14):
#    alan = pi * r * r
#    return alan
#alan = daireAlan(5,3)
#print(alan)

def silindirHacim(r=1, h=1, pi=3.14):
    hacim = pi * r * r * h
    return hacim 

hacim = silindirHacim(5,3.15)
print(hacim)
