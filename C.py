'''@author: Juan Elier Rosales Rosas
Descripción: Indica la distancia maxima entre dos locales para colocar sucursales.
Entradas:
Un entero N (1 <= N <= 10^5) que representa el número de locales disponibles.
N enteros que representan las posiciones de los locales.
Un entero M (1 <= M <= N) que representa el número de sucursales que se planean abrir.
'''
def can_place_branches(locations, m, distance):
    # Coloca la primera sucursal en el primer local
    branches_placed = 1
    last_position = locations[0]
    
    # Recorre los locales para colocar las sucursales
    for i in range(1, len(locations)):
        if locations[i] - last_position >= distance:
            branches_placed += 1
            last_position = locations[i]
            if branches_placed == m:
                return True
    return False

# Función para calcular la máxima distancia entre dos locales
def max_distance(locations, m):
    locations.sort() 
    start = 1
    end = locations[-1] - locations[0]
    
    # Buscar la máxima distancia
    while start <= end:
        mid = (start + end) // 2
        if can_place_branches(locations, m, mid):
            start = mid + 1
        else:
            end = mid - 1
    return end

def main():
    # Leer el número de locales
    n = int(input())
    # Leer las posiciones de los locales
    locations = list(map(int, input().split()))
    # Leer el número de sucursales que se planean abrir
    m = int(input())
    
    # Calcular la máxima distancia
    score = max_distance(locations, m)
    print(score)

# Ejecución del código
if __name__ == "__main__":
    main()
