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

if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici

    pass
