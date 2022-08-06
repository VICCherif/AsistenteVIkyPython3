from usuarios import acciones

hazEl = acciones.Acciones()

while True:
    accion = input("¿Que quieres hacer? : ")
    if accion == "registro":
        hazEl.registro()
    elif accion == "Entrar":
        hazEl.login()
    else:
        print("la opcion ingresada no existe")
    if accion == "registro" or accion == "Entrar":
        break