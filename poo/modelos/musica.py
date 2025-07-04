# exercicio 001

class Musica:
    def __init__(self, nome, artista, duracao: int):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao

    def __str__(self):
        return f'Nome: {self.nome} | Artista: {self.artista} | Duração(min): {self.duracao}'
    
musica1 = Musica('Bohemian Rhapsody', 'Queen', 355)
musica2 = Musica('Imagine', 'John Lennon', 183)
musica3 = Musica('Shape of You', 'Ed Sheeran', 234)

print(musica2)