# Desafios
# Desafio 1
class Cliente:
    clientes = []
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone
        Cliente.clientes.append(self)

    def __str__(self):
        return f'Nome: {self.nome} | Telefone: {self.telefone}'

    def listar_clientes():
        print(f'{'Nome'.ljust(25)} | {'Telefone'}')
        for cliente in Cliente.clientes:
            print(f'{cliente.nome.ljust(25)} | {cliente.telefone}')

cliente1 = Cliente(nome='Diego', telefone='(47)99698-0218')
cliente2 = Cliente('Ranna', '(47)99950-1087')
# Cliente.listar_clientes()

# Desafio 2
class Pessoa:
    pessoas = []
    def __init__(self, nome='', idade=0, profissao=''):
        self.nome = nome.title()
        self.idade = idade
        self.profissao = profissao.title()
        Pessoa.pessoas.append(self)

    def __str__(self):
        return f'Nome: {self.nome} | Idade: {self.idade} | {self.profissao}' 

    @property
    def saudacao(self):
        if self.profissao:
            return f'Olá sou {self.nome}! Eu trabalho como {self.profissao}'
        else:
            return f'Olá sou {self.nome}!'
    
    def aniversario(self):
        self.idade += 1
'''
# Criando 3 instâncias da classe Pessoa
pessoa1 = Pessoa(nome='Alice', idade=25, profissao='Engenheira')
pessoa2 = Pessoa(nome='Luiza', idade=30, profissao='Desenvolvedor')
pessoa3 = Pessoa(nome='Jaque', idade=22)

# Imprimindo informações iniciais
print("Informações Iniciais:")
print(pessoa1)
print(pessoa2)
print(pessoa3)
print()

# Utilizando o método de instância aniversario para aumentar a idade de uma pessoa
pessoa1.aniversario()
pessoa3.aniversario()

# Imprimindo informações após aniversário
print("Informações após aniversário:")
print(pessoa1)
print(pessoa3)
print()

# Utilizando o método de classe saudacao para exibir mensagens personalizadas
print(pessoa1.saudacao)
print(pessoa2.saudacao)
print(pessoa3.saudacao)
'''
# Desafio 3
class ContaBancaria:
    def __init__(self, titular='', saldo=0):
        self.titular = titular.title()
        self._saldo = saldo
        self._ativo = False

    def __str__(self):
        return f'Titular: {self.titular} | Saldo: R${self._saldo} | Status: {self._ativo}'
    
    @classmethod
    def ativar_conta(cls, conta):
        conta._ativo = True
'''
# Criando 2 instâncias da classe ContaBancaria
conta1 = ContaBancaria(titular='Diego Silveira', saldo=500)
conta2 = ContaBancaria(titular='Ranna Silveira', saldo=1000)

# Imprimindo informações iniciais
print("Informações Iniciais:")
print(conta1)
print(conta2)
print()

# Ativar conta
conta3 = ContaBancaria(titular='Carlos', saldo=200)
print(f'Antes de ativar: Conta ativa? {conta3._ativo}')
ContaBancaria.ativar_conta(conta3)
print(f'Depois de ativar: Conta ativa? {conta3._ativo}')
'''

# Desafio 3
class ContaBancariaPythonica:
    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False

    @property
    def titular(self):
        return self._titular

    @property
    def saldo(self):
        return self._saldo

    @property
    def ativo(self):
        return self._ativo

'''
# 5) Crie uma instância da classe e imprima o valor da propriedade titular.    
conta4 = ContaBancaria(titular='Diego Silveira', saldo=500)
print(f"Titular da conta 4: {conta4.titular}")
'''
# Desafio 4
class ClienteBanco:
    def __init__(self, nome, idade, endereco, cpf, profissao):
        self.nome = nome.title()
        self.idade = idade
        self.endereco = endereco.upper()
        self.cpf = cpf
        self.profissao = profissao.title()

    @classmethod
    def criar_conta(cls, titular, saldo_inicial):
        conta = ContaBancariaPythonica(titular, saldo_inicial)
        return conta

'''
cliente1 = ClienteBanco("Ana", 30, "Rua A", "123.456.789-01", "Backend")
cliente2 = ClienteBanco("Luiza", 25, "Rua B", "987.654.321-01", "Estudante")
cliente3 = ClienteBanco("Vinny Neves", 40, "Rua C", "111.222.333-44", "Frontend")

conta_cliente1 = ClienteBanco.criar_conta("Ana", 2000)
print(f"Conta de {conta_cliente1.titular} criada com saldo inicial de R${conta_cliente1.saldo}")
'''

# Desafio 5
class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo.title()
        self.autor = autor.title()
        self.ano_publicacao = ano_publicacao
        self.disponivel = True

    def __str__(self):
        return f' Título: {self.titulo} | Autor: {self.autor} | Ano de publicação: {self.ano_publicacao} | Status: {self.disponivel}'
    
    def emprestar(self):
        self.disponivel = not self.disponivel

    @staticmethod
    def verificar_disponibilidade(ano):
        livros_disponiveis = [livro for livro in Livro.livros if livro.ano_publicacao == ano and livro.disponivel]
        return livros_disponiveis





