'''@author: Juan Elier Rosales Rosas
Descripción: Programa que imprime el orden en que las personas deben ser atendidas en una fila de acuerdo a las restricciones dadas.
Entradas:
Un entero N (1 <= N <= 10^5) que representa el número de personas en la fila.
N líneas con dos cadenas A y B que representan que la persona A debe ser atendida antes que la persona B.
'''
def main():
    # Leer el tipo de consulta
    import sys
    input = sys.stdin.read
    from collections import defaultdict, deque

    data = input().strip().split('\n')
    
    N = int(data[0].strip())
    if N == 1:
        return

    # Crear el grafo dirigido
    adj_list = defaultdict(list)
    in_degree = defaultdict(int)
    
    people = set()
    
    for line in data[1:]:
        A, B = line.split()
        adj_list[B].append(A)
        in_degree[A] += 1
        people.add(A)
        people.add(B)
    
    # Encontrar el nodo inicial (sin aristas entrantes)
    start = None
    for person in people:
        if in_degree[person] == 0:
            start = person
            break

    # Recorrer el grafo en anchura
    result = []
    queue = deque([start])
    
    while queue:
        current = queue.popleft()
        result.append(current)
        for neighbor in adj_list[current]:
            queue.append(neighbor)
    
    # Imprimir el orden de las personas
    for person in result:
        print(person)

if __name__ == "__main__":
    main()
