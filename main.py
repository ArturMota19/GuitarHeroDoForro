# Escopo inicial
from tupy import *
from score import Score
from notes import Notes
from threading import Timer

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
	global NotasEsquerdaQ
	global NotasDireitaW
	for i in NotasEsquerdaQ:
		if i.update():
			NotasEsquerdaQ.remove(i)
			i.destroy()
	for i in NotasDireitaW:
		if i.update():
			NotasDireitaW.remove(i)
			i.destroy()
   	#Partitura para mais à esquerda
	if keyboard.is_key_just_down('q'):
		if h[0].y / NotasEsquerdaQ[0].y >= 0.95 and h[0].y / NotasEsquerdaQ[0].y <= 1.18:
			NotasEsquerdaQ[0].y += 501
			scorePlayer.increment(10)
		else:
			NotasEsquerdaQ[0].y += 501
			scorePlayer.decrement(5)
   
   	#Partitura para mais à direita
	if keyboard.is_key_just_down('w'):
		if h[1].y / NotasDireitaW[0].y >= 0.95 and h[1].y / NotasDireitaW[0].y <= 1.18:
			NotasDireitaW[0].y += 501
			scorePlayer.increment(10)
		else:
			NotasDireitaW[0].y += 501
			scorePlayer.decrement(5)
   

#Partitura para mais à esquerda
NotasEsquerdaQ = [Notes(100,-20,'',0,3 ), Notes(100,-52,'',0,3 ), Notes(100,-93,'',0,3 ), Notes(100,-147,'',0,3 ),
                  Notes(100,-230,'',0,3 ),Notes(100,-370,'',0,3 ),Notes(100,-450,'',0,3 ),Notes(100,-564,'',0,3 ),
                  Notes(100,-684,'',0,3 ),Notes(100,-759,'',0,3 )
                  ]
#Partitura para mais à direita
NotasDireitaW = [Notes(200,-50,'',0,5 ), Notes(200,-120,'',0,5 ), Notes(200,-250,'',0,5 ), Notes(200,-300,'',0,5 ),
                 Notes(200,-360,'',0,5 ),Notes(200,-400,'',0,5 ),Notes(200,-490,'',0,5 ),Notes(200,-560,'',0,5 ),
                 Notes(200,-780,'',0,5 ),Notes(200,-800,'',0,5 ),Notes(200,-840,'',0,5 ),Notes(200,-900,'',0,5 ),
                 Notes(200,-980,'',0,3 ),Notes(200,-1060,'',0,3 ),Notes(200,-1200,'',0,3 )
                 ]

h = [HitBox(100, 400), HitBox(200, 400)]
scorePlayer = Score()
run(globals())