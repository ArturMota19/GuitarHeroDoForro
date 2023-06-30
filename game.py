from tupy import *
from user import User
from song import Song
from notes import Notes
from score import Score


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
    counter = 0

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

    def update(self):
        for i in song.musicSheet:
            if i.update():
                song.musicSheet.remove(i)
                i.destroy()

        # Como não implementamos uma musica ainda
        ###############################################################################################
        if self.counter == 30: # Gera notas aleatórias na tela
            song.musicSheet.append(Notes(float(random.randint(0,3)*50+300), 0.0, "star.png", "angle", 10))
            self.counter = 0

        self.counter += 1
        ################################################################################################


# A partitura é uma lista de tuplas, onde cada tupla contém a posição na tela e o tempo em que ela deve ser tocada
# A posição na tela é um inteiro representando a posição horizontal na tela, já que o y é fixo em 0
       
partitura = []

player = User("Fulano", "avatar.png")
song = Song("Melodia", partitura, "Easy")
game = Game(player, song)
score = Score()
score.increment(5)

def update():
    game.update()
run(globals())
