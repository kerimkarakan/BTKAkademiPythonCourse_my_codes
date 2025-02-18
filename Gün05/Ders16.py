class Urun():
    def __init__(self):
        self.urun_ad = input("ürün bilgisi giriniz: ")
        self.urun_fiyati = int(input(f"{self.urun_ad} fiyatını giriniz: "))
        self.urun_adet = int(input(f"{self.urun_ad} adet bilgisi giriniz: "))
        self.urun_tutar = self.urun_adet * self.urun_fiyati

    def adetArttir(self):
        pass
    def adetAzalt(self):
        pass
    def __repr__(self):
        return f"{self.urun_ad}"
    
    # def __str__(self):
    #     return (self.urun_ad,self.urun_tutar)

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
        urun = Urun()
        self.tutar += urun.urun_tutar
        self.icerik[urun.urun_ad] = urun
        print(self.icerik[urun.urun_ad], " ürünü sepete eklendi.")
        return self.tutar

    def urunCikar(self):
        urun_ad = input("çıkartmak için ürün bilgisi giriniz: ")
        urun = self.icerik[urun_ad]
        self.tutar -= urun.urun_tutar
        print(self.icerik[urun_ad], " ürünü sepetten çıkartıldı.")
        self.icerik.pop(urun_ad)
        return self.tutar

    def faturaTutari(self):
        print("güncel fatura tutari: ",self.tutar)
        return self.tutar

    def __str__(self):
        return self.m_adi+"adlı müşterinin faturası."

musteri = Fatura("hamza","1452","bugün")

while True:
    cevap = int(input("ürün ekle 1\t ürün çıkart: 2\t tutar göster : 3\t"))
    if cevap == 1:
        musteri.urunEkle()
    elif cevap == 2:
        musteri.urunCikar()
    elif cevap == 3:
        musteri.faturaTutari()
    else:
        print("hatalı işlem girişi")


