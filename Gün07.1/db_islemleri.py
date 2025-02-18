# bu kodlarla veritabanına bağlanığp çeşitli işlemler yapıyoruz
from orm_db import *

Base.metadata.bind = engine # bind bağlanmaya yarıyormuş
DBSession = sessionmaker(bind=engine)
session = DBSession()

def birimListele():
    birimler = session.query(Birim).all() # oturum üzerinden sorgu yapıp tüm verileri bize getirecek bu kod
    for birim in birimler:
        print(birim.birim_id, birim.birim_adi)
    return birimler

def birimEkle():
    birimadi = input("bir birim adi giriniz")
    yeniBirim = Birim(birim_adi=birimadi)
    session.add(yeniBirim) # bu şekilde birimi ekliyoruz
    session.commit() # bu ekleme işlemini onaylıyoruz session.commit ile

def birimGuncelle():
    birimListele()
    birimid = int(input("Güncellemek istediğiniz birimin idsi giriniz"))
    birim = session.query(Birim).filter(Birim.birim_id == birimid).first() # burda bir filtreleme yaptık 
    yeni_birim_adi = input("Yeni birim adini giriniz")
    birim.birim_adi = yeni_birim_adi
    session.commit()
    return birimListele()

def birimSil():
    birimListele()
    birimid = int(input("Silmek istediğiniz birimin idsi giriniz"))
    birim = session.query(Birim).filter(Birim.birim_id == birimid).delete()
    session.commit()
    return birimListele()


birimEkle()
birimSil()

