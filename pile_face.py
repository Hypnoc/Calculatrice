import random 

capital = 100
nombre_lancer = 0
lancer = random.randint(1, 100)


for i in range(100):
    if lancer <= 49:
        capital +=1
        nombre_lancer += 1
        print(f"lancer #{nombre_lancer}")
        print(f"résultat du lancer : {lancer}")
        print(f"montant capital : {capital}")
        print("************************")
        lancer = random.randint(1, 100)
    else:
        capital -=1
        nombre_lancer += 1
        print(f"lancer #{nombre_lancer}")
        print(f"résultat du lancer : {lancer}")
        print(f"montant capital : {capital}")
        print("************************")
        lancer = random.randint(1, 100)
