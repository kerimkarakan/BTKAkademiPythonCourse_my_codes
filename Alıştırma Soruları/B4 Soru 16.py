uce_bolunnen = []

bese_bolunen = []

harici_sayilar = []

for i in range(100):
    if i % 3 == 0:
        uce_bolunnen.append(i)
    elif i % 5 == 0:
        bese_bolunen.append(i)
    elif i % 5 != 0 and i % 3 != 0:
        harici_sayilar.append(i)

print(f"0 ile 100 arasında üçe bölünen sayılar: {uce_bolunnen}")
print(f"0 ile 100 arasında beşe bölünen sayılar: {bese_bolunen}")
print(f"0 ile 100 arasında üçe de beşe de bölünemeyen sayılar: {harici_sayilar}")
