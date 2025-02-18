# teşekkür takdir alma uygulamasının "elif" ile yapılışı

puan = int(input("Ortalamanızı giriniz : "))

if puan < 70 :
    print("Belge alamazsınız.")
elif puan < 85 :
    print("Teşekkür belgesi almaya hak kazandınız!")
elif puan <= 100 :
    print("Takdir belgesi almaya hak kazandınız!")
else: 
    print("Geçerli bir not girmediniz.")

# "elif" else ve if in birleşimidir ve eğer değilse anlamında kullanılır

