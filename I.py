'''@author: Juan Elier Rosales Rosas
Descripción: Programa que imprime + si el producto de los elementos en un rango es positivo, - si es negativo y 0 si es 0.
Entradas:
En la primera línea se encuentran dos enteros N y Q (1 <= N, Q <= 10^5) que representan el número de elementos y el número de consultas.
En la segunda línea se encuentran N enteros que representan los elementos del arreglo.
En las siguientes Q líneas se encuentran las consultas. Cada consulta es de la forma:
M A B: Donde A y B son enteros que representan el rango de elementos y M es la operación a realizar.
C I V: Donde I es un entero que representa la posición del elemento a actualizar y V es el nuevo valor del elemento.
'''
class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [1] * (2 * self.n)
        # Crear el Segment Tree con los signos de los elementos
        for i in range(self.n):
            self.tree[i + self.n] = self.sign(data[i])
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] * self.tree[2 * i + 1]
    
    #Función para obtener el signo de un número
    def sign(self, x):
        if x > 0:
            return 1
        elif x < 0:
            return -1
        else:
            return 0

    #Función para actualizar el valor de un elemento
    def update(self, index, value):
        index += self.n
        self.tree[index] = self.sign(value)
        while index > 1:
            index //= 2
            self.tree[index] = self.tree[2 * index] * self.tree[2 * index + 1]
    
    #Función para calcular el producto de los elementos en el rango [left, right)
    def product(self, left, right):
        left += self.n
        right += self.n + 1
        result = 1
        while left < right:
            if left % 2 == 1:
                result *= self.tree[left]
                left += 1
            if right % 2 == 1:
                right -= 1
                result *= self.tree[right]
            left //= 2
            right //= 2
        return result

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    n, q = map(int, data[0].split())
    arr = list(map(int, data[1].split()))
    
    # Crear el Segment Tree con los signos de los elementos
    seg_tree = SegmentTree(arr)
    
    output = []
    
    # Procesar las consultas
    for i in range(2, 2 + q):
        query = data[i].split()
        if query[0] == 'M':
            A, B = map(int, query[1:])
            product_sign = seg_tree.product(A - 1, B - 1)
            if product_sign > 0:
                output.append('+')
            elif product_sign < 0:
                output.append('-')
            else:
                output.append('0')
        elif query[0] == 'C':
            I, V = map(int, query[1:])
            seg_tree.update(I - 1, V)
    
    # Imprimir el resultado
    sys.stdout.write("\n".join(output) + "\n")

if __name__ == "__main__":
    main()

