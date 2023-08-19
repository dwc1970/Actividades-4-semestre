class Usuario:
    def __init__(self, id_usuario=None, userneme=None, password=None):
        self._id_usuario = id_usuario
        self._username = userneme
        self._password = password

    def __str__(self):
        return  f'Usuiario: {self._id_usuario} {self._username} {self._password}'

    #Metodod Get y Set
    @property
    def id_usuario(self):
        return self._id_usuario

    @id_usuario.setter
    def id_usuario(self, id_usuario):
        self._id_usuario = id_usuario

    @property
    def username(self):
        return self._username
    @username
    def username(self, username):
        self._username = username

    @property
    def password(self):
        return self._password
    @password
    def password(self, password):
        return self._password = password

