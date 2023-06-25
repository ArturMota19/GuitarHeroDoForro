# Escopo inicial
from tupy import *
from score import Score

class Star(Image):
	def __init__(self, x: float) -> None:
		self.x = x
	def update(self):
		self.y += 2
		if self.y > 500:
			return True

class HitBox(Image):
	def __init__(self, x: float, y: float) -> None:
		self.x = x
		self.y = y

"""
	Tentativa de implementação por qwer (por hora) no update, sendo;
	q -> mais à esquerda
	r -> mais à direita
"""

def update():
	global s
	for i in s:
		if i.update():
			s.remove(i)
			i.destroy()
	if keyboard.is_key_just_down('q'):
		if h[0].y / s[0].y >= 0.95 and h[0].y / s[0].y <= 1.18:
			s[0].y += 501
			scorePlayer.increment(10)
		else:
			s[0].y += 501
			scorePlayer.decrement(5)
   
s = [Star(100), Star(200)]
h = [HitBox(100, 400), HitBox(200, 400)]
scorePlayer = Score()
run(globals())