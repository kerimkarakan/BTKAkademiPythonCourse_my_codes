
gun = input("gün değeri giriniz:")

match gun:
    case "pazartesi":
     print("birinci gün")
    case "salı":
     print("ikinci gün")
    case _: 
     print("hatalı gün girdiniz.")