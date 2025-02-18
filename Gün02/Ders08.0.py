# teşekkür takdir alma programı

# burda iç içe yazıyoruz yani bir koşul gerçekleşmediğinde diğer koşula bakıyoruz o da gerçekleşmediğinde diğer koşula bakıyoruz
puan = int(input("Ortalamanızı giriniz : "))

if puan < 70 :
    print("Belge alamazsınız.")
else:
    if puan < 85 :
        print("Teşekkür belgesi almaya hak kazandınız!")

    else:
        if puan <= 100 :
            print("Takdir belgesi almaya hak kazandınız!")

        else: 
            print("Geçerli bir not girmediniz.")

    