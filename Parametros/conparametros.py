def mostrar_calificacion(nombre, materia, calificacion):
    print("----- CALIFICACIÓN -----")
    print("Alumno:", nombre)
    print("Materia:", materia)
    print("Calificación:", calificacion)

    if calificacion >= 7:
        print("Resultado: Aprobado")
    else:
        print("Resultado: Reprobado")

mostrar_calificacion("Rene", "Programación", 8.5)