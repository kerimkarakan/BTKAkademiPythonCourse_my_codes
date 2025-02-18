isaret = "@"
com = ".com"


isaret_com = isaret + com

kmail_adresi = input("Mail adresinizi giriniz: ")

if isaret_com not in kmail_adresi:
    print("Girdiğiniz mail adresi hatalı. Lütfen doğru bir mail adresi girdiğinizden emin olunuz.")
else:
    print("Girdiğiniz mail adresi doğru.")


