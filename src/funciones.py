def iniciar_contador(rounds,total_scores,rounds_won,best_round):
    for participante in rounds[0]['scores'].keys():
        total_scores[participante] = 0
        rounds_won[participante] = 0
        best_round[participante] = 0
        
def print_position_round(round_scores, rounds_won):
    order = sorted(round_scores, key=lambda x: round_scores[x], reverse=True)
    winner_round = order[0]
    
    print(f'Ganador: {winner_round} ({round_scores[winner_round]} pts)')
    rounds_won[winner_round] += 1
    print('Tabla de posiciones')
    
    for i,participante in enumerate(order, start=1):
        print(f' {i} -  {participante}')
        
def print_final_position(total_scores, rounds_won, best_round, rounds):
    print("\nTabla de posiciones final:")
    print(f"{'Participante':<12} {'Puntaje':>8} {'Rondas gan.':>12} {'Mejor ronda':>12} {'Promedio':>9}")
    print("-" * 55)

    order = sorted(total_scores, key = lambda x:total_scores[x], reverse = True)

    for participante in order:
        promedio = total_scores[participante] / len(rounds)
        print(f'{participante:<12} {total_scores[participante]:>8} {rounds_won[participante]:>12}{best_round[participante]:>12} {promedio:>9.2f}')