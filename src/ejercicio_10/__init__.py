def ranking_round (rounds):
    """"""
    # Diccionario para ir acumulando los puntajes
    ranking = {}

    for one_round in rounds:
        for player in one_round:
            values_player = one_round[player]
            if player not in ranking:
                ranking[player] = {'kills': 0, 'assists': 0, 'deaths': 0}
        
            # Sumo sus estadísticas a los totales
            ranking[player]['kills'] += values_player['kills']
            ranking[player]['assists'] += values_player['assists']
            ranking[player]['deaths'] += int(values_player['deaths'])  # Convertimos bool a int, True 1 False 0
        
        # Imprime el ranking luego de cada ronda, ver como devolverlo al programa principal
        print("Ranking después de la ronda:", one_round+1, ranking)