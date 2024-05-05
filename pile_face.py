import random 

capital = 0
nombre_lancer = 0
lancer = random.randint(1, 100)


for i in range(10000):
    if lancer <= 49:
        capital +=1
        nombre_lancer += 1
        lancer = random.randint(1, 100)
        print(f"lancer #{nombre_lancer}")
        print(f"résultat du lancer : {lancer}")
        print(f"montant capital : {capital}")
    else:
        capital -=1
        nombre_lancer += 1
        lancer = random.randint(1, 100)
        print(f"lancer #{nombre_lancer}")
        print(f"résultat du lancer : {lancer}")
        print(f"montant capital : {capital}")
