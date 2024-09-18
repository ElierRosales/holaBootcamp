'''@author: Juan Elier Rosales Rosas
Descripción: Leer el numero que inserte el usuario y devolver la suma de los digitos
Entradas:
num= numero entre 1 y 100000. 

'''
def main():
    try:
        numero = int(input().strip())
        if 1 <= numero <= 100000:
            print(sum(int(digito) for digito in str(numero)))
        else:
            print(0)
    except ValueError:
        print(0)

if __name__ == "__main__":
    main()
