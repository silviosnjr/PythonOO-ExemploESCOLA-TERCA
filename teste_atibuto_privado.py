class User :
    def __init__(self, username, password):
        self.usuario = username
        self.senha = password


usuarioSilvio = User("silviosnjr", "9998")

print(usuarioSilvio.usuario, usuarioSilvio.senha)