import logging
from logger_base impor log
from conexion import Conexion
class CursorDelPool:
    def __init__(self):
        self._conexion = None
        self._cursor = None

    def __enter__(self):
        logging.debug('Inicio del metodo with __enter__')
        self._conexion =Conexion.obtenerConexion()
        self._cursor = self._conexion.cursor()
        return  self._cursor

    def __exit__(self, tipo_exeption, valor_execption, detalle_exeption):
        log.debubg('se ejecuta el metodo exit')
        if valor_execption:
            self._conexion.rollback()
            log.debubg(f'Ocurrio una exeopcion: {valor_execption}')
        else:
            self._conexion.commit()
            log.debug('commit de la transaccion')
        self._cursor.close()
        Conexion.liberarConexion(self._conexion)


        if __name__ =='__main__':
            with CursorDelPool() as cursor:
            log.debubg('Dentro del bloquewith')
            cursor.execute('SELECT * FROM persona')
            log.debug(cursor.fetchall())




