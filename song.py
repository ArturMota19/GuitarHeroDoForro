from notes import Notes

class Song:
    """
    Classe responsável por armazenar os dados de uma música.

    Atributos privados:
    - __name: nome da música
    - __musicSheet: lista de instâncias da classe Notes representando as notas da música
    - __difficulty: dificuldade da música

    Métodos públicos:
    - (outros métodos relacionados à música)
    """
    def __init__(self, name: str, musicSheet: list[Notes], difficulty: str) -> None:
        self.__name = name
        self.__musicSheet = musicSheet
        self.__difficulty = difficulty

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        self.__name = value

    @property
    def musicSheet(self) -> list[Notes]:
        return self.__musicSheet

    @musicSheet.setter
    def musicSheet(self, value: list[Notes]) -> None:
        self.__musicSheet = value

    @property
    def difficulty(self) -> str:
        return self.__difficulty

    @difficulty.setter
    def difficulty(self, value: str) -> None:
        self.__difficulty = value
