# Escopo inicial
from tupy import *

class Star(Image):
	def update(self):
		self.y += 2

star1 = Star()
star2 = Star()
star1.x = 100
star2.x = 200

run(globals())