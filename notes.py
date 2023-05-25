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
        self.__x = x
        self.__y = y
        self.__file = file
        self.__angle = angle
        self.__speed = speed

    @property
    def x(self) -> float:
        return self.__x

    @x.setter
    def x(self, value) -> None:
        self.__x = value

    @property
    def y(self) -> float:
        return self.__y

    @y.setter
    def y(self, value) -> None:
        self.__y = value

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

    def fall(self):
        """
        Atualiza a posição da nota e verifica se ela foi acertada pelo jogador.
        """

        pass
