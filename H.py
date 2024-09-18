'''@author: Juan Elier Rosales Rosas
Descripción: Leer el numero que inserte el usuario y devolver la suma de los digitos
Entradas:
num= numero entre 1 y 100000. 

'''
def sum_digitos(num):
    if 1 <= num <= 100000:
        return sum(int(digito) for digito in str(num))
    else:
        return 0

def main():
    try:
        print("Ingresa un número entre 1 y 100000:")
        num = int(input().strip())
        print(sum_digitos(num))
    except ValueError:
        print(0)

if __name__ == "__main__":
    main()
