from tupy import *

class Menu(Image):
    def __init__(self):
        self.file = 'start.png'
        self.x = 450
        self.y = 250
        self.end = False
    def update(self):
        if keyboard.is_key_just_down('space'):
              self.file = 'dificult.png'
        if self.file == 'dificult.png':
            if keyboard.is_key_just_down('1'):
                    """ implementar função da dificuldade fácil """
                    self.file = 'bg.png'
                    self.end = True
            elif keyboard.is_key_just_down('2'):
                    """ implementar função da dificuldade média """
                    self.file = 'bg.png'
                    self.end = True
            elif keyboard.is_key_just_down('3'):
                    """ implementar função da dificuldade difícil """
                    self.file = 'bg.png'
                    self.end = True

    