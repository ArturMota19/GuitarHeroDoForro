from tupy import *
from user import User
from song import Song

class Game:
    """
    Classe responsável por gerenciar o funcionamento da partida.

    Atributos privados:
    - player: instância da classe User representando o jogador
    - song: instância da classe Song representando a música
    - score: pontuação atual do jogador
    - isPaused: indica se o jogo está pausado ou não

    Métodos públicos:
    - play(): inicia a partida
    - pause(): pausa o jogo
    - restart(): reinicia a partida
    - end(): encerra o jogo
    """
    def __init__(self, player: User, song: Song):
        self.__player = player
        self.__song = song
        self.__score = 0
        self.__isPaused = False

    @property
    def player(self):
        return self.__player

    @player.setter
    def player(self, value):
        self.__player = value

    @property
    def song(self):
        return self.__song

    @song.setter
    def song(self, value):
        self.__song = value

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        self.__score = value
    
    @property
    def isPaused(self):
        return self.__isPaused
    
    @isPaused.setter
    def isPaused(self, value):
        self.__isPaused = value

    def play(self):
        """
        Inicia a partida.
        """
        pass

    def pause(self):
        """
        Pausa o jogo.
        """
        pass

    def restart(self):
        """
        Reinicia a partida.
        """
        pass

    def end(self):
        """
        Encerra o jogo.
        """
        pass

run(globals())
