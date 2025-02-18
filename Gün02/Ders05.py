# ehliyet alma programı yapıyoruz

#benim yaptığım :

dogum_yili = int(input("Doğum yılınızı giriniz:"))

if dogum_yili <= 2006 : 
    print("Ehliyet alabilirsiniz!")

else: 
    print("Ehliyet alamazsınız.")


# hocanın yaptığı :

d_yili = int(input("Doğum yılınızı giriniz: "))
yas = 2024 - d_yili
if yas >= 18 :
    print("Ehliyet alabilirsiniz!")

else:
    print("Ehliyet alamzasınız.")
    print(f"Ehliyet alamzasınız {yas} yaşındasınız.") # "f string" parantezin içine değişken koyabilmemizi sağlıyor
    print(f"{18-yas} yıl kadar daha beklemeniz gerekmektedir.")


