from tupy import *

class Menu(BaseImage):
    def __init__(self):
        super().__init__('start.png', 450, 250)
        self._end = False
    def update(self):
        if keyboard.is_key_just_down('space'):
              self._file = 'dificult.png'
        if self._file == 'dificult.png':
            if keyboard.is_key_just_down('1'):
                    """ implementar função da dificuldade fácil """
                    self._file = 'bg.png'
                    self._end = True
            if keyboard.is_key_just_down('2'):
                    """ implementar função da dificuldade média """
                    self._file = 'bg.png'
            if keyboard.is_key_just_down('3'):
                    """ implementar função da dificuldade difícil """
                    self._file = 'bg.png'

    