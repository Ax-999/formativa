import externo as rd

turistas = {
    "001": ["John Doe", "Estados Unidos", "12-01-2024"],
    "002": ["Emily Smith", "Estados Unidos", "23-03-2024"],
    "012": ["Julian Martinez", "Argentina", "19-09-2023"],
    "014": ["Agustin Morales", "Argentina", "28-03-2024"],
    "005": ["Carlos Garcia", "Mexico", "10-05-2024"],
    "006": ["Maria Lopez", "Mexico", "08-12-2023"],
    "007": ["Joao Silva", "Brasil", "20-06-2024"],
    "003": ["Michael Brown", "Estados Unidos", "05-07-2023"],
    "004": ["Jessica Davis", "Estados Unidos", "15-11-2024"],
    "008": ["Ana Santos", "Brasil", "03-10-2023"],
    "010": ["Martin Fernandez", "Argentina", "13-02-2023"],
    "011": ["Sofia Gomez", "Argentina", "07-04-2024"],
}
opcion = ""
while opcion != 4:
    opcion = rd.menu()
    if opcion == "4":
        print("Programa terminado")
        break
    elif opcion == "1":
        print("Turista por pais")
        pais = input("Ingrese pais: ")
        rd.turista_por_pais(turistas,pais)
    elif opcion == "2":
        print("Turista por mes")
        while True:
            mes = input("Ingrese mes a buscar [1-12]: ")
            try:
                if int(mes) >=1 and int(mes) <= 12:
                    break
                else:
                    print("Debe ser un valor entre 1 y 12")
            except:
                print("Debe ser un numero")
        print(f"El numero de turista en ese mes equivale al {rd.turista_Por_Mes(turistas,mes)}% del total")
    elif opcion == "3":
        print("Eliminar turistas")
        turistas = rd.eliminarTurista(turistas)
        print(turistas)
    else:
        print("Opcion no existe")