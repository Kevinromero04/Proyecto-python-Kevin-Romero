import funcion_g_c_aprobados as gg
def modi_cordi():
    nuevo = gg.cargar_ususario_aprobados()
    documento = int(input("Digite el documento del camper para colocarle la nota: "))
    if str(documento) in nuevo["campers"]:
        
        nota1 = int(input("Digite la nueva nota: "))
        nuevo["campers"][str(documento)]["Nota Final"].clear()
        gg.guardar_usuario_aprobados(nuevo)
        nuevo["campers"][str(documento)]["Nota Final"].append(nota1)
        gg.guardar_usuario_aprobados(nuevo)
        print("Nota agregada")
        print("**************************************************")
    else:
        print("El camper no existe")
        
