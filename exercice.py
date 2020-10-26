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


if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici

    pass
