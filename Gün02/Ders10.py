# tek satırda koşullu ifadeler

a = 5
if a > 4 :
    b = "büyüktür"
else: 
    b = "küçüktür"

print(a, b)      

c = "büyüktür" if a > 4 else "küçüktür"

print(a,c)

#bu şekilde tek satırda koşullu ifade yazmış oluyoruz

print("büyüktür" if a > 4 else "küçüktür")
