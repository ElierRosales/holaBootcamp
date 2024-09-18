'''@author: Juan Elier Rosales Rosas
Descripción: Leer la cadena de caracteres y escribir el numero de personas distintas que Antonio pudo haber visto
Entradas:
+ = persona entra
- = persona sale
Problema detectado: Como una persona puede salir y entrar arbitrareamente, el contador no aumenta hasta que se vea
"una persona diferente" esto porque la persona pudo: +-+- así que consideraremos esto como una sola persona
las secuencias que aumentaran son las secuencias donde se repiten entradas o salidas como: +++--- o -++- ya que una
persona no puede tener una doble entrada. 

'''
def _main(cadena):
    # Inicializamos variables
    current_people = 0
    max_people = 0
    people_inside = 0

    for action in cadena:
        if action == '+':
            current_people += 1
        elif action == '-':
            if current_people > 0:
                current_people -= 1
            else:
                people_inside += 1
        
        max_people = max(max_people, current_people)

    # Ajustamos people_inside para tener en cuenta las entradas que pueden haber cancelado las salidas
    people_inside = max(people_inside - current_people, 0)
    
    # Retornamos el número máximo de personas dentro + el número ajustado de salidas sin entradas registradas
    return max_people + people_inside

# Para leer los casos de prueba
while True:
    try:
        cadena = input().strip()
        if 1 <= len(cadena) <= 300:
            print(_main(cadena))
    except EOFError:
        break
    except Exception as e:
        print(f"Error: {e}")

