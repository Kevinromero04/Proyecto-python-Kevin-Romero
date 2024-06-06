import json
import menus
import fun_trainers_notas as nota
import trainer_c_g as mm

def wel_train ():
    ss = mm.cargar_trainer()
    clave = input("Digite la clave: ").lower()
    
    if clave in ss["Trainers"]:
        usuario = ss["Trainers"][clave]["usuario"]
        print("Bienvenido Trainer", usuario)
        print("**************************************************")
        while True:
            menus.menu_trainer()
            opc= int(input("Seleccione una opcion: "))
            if opc == 1:
                nota.notas_trainers()
            elif opc == 2:
                print("Saliendo..")
                break
            else:
                print("Numero invalido")
    else:
        print("Clave invalida")
        print("**************************************************")
        

