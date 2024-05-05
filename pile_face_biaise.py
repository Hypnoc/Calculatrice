
# Un jeu avec deux pièces biaisées. 
# La première pièce donne pile avec une probabilité p1 = 0.09 et la seconde pièce donne pile avec une probabilité p2 = 0.74.
# Le joueur de ne peut miser qu’un euro à la fois ! En revanche, on regarde à chaque lancé son capital (la somme d’argent total)
# dont il dispose pour déterminer quelle pièce lancer : si le capital est un multiple de 3, on lance la pièce numéro une, 
# sinon on lance la seconde pièce. Comme dans le jeu A, le joueur remporte sa mise plus un euro supplémentaire si la pièce
# choisie tombe sur pile, sinon il perd sa mise.


import random 

capital = 1000
nombre_lancer = 0
lancer = random.random()


for i in range(1, 10001):
    if capital % 3 == 0 and capital != 0:

        if lancer <= 0.09:
            nombre_lancer += 1
            capital += 1
            print(f"lancer #{nombre_lancer}")
            print(f"résultat du lancer : {lancer}")
            print(f"montant capital : {capital}")
            print("***********************************")
            lancer = random.random()
        else:
            nombre_lancer += 1
            capital -= 1
            print(f"lancer #{nombre_lancer}")
            print(f"résultat du lancer : {lancer}")
            print(f"montant capital : {capital}")
            print("***********************************")
            lancer = random.random()
    else:
    
        if lancer <= 0.74:
            nombre_lancer += 1
            capital += 1
            print(f"lancer #{nombre_lancer}")
            print(f"résultat du lancer : {lancer}")
            print(f"montant capital : {capital}")
            print("***********************************")
            lancer = random.random()
        else:
            nombre_lancer += 1
            capital -= 1
            print(f"lancer #{nombre_lancer}")
            print(f"résultat du lancer : {lancer}")
            print(f"montant capital : {capital}")
            print("***********************************")
            lancer = random.random()