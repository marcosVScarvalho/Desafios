import random
import string

class GeradorSenha:

    @staticmethod
    
    def gerar(comprimento = 8):
        caracteres = string.ascii_letters + string.digits + string.punctuation
        senha = ''.join(random.choice(caracteres) for _ in range (comprimento))
        return senha
    
print('Senha nova gerada:')
senha = GeradorSenha.gerar(12)
print(senha)
