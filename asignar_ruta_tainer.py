import trainer_c_g as pp
import menus 
import prueba_carga as gg
import mostrar_inscritos as ss

def bebesita():
    uaa = pp.cargar_trainer()
    brr = gg.cargar_rutas()
    print("Estos son los trainers y su informacion")
    ss.mos_trains()
    documento = input("Digite la clave del trainer: ")
    if str(documento) in uaa["Trainers"]:
        while True:
            menus.menu_rutas()
            opc1 = int(input("Seleccione una ruta: "))
            if opc1 == 1:
                    brr["Rutas"]["NetCore"]["M1"]["Trainer"] = documento
                    brr["Rutas"]["NetCore"]["M2"]["Trainer"] = documento
                    uaa["Trainers"][str(documento)]["Ruta"] = "NetCore"
                    uaa["Trainers"][str(documento)]["Salon"] = "Apolo"
                    uaa["Trainers"][str(documento)]["Horario"] = "10:00 am a 2:00 pm y 6:00 pm a 10:00 pm "
                    pp.guardar_trainer(uaa)
                    gg.guarda_rutas(brr)

            elif opc1 == 2:
                    brr["Rutas"]["NodJs"]["K1"]["Trainer"] = documento
                    brr["Rutas"]["NodJs"]["K2"]["Trainer"] = documento
                    uaa["Trainers"][str(documento)]["Ruta"] = "NodJs"
                    uaa["Trainers"][str(documento)]["Salon"] = "Artemis"
                    uaa["Trainers"][str(documento)]["Horario"] = "6:00 am a 10:00 pm y 2:00 pm a 6:00 pm "
                    pp.guardar_trainer(uaa)
                    gg.guarda_rutas(brr)


            elif opc1 == 3:
                    brr["Rutas"]["Java"]["U1"]["Trainer"] = documento
                    brr["Rutas"]["Java"]["U2"]["Trainer"] = documento
                    uaa["Trainers"][str(documento)]["Ruta"] = "Java"
                    uaa["Trainers"][str(documento)]["Salon"] = "Sputnik"
                    uaa["Trainers"][str(documento)]["Horario"] = "10:00 am a 2:00 pm y 6:00 pm a 10:00 pm "
                    pp.guardar_trainer(uaa)
                    gg.guarda_rutas(brr)
            else:
                print("Opción de ruta no válida")
    else:
        print("contraseña de trainer invalido")
        print("**************************************************")

bebesita()