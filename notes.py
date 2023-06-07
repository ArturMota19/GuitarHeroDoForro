from tupy import *


class Notes(Image):
    """
    Classe responsável por armazenar os dados de uma nota.

    Atributos privados:
    - _x: posição horizontal da nota
    - _y: posição vertical da nota
    - _file: imagem da nota
    - _angle: ângulo da nota
    - _speed: velocidade da nota

    Métodos públicos:
    - fall(): atualiza a posição da nota e verifica se ela foi acertada pelo jogador
    """
    def __init__(self, x: float, y: float, file: str, angle: str, speed: float) -> None:
        self.file = file
        self.x = x
        self.y = y
        self.__angle = angle
        self.__speed = speed


    @property
    def file(self) -> str:
        return self.__file

    @file.setter
    def file(self, value) -> None:
        self.__file = value

    @property
    def angle(self) -> float:
        return self.__angle

    @angle.setter
    def angle(self, value) -> None:
        self.__angle = value

    @property
    def speed(self) -> float:
        return self.__speed

    @speed.setter
    def speed(self, value) -> None:
        self.__speed = value

    def update(self):
        """
        Atualiza a posição da nota e verifica se ela foi acertada pelo jogador.
        """
        if self.y > 500:
            return True
        self.y += self.speed
                
