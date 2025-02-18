# birbirini çaiıran fonksiyonlar 

def birinci():
    print("Birinci çalıştı.")
    return ikinci()

def ikinci():
    print("İkinci çalıştı.")
    return ucuncu()

def ucuncu():
    print("Üçüncü çalıştı.")
    return 3 

if __name__ == '__main__':
    print("hello world")
    a = birinci()
    print(a)
    