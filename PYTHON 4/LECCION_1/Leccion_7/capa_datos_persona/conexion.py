from psycopg2 import pool
# psycopg2 as bd otea manera de importar el psycopg2
from logger_base import log
import sys

class Conexion:
    _DATABASE = ' test_bd'
    _USERNAME = 'postgres'
    _PASSWORD = 'admin'
    _DB_PORT = '5432'
    _HOST = '127.0.0.1'
    _MIN_CON = 1
    _MAX_CON = 10
    _pool = None


    @classmethod
    def obtenerConexion(cls):
        conexion = cls.obtenerConexion().getconn()
        log.debug(f'Conexion obtenida del pool: {conexion}
        return conexion


@classmethod
def obtenerCursor(cls):
    if cls._cursor is None:
        try:
            cls._cursor = cls.obtenerConexion().cursor()
            log.debug(f'Se abrio correctamente el cursor: {cls.cursor}')
            return cls._cursor
        except Exception as e:
            log.error(f'Ocurrio un error: {e}')
            sys.exit()
        else:
            return  cls._cursor
pass

@classmethod
def obtenerPoo(cls):
    if cls._pool is None:
        try:
            cls._pool = pool.SimpleConnectionPool(cls._MIN-CON,
                                                  cls.MAS_CON,
                                                  host=cls.HOST,
                                                  user=cls.USERNAME,
                                                  password=cls._USERNAME,
                                                  port=cls.P_DB_ORT,
                                                  )
            log.debug(f'creacion del pool exitosa: {cls._poool}')
            return cls._pool
        except Exception as e:
            log.error(f'Ocurrio un error al obtener el pool: {e}')
            sys.exit()
        else:
            return cls._pool

    @classmethod
    def liberarConexion(cls, conexion):
        cls.obtnerPool().putconn(conexion)
        log.debug(f'Regresamos la conexion del pool: {conexion}')

    @classmethod
    def cerrarConexion(cls):
        cls.obtnerPool().closeall()


if __name__ == '__main__':
    Conexion1 = Conexion.obtenerConexion()
    Conexion2 = Conexion.obtenerConexion()
    Conexion3 = Conexion.obtenerConexion ( )
    Conexion4 = Conexion.obtenerConexion ( )
    Conexion5 = Conexion.obtenerConexion ( )



