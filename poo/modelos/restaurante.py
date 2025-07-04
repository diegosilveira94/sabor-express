from modelos.avaliacao import Avaliacao
class Restaurante:
    """
    Representa um restaurante e suas características.

    Returns:
        _type_: _description_
    """    
    restaurantes = []
    def __init__(self, nome, categoria):
        """
        Inicializa uma instância de Restaurante.

        Args:
            nome (str): O nome do restaurante.
            categoria (str): A categoria do restaurante.
        """        
        self.nome =  nome.title()
        self.categoria = categoria.title()
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        """Formatação da instância em string

        Returns:
            str: Retorna uma representação em string do restaurante
        """        
        return f'{self._nome} | {self._categoria}'

    @classmethod
    def listar_restaurantes(cls):
        """
        Exibe uma lista formatada de todos os restaurantes.
        """        
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | {'Status'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante.nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}')

    @property
    def ativo(self):
        """
        Status de atividade do restaurante.

        Returns:
            str: Retorna um símbolo indicando o estado de atividade do restaurante.
        """        
        return '☑' if self._ativo else '☐'
    
    def alternar_estado(self):
        """
        Alterna o status de atividade do restaurante
        """        
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        """
        Registra as avaliações dos restaurantes.

        Args:
            cliente (str): O nome do cliente que fez a avaliação.
            nota (float): A nota atribuída ao restaurante (entre 1 e 5).
        """        
        if nota > 0 and nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        """
        Média das avaliações do restaurante.

        Returns:
            float: Retorna a média de todas as notas do restaurante recebidas.  
        """        
        if not self._avaliacao:
            return '-'
        soma_das_notas = sum(_avaliacao._nota for _avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media