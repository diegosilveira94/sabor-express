from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_praca.receber_avaliacao('Diego', 10)
restaurante_praca.receber_avaliacao('Ranna', 8)
restaurante_praca.receber_avaliacao('Pandora', 5)
restaurante_praca.receber_avaliacao('Pipo', 3)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()