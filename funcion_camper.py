import menus
import mostrar_usuarios
def camper():
    while True:
        try:
            menus.menu_camper()
            opc = int(input("Seleccione una opcion: "))
            if opc == 1:
                mostrar_usuarios.mos_campers()
            elif opc == 2:
                mostrar_usuarios.mos_notas_campers()
            elif opc == 3:
                mostrar_usuarios.mos_horario()
            elif opc == 4:
                break
            else:
                print("Numero invalido")
        except Exception:
            print("porfavor ingrese un dato valido")
        finally:print("**************************************************")

