def view_rounds(rounds):
    round_number = 1
    for one_round in rounds:
        print(f"\n Ronda numero {round_number} \n")
        print("{:<8} {:<6} {:<12} {:<8} {:<8}".format("Jugador", "Kills", "Asistencias", "Muertes", "Puntaje"))
        print("-" * 45)

        for player in one_round:
            data_player = one_round[player]
            # Calculo el puntaje total de cada jugador
            puntaje = (data_player['kills'] * 3) + (data_player['assists'] * 1) - (int(data_player['deaths']) * 1)
            print("{:<10} {:<6d} {:<12d} {:<7d} {:<8d}".format(player, data_player['kills'], data_player['assists'], data_player['deaths'], puntaje))
        
        round_number += 1