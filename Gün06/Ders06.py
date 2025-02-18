try:
    a = int(input("Enter a number: "))
    print(a)
    #k = a/0
    z= "q"/"w"
except ValueError:
    print("Hatalı veri girdiniz.")
except ZeroDivisionError:
    print("Hata olarak 0 a bölme var uygulamada.")
except Exception as e: #hatayı altta yazdırmak için e harfine tanımladık hatayı(herhangi bir şey olabilir e yerine)
    print("Aldığınız hata: ", e)

