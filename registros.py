import funciones_guarda_muestra as guarda
import funcion_g_c_aprobados as gg

def registrar_Usuario():
    print("**************************************************")
    nuevo = gg.cargar_ususario_aprobados()
    dato=guarda.cargar_ususario()
    regis_usuario={}
    doc = int(input("Ingrese el documento: "))
    if str(doc) in nuevo["campers"]:
        print("hay un camper ya existente!")
    else:
        if str(doc) in dato["registrados"]:
            print("Participante ya existe!")
            return
        else:
            regis_usuario["Nombre"] = input("Ingrese sus nombres: ")
            regis_usuario["Apellidos"] = input("Ingrese sus apellidos: ")
            regis_usuario["Direccion"] = input("Ingrese su Direccion: ")
            regis_usuario["Acudiente"] = input("Ingrese su Acudiente: ")
            regis_usuario["Telefono"] = int(input("Ingrese su numero de telefono: "))
            regis_usuario["Telefono Fijo"] = input("Ingrese su telefono fijo (en caso de no tener escribir 0): ")
            regis_usuario["Estado"] = "Inscrito"
            regis_usuario["Riesgo"] = "No"
            regis_usuario["Nota Final"] = []
            regis_usuario["Notas 10%"] = []
            regis_usuario["Notas 60%"] = []
            regis_usuario["Notas 30%"] = []
            regis_usuario["Ruta"] = ""
            regis_usuario["Horario"] = ""
            print("Felicitaciones has sido inscrito")
            dato["registrados"][doc]= regis_usuario
            guarda.guardar_usuario(dato)
            print("Participante registrado!")   
        print("**************************************************")



