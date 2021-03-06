def check_char(ch):
    print("0 si el valor ingresado es un caracter entre a-z")
    if (ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z'):  # Delimita rangos de letras.
        if len(ch) > 1:  # Delimita que solo se ingrese un caracter.
            print("Ingresó más de 1 caracter, por favor ingresar solo 1 caracter")
        else:
            return '0'  # asigna el número 0 a la variable para que se termine el while
    else:
        print("Valor erroneo, ingresar solo letras")


def caps_switch(ch):
    print("Este programa admite caracteres entre a-z y los pasa a mayusculas o viceversa")
    if (ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z'):  # Delimita los rangos permitidos.
        if len(ch) > 1:  # Delimita que solo se ingrese un caracter.
            print("Ingresó más de 1 caracter, por favor ingresar solo 1 caracter")
        else:
            return (ch.swapcase())  # Swapcase pasa de min a mayus o viceversa.
    else:
        print("Valor erroneo, ingresar solo letras")
