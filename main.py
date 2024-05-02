import sys
def main():
  
    nombre1 = input("Nombre #1 : ")
    nombre2 = input("Nombre #2 : ")
    operation = input("Entrez l'operation +, -, * ou / : ")
    resultat = 0
    
    if not nombre1.isnumeric() or not nombre2.isnumeric() :
        print("Erreur: Les deux valeurs doivent être des nombres entiers")
        sys.exit()
    else : 
        nombre1 = int(nombre1)
        nombre2 = int(nombre2)   

    match operation:
        case "+":
            resultat = nombre1 + nombre2
            print(f"Le résultat est {resultat}")
        case "-":
            resultat = nombre1 - nombre2
            print(f"Le résultat est {resultat}")
        case "*":
            resultat = nombre1 * nombre2
            print(f"Le résultat est {resultat}")
        case "/":
            if nombre2 == 0:
                print("Division par 0 impossible !")
                sys.exit()
            else:
                resultat = nombre1 / nombre2
                print(f"Le résultat est {resultat}")                
        case _:  
            print("Erreur: Vous devez entrer +, -, * ou / pour l'opération")
            sys.exit()

# Ne touchez pas le code ci-dessous
if __name__ == "__main__":
    main()