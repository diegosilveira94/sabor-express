""" 1 - Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade.
"""
pessoas = [{
    'Diego':{'nome':'Diego Silveira','idade':30,'cidade':'Joinville'}
}]
"""Instrutor:
pessoa = {'nome': 'Felipe', 'idade': 30, 'cidade': 'São Paulo'}
"""


"""
 2 - Utilizando o dicionário criado no item 1:
"""
# Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
print(f'Idade sem alteração: {pessoas[0]['Diego']['idade']}')
pessoas[0]['Diego']['idade'] = 31
print(f'Idade com alteração: {pessoas[0]['Diego']['idade']}')

# Adicione um campo de profissão para essa pessoa;
pessoas[0]['Diego']['profissão'] = "Desenvolvedor"
print(f'Adicionado campo de profissão{pessoas}')
      
# Remova um item do dicionário.
del pessoas[0]['Diego']['cidade']
print(pessoas)
"""Instrutor:
# Atualização de Idade
pessoa['idade'] = 31

# Adicionando Profissão
pessoa['profissao'] = 'Engenheiro'

# Remoção de Elemento
del pessoa['cidade']

"""

""" 3 - Crie um dicionário que relacione os números de 1 a 5 aos seus respectivos quadrados.
"""
quadrados_numeros = {}
numero = 0
for i in range(1,6):
    quadrados_numeros[i] = i ** 2
print(quadrados_numeros)
"""Instrutor:
numeros_quadrados = {x: x**2 for x in range(1, 6)}
print(numeros_quadrados)
"""

""" 4 - Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário. 
"""
clientes = [
    {'nome':'Ana Souza','idade': 25, 'cidade': 'Curitiba', 'profissão': 'Designer'},
    {'nome':'Carlos Lima','idade': 32, 'cidade': 'Recife', 'profissão': 'Engenheiro'},
    {'nome':'Mariana Rocha','idade': 28, 'cidade': 'São Paulo', 'profissão': 'Desenvolvedora'}
]
chave_pesquisada = 'sexo'
for cliente in clientes:
    cliente_pesquisado = 'Encontrado' if chave_pesquisada in cliente else 'Não encontrado'
    print(cliente)
print(f'{chave_pesquisada} : {cliente_pesquisado}')
""" Instrutor:
pessoa = {'nome': 'Amanda', 'idade': 19, 'cidade': 'São Luís'}
if 'nome' in pessoa:
    print("A chave 'nome' existe no dicionário.")
else:
    print("A chave 'nome' não existe no dicionário.")

"""

""" 5 - Escreva um código que conte a frequência de cada palavra em uma frase utilizando um dicionário.
"""
frase = 'A dedicação diária aliada à paciência transforma pequenos esforços em grandes conquistas mesmo quando os resultados demoram a aparecer e o caminho parece incerto confuso ou difícil de seguir'
frequencia = {}
palavras = frase.split()
for palavra in palavras:
    if palavra in frequencia:
        frequencia[palavra] += 1
    else:
        frequencia[palavra] = 1

print(frequencia)
"""Instrutor:
frase = "Python se tornou uma das linguagens de programação mais populares do mundo nos últimos anos."
contagem_palavras = {}
palavras = frase.split()
for palavra in palavras:
    contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1
print(contagem_palavras)
"""