'''@author: Juan Elier Rosales Rosas
Descripción: Programa que calcula el puntaje de dos palabras y determina quien gana.
Entradas:
2 lineas con palabras de longitud entre 1 y 100 caracteres.
1 cadena de caracteres que representa la palabra de Ana.
1 cadena de caracteres que representa la palabra de Carolina.
'''
def calcular_puntaje(word):
    score = 0
    for char in word:
        if char.isdigit():
            score += int(char)
        elif char.islower():
            # Definir puntaje para letras minusculas
            score += 10 + ord(char) - ord('a')
        elif char.isupper():
            # Definir puntaje para letras mayusculas
            score += 2 * (10 + ord(char.lower()) - ord('a'))
    return score

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    if len(data) != 2:
        print("Error: se esperaban exactamente dos líneas de entrada.")
        return
    
    # Leer las palabras
    ana_word = data[0].strip()
    carolina_word = data[1].strip()
    
    # Verificar que las palabras estén dentro del rango de longitud
    if not (1 <= len(ana_word) <= 100) or not (1 <= len(carolina_word) <= 100):
        print("Error: las longitudes de las palabras deben estar entre 1 y 100.")
        return

    # Calcular los puntajes
    ana_score = calculate_score(ana_word)
    carolina_score = calculate_score(carolina_word)
    
    # Determinar quien gano
    if ana_score > carolina_score:
        print(f"Ana {ana_score}")
    else:
        print(f"Carolina {carolina_score}")

if __name__ == "__main__":
    main()