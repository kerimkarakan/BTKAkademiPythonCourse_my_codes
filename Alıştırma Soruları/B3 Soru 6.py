yiyecekler = "Hamburger" , "Dürüm" , "Döner" 
icecekler = "Kola" , "Ayran" , "Soda"

menu = yiyecekler + icecekler

print(f"Restorantımıza hoşgeldiniz.\nMenümüzde yiyecek olarak bunlar bulunmaktadır: {yiyecekler} \nİçecek olarak ise bunlar bulunmaktadır: {icecekler}")

cevapye = input("Sipariş vermek istediğiniz yiyeceği giriniz: ")
cevapic = input("Sipariş vermek istediğiniz içeceği giriniz: ")

siparis = cevapye + cevapic

if cevapye in yiyecekler and cevapic in icecekler and siparis == cevapye + cevapic:
    print("Siparişiniz doğru. \nAfiyet olsun!")
else:
    print("Girdiğiniz içecek veya yiyecek bilgisi yanlıştır. Lütfen menümüzde olan yiyecek veya içeceklerden birisini sipariş ettiğinizden emin olunuz.")


    
