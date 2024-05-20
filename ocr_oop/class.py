# J’ai une boîte à outils. Cette boîte à outils peut contenir des outils, et je peux ajouter ou enlever des outils à la boîte à outils.

# Je possède aussi des marteaux. Les marteaux peuvent être de couleurs différentes, et peuvent être utilisés pour planter et pour 
# retirer des clous. Je peux également changer la couleur d’un marteau en le peignant.

# Enfin, je possède aussi des tournevis. Ils ont une taille (mesurée en millimètres) et peuvent être utilisés pour serrer ou desserrer
# une vis.

class toolbox ():
    def __init__(self):
        self.tool = []

    def add_tool(self, a):
        tool += a
        return toolbox
    
    def remove_tool(self, a):
        tool -= a
        return toolbox
    
class marteau():
    def __init__(self, color):
        self.color = color

    def put_nail(self):
        print("le clou est planté")

    def remove_nail(self):
        print("le clou est retiré")

class tournevis():
    def __init__(self, length):
        self.length = length
    
    def serrer(self):
        print("la vis est serrée")

    def desserer(self):
        print("la vis est desserée")