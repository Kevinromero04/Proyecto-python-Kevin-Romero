
import funciones_guarda_muestra as guarda
import funcion_g_c_aprobados as gg

def aprobar ():
    while True:
        try:
            documento = int(input("Digite el documento del camper inscrito: "))
            nuevo = guarda.cargar_ususario()
            if str(documento) in nuevo["registrados"]:
                nota1 = int(input("Digite la nota teorica del camper inscrito: "))
                nota2 = int(input("Digite la nota practica del camper inscrito: "))
                nota3 = ((nota1 + nota2)/2)
                if nota3 >= 60:
                    nuevo["registrados"][str(documento)]["Estado"] = "Aprobado"        
                    print("Camper aprobado")
                    print("**************************************************")
                    guarda.guardar_usuario(nuevo)
                    break
                elif nota3 <= 59:
                    
                    nuevo["registrados"][str(documento)]["Estado"] = "Denegado"
                    nuevo["campers"].pop(str(documento))
                    guarda.guardar_usuario(nuevo)   
                    print("Camper denegado")
                    print("**************************************************")
                    break
                        
            else:
                print("El documento no coincide con ningun usuario registrado")
                print("**************************************************")
        except Exception:
            print("porfavor ingrese un dato valido")
        finally:print("**************************************************")
        
def mover_usuario_aprobado():
    while True:
        try:
            documento = int(input("Necesitamos que confirme el documento: "))
            nuevo = guarda.cargar_ususario()
            nuevo["campers"] = nuevo.pop("registrados")
            if str(documento) in nuevo["campers"]:
                usuario = nuevo["campers"][str(documento)]
                
                if usuario["Estado"] == "Aprobado":
                    juju =gg.cargar_ususario_aprobados()
                    juju["campers"][str(documento)]= usuario
                    gg.guardar_usuario_aprobados(juju)
                    nuevo["registrados"] = nuevo.pop("campers")
                    nuevo["registrados"].pop(str(documento))
                    guarda.guardar_usuario(nuevo)
                    print("Muchas gracias por la confirmacion")
                    print("**************************************************")
                    break
                else:
                    print("Paso algo mal intenta de nuevo")
                    print("**************************************************")
                    break
            else:
                print("El documento con el documento registrado")
                print("**************************************************")
        except Exception:
            print("porfavor ingrese un dato valido")
        finally:print("**************************************************")



