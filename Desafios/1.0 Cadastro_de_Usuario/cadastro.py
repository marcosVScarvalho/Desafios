class Usuario:
    def __init__(self,nome,email,idade):
        self.nome = nome
        self.email = email
        self.idade = idade
    
    def __str__(self):
        return f'{self.nome} | {self.email} | {self.idade}'
    
class SistemaCadastro:
    usuarios = []

    def adicionar_usuario(self,usuario):
        self.usuarios.append(usuario)
    
    @classmethod
    def listar_usuarios(cls):
        print (f'{'Nome'.ljust(25)} | {'Email'.ljust(25)} | {'idade'}')
        for usuario in cls.usuarios:
            print (f'{usuario.nome.ljust(25)} | {usuario.email.ljust(25)} | {usuario.idade} ')

usuario = Usuario("Camila", "camila@email.com", 25)
cadastro = SistemaCadastro()
cadastro.adicionar_usuario(usuario)
cadastro.listar_usuarios()
