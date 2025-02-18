# bilgisayarda pencere açma

from tkinter import * # tkinter bir arayüz kütüphanesi

def yazdir():
    print("Buton tıklandı.")

pencere = Tk()
pencere.geometry('400x300') # bu pencerenin büyüklüğünü gösteriyor
pencere.title("BTK Akademi Python Kursu")
buton1 = Button(text="Buton bir" , fg="black", bg="blue" , command=yazdir)
buton2 = Button(text="Buton iki" , fg="red", bg="blue")
buton3 = Button(text="Buton üç" , fg="red", bg="blue")

buton1.pack(side=LEFT)
buton2.pack() # pack ile butonu ekliyoruz
buton3.pack(side=RIGHT)

yazi = Label(pencere, text="Merhaba BTK öğrencileri" , font=("Arial" , 15))
yazi.pack()

pencere.mainloop() # bu sürekli ekranda gösteriyor pencereyi





