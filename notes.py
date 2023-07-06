from tupy import *


class Notes(Image):
    """
    Classe responsável por armazenar os dados de uma nota.

    Atributos privados:
    - x: posição horizontal da nota
    - y: posição vertical da nota
    - _file: imagem da nota
    - _angle: ângulo da nota
    - _speed: velocidade da nota

    Métodos públicos:
    - fall(): atualiza a posição da nota e verifica se ela foi acertada pelo jogador
    """
    def __init__(self, x: float, y: float, file: str, angle: int, speed: float) -> None:
        self.file = file
        self.x = x
        self.y = y
        self.__speed = speed
        self.angle = angle

    @property
    def speed(self) -> float:
        return self.__speed

    @speed.setter
    def speed(self, value) -> None:
        self.__speed = value

    def update(self):
        if self.y > 450:
            return False
        self.y += self.speed

                
