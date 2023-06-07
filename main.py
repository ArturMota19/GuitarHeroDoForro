# Escopo inicial
from tupy import *

class Star(Image):
	def __init__(self, x: float) -> None:
		self.x = x
	def update(self):
		self.y += 10
		if self.y > 500:
			return True

def update():
	global s
	for i in s:
		if i.update():
			s.remove(i)
			i.destroy()

s = [Star(100), Star(200) ]
run(globals())