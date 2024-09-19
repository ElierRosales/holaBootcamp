'''@author: Juan Elier Rosales Rosas
Descripción: Programa que calcula el puntaje de dos palabras y determina quien gana.
Entradas:
un entero N indicando la cantidad de codigos enviados.
N renglones con el formato: "participante problema puntaje" donde:
Participante representa identificador del participante (1 <= |Participante| <= 10^3).
problema representa el problema resuelto por el participante (A, B, C, D).
puntos es la cantidad de puntos obtenidos en el problema (0 <= puntos <= 100).
'''
def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')
    
    from collections import defaultdict
    
    # Leer la cantidad de códigos enviados
    N = int(data[0])
    
    # Diccionario para almacenar el mejor puntaje de cada participante en cada problema
    scores = defaultdict(lambda: defaultdict(int))
    
    # Leer los resultados y actualizar los mejores puntajes
    for i in range(1, N + 1):
        participant, problem, points = data[i].split()
        points = int(points)
        
        if points > scores[participant][problem]:
            scores[participant][problem] = points
    
    # Calcular el puntaje total para cada participante
    total_scores = {}
    for participant, problems in scores.items():
        total_scores[participant] = sum(problems.values())
    
    # Ordenar los participantes por puntaje total descendente, y en caso de empate por orden alfabético
    sorted_participants = sorted(total_scores.items(), key=lambda x: (-x[1], x[0]))
    
    # Imprimir los 4 mejores participantes
    for i in range(min(4, len(sorted_participants))):
        print(sorted_participants[i][0])

if __name__ == "__main__":
    main()

