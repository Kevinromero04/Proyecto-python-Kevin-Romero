import json
def mos_ins ():
    file = open("registros.json")
    regis = json.load(file)
    for documento , datos in regis["registrados"].items():
        print("El usuario ", datos["Nombre"],datos["Apellidos"],", Con el documento",datos[str(documento)] ,", que vive en la direccion ",datos["Direccion"],", con el acudiente ",datos["Acudiente"],", con numero de telefon ",datos["Telefono"],", con numero fijo ",datos["Telefono Fijo"],", que esta en el estado ",datos["Estado"] )
        print("**************************************************")
def mos_trains():
    file = open("trainers.json")
    regisa = json.load(file)
    for clave , datos in regisa["Trainers"].items():
        print("El trainer con el usuario", datos["usuario"], ", con la ruta", datos["Ruta"], ", le corresponde los horarios", datos["Horario"], ", se le asigno el siguiente salon", datos["Salon"])
        print("**************************************************")

