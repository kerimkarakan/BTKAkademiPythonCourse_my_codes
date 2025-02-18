programlama_dilleri = "java" , "python" ,  "swift" 

print(f"Geçerli programlama dilleri bunlardır: {programlama_dilleri}")

kullanicinin_sevdigi_dil = input("Hangi programlama dilini seviyorsunuz (1 tane giriniz): ")

if kullanicinin_sevdigi_dil in programlama_dilleri and kullanicinin_sevdigi_dil == "java":
    print("Ahmet ve mehmet de java dilini yazıyor!")

elif kullanicinin_sevdigi_dil in programlama_dilleri and kullanicinin_sevdigi_dil == "python":
    print("Ali ve veli de python dilini yazıyor!")

elif kullanicinin_sevdigi_dil in programlama_dilleri and kullanicinin_sevdigi_dil == "swift":
    print("Kaan ve halil de swift dilini yazıyor!")

else:
    print("Lütfen geçerli bir kodlama dili girdiğinizden emin olunuz.")


