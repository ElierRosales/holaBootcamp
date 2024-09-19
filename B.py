'''@author: Juan Elier Rosales Rosas
Descripción: Programa que calcula la cantidad de pasos que se deben dar para salir de un laberinto numerico.
Entradas:
2 enteros N y M (1 <= N, M <= 50) que representan el tamaño del laberinto.
2 enteros x0 y y0 (1 <= x0 <= N, 1 <= y0 <= M) que representan la posición inicial.
N filas con M enteros cada una (0 <= labi,j <= 15) que representan el laberinto.
'''
from collections import deque

def main():
    # Definir direcciones y movimientos
    dx = [0, -1, 0, 1]
    dy = [-1, 0, 1, 0]
    movement = [1, 2, 4, 8]  # Paredes: izquierda, arriba, derecha, abajo

    # Leer tamaño de arreglo
    print("Indique el tamaño del arreglo (dos valores separados por un espacio)")
    N, M = map(int, input().split())
    
    # Verificar que N y M estén en los límites correctos
    if not (0 <= N <= 50 and 0 <= M <= 50):
        print(-1)
        return
    
    print("Indique la posición inicial (dos valores separados por un espacio)")
    x0, y0 = map(int, input().split())
    
    # Ajustamos las coordenadas x0 y y0 para que sean índices base 0
    x0 -= 1
    y0 -= 1

    # Función para validar si una celda está dentro del laberinto
    def validate(x, y):
        return 0 <= x < N and 0 <= y < M

    # Función para verificar si una celda es salida
    def exit(x, y, value):
        if y == 0 and not (value & 1):  # Pared izquierda
            return True
        if x == 0 and not (value & 2):  # Pared arriba
            return True
        if y == M - 1 and not (value & 4):  # Pared derecha
            return True
        if x == N - 1 and not (value & 8):  # Pared abajo
            return True
        return False

    # Verificar que la posición inicial esté dentro del laberinto
    if not validate(x0, y0):
        print(-1)
        return
    
    # Crear el laberinto
    maze = []
    for _ in range(N):
        row = list(map(int, input().split()))
        # Verificar que cada valor de la fila esté en el rango 0 <= labi,j <= 15
        if any(not (0 <= value <= 15) for value in row):
            print(-1)
            return
        maze.append(row)

    # Algoritmo de búsqueda Breadth-first search (BFS)
    visited = [[False] * M for _ in range(N)]
    tale = deque([(x0, y0, 0)])  # (x, y, pasos)
    visited[x0][y0] = True

    while tale:
        x, y, steps = tale.popleft()
        value = maze[x][y]
        
        # Verificar si es una salida
        if exit(x, y, value):
            print(steps)
            return
        
        # Intentar moverse en las 4 direcciones
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            # Verificar si es posible moverse en esta dirección
            if validate(nx, ny) and not visited[nx][ny] and not (value & movement[i]):
                visited[nx][ny] = True
                tale.append((nx, ny, steps + 1))
                
    # En caso de no encontrar salida
    print(-1)

if __name__ == "__main__":
    main()
