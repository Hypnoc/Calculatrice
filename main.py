def main():
    
    nombre1 = input("Nombre #1 : ")
    nombre2 = input("Nombre #2 : ")
    operation = input("Entrez l'operation +, -, * ou / : ")
    resultat = 0
    
    if not nombre1.isnumeric() or not nombre2.isnumeric() :
        print("Erreur: Les deux valeurs doivent être des nombres entiers")
    else : 
        nombre1 = int(nombre1)
        nombre2 = int(nombre2)

    match operation:
        case "+":
            resultat = nombre1 + nombre2
        case "-":
            resultat = nombre1 - nombre2
        case "*":
            resultat = nombre1 * nombre2
        case "/":
            if nombre2 == 0:
                print("Division par 0 impossible !")
            else:
                resultat = nombre1 / nombre2
        case _:
            print("Erreur: Vous devez entrer une opération entre +, -, * ou /.")

    print(f"Le résultat est {resultat}")

# Ne touchez pas le code ci-dessous
if __name__ == "__main__":
    main()