def view_rounds(rounds):
    round_number = 1
    for one_round in rounds:
        print(f"\n Ronda numero{round_number} \n")
        print("{:<8} {:<6} {:<12} {:<8}".format("Jugador", "Kills", "Asistencias", "Muertes"))
        print("-" * 35)

        for player in one_round:
            data_player = one_round[player]
            print("{0:6} {1:5d} {2:8d} {3:9d}".format(player, data_player['kills'], data_player['assists'], data_player['deaths']))
        
        round_number += 1