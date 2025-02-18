gunler = "Pazartesi" , "Salı" , "Çarşamba" , "Perşembe" , "Cuma" , "Cumartesi" , "Pazar" 
mahalleler = "a" , "b" , "c" , "d" , "e" , "f" , "g"

pazarlamaci_gun = input("Günlerden hangi gün giriniz: ")

if pazarlamaci_gun in gunler and pazarlamaci_gun == "Pazartesi":
    print("Bugün a mahallesine gideceksin.")
elif pazarlamaci_gun in gunler and pazarlamaci_gun == "Salı":
    print("Bugün b mahallesine gideceksin.")
elif pazarlamaci_gun in gunler and pazarlamaci_gun == "Çarşamba":
    print("Bugün c mahallesine gideceksin.")
elif pazarlamaci_gun in gunler and pazarlamaci_gun == "Perşembe":
    print("Bugün d mahallesine gideceksin.")
elif pazarlamaci_gun in gunler and pazarlamaci_gun == "Cuma":
    print("Bugün e mahallesine gideceksin.")
elif pazarlamaci_gun in gunler and pazarlamaci_gun == "Cumartesi":
    print("Bugün f mahallesine gideceksin.")
elif pazarlamaci_gun in gunler and pazarlamaci_gun == "Pazar":
    print("Bugün g mahallesine gideceksin.")

else:
    print("Gün bilgisini doğru girdiğinizden emin olunuz.")
