'''@author: Juan Elier Rosales Rosas
Descripción: Dado el arreglo B determina el arreglo A tal que A[i] = B[i] xor B[i - 1] para 0 < i < n.
Entradas:
varios casos de prueba, cada uno con la siguiente estructura:
primera linea contiene un entero n (1 <= n <= 10^4) que representa la longitud del arreglo.
'''
def reconstruct_array(n, B):
    A = [0] * n
    A[0] = B[0]
    for i in range(1, n):
        A[i] = B[i] ^ B[i - 1]
    return A

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')
    
    i = 0
    results = []
    while i < len(data):
        n = int(data[i].strip())
        if n == 0:
            break
        i += 1
        B = list(map(int, data[i].strip().split()))
        i += 1
        
        # Reconstruir A a partir de B
        A = reconstruct_array(n, B)
        
        # Recopilar resultados para este caso
        results.append(" ".join(map(str, A)))
    
    # Imprimir resultados
    for result in results:
        print(result)

if __name__ == "__main__":
    main()