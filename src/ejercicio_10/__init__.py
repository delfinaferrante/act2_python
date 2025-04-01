def view_final_ranking(final_ranking):
    """Imprime el ranking final en orden decreciente"""
    print("\n Ranking Final \n")
    print("{:<8} {:<6} {:<12} {:<8} {:<8} {:<6}".format("Jugador", "Kills", "Asistencias", "Muertes", "MVPs", "Puntos"))
    print("-" * 50)
    
    # Ordeno de forma decreciente el ranking en relación a los puntos totales
    ranking_ord = sorted(final_ranking.items(), key=lambda x: x[1]['points'], reverse=True)

    for player, data_player in ranking_ord:
        print("{:<10} {:<6d} {:<12d} {:<7d} {:<8d} {:<6d}".format(player, data_player['kills'], data_player['assists'], data_player['deaths'], data_player['count_mvp'], data_player['points']))
    
    print("-" * 50)

def add_mvp_ranking(final_ranking, mvp_counter):
    """Agrega al ranking la cantidad de veces que un jugador fue MVP"""
    # Recorro las claves del ranking, que son los jugadores
    for player in mvp_counter:
        count = mvp_counter[player]
        if player in final_ranking:
            final_ranking[player]['count_mvp'] = count

def actualizar_ranking(one_round, final_ranking):
    """Actualiza el diccionario con el ranking final de los jugadores. Acumula sus puntos"""
    for player in one_round:
        data_player = one_round[player]

        if player not in final_ranking:
            final_ranking[player] = {'kills': 0, 'assists': 0, 'deaths': 0, 'count_mvp': 0, 'points': 0}

        final_ranking[player]['kills'] += data_player['kills']
        final_ranking[player]['assists'] += data_player['assists']
        final_ranking[player]['deaths'] += int(data_player['deaths'])
        final_ranking[player]['points'] += calculate_score(data_player)

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
    """Función que recorre los rounds, imprime los datos y devuelve contador de mvp y ranking final"""
    mvp_counter = {}
    final_ranking = {}
    round_number = 1

    for one_round in rounds:
        view_table(round_number, one_round)
        mvp, max_points = search_mvp(one_round)
        actualizar_mvp(mvp, mvp_counter, max_points)
        actualizar_ranking(one_round, final_ranking)
        round_number += 1 

    add_mvp_ranking(final_ranking, mvp_counter)
    #view_final_ranking(final_ranking)
    #return mvp_counter
    return mvp_counter, final_ranking