def main():
    nombre_a_gauche = input("chiffre_#1 :")
    nombre_a_droite = input("chiffre #2 :")
    operation = input("+, -, *, / : ")
    resultat = 0
    
    if not nombre_a_gauche.isnumeric() or not nombre_a_droite.isnumeric() :
        print("Erreur: les deux nombres doivent être des nombres entiers")
    else : int(resultat)

# Ne touchez pas le code ci-dessous
if __name__ == "__main__":
    main()