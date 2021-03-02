def check_char():
    print("Este programa devuelve un 0 si el valor ingresado es un caracter entre a-z")
    ch=" "                                                             #declaracion de la variable tipo string

    while ch != "0":                                                   #se termina si la variable es igual a 0
        ch=input("Ingrese un caracter entre a-z:  ")                   # asigma el valor nuevo a la variable ch
        
        if (ch>= 'a' and ch<= 'z') or (ch>= 'A' and ch<= 'Z'):         #delimita los rangos permitidos 
                
            if len (ch)>1:                                             # delimita que solo se ingrese un caracter
                print ("Ingresó más de 1 caracter, por favor ingresar solo 1 caracter")
                    
            else:
                ch="0";                                                # asigna el número 0 a la variable para que se termine el while
                print (ch)
        else :
            print ("Valor erroneo, ingresar solo letras")

def caps_switch():
    print("Este programa admite caracteres entre a-z y los cambia a may[usculas o viceversa")
    ch=" "                                                             #declaracion de la variable tipo string

    while ch != "0":                                                   #se termina si la variable es igual a 0
        ch=input("Ingrese un caracter entre a-z:  ")                   # asigma el valor nuevo a la variable ch
        
        if (ch>= 'a' and ch<= 'z') or (ch>= 'A' and ch<= 'Z'):         #delimita los rangos permitidos 
                
            if len (ch)>1:                                             # delimita que solo se ingrese un caracter
                print ("Ingresó más de 1 caracter, por favor ingresar solo 1 caracter")
                    
            else:           
               print (ch.swapcase())                                   #swapcase cambia de minuscula a mayuscula o viceversa a la variable
               ch="0";                                                 # asigna el número 0 a la variable para que se termine el while    
                    
        else :
            print ("Valor erroneo, ingresar solo letras")

        
