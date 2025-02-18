# burda belki İlkokul Ortaokul Lise ve Üniversitenin büyüklük sıralarını bilgisyara anlatıp ordan arka planda kendisinin hesaplamasını sağlayabiliriz ama bu şekilde de olu
yas_bilgisi = int(input("Yaşınızı giriniz: "))

egitim_bilgisi = input("Eğitim bilgisi giriniz (İlkokul, Ortaokul, Lise, Üniversite): ")

if yas_bilgisi >= 18 and egitim_bilgisi == "Lise":
    print("Ehliyet almaya uygunsunuz.")

elif yas_bilgisi >= 18 and egitim_bilgisi == "Üniversite":
    print("Ehliyet almaya uygunsunuz.") 

elif 0 < yas_bilgisi <= 18 and egitim_bilgisi == "Lise":
    print("Maalesef ehliyet almaya uygun değilsiniz.")

elif 0 < yas_bilgisi <= 18 and egitim_bilgisi == "İlkokul":
    print("Maalesef ehliyet almaya uygun değilsiniz.")

elif 0 < yas_bilgisi <= 18 and egitim_bilgisi == "Ortaokul":
    print("Maalesef ehliyet almaya uygun değilsiniz.")

else:
    print("Bilgilerinizi doğru giriniz.")














