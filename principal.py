import menus

import registros
import fun_coor
import funcion_trainer
import funcion_camper
while True:
    try:
        menus.menu_1()
        opc1 = int(input("Seleccione una opcion: "))
        if opc1 == 1:
            funcion_trainer.wel_train()
        elif opc1 == 2:
            funcion_camper.camper()
        elif opc1 == 3:
            fun_coor.wel_coor()
        elif opc1 == 4:
            registros.registrar_Usuario()
        elif opc1 == 5:
            print("Saliendo...")
            break
        else:
            print("Numero incorrecto")
    except Exception:
        print("porfavor ingrese un dato valido")
    finally:print("**************************************************")

        
