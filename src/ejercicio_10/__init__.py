def actualizar_mvp(mvp, mvp_counter, max_points):
    """Actualiza el diccionario contador de MVP"""
    # Pregunto si mvp tiene algun valor y contabilizo la cantidad de veces que fue MVP
    if mvp:
        mvp_counter[mvp] = mvp_counter.get(mvp, 0) + 1
        print(f"\n MVP: {mvp} con {max_points} puntos")

def search_mvp(one_round):
    """Determina el MVP de cada round"""
    mvp = None
    max_points = -1

    for player in one_round:
        data_player = one_round[player]
        points = calculate_score(data_player)

        # Verifico si el jugador en el que estoy es el MVP
        if points > max_points:
            max_points = points
            mvp = player

    return mvp, max_points

def calculate_score(data_player):
    """Calcula el puntaje de un jugador en un round"""
    return (data_player['kills'] * 3) + (data_player['assists'] * 1) - (int(data_player['deaths']) * 1)

def view_table(round_number, one_round):
    """Imprime la tabla con los datos de los rounds"""
    print(f"\n Ronda numero {round_number} \n")
    print("{:<8} {:<6} {:<12} {:<8} {:<8}".format("Jugador", "Kills", "Asistencias", "Muertes", "Puntaje"))
    print("-" * 45)

    for player in one_round:
        data_player = one_round[player]
        # Calculo el puntaje total de cada jugador
        points = calculate_score(data_player)
        print("{:<10} {:<6d} {:<12d} {:<7d} {:<8d}".format(player, data_player['kills'], data_player['assists'], data_player['deaths'], points))
 
def view_rounds(rounds):
    """Función que recorre los rounds e imprime los datos"""
    mvp_counter = {}
    round_number = 1

    for one_round in rounds:
        view_table(round_number, one_round)
        mvp, max_points = search_mvp(one_round)
        actualizar_mvp(mvp, mvp_counter, max_points)
        round_number += 1 

    return mvp_counter