print("Pi'nin değeri nedir?")
pi_degeri = int(input())
print("Dairenin yarı çap değeri nedir?")
yaricap = int(input())
print("Bu dairenin alanı : " , pi_degeri*(yaricap**2))



#hocanın yaptığı böyle:

r = float(input("bir yarıçap değeri giriniz: \t"))
pi = float(input("hesaplama için pi değerini giriniz: \t"))
alan = pi * (r**2)
cevre = 2 * pi * r
print(r, "yarı çaplı dairenin alanı : " , alan , "çevresi:" , cevre)

