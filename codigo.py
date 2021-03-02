def check_char(ch):
    print("Este programa devuelve un 0 si el valor ingresado es un caracter entre a-z")
                                                      
        
        
    if (ch>= 'a' and ch<= 'z') or (ch>= 'A' and ch<= 'Z'):         #delimita los rangos permitidos 
                                
        if len (ch)>1:                                             # delimita que solo se ingrese un caracter
            print ("Ingresó más de 1 caracter, por favor ingresar solo 1 caracter")
                                    
        else:
            return '0'
                                                            # asigna el número 0 a la variable para que se termine el while
            
    else :
        print ("Valor erroneo, ingresar solo letras")

def caps_switch(ch):
    print("Este programa admite caracteres entre a-z y los cambia a may[usculas o viceversa")
                                                               

    
                          
        
    if (ch>= 'a' and ch<= 'z') or (ch>= 'A' and ch<= 'Z'):         #delimita los rangos permitidos 
                
        if len (ch)>1:                                             # delimita que solo se ingrese un caracter
            print ("Ingresó más de 1 caracter, por favor ingresar solo 1 caracter")
                    
        else:           
            return (ch.swapcase())                                   #swapcase cambia de minuscula a mayuscula o viceversa a la variable
                                                                
                    
    else :
        print ("Valor erroneo, ingresar solo letras")

        
