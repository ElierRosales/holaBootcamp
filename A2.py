'''@author: Juan Elier Rosales Rosas
Descripción: Mejorando el codigo.

'''
def calcular_minimo_personas(secuencia):
    max_personas = 0
    personas_actuales = 0
    for char in secuencia:
        if char == '+':
            personas_actuales += 1
            max_personas = max(max_personas, personas_actuales)
        elif char == '-':
            personas_actuales -= 1
    # Ajustamos personas_actuales para tener en cuenta las salidas que no tienen entradas registradas
    return max(max_personas, 1)

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    resultados = []
    for secuencia in data:
        resultado = calcular_minimo_personas(secuencia)
        resultados.append(str(resultado))
    
    print("\n".join(resultados))

if __name__ == "__main__":
    main()