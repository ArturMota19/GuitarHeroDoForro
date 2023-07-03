from tupy import *

class Menu(BaseImage):
    def __init__(self) -> None:
        super().__init__(file = 'start.png', x = 450, y= 250)
        self._end = False
        self._easy = False
        self._medium = False
        self._hard = False