from menus import menu_notasr
import funcion_g_c_aprobados as gg
def notas_trainers():  
    nuevo = gg.cargar_ususario_aprobados()
    documento = int(input("Digite el documento del camper para colocarle la nota: "))
    if str(documento) in nuevo["campers"]:
        
        while True:
            menu_notasr()
            uua = int(input("Seleccione una opcion: "))
            if uua == 1:
                nota1 = int(input("Digite la nota de la practica: "))
                nota2 = (nota1 * 0.6)
                nuevo["campers"][str(documento)]["Notas 60%"].append(nota2)
                nuevo["campers"][str(documento)]["Nota Final"].append(nota2)
                suma = sum(nuevo["campers"][str(documento)]["Nota Final"])
                nuevo["campers"][str(documento)]["Nota Final"]= [suma]
                gg.guardar_usuario_aprobados(nuevo)
                print("Nota 60% agregada")
                print("**************************************************")
            elif uua == 2:
                nota1 = int(input("Digite la nota teorica: "))
                nota2 = (nota1 * 0.3)
                nuevo["campers"][str(documento)]["Notas 30%"].append(nota2)
                nuevo["campers"][str(documento)]["Nota Final"].append(nota2)
                suma = sum(nuevo["campers"][str(documento)]["Nota Final"])
                nuevo["campers"][str(documento)]["Nota Final"]= [suma]
                gg.guardar_usuario_aprobados(nuevo)
                print("Nota 30% agregada")
                print("**************************************************")
            elif uua == 3:
                nota1 = int(input("Digite la nota de los quizzis: "))
                nota2 = (nota1 * 0.1)
                nuevo["campers"][str(documento)]["Notas 10%"].append(nota2)
                nuevo["campers"][str(documento)]["Nota Final"].append(nota2)
                suma = sum(nuevo["campers"][str(documento)]["Nota Final"])
                nuevo["campers"][str(documento)]["Nota Final"]= [suma]
                gg.guardar_usuario_aprobados(nuevo)
                print("Nota 10% agregada")
                print("**************************************************")
            elif uua == 4:
                print("saliendo")
                break
            if suma >= 60:
                nuevo["campers"][str(documento)]["Riesgo"] = "bajo"
                gg.guardar_usuario_aprobados(nuevo)
            elif suma <= 59:
                nuevo["campers"][str(documento)]["Riesgo"] = "alto" 
                gg.guardar_usuario_aprobados(nuevo)
            else:
                print("Número incorrecto, intente de nuevo")
    else:
        print("El documento no coincide con ningun camper")
        print("**************************************************")
        return
    



