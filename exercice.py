# example context manager :
class ContextManagedList:
    def __init__(self,1:list)-> None:
        self.1 = 1

    def __enter__(self): # assure qu'on fait cette opération avec d,ouvrire 
        print("enter")
        return self
    
    def __exist__(seld,exc_type,exc_val,exc_tb):#assure que certaines opérations sont effectué au moment ou on le désrier
        #une fois que le code est fait et qu'on sort du fichier ce code vas rouler 
        print("exit")

with ContextManagedList([1,2])as my_list:
    raise(Exception)
#!/usr/bin/env python
# -*- coding: utf-8 -*-


# TODO: Importez vos modules ici



# TODO: Définissez vos fonction ici
def compare_files(nom_fichier_1:str,nom_fichier_2:str):
    with open(nom_fichier_1,"r") as f1, open(nom_fichier_2, "r"):
        same = True

        while same :
            a = f1.read()
            b=f2.rwad()

            same = a == b 
    return same

def final_space(file1,file2):
    with open(file1,"r") as data, open(file2,"w")as result:
        result.write(data.read().replace(" ","  "))

def convert_grades():

def grades(note_file,target_file):
    correspondances = {20: "F", 40: "D", 50: "C", 70: "B", 85: "A"

    with open(note_file,'r') as note_data, open(target_file, 'w') as target :
        for line in note_data.readlines.keys():
            note = float(line, 3)   #results= []
            if grade in correspondances.keys():
                if grade == 85 and note > grade :
                    target.write('A*")      #results.appends("A*") = une autre option
                if note <= grade:
                    target.write(correspondances[grade]+ "\n") #le \n vas insérer une nouvelle ligne
                    # autre option results.append (même chose )
                    break
            #target.writelines(results)

import json
class LivreDeRecettes : #faire jsn
    def __init__(self):
        self.filename = "recettes.json"
        self.id = 0
        with open(self.filename, mode='w') as fichier:
            json.dump({"recettes": []}, fichier, ingrediant = 4)
    
    def ajouter_une_recette(self,nom:str, ingrediants : list) -> int:
        with open(self.filename,"r") as fichier:

            recettes=json.load(fichier)
            recettes_liste= recettes["recettes"]
            recettes_liste.append({
                "id" :self.id,
                "nom" : nom, 
                "ingrediants" : ingrediants
            })

        with open(self.filename, "w") as fichier : 
            json.dump(recettes,fichier, indent=4) #dump vas dumper un object dans fichier jason, genr print mais un gros chunk
            # vas print la variable recette avec un indentation 
        
        self.id +=1 
    
    def recuperer_une_recette(self, recette_id:int) -> tuple:
        with open (self.filename, mode='r') as fichier:

            livre = json.load(fichier)
            for recette in livre["recettes"]:
                if recette["id"] == recette_id:
                    return recette["nom"], recette["ingrediants"]

            return "la recette n'existe pas", None 

def nombre_croissant(fichier):
    with open(fichier, "r") as texte:
        result = []
    
        for line in text.read(): # pour chaque line 
            print(line.split())
            for word in line.split():
                if word.isdigit:
                    print(int(word)) # vas extraire out les nombres de notre list 
#return sorted([int(word) for word in text.read().split() if word,isdidget()]) -> en une ligne 
        return sorted(result)

if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    livre_de_recettes = LivreDeRecettes()


    grades("notes.txt", "grades.tx")

    correspondances = {20: "F", 40: "D", 50: "C", 70: "B", 85: "A"
    

    pass
