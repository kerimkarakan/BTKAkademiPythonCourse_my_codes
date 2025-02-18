# koşullu ifadeler için if yapısı kullanılır
# koşullu ifadeler yani if True değerini arar

ad = input("adınızı giriniz : ")
if ad == "Kerim" :
    print("Adaşız seninle!")

# aşağıdakinin ikiside aynı şeyi söylüyor
if not (ad == "Kerim") :
    print("adaş değiliz")

if ad != "Kerim" :
    print("adaş değiliz")


