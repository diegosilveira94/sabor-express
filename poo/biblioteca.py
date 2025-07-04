from desafios.desafios import Livro

# Criando 2 instâncias da classe Livro
livro1 = Livro('a menina que roubava livros', 'markus zusak', 2005)
livro2 = Livro('o pequeno principe', 'Antoine de Saint-Exupéry', 1943)
livro3 = Livro("Data Science Fundamentals", "Jane Smith", 2020)

livro1.emprestar()

Livro.livros = [livro1, livro2, livro3]  # Adicionando os livros à lista de livros

ano_especifico = 2020
livros_disponiveis_ano = Livro.verificar_disponibilidade(ano_especifico)
print(f'Livros disponiveis em {ano_especifico}: {livros_disponiveis_ano}')

# Criando 2 instâncias da classe Livro
livro1 = Livro('a menina que roubava livros', 'markus zusak', 2005)
livro2 = Livro('o pequeno principe', 'Antoine de Saint-Exupéry', 1943)
livro3 = Livro("Data Science Fundamentals", "Jane Smith", 2020)
# Imprimindo informações iniciais
print("Informações Iniciais:")
print(livro1)
print(livro2)
print()

# Imprimindo informações após emprestar
livro1.emprestar()
print("Informações após emprestar:")
print(livro1)
print(livro2)
print()