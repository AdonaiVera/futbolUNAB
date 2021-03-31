#!/usr/bin/python3
"""
Author: Alhim Adonaí Vera Gonzalez
Date: 30/03/2021
TEST FORMADORES Y TUTORES CICLO 1
"""

from datetime import datetime

def check_number():
    """
    Validación de entrada de dato int
    """
    check=False
    num = 0
    while(not check):
        
        try:
            num = int(input("Introduce un numero entero: "))
            check=True
        except ValueError:
            print('Error, introduce un numero entero')

    return num

def check_date():
    """
    Validación de entrada de dato int
    """
    check=False
    date = datetime.now()
    while(not check):
        try:
            strInput = input("Introduce la fecha del partido en formato dd/mm/yyyy: ")
            date = datetime.strptime(strInput, "%d/%m/%Y")
            check=True
        except ValueError:
            print('Error, introduce una fecha valida con el siguiente formato %d/%m/%Y')

    return date
    


def order_algorithm(match_play):
    """
    Algoritmo de ordenamiento, fecha más reciente a mas antigua. 
    """
    match_old = match_play
    match_order = []
    for element in range(len(match_old)):
        maximo = max(match_old, key=lambda d: d["fecha"])
        maxIndex = match_old.index(maximo)
        match_order.append(match_old[maxIndex])
        match_old.pop(maxIndex)

    
    return match_order

def leaderboard(match_play):
    """
    Función encargada de mostrar la tabla de clasificación final por el equipo de la UNAB
    """
    nCountWin = 0
    nCountLoss = 0
    nCountDraw = 0
    nCountTotalPoint = 0
    for x in range(0,len(match_play)):
        if match_play[x]["gol_unab"] < match_play[x]["gol_rival"]:
            nCountLoss+=1
        elif match_play[x]["gol_unab"] > match_play[x]["gol_rival"]:
            nCountWin+=1
            nCountTotalPoint+=3
        else:
            nCountDraw+=1
            nCountTotalPoint+=1


    print("+-----------------------------+----------+")
    print("|TABLA DE CLASIFICACIÓN UNAB  | CANTIDAD |")
    print("+-----------------------------+----------+")
    print("|Partidos jugados             |{:>10}|".format(len(match_play)))
    print("|Partidos Ganados             |{:>10}|".format(nCountWin))
    print("|Partidos Empatados           |{:>10}|".format(nCountDraw))
    print("|Partidos Perdidos            |{:>10}|".format(nCountLoss))
    print("|Total puntos                 |{:>10}|".format(nCountTotalPoint))

    
def check_results(match_play):
    """
    Función encargada de mostrar los resultados de los partidos
    """
    match_order = order_algorithm(match_play)
    match_play = match_order
    print("*** RESULTADOS ***")
    print("+----------+--------------------------------+")
    print("|Fecha     |Equipo 1 Goles VS Goles Equipo 2|")
    print("+----------+--------------------------------+")
    for x in range(0,len(match_order)):
        print("|{:<10} - UNAB ({}) VS ({}) {:<14}|".format(match_order[x]["fecha"].strftime("%d-%m-%Y"), match_order[x]["gol_unab"],match_order[x]["gol_rival"], match_order[x]["NombreRival"]))
        print("+----------+--------------------------------+")

    return match_play
def register_play(match_play):
    """
    Función encargada de registrar nuevos juegos.
    """
    check = False
    print('Registro de nuevos partidos: ')
    while(not check):
        
        datePlay = check_date()
        
        strRival = input("Introduce el nombre del equipo Rival: ")
        print("Introduce la cantidad de goles del equipo Rival: ")
        gol_rival = check_number()
        print("Introduce la cantidad de goles del equipo UNAB")
        gol_unab = check_number()

        dict_match = {
        "fecha": datePlay,
        "NombreRival": strRival,
        "gol_rival": gol_rival,
        "gol_unab": gol_unab
        }

        match_play.append(dict_match)

        print("*** REGISTRO EXITOSO ***")
        print("--------------------- ------------ -------------------------")
        print ("1. Registrar un nuevo partido")
        print ("2. Volver al menu principal")
        return_option = check_number()
      
        if return_option == 1:
            print('-------- Nuevo registro --------')
        elif return_option == 2:
            check = True
        else:
            print('--- Opción invalida, regresando al menu principal ---')
            check = True

    return match_play

def main():  
    """
    Función principal
    """  
    exit_app = False
    option = 0
    match_play = []

    print("--------------------- ------------ -------------------------")
    print ("*** BIENVENIDOS AL TORNEO ASCUN 2021 POST COVID ***")
    
    
    while not exit_app:
        print("--------------------- ------------ -------------------------")
        print ("A continuación se visualiza el menu de acciones: ")
        print ("1. Registrar Partido")
        print ("2. Ver Resultados")
        print ("3. Tabla de Clasificación")
        print ("4. Salir")
        print("--------------------- ------------ -------------------------")
        
    
        option = check_number()
    
        if option == 1:
            match_play = register_play(match_play)
        elif option == 2:
            match_play = check_results(match_play)
        elif option == 3:
            leaderboard(match_play)
        elif option == 4:
            exit_app = True
        else:
            print ("Introduce un numero entre 1 y 4")

    print ("Cierre de la APP")


if __name__ == "__main__":
   main()