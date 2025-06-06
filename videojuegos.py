videojuegos = []
plataformas = ("PC", "PS5", "Xbox Series X", "Nintendo Switch")

while True:
    print("\n---MENÚ DE VIDEOJUEGOS---")
    print("1. Registrar videojuego")
    print("2. Ver videojuego")
    print("3. Modificar videojuego")
    print("4. Eliminar videojuego")
    print("5. Salir")

    opcion = input("Seleccione una opcion (1-5):")
    try:
        if opcion == "1":
            pass
        elif opcion == "2":
            pass
        elif opcion == "3":
            pass
        elif opcion == "4":
            pass
        elif opcion == "5":
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida.")
        
            if opcion == "1":
                codigo = int(input("Ingrese el código del videojuego: "))
                nombre = input("Ingrese el nombre del videojuego: ")
                genero = input("Ingrese el nombre del videojuego: ")

                print("\nPlataformas disponibles:")
                print("1. PC")
                print("2. PS5")
                print("3. Xbox Series X")
                print("4. Nintendo Switch")

                plataforma_codigo = int(input("Seleccione el número de las plataforma: "))
                plataforma = plataformas[plataforma_codigo - 1]
                
                videojuego = {
                    "codigo": codigo,
                    "nombre": nombre,
                    "genero": genero,
                    "plataforma": plataforma
                }

                videojuegos.append(videojuego)
                print ("Videojuego registrado correctamente. ")

            elif opcion == "2":
                if len(videojuegos) == 0:
                    print("No hay videojuegos registrados.")
                else:
                    print("\n--- LISTA DE VIDEOJUEGOS ---")
                    for v in videojuegos: 
                        print (f"Codigo: {v['codigo']}, Nombre: {v['nombre']}, Género: {v['genero']}, Plataforma: {v['plataforma']}")

            elif opcion == "3":
                codigo = int(input("Ingrese el código del videojuego a modificar: "))
                encontrado = False
                for v in videojuegos:
                    if v["codigo"] == codigo:
                        v["nombre"] = input("Nuevo nombre: ")  
                        v["genero"] = input("Nuevo género: ")

                        print("\nPlataformas disponibles:")
                        print("\nPlataformas disponibles:")
                        print("1. PC")
                        print("2. PS5")
                        print("3. Xbox Series X")
                        print("4. Nintendo Switch")  

                        plataforma_codigo = int(input("Seleccione el número de las plataforma: "))
                        plataforma = plataformas[plataforma_codigo - 1]        

                        print("Videojuego modificado correctamente.")
                        encontrado = True
                        break
                if not encontrado:
                    print("Videojuego no encontrado.") 
                elif opcion == "4":
                    codigo = int(input("Ingrese el código del videojuego a eliminar: "))
                    eliminado = False
                    for v in videojuegos:
                        if v["codigo"] == codigo:
                            videojuegos.remove(v)
                            print("Videojuego eliminado correctamente.")
                            eliminado = True
                            break
                    if not eliminado:
                        print("Videojuego encontrado.")
                elif opcion == "5":
                    print ("Saliendo del programa.")
                    break
                else:
                    if opcion not in ["1", "2", "3", "4", "5"]:
                        print("Opción inválida, elige un número del 1 al 5.")                
    except:
        print("n¡UPS! ALGO SALIÓ MAL!")