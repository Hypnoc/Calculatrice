import requests
import os
import shutil

def url_id(id):
    id = str(site_choisi)
    url_valide = url2 + "?id=" + id
    return url_valide


url1 = "https://my-json-server.typicode.com/tiko69/JSONserver/websites"
url2 = "https://my-json-server.typicode.com/tiko69/JSONserver/website"

# Effectuer une requête GET
# créer un dictionnaire avec les données Json
reponse1 = requests.get(url1)
data = reponse1.json()

liste = []

# Vérifier si la requête a réussi (code de statut 200)
if reponse1.status_code == 200:
    for i in data:
        print(str(i["id"]) + " : " + str(i["website"]))
        liste.append(i["id"])
else:
    print("La requête a échoué avec le code de statut :", reponse1.status_code)

site_choisi = input("Choisissez l'id du site à créer : ")

while int(site_choisi) not in liste:
    site_choisi = input(f"L'id que vous avez entré n'est pas valide. Veuillez entrer une valeur valide parmi {liste} : ")

nom_url = url_id(site_choisi)

print(f"url choisi : {nom_url}")


reponse2 = requests.get(nom_url)
data2 = reponse2.json()

data3 = data2[0]

liste_cle = []
liste_valeur = []

for i in data3:
    liste_cle.append(i)
    liste_valeur.append(data3[i])

print(liste_cle)
print(liste_valeur)

dico_json = {}
for i in range(6):
    dico_json[liste_cle[i]] = liste_valeur[i]


chemin_dossier_a_creer = "C:/Users/Utilisateur/Documents/SIMPLON/COURS/python/api/websiteGenerator/websites"


for i in data2:
    nom_dossier_a_creer = i["title"]

os.chdir(chemin_dossier_a_creer)
os.mkdir(nom_dossier_a_creer)

# Copie du fichier
chemin_fichier_html_a_copier = "C:/Users/Utilisateur/Documents/SIMPLON/COURS/python/api/websiteGenerator/templates/index.html"
chemin_destination_html_a_coller = f"C:/Users/Utilisateur/Documents/SIMPLON/COURS/python/api/websiteGenerator/websites/{nom_dossier_a_creer}/index.html"
shutil.copy(chemin_fichier_html_a_copier, chemin_destination_html_a_coller)

for i in data2:
    nom_asset = i["img"]["src"]

chemin_asset_copier = f"C:/Users/Utilisateur/Documents/SIMPLON/COURS/python/api/websiteGenerator/assets/{nom_asset}"
chemin_destination_asset_a_coller = f"C:/Users/Utilisateur/Documents/SIMPLON/COURS/python/api/websiteGenerator/websites/{nom_dossier_a_creer}/"
chemin_asset = f"file:///C:/Users/Utilisateur/Documents/SIMPLON/COURS/python/api/websiteGenerator/websites/{nom_dossier_a_creer}/{nom_asset}"
shutil.copy(chemin_asset_copier, chemin_destination_asset_a_coller)


with open(chemin_destination_html_a_coller, "r") as fichier_html:
    contenu_html = fichier_html.read()

    for cle in dico_json:
    # Vérifier si la clé existe dans la chaîne var1
        if cle in contenu_html:
        # Remplacer la clé par sa valeur correspondante de var2
            contenu_html = contenu_html.replace(cle, str(dico_json[cle]))

    contenu_html_modifie = contenu_html
    contenu_html.replace("[img.src]", chemin_asset)
                                    
with open(chemin_destination_html_a_coller, "w") as fichier_html:
    fichier_html.write(contenu_html_modifie)