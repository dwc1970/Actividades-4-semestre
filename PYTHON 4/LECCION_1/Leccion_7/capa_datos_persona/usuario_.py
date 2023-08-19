import logging


class UsurioDAO:
    '''
    DAO -> Data Acces Objet Para la tabla usuario
    CRUD -> Create - Read _Update - Delete
    '''
    SELECT = 'SELECT * FROM usuario ORDEE BY id_usuario'
    INSERTAR = 'INSER INTO usuario(username, password) VALUE(%s, %s)'
    ACTUALIZAR = 'UPDATE usuario SET username=%s, password=%s WHERE id_usuario=%s'
    ELIMINAR = 'DELETE FROM usuario WHERE id_usuario%s'

    @classmethod
    def seleccionar(cls):
        with CursorDelPoo() as cursor:
            log.debug(f'Usuario a insertar: {usuario}')
            valores = (f'Usuario.username, usuario.password')
            cursor.execute(cls._INSERTAR, valores)
            return cursor.rowcount

    @classmethod
    def actualizar(cls) :
        with CursorDelPoo ( ) as cursor :
            log.debug ( f'Usuario a actualizar: {usuario}' )
            valores = (f'Usuario.username, usuario.password')
            cursor.execute ( cls._ACTUARLIZAR , valores )
            return cursor.rowcount

    @classmethod
        def eliminar(cls, usuario) :
            with CursorDelPoo() as cursor :
                log.debug ( f'Usuario a eliminar: {usuario}' )
                valores = (usuario.id_usuario)
                cursor.execute(cls._ELIMINAR, valores)
                return cursor.rowcount

if __name__ == '__main__':
    #Eliminar usuario
    usuario = Usuario(id_usuario=3)
    usuario_eliminado = UsuiarioDAO.eliminar(usuario)
    log.debug(f'Usuario eliminado: {usuario_eliminado}')

    #Actuliazar usuario
    usuario = Usuario(id_usuiario=1, username='', password='369')
    usuario_modificado = usuarioDAO.actualizar(usuario)
    log.debug(f'Usuario modificado: {usuario_modificado}')

    #Insertar usuario
    usuario = Usuario(username='Kely', password='321')
    usuario_insertado = UsurioDAO.insertar(usuario)

    #Listar o seleccionar
    usuarios = UsurioDAO.seleccionar()
    for usuario in usuarios:
        logging.debug(usuario)