'''@author: Juan Elier Rosales Rosas
Descripción: Programa que calcula el numero de cuadrados y rectangulos que se pueden formar en un table de NxN.
Entradas:
Un entero N (1 <= N <= 10^5) que representa el tamaño del tablero.
'''

# Función para calcular el número de cuadrados y rectángulos
def count_squares_and_rectangles(N):
    # Total de cuadrados
    total_squares = sum((N - k + 1) ** 2 for k in range(1, N + 1))
    
    # Total de rectángulos
    total_rectangles = (N * (N + 1) // 2) ** 2
    
    return total_squares, total_rectangles

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    #
    results = []
    for num in data:
        N = int(num)
        squares, rectangles = count_squares_and_rectangles(N)
        results.append(f"{squares} {rectangles}")
    
    print("\n".join(results))

if __name__ == "__main__":
    main()
