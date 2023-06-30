from tupy import *

class Menu(BaseImage):
    def __init__(self):
        super().__init__('start.png', 450, 250)
    def update(self):
        if (320 < mouse.x < 580) and (200 < mouse.y < 250):
            if mouse.is_button_down():
                self._file = 'dificult.png'
        if self._file == 'dificult.png':
            """ funcao para iniciar modo facil """
            if (320 < mouse.x < 580) and (140 < mouse.y < 218):
                if mouse.is_button_down():
                    return
            """ funcao para iniciar modo medio """
            if (320 < mouse.x < 580) and (263 < mouse.y < 333):
                if mouse.is_button_down():
                    return
            """ funcao para iniciar modo dificil """
            if (320 < mouse.x < 580) and (376 < mouse.y < 450):
                if mouse.is_button_down():
                    return 

    