üce_tam_bolunen = []

bese_tam_bolunen = []

uce_ve_bese_tam_bolunen = []

for i in range(100):
  
  if i % 5 == 0 and i % 3 == 0:
     uce_ve_bese_tam_bolunen.append(i)  
  
  elif i % 3 == 0:
      üce_tam_bolunen.append(i)

  elif i % 5 == 0:
      bese_tam_bolunen.append(i)   

print(f"0 ile 100 arasında üçe tam bölünen sayılar = {üce_tam_bolunen}")
print(f"0 ile 100 arasında beşe tam bölünen sayılar = {bese_tam_bolunen}")
print(f"0 ile 100 arasında hem üçe hem beşe tam bölünen sayılar = {uce_ve_bese_tam_bolunen}")
 

