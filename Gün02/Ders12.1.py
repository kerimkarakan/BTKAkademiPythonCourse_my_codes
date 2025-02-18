
gun = input("gün değeri giriniz:")

match gun:
    case 1 :
     print("pazartesi")
    case 2 :
     print("salı")
    case _: 
     print("hatalı gün girdiniz.")