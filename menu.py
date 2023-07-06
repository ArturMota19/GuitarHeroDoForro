from tupy import *

class Menu(BaseImage):
    def __init__(self) -> None:
        super().__init__(file = 'start.png', x = 450, y= 250)
        self._end = False
        self._easy = False
        self._medium = False
        self._hard = False

class HitBox(Image):
	def __init__(self, x: float, y: float, file: str, angle: int) -> None:
		self.x = x
		self.y = y
		self.file = file
		self.angle = angle
		self._hide()
  
class PersonagemAssets(Image):
	def __init__(self, file) -> None:
		self.x = 770
		self.y = 310
		self.file = file
