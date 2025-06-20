def menu():
    print("Menu principal")
    print("1- turista por pais")
    print("2- turista por mes")
    print("3- eliminar turista")
    print("4- Salir")
    op = input("==|== ")
    return op 

def turista_por_pais(diccionario_turista,pais):
    lista = []
    for key in diccionario_turista:
        if diccionario_turista[key][1].upper() == pais.upper():
            lista.append(diccionario_turista[key][0])
    if len(lista) == 0:
        print("No hay turistas de pais")
    else:
        print(lista[:])

def turista_Por_Mes(turista_mes,mes):
    if len(mes) == 1:
        mes = "0" + mes
    contador = 0
    for key in turista_mes:
        fecha = turista_mes[key][2]
        m = fecha[3:5]
        if mes == m:
            contador +=1
    try:
        promedio = round((contador/len(turista_mes))*100,1)
    except:
        print("El diccionario esta vacio")
        return 0
    return promedio
    
def eliminarTurista(eliminar_turista):
    nombre = input("Ingrese el nombre del turista que desee eliminar ")
    for key in eliminar_turista:
        if eliminar_turista[key][0].upper() == nombre.upper():
            del eliminar_turista[key]
            print("Turista eliminado")
            break
    else:
        print("Turista No encontrado no se puedo eliminar")
    return eliminar_turista