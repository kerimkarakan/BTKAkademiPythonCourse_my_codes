# yemek sipariş uygulaması 3

yemek = input("Yemek bilgisi giriniz: ")

if yemek == "pide" :
    icecek = input("İçecek bilgisi giriniz : ")
    if icecek == "ayran" :
     print("Sipariş bilgisi doğru!")

    else: 
           print("Yemek doğru içecek yanlış.")

else:
    print("Sipariş bilgisi yanlış.")


