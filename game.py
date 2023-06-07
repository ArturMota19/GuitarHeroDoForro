from tupy import *
from user import User
from song import Song
from notes import Notes

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

        if self.counter == 30: # Gera notas aleatórias na tela
            song.musicSheet.append(Notes(float(random.randint(10,200)), 0.0, "star.png", "angle", 10))
            self.counter = 0

        self.counter += 1
        

#nota = Notes(float(random.randint(0,200)), 0.0, "star.png", "angle", 10)

# (x: float, y: float, file: str, angle: str, speed: float) -> None

partitura = []

player = User("Fulano", "avatar.png")
song = Song("Melodia", partitura, "Easy")
game = Game(player, song)

def update():
    game.update()
run(globals())
