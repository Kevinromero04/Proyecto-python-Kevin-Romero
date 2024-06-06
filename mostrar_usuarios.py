import json
import funcion_g_c_aprobados as gg
def mos_ins ():
    file = open("registros.json")
    regis = json.load(file)
    for documento , datos in regis["registrados"].items():
        print("")
        print("El usuario ", datos["Nombre"],datos["Apellidos"],", Con el documento",documento,", que vive en la direccion ",datos["Direccion"],", con el acudiente ",datos["Acudiente"],", con numero de telefon ",datos["Telefono"],", con numero fijo ",datos["Telefono Fijo"],", que esta en el estado ",datos["Estado"] )
        print("")
        print("**************************************************")
def mos_trains():
    file = open("trainers.json")
    regisa = json.load(file)
    for clave , datos in regisa["Trainers"].items():
        print("")
        print("El trainer con el usuario: ", datos["usuario"], ", con la ruta:", datos["Ruta"], ", le corresponde los horarios: ", datos["Horario"], ", se le asigno el siguiente salon: ", datos["Salon"])
        print("")
        print("**************************************************")

def mos_campers():
    nuevo=gg.cargar_ususario_aprobados()
    doc = int(input("Ingrese el documento: "))
    if str(doc) in nuevo["campers"]:
        print("")
        print("El usuario ", nuevo["campers"][str(doc)]["Nombre"],nuevo["campers"][str(doc)]["Apellidos"],", Con el documento",doc,", que vive en la direccion ",nuevo["campers"][str(doc)]["Direccion"],", con el acudiente ",nuevo["campers"][str(doc)]["Acudiente"],", con numero de telefon ",nuevo["campers"][str(doc)]["Telefono"],", con numero fijo ",nuevo["campers"][str(doc)]["Telefono Fijo"],", que esta en el estado ",nuevo["campers"][str(doc)]["Estado"] )
        print("")
        print("**************************************************")
    else:
        print("No existe ningun camper con ese documento")

def mos_notas_campers():
    nuevo=gg.cargar_ususario_aprobados()
    doc = int(input("Ingrese el documento: "))
    if str(doc) in nuevo["campers"]:
        print("")
        print("El usuario ", nuevo["campers"][str(doc)]["Nombre"],nuevo["campers"][str(doc)]["Apellidos"],"tiene las siguientes notas")
        print("La nota del 10% es: ", nuevo["campers"][str(doc)]["Notas 10%"], "la nota del 30% es: ", nuevo["campers"][str(doc)]["Notas 30%"],"la nota del 60% es: ", nuevo["campers"][str(doc)]["Notas 60%"])
        print("la nota final es: ",nuevo["campers"][str(doc)]["Nota Final"])
        print("")
        print("**************************************************")
    else:
        print("No existe ningun camper con ese documento")
        
def mos_horario():
    nuevo=gg.cargar_ususario_aprobados()
    doc = int(input("Ingrese el documento: "))
    if str(doc) in nuevo["campers"]:
        print("")
        print("Te toco en el horario:  ", nuevo["campers"][str(doc)]["Horario"])
        print("Te toco en el ruta:  ", nuevo["campers"][str(doc)]["Ruta"])
        print("Te toco en el grupo:  ", nuevo["campers"][str(doc)]["Grupo"])
        print("")
        print("**************************************************")
    else:
        print("No existe ningun camper con ese documento")

def mos_camp ():
    file = open("campers.json")
    regis = json.load(file)
    for documento , datos in regis["campers"].items():
        print("")
        print("El camper ", datos["Nombre"],datos["Apellidos"],", Con el documento",documento)
        print("Esta en la ruta: ", datos["Ruta"],"en el grupo: ",datos["Grupo"],"en el horario:",datos["Horario"])
        print("")
        print("**************************************************")


