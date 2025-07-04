"""1 - Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o número é par ou ímpar.
"""
def numero_impar_par(numero):
    print(f'\n Número digitado: {numero}')
    if numero % 2 == 0:
        print(' O número digitado é par')
    else:
        print(' O número digitado é ímpar')
numero_impar_par(21)

"""2 - Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar a idade em categorias de acordo com as seguintes condições:

    Criança: 0 a 12 anos;
    Adolescente: 13 a 18 anos;
    Adulto: acima de 18 anos. """

def classificar_pessoas(idade):
    print(f'\n Idade informada: {idade}')
    if (idade >= 0 and idade <= 12):
        print(' Você é uma criança')
    elif (idade > 12 and idade <=18):
        print(' Você é um adolescente')
    elif (idade > 18 and idade <= 120):
        print(' Você é um adulto')
    else:
        print('Digite uma idade válida')
classificar_pessoas(20)

""" 3 - Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você.
"""

def validar_senha(usuario, senha):
    print(f'\n Usuário digitado: {usuario}')
    print(f' Senha digitada: {senha}')
    if(usuario != 'Harry Potter'):
        print(' O usuário está incorreto.')
    if(senha != 'Edwiges@10'):
        print(' A senha está incorreta')
validar_senha(usuario='Diego', senha='Pandora@65')

"""4 - Solicite ao usuário as coordenadas (x, y) de um ponto qualquer e utilize uma estrutura if elif else para determinar em qual quadrante do plano cartesiano o ponto se encontra de acordo com as seguintes condições:

    Primeiro Quadrante: os valores de x e y devem ser maiores que zero;
    Segundo Quadrante: o valor de x é menor que zero e o valor de y é maior que zero;
    Terceiro Quadrante: os valores de x e y devem ser menores que zero;
    Quarto Quadrante: o valor de x é maior que zero e o valor de y é menor que zero;
    Caso contrário: o ponto está localizado no eixo ou origem.
"""
def localizar_quadrante_cartesiano(x,y):
    print(f'\n Coordenada <x> informado: {x}')
    print(f' Coordenada <y> informado: {y}')
    if (x > 0 and y > 0):
        print(' Segundo as coordenadas, está localizado no Primeiro Quadrante')
    elif (x < 0 and y > 0):
        print(' Segundo as coordenadas, está localizado no Segundo Quadrante')
    elif (x < 0 and y < 0):
        print(' Segundo as coordenadas, está localizado no Terceiro Quadrante')
    elif (x > 0 and y < 0):
        print(' Segundo as coordenadas, está localizado no Quarto Quadrante')
    else:
        print(' O ponto está localizado no eixo ou origem')
localizar_quadrante_cartesiano(x=0,y=0)