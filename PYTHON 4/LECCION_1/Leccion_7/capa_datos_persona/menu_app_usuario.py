opcion = None
while opcion ! = 5:
    print('Opciones: ')
    print('1. Listar Usuiarios')
    print('2. Agregar Usuario')
    print('3. Modificar Usuario')
    print('4. Eliminar usuario')
    print('5. Salir')
    opcion = int( input('Digite la opcion (1-5):'))
    if opcion == 1:
        usuarios = UsuarioDAO.seleccionar()
        for usuario in usuarios:
            log.info(usuario)
    elif opcion == 2:
        username_var = input('Digite el nombre del usuario:')
        password_var = input('Digite su contraseña: ')
        usuario = Usuario(username =username_var, password = password_var)
        usuario_insertado = UsuarioDAO.insertar(usuario)
        log.info(f'Usuario insertado: {usuario_insertado}')

    elif opcion == 23
        id_usuario_var = input ( 'Digite el id del usuario a modificar:' )
        username_var = input ( 'Digite el nombre del usuario a modificar:' )
        password_var = input ( 'Digite la contraseña del usuario a modificar : ' )
        usuario = Usuario(id_usuario=id_usuario_var, username=username_var , password=password_var )
        usuario_insertado = UsuarioDAO.actualizar( usuario )
        log.info ( f'Usuario actualizado: {usuario_actualizado}' )

else:
    log.info('Salimos de la aplicacion, Hasta pronto !! ')

    # Terminar las opciones que faltan 
