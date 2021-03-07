def requisitos(cadena: str, nums: set, alfabeto: set, iniciales: list, matricula: str):
    # Se define un metodo llamado requisitos.
    checkpoint = False
    x = 1
    # El primer requisito es comprobar que el primer index (caracter)
    # sea un numero
    if not cadena:
        return False

    if cadena[0] not in nums:
        return False
    # El segundo requisito comprobar cualquier combinación de letras y dígitos intermedia,
    # válidos en elalfabeto
    while x < len(cadena):
        if cadena[x] not in alfabeto and cadena[x] not in nums:
            return False
        # Tercer requisito que la cadena contenga tus iniciales en forma consecutiva al menos una vez.
        if not checkpoint:
            if cadena[x] in iniciales and x != (len(cadena) - 1):
                if iniciales.index(cadena[x]) != (len(iniciales) - 1) and (
                        cadena[x + 1] == iniciales[iniciales.index(cadena[x]) + 1]):
                    checkpoint = True
        # Quinto requsito que acepte puntos intermedios,pero no en forma consecutiva.
        if cadena[x] == '.':
            if cadena[x + 1] == '.':
                return False
        x += 1
    # Cuarto requsito que  la  cadena  contengacomo  últimos  símbolos  un  punto  seguido  de  tu  número de
    # matrículacompleto.
    tokens = cadena.split('.')
    return tokens[-1] == matricula and checkpoint


def main():
    checkpoint = 'A'

    # ingresar nombre
    nombre = input("Deme un nombre: ")
    matricula = input("Deme una matricula: ")

    alfabeto = list(set(nombre + matricula))
    print(alfabeto)

    alfabeto = set(nombre.lower().lstrip())
    alfabeto.add('.')
    nums = set(matricula)
    iniciales = [tokens[0] for tokens in nombre.lower().split(' ')]

    while checkpoint == 'A':
        cadena = input("Introduzca una cadena: ")

        # comprobacion con el metodo requsitos
        if requisitos(cadena, nums, alfabeto, iniciales, matricula):
            print("Cadena Valida! ")
        else:
            print("Cadena invalida! ")

        while True:
            checkpoint = input("¿Quiere seguir analizando cadenas? (A = Si, B = No): ")
            checkpoint = checkpoint.upper()

            if checkpoint in ('A', 'B'):
                break
            print("Intente de nuevo...")


if __name__ == "__main__":
    main()
