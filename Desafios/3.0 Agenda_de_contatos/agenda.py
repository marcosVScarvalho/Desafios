class Contato:
    def __init__(self,nome,telefone,email):
        self.nome = nome
        self.telefone = telefone
        self.email = email

    def __str__(self):
        return f'{self.nome} | {self.telefone} | {self.email}'
    
class Agenda:
    contatos = []

    def adicionar_contato(self, contato):
        self.contatos.append(contato)

    @classmethod
    def salvar_em_arquivo(cls):
        f = open('3.1 Salvar' , 'w')
        for contato in cls.contatos:
            f.write(contato.__str__() + '\n')

    def carregar_de_arquivo():
        f = open('Salvar')
        print(f.read())


contato = Contato("Ana", "11999999999", "ana@email.com")
agenda = Agenda()
agenda.adicionar_contato(contato)
agenda.salvar_em_arquivo()
