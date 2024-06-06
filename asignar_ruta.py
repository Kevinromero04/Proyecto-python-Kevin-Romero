import funcion_g_c_aprobados as gg
import grupos_guarda_carga as grup
import menus 
def rutas ():
    while True:
        try:
            documento = int(input("Digite el documento del camper inscrito: "))
            nuevo = gg.cargar_ususario_aprobados()
            gr = grup.cargar_rutas()
            if str(documento) in nuevo["campers"]:
                print("Que ruta le quieres asignar")
                menus.menu_rutas()
                opc1 = int(input("seleccione:"))
                if opc1 == 1:
                    gr["M1"]["campers"].append(documento)
                    nuevo["campers"][str(documento)]["Ruta"] = "NetCore"
                    nuevo["campers"][str(documento)]["Ruta"] = "6:00 pm a 10:00 pm"
                    gg.guardar_usuario_aprobados(nuevo)
                    grup.guardar_rutas(gr)
                    break
                elif opc1 == 2:
                    gr["M2"]["campers"].append(documento)
                    nuevo["campers"][str(documento)]["Ruta"] = "NodeJs"
                    nuevo["campers"][str(documento)]["Ruta"] = "10:00 am a 2:00 pm"
                    gg.guardar_usuario_aprobados(nuevo)
                    
                    grup.guardar_rutas(gr)
                    break
                elif opc1 == 3:
                    gr["M3"]["campers"].append(documento)
                    nuevo["campers"][str(documento)]["Ruta"] = "Java"
                    nuevo["campers"][str(documento)]["Ruta"] = "6:00 am 10:00 am"
                    gg.guardar_usuario_aprobados(nuevo)
                    grup.guardar_rutas(gr)
                    break
                elif opc1 == 4:
                    gr["M3"]["campers"].append(documento)
                    nuevo["campers"][str(documento)]["Ruta"] = "Java"
                    nuevo["campers"][str(documento)]["Ruta"] = "2:00 pm a 6:00 pm"
                    gg.guardar_usuario_aprobados(nuevo)
                    grup.guardar_rutas(gr)
                    break
                else:
                    print("Opcion no valida")        
            else:
                print("Camper no existente")
        except Exception:
            print("porfavor ingrese un dato valido")
        finally:print("**************************************************")
        

            
        