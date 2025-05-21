class Usuario():
    def __init__(self,nome,email,idade):
        self.nome = nome
        self.email = email
        self.idade = idade
    
    def __str__(self):
        return f'{self.nome} | {self.email} | {self.idade}'
    
class SistemaCadastro():
    usuarios = []

    def adicionar_usuario(self,usuario):
        self.usuarios.append(usuario)
    
    def listar_usuarios(self):
        print (f'{'Nome'.ljust(25)} | {'Email'.ljust(25)} | {'idade'}')
        for usuario in SistemaCadastro.usuarios:
            print (f'{usuario.nome.ljust(25)} | {usuario.email.ljust(25)} | {usuario.idade} ')

usuario = Usuario("Camila", "camila@email.com", 25)
cadastro = SistemaCadastro()
cadastro.adicionar_usuario(usuario)
cadastro.listar_usuarios()
