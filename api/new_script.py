import requests
import os
import shutil

# appeler route website
# demander user quel site
# appeler le bon site
# importer fichier index-template vers dossier websites
# importer image correspondante vers dossier websites
# réécrire code html avec les valeur du bon site

url1 = "https://my-json-server.typicode.com/tiko69/JSONserver/websites"
response1 = requests.get(url1)
data = response1.json()

for cle in data:
    print(str(cle["id"]) + " : " + str(cle["website"]))

choix = input("Quel site souhaitez-vous créer ? ")

url2 = f"https://my-json-server.typicode.com/tiko69/JSONserver/website?id={choix}"
response2 = requests.get(url2)
data2 = response2.json()

nom_dossier = data2[0]["title"]
nom_image = data2[0]["img"]["src"]

source = f"websiteGenerator{os.sep}templates{os.sep}index.html"
destination = f"websiteGenerator{os.sep}websites{os.sep}{nom_dossier}"

if os.path.exists(destination):
    shutil.rmtree(destination)

os.makedirs(destination)
shutil.copy(source, destination)

shutil.copy(f"websiteGenerator{os.sep}assets{os.sep}{nom_image}", destination)

with open(f"{destination}{os.sep}index.html", "r") as file:
    indexhtml = file.read()

indexhtml = indexhtml.replace("[img.src]", f"file:{os.sep}C:/Users/Utilisateur/Documents/SIMPLON/COURS/python/api/{destination}{os.sep}{nom_image}")

with open(f"{destination}{os.sep}index.html", "w") as file:
    file.write(indexhtml)

