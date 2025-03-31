def view_rounds(rounds):
    mvp_counter = {}
    round_number = 1

    for one_round in rounds:
        print(f"\n Ronda numero {round_number} \n")
        print("{:<8} {:<6} {:<12} {:<8} {:<8}".format("Jugador", "Kills", "Asistencias", "Muertes", "Puntaje"))
        print("-" * 45)

        mvp = None
        max_points = -1

        for player in one_round:
            data_player = one_round[player]

            # Calculo el puntaje total de cada jugador
            points = (data_player['kills'] * 3) + (data_player['assists'] * 1) - (int(data_player['deaths']) * 1)
            print("{:<10} {:<6d} {:<12d} {:<7d} {:<8d}".format(player, data_player['kills'], data_player['assists'], data_player['deaths'], points))

            # Verifico si el jugador en el que estoy es el MVP
            if points > max_points:
                max_points = points
                mvp = player

        # Pregunto si mvp tiene algun valor y contabilizo la cantidad de veces que fue MVP
        if mvp:
            mvp_counter[mvp] = mvp_counter.get(mvp, 0) + 1
            print(f"\n MVP: {mvp} con {max_points} puntos")

        round_number += 1 
    return mvp_counter