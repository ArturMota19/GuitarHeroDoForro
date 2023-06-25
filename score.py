from tupy import *
from user import User
from notes import Notes

class Score(Label):
    def __init__(self) -> None:
        super().__init__('Score: 0', 40, 9, font='Arial 20')
        self.__score = 0
        self.__highscore = 0
        
    def increment(self, value: int) -> None:
        """
        Método chamado quando uma nota é acertada pelo jogador.
        Atualiza a pontuação do jogador.
        """
        self.__score += value
        self.text = f'Score: {self.__score}'
                
        if self.__score >= self.__highscore:
            self.__highscore == self.__score
        else:
            self.__highscore == self.__highscore
    def decrement(self, value: int) -> None:
        """
        Atualiza a pontuação do jogador.
        """
        self.__score -= value
        self.text = f'Score: {self.__score}'
                
