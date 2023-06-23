from tupy import *

class User(Image):
    """
    Classe responsável por armazenar os dados do jogador.

    Atributos:
    - highscore: pontuação máxima do jogador
    - name: nome do jogador
    - file: imagem do jogador

    Métodos:
    - hit_note(): é chamado quando uma nota é acertada pelo jogador
    """
    def __init__(self, name: str, file: str) -> None:        
        self.__highscore = 0
        self.__score = 0
        self.__name = name
        self.__file = file
        self._hide()

    def hit_note(self, value: int) -> None:
        """
        Método chamado quando uma nota é acertada pelo jogador.
        Atualiza a pontuação do jogador.
        """        
        pass
