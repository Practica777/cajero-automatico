print('\n *Cajero automático *\n')

def crear_cuenta(nombre, apellidos, dni, gmail, password):
    # Apartado para crear el usuario.
    lista_nombre = [], lista_apellidos = [], lista_dni = [], lista_gmail = [], lista_password = []
    lista_nombre.append(nombre), lista_apellidos.append(apellidos), lista_dni.append(dni), lista_gmail.append(gmail), lista_password.append(password)
    return lista_nombre, lista_apellidos, lista_dni, lista_gmail, lista_password
    

def iniciar_sesion():
    # Apartado de inicio de sesión
    

    
    
    
def menu():
    # Creando menú:
    print('\n * Crear cuenta * \n')
    
    print('[1]. Crear cuenta')
    print('[2]. Iniciar sesión')
    print('[3]. Retirar dinero')
    print('[4]. Depositar dinero')
    print('[5]. Transferir dinero')
    print('[6]. Cambiar contraseña')
    print('[7]. Salir')
    
    opcion = input('Escoja una opción: [1][2][3][4][5][6][7]> ')
    
    if opcion == 1:
        nombre = input('Nombres: ')
        apellidos = input('Apellidos: ')
        dni = input('DNI: ')
        gmail = input('Gmail: ')
        password = input('contraseña: ')
        crear_cuenta(nombre, apellidos, dni, gmail, password)
        print('\n * Cuenta creada exitosamente * \n')
        exit
    elif opcion == 2:
        
        
        
menu()

