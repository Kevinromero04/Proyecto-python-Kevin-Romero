import funcion_g_c_aprobados as pp
import menus 
import funcion_g_c_aprobados as pp
import menus 
import prueba_carga as gg

def rhlm():
    uaa = pp.cargar_ususario_aprobados()
    brr = gg.cargar_rutas()
    documento = int(input("Digite el documento del camper que deseas asignarle una ruta"))
    if str(documento) in uaa["campers"]:
        while True:
            menus.menu_rutas()
            opc1 = int(input("Seleccione una ruta: "))
            if opc1 == 1:
                print("Los grupos de NetCore son:")
                menus.menu_NetCore()
                opc2 = int(input("Elija una opcion: "))
                if opc2 == 1:
                    brr["Rutas"]["NetCore"]["M1"]["campers"].append(documento)
                    uaa["campers"][str(documento)]["Ruta"] = "NetCore"
                    uaa["campers"][str(documento)]["Grupo"] = "M1"
                    uaa["campers"][str(documento)]["Horario"] = "6:00 pm a 10:00 pm"
                    pp.guardar_usuario_aprobados(uaa)
                    gg.guarda_rutas(brr)
                    print("La ruta y el grupo a sido asignado al camper")
                    break  
                elif opc2 == 2:
                    brr["Rutas"]["NetCore"]["M2"]["campers"].append(documento)
                    uaa["campers"][str(documento)]["Ruta"] = "NetCore"
                    uaa["campers"][str(documento)]["Grupo"] = "M2"
                    uaa["campers"][str(documento)]["Horario"] = "10:00 am a 2:00 pm"
                    pp.guardar_usuario_aprobados(uaa)
                    gg.guarda_rutas(brr)
                    print("La ruta y el grupo a sido asignado al camper")
                    break  
                else:
                    print("Numero invalido")
            elif opc1 == 2:
                print("Los grupos de NodeJs son:")
                menus.menu_NodeJs()
                opc3 = int(input("Elija una opcion: "))
                if opc3 == 1:
                    brr["Rutas"]["NodeJs"]["K1"]["campers"].append(documento)
                    uaa["campers"][str(documento)]["Ruta"] = "NodeJs"
                    uaa["campers"][str(documento)]["Grupo"] = "K1"
                    uaa["campers"][str(documento)]["Horario"] = "6:00 pm a 10:00 pm"
                    pp.guardar_usuario_aprobados(uaa)
                    gg.guarda_rutas(brr)
                    print("La ruta y el grupo a sido asignado al camper")
                    break  
                elif opc3 == 2:
                    brr["Rutas"]["NodeJs"]["K2"]["campers"].append(documento)
                    uaa["campers"][str(documento)]["Ruta"] = "NodeJs"
                    uaa["campers"][str(documento)]["Grupo"] = "K2"
                    uaa["campers"][str(documento)]["Horario"] = "10:00 am a 2:00 pm"
                    pp.guardar_usuario_aprobados(uaa)
                    gg.guarda_rutas(brr)
                    print("La ruta y el grupo a sido asignado al camper")
                    break  
                else:
                    print("Numero invalido")
            elif opc1 == 3:
                print("Los grupos de Java son:")
                menus.menu_Java()
                opc4 = int(input("Elija una opcion: "))
                if opc4 == 1:
                    brr["Rutas"]["Java"]["U1"]["campers"].append(documento)
                    uaa["campers"][str(documento)]["Ruta"] = "Java"
                    uaa["campers"][str(documento)]["Grupo"] = "U1"
                    uaa["campers"][str(documento)]["Horario"] = "6:00 pm a 10:00 pm"
                    pp.guardar_usuario_aprobados(uaa)
                    gg.guarda_rutas(brr)
                    print("La ruta y el grupo a sido asignado al camper")
                    break  
                elif opc4 == 2:
                    brr["Rutas"]["Java"]["U2"]["campers"].append(documento)
                    uaa["campers"][str(documento)]["Ruta"] = "Java"
                    uaa["campers"][str(documento)]["Grupo"] = "U2"
                    uaa["campers"][str(documento)]["Horario"] = "10:00 am a 2:00 pm"
                    pp.guardar_usuario_aprobados(uaa)
                    gg.guarda_rutas(brr)
                    print("La ruta y el grupo a sido asignado al camper")
                    break  
                else:
                    print("Numero invalido")
            else:
                print("Opción de ruta no válida")
    else:
        print("Documento invalido")
        print("**************************************************")
        
