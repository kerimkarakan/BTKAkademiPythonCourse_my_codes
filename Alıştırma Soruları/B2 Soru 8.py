not_ortalamasi = int(input("Not ortalamanızı giriniz : "))

if not_ortalamasi >= 85 and not_ortalamasi <= 100:
    print("Tebrikler takdir belgesi almaya hak kazandınız!")

elif not_ortalamasi >= 70 and not_ortalamasi < 85 :
    print("Tebrikler teşekkür belgesi almaya hak kazandınız!")

elif not_ortalamasi < 70 and not_ortalamasi > 0:
    print("Maalesef hiçbir belge alamadanız.")

else:
    print("Geçersiz bir not girdiniz.")