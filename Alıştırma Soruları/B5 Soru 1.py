menu = {"yemekler" : ["kebap" , "pide" , "lahmacun"],
        "içecekler" : ["ayran" , "su" , "kola"]}

siparis = []

while True:
   cevap = input("Yemeklere bakmak için 1, içeceklere bakmak için 2, siparişi sonlandırmak için 3'e basınız: ")

   if cevap == "1":
       print("Yemekler: " , menu["yemekler"])
       yemek_siparisi = input("Hangi yemeği yemek istediğinizi giriniz: ")
       siparis.append(yemek_siparisi)
       print("Yemek siparişiniz alındı.")
       if yemek_siparisi not in menu["yemekler"]:
           print("İstediğiniz yemek elimizde bulunmamaktadır.")
           siparis.remove(yemek_siparisi)

   elif cevap == "2":
       print("İçecekler: " , menu["içecekler"])
       icecek_siparisi = input("Hangi içeceği içmek istediğinizi giriniz: ")
       siparis.append(icecek_siparisi)
       print("İçecek siparişiniz alındı.")
       if icecek_siparisi not in menu["içecekler"]:
           print("İstediğiniz içecek elimizde bulunmamaktadır.")
           siparis.remove(icecek_siparisi)

   elif cevap == "3":
       print("Sipariş sonlandırıldı.")
       print("Siparişiniz: " , siparis)
       break
       

   else:
       print("Geçerli bir işlem giriniz.")
   continue



