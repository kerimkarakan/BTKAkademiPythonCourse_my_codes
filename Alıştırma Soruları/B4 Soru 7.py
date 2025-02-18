# the issue with this code is that it only checks if the password is the same as itself, rather than checking if the two passwords entered by the user are the same.
for i in range(2):
    sifre = input("Sisteme giriş yapmak için 2 kere aynı şifreyi giriniz: ")

if sifre == sifre:
    print("Sisteme başarıyla giriş yapıldı.")

else: 
    print("Sisteme giriş yapabilmek için 2 kere aynı şifreyi girmeniz gerekmektedir.")

# versiyon 1
    
sifreler = []
print("Sisteme giriş yapabilmeniz için 2 kere aynı şifreyi girmeniz gerekmektedir.")

for i in range(2):
    sifre = input(f"{i+1}. şifreyi giriniz: ")
    sifreler.append(sifre)

if sifreler[0] == sifreler[1]:
    print("Sisteme başarıyla giriş yapıldı.")

else:
    print("Şifreleri kontrol edip tekrar deneyiniz.")

# versiyon 2

print("Sisteme giriş yapabilmeniz için 2 kere aynı şifreyi girmeniz gerekmektedir.")

for i in range(2):
    sifre = input(f"{i+1}. şifreyi giriniz: ")

    if i == 0:
        ilk_sifre = sifre

    elif i == 1:
        ikinci_sifre = sifre

if ilk_sifre == ikinci_sifre:
    print("Sisteme başarıyla giriş yapıldı.")

else:
    print("Şifrelerinizi kontrol edip tekrar deneyiniz.")

