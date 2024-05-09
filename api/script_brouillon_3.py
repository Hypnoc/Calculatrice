with open(chemin_destination_html_a_coller, "r") as fichier_html:
    contenu_html = fichier_html.read()
    for i in data2:
        cle = i[0]
        valeur = i[0][0]
        while i != "[img.src]":
            contenu_html_modifie = contenu_html.replace("[title]", data2[0]["title"]) \
                                    .replace("[body.color]", data2[0]["body"]["color"]) \
                                    .replace("[h1.background-color]", data2[0]["h1"]["background-color"]) \
                                    .replace("[h1.color]", data2[0]["h1"]["color"]) \
                                    .replace("[h1.text]", data2[0]["h1"]["text"]) \
                                    .replace("[p.color]", data2[0]["p"]["color"]) \
                                    .replace("[p.text]", data2[0]["p"]["text"]) \
                                    .replace("[img.src]", chemin_asset) \
                                    
with open(chemin_destination_html_a_coller, "w") as fichier_html:
    fichier_html.write(contenu_html_modifie)