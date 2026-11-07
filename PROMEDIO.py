#Sistema De Gestion de Estudiantes

from unittest import case


Ids=[]
Nombres=[]
Edades=[]
Carreras=[] 
Notas=[]

contador=0
bandera=True

while bandera==True:
    print("\nSistema de gestion de estudiantes")
    print("1. Agregar estudiante")
    print("2. Mostrar estudiantes")
    print("3. Buscar estudiante por ID")
    print("4. Salir")

    try:
        opcion = int(input("Ingrese una opción: "))
    except ValueError:
        print("Error Ingrese un número válido")
        continue 
    match opcion:
        case 1:
            print("\nregistro de estudiante")

            try:
                id_estudiantenuevo = int(input("Ingrese el ID del estudiante: "))
            except ValueError:
                print("Error: ID no válido")
                continue

            id_estingresado = False
            for documento in Ids:
                if documento == id_estudiantenuevo:
                   id_estingresado = True
                   break
            if id_estingresado==True:
                print("Error: El ID ya está registrado")
            else:
                nombre_estudiantenuevo = input("Ingrese el nombre completo del estudiante: ")
                while  nombre_estudiantenuevo=="":
                    print("Error: El nombre no puede estar vacío")
                    nombre_estudiantenuevo = input("Ingrese el nombre completo del estudiante: ")
                try:
                    edad_estudiantenuevo = int(input("Ingrese la edad del estudiante: "))
                except ValueError:
                    print("Error: Edad no válida")
                    continue
                while edad_estudiantenuevo<0:
                    print("Error: La edad no puede ser negativa")
                    try:
                        edad_estudiantenuevo = int(input("Ingrese la edad del estudiante: "))
                    except ValueError:
                        print("Error: Edad no válida")
                        continue
                carrera_estudiantenuevo = input("Ingrese la carrera del estudiante: ")
                while carrera_estudiantenuevo=="":
                    print("Error: La carrera no puede estar vacía")
                    carrera_estudiantenuevo = input("Ingrese la carrera del estudiante: ")
                try:
                    nota_estudiantenuevo = float(input("Ingrese la nota del estudiante: "))
                except ValueError:
                    print("Error: Nota no válida")
                    continue
                while nota_estudiantenuevo<0 or nota_estudiantenuevo>5:
                    print("Error: La nota debe estar entre 0 y 5")
                    try:
                        nota_estudiantenuevo = float(input("Ingrese la nota del estudiante: "))
                    except ValueError:
                        nota=-1
                        
                Ids.append(id_estudiantenuevo)
                Nombres.append(nombre_estudiantenuevo)
                Edades.append(edad_estudiantenuevo)
                Carreras.append(carrera_estudiantenuevo)
                Notas.append(nota_estudiantenuevo)

                contador+=1
                print("\nEstudiante registrado exitosamente")
                print("Total de estudiantes registrados:", contador)

        case 2:       
            print("\nLista de estudiantes")
            if contador==0:
                print("No hay estudiantes registrados") 
            else:
                sumatoria = 0
            for i in range(contador):
                print("ID:", Ids[i])
                print("Nombre completo:", Nombres[i])
                print("Edad:", Edades[i])
                print("Carrera:", Carreras[i])
                print("Nota:", Notas[i])
                print("-------------------")
                if Notas[i]>=3.0:
                 print("El estudiante ha aprobado")  
                else:
                    print("El estudiante ha reprobado")

                sumatoria+=Notas[i]
                promedio=sumatoria/contador
                print("Total de estudiantes:", contador)
                print("Sumatoria del grupo:", round(sumatoria, 2))
                print("Promedio del grupo:", round(promedio, 2))
                
        case 3:
    
            print("\nBUSCAR ESTUDIANTE POR ID")
            
            buscar = input("Ingrese el ID: ").strip()
            encontrado = False
            for i in range(contador):
                if str(Ids[i]).strip() == buscar:
                    print("Estudiante encontrado")
                    print("ID:", Ids[i])
                    print("Nombre:", Nombres[i])
                    print("Edad:", Edades[i])
                    print("Carrera:" , Carreras[i])
                    print("Nota:", Notas[i])
                    encontrado = True
                    break   
            
            if encontrado == False:
                            print("Estudiante no encontrado")
            
        case 4:
            print("Saliendo del sistema. Gracias por utilizar nuestro programa.")
        case _:
            print("Opción inválida. Por favor, ingrese un número del 1 al 4.")