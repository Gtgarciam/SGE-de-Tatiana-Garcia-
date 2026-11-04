
# Sistema de Gestion de Estudiantes

estudiantes = []
contador = 0
salir = False

while salir == False:

    print("\nSISTEMA DE GESTION DE ESTUDIANTES")
    print("1. Agregar estudiante")
    print("2. Mostrar estudiantes")
    print("3. Buscar estudiante por ID")
    print("4. Salir")

    opcion = input("Ingrese una opcion: ")

    match opcion:

        case "1":
            print("\nAGREGAR ESTUDIANTE")

            id = input("Ingrese el ID: ")
            nombre = input("Ingrese el nombre: ")

            try:
                nota = float(input("Ingrese la nota (0 a 5): "))

                if nota >= 0 and nota <= 5:
                    repetido = False

                    for estudiante in estudiantes:
                        if estudiante[0] == id:
                            repetido = True

                    if repetido == False:
                        estudiantes.append([id, nombre, nota])
                        contador = contador + 1
                        print("Estudiante agregado correctamente")
                    else:
                        print("El ID ya existe")
                else:
                    print("La nota debe estar entre 0 y 5")

            except ValueError:
                print("Debe ingresar una nota numerica")

        case "2":
            print("\nLISTA DE ESTUDIANTES")

            if contador == 0:
                print("No hay estudiantes registrados")
            else:
                suma = 0

                for estudiante in estudiantes:
                    print("ID:", estudiante[0])
                    print("Nombre:", estudiante[1])
                    print("Nota:", estudiante[2])
                    print("-------------------")

                    suma = suma + estudiante[2]

                promedio = suma / contador

                print("Total de estudiantes:", contador)
                print("Promedio del grupo:", round(promedio, 2))

        case "3":
            print("\nBUSCAR ESTUDIANTE")

            buscar = input("Ingrese el ID: ")
            encontrado = False

            for estudiante in estudiantes:
                if estudiante[0] == buscar:
                    print("Estudiante encontrado")
                    print("ID:", estudiante[0])
                    print("Nombre:", estudiante[1])
                    print("Nota:", estudiante[2])
                    encontrado = True

            if encontrado == False:
                print("Estudiante no encontrado")

        case "4":
            print("Gracias por utilizar el sistema")
            salir = True

        case _:
            print("Opcion incorrecta")

