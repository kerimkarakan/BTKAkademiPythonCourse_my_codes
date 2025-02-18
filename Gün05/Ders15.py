class Fatura():
    baslik = "Halil Pazarlama"
    odeme = True

    def __init__(self, m_adi, v_no, tarih):
        self.m_adi = m_adi
        self.v_no = v_no
        self.tarih = tarih
        self.tutar = 0
        self.icerik = {}

    def urunEkle(self):
        urun_ad = input("ürün bilgisi giriniz: ")
        urun_fiyati = int(input(f"{urun_ad} fiyatını giriniz: "))
        urun_adet = int(input(f"{urun_ad} adet bilgisi giriniz: "))
        urun_tutar = urun_adet * urun_fiyati
        self.tutar += urun_tutar
        self.icerik[urun_ad] = [urun_ad,urun_adet, urun_fiyati,urun_tutar]
        print(self.icerik[urun_ad], " ürünü sepete eklendi.")
        return self.tutar

    def urunCikar(self):
        urun_ad = input("çıkartmak için ürün bilgisi giriniz: ")
        # urun_adet = int(input(f"{urun_ad} adet bilgisi"))
        urun_tutar = self.icerik[urun_ad][3]
        self.tutar -= urun_tutar
        print(self.icerik[urun_ad], " ürünü sepetten çıkartıldı")
        self.icerik.pop(urun_ad)
        return self.tutar

    def faturaTutari(self):
        print("güncel fatura tutari: ",self.tutar)
        return self.tutar


    def __str__(self):
        return self.m_adi+" adlı müşterinin faturası."


musteri = Fatura("hamza","1452","bugün")

while True:
    cevap = int(input("Ürün ekle : 1 \t "
                      "Ürün çıkar: 2\n"
                      "Fatura tutarı göster: 3\t, "
                     ))
    if cevap == 1:
        musteri.urunEkle()
    elif cevap == 2:
        musteri.urunCikar()
    elif cevap == 3:
        musteri.faturaTutari()
    else:
        print("hatalı işlem girişi")



