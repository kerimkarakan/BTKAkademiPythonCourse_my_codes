adet = int(input("kaç dilim pizza istersiniz"))

#yöntem 1

while adet > 0 :
    print("pizzanız geldi afiyet olsun")
    adet -= 1

#yöntem 2
i = 1
while adet > i : 
    print(i , ". pizzanız geldi afiyet olsun")
    i += 1