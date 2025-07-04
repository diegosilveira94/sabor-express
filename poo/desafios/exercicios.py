'''
Exercícios

    Atribua o valor 'Italiana' ao atributo categoria da instância restaurante_praca da classe Restaurante.
    Acesse o valor do atributo nome da instância restaurante_praca da classe Restaurante.
    Verifique o valor inicial do atributo ativo para a instância restaurante_praca e exiba uma mensagem informando se o restaurante está ativo ou inativo.
    Acesse o valor do atributo de classe categoria diretamente da classe Restaurante e armazene em uma variável chamada categoria.
    Altere o valor do atributo nome para 'Bistrô'.
    Crie uma nova instância da classe Restaurante chamada restaurante_pizza com o nome 'Pizza Place' e categoria 'Fast Food'.
    Verifique se a categoria da instância restaurante_pizza é 'Fast Food'.
    Mude o estado da instância restaurante_pizza para ativo.
    Imprima no console o nome e a categoria da instância restaurante_praca.
'''

class Restaurante:
    nome =  ''
    categoria = ''
    ativo = False

restaurante_praca = Restaurante()
restaurante_praca.nome = 'Praça'

# Atribua o valor 'Italiana' ao atributo categoria da instância restaurante_praca da classe Restaurante.
restaurante_praca.categoria = 'Italiana' #
restaurante_pizza = Restaurante()

restaurantes = [restaurante_pizza, restaurante_praca]

# Acesse o valor do atributo nome da instância restaurante_praca da classe Restaurante.
print(restaurante_praca.categoria)

# Verifique o valor inicial do atributo ativo para a instância restaurante_praca e exiba uma mensagem informando se o restaurante está ativo ou inativo.
print(f'O restaurante {restaurante_praca.nome} está {'ativo' if restaurante_praca.ativo == True else 'inativo'}')

# Acesse o valor do atributo de classe categoria diretamente da classe Restaurante e armazene em uma variável chamada categoria.
Restaurante.categoria = 'Fast Food'

# Verifique se a categoria da instância restaurante_pizza é 'Fast Food'
print(restaurante_pizza.categoria)

# Altere o valor do atributo nome para 'Bistrô'.
Restaurante.nome = 'Bistrô'

# Crie uma nova instância da classe Restaurante chamada restaurante_pizza com o nome 'Pizza Place' e categoria 'Fast Food'.
restaurante_pizza_place = Restaurante()
restaurante_pizza_place.nome = 'Pizza Place'
restaurante_pizza_place.categoria = 'Fast Food'

# Mude o estado da instância restaurante_pizza para ativo.
restaurante_pizza.ativo = True
print(f'O restaurante {restaurante_pizza.nome} está {'ativo' if restaurante_pizza.ativo == True else 'inativo'}')

# Imprima no console o nome e a categoria da instância restaurante_praca.
print(f'O restaurante {restaurante_praca.nome}, categoria: {restaurante_praca.categoria}')