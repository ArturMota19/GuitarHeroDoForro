# Escopo inicial
from tupy import *
from score import Score
from notes import Notes
from menu import Menu
from winsound import PlaySound
import pygame

class Star(Image):
	def _init_(self, x: float) -> None:
		self.x = x
	def update(self):
		self.y += 2
		if self.y > 500:
			return True

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

"""
	Tentativa de implementação por qwer (por hora) no update, sendo;
	q -> mais à esquerda
	r -> mais à direita
"""

menu = Menu()

######### uso permitido do pygame para tocar a música ##########
pygame.init()	
def play(music):
    pygame.mixer.music.load(f"assets/sounds/{music}")
    pygame.mixer.music.play()
################################################################   

h = [HitBox(100, 400, 'HitBoxArrow.png', 0), HitBox(200, 400, 'HitBoxArrow.png', 180), HitBox(300, 400, 'HitBoxArrow.png', 90), HitBox(400, 400, 'HitBoxArrow.png', 270)]

if menu._end == False:
	def update():
		global h
		if keyboard.is_key_just_down('space'):
			menu._file = 'music.png'

		""" if para o menu de seleção de músicas """

		if keyboard.is_key_just_down('a'):
			menu._file = 'dificult.png'
			play('tarecoemariola.ogg')
		if keyboard.is_key_just_down('b'):
			menu._file = 'dificult.png'
			play('deixaeutesuperar.ogg')
		if keyboard.is_key_just_down('c'):
			menu._file = 'dificult.png'
			play('ocheirodecarolina.ogg')
		if keyboard.is_key_just_down('d'):
			menu._file = 'dificult.png'
			play('oxotedasmeninas.ogg')
		if keyboard.is_key_just_down('e'):
			menu._file = 'dificult.png'
			play('luaminha.ogg')

		""" if para o menu de dificuldades """

		if menu._file == 'dificult.png':
			if keyboard.is_key_just_down('1'):
					menu._easy = True
     
					menu._file = 'bg.png'
					menu._end = True
			elif keyboard.is_key_just_down('2'):
					menu._medium = True
     
					menu._file = 'bg.png'
					menu._end = True
			elif keyboard.is_key_just_down('3'):
					menu._hard = True

					menu._file = 'bg.png'
					menu._end = True
		## modo facil		
		if menu._end == True and menu._easy == True:
			""" o _show() é para mostrar as 2 hitboxs do modo fácil """
			h[0]._show()
			h[1]._show()
			global NotasEsquerda
			global NotasDireita
			for i in NotasEsquerda:
				""" Função para deletar nota ao passar de y 450 e decrementa o score em 5 """
				if i.y > 450:
					NotasEsquerda.remove(i)
					i.destroy()
					scorePlayer.decrement(5)
				if i.update():
					NotasEsquerda.remove(i)
					i.destroy()
			for i in NotasDireita:
				""" Função para deletar nota ao passar de y 450 e decrementa o score em 5 """
				if i.y > 450:
					NotasDireita.remove(i)
					i.destroy()
					scorePlayer.decrement(5)
				if i.update():
					NotasDireita.remove(i)
					i.destroy()
			#Partitura para mais à esquerda
			if keyboard.is_key_just_down('Left') and len(NotasEsquerda) != 0:
				if h[0].y / NotasEsquerda[0].y >= 0.95 and h[0].y / NotasEsquerda[0].y <= 1.18:
					NotasEsquerda[0].y += 501
					scorePlayer.increment(10)
					randomNumero = random.randint(1, 38)
					personagem.file = f'Personagem{randomNumero}.png'
				else:
					NotasEsquerda[0].y += 501
					scorePlayer.decrement(5)
		
			#Partitura para mais à direita
			if keyboard.is_key_just_down('Right') and len(NotasDireita) != 0:
				if h[1].y / NotasDireita[0].y >= 0.95 and h[1].y / NotasDireita[0].y <= 1.18:
					NotasDireita[0].y += 501
					scorePlayer.increment(10)
					randomNumero = random.randint(1, 38)
					personagem.file = f'Personagem{randomNumero}.png'
				else:
					NotasDireita[0].y += 501
					scorePlayer.decrement(5)
	
		## modo medio
		if menu._end == True and menu._medium == True:
			""" o _show() é para mostrar as 3 hitboxs do modo fácil """
			h[0]._show()
			h[1]._show()
			h[2]._show()
			global NotasBaixo
			for i in NotasEsquerda:
				""" Função para deletar nota ao passar de y 450 e decrementa o score em 5 """
				if i.y > 450:
					NotasEsquerda.remove(i)
					i.destroy()
					scorePlayer.decrement(5)
				if i.update():
					NotasEsquerda.remove(i)
					i.destroy()
			for i in NotasDireita:
				""" Função para deletar nota ao passar de y 450 e decrementa o score em 5 """
				if i.y > 450:
					NotasDireita.remove(i)
					i.destroy()
					scorePlayer.decrement(5)
				if i.update():
					NotasDireita.remove(i)
					i.destroy()
			for i in NotasBaixo:
				""" Função para deletar nota ao passar de y 450 e decrementa o score em 5 """
				if i.y > 450:
					NotasBaixo.remove(i)
					i.destroy()
					scorePlayer.decrement(5)
				if i.update():
					NotasBaixo.remove(i)
					i.destroy()
			#Partitura para mais à esquerda
			if keyboard.is_key_just_down('Left') and len(NotasEsquerda) != 0:
				if h[0].y / NotasEsquerda[0].y >= 0.95 and h[0].y / NotasEsquerda[0].y <= 1.18:
					NotasEsquerda[0].y += 501
					scorePlayer.increment(10)
					randomNumero = random.randint(1, 38)
					personagem.file = f'Personagem{randomNumero}.png'
				else:
					NotasEsquerda[0].y += 501
					scorePlayer.decrement(5)
		
			#Partitura para mais à direita
			if keyboard.is_key_just_down('Right') and len(NotasDireita) != 0:
				if h[1].y / NotasDireita[0].y >= 0.95 and h[1].y / NotasDireita[0].y <= 1.18:
					NotasDireita[0].y += 501
					scorePlayer.increment(10)
					randomNumero = random.randint(1, 38)
					personagem.file = f'Personagem{randomNumero}.png'
				else:
					NotasDireita[0].y += 501
					scorePlayer.decrement(5)
     
			#Partitura para baixo
			if keyboard.is_key_just_down('Down') and len(NotasBaixo) != 0:
				if h[1].y / NotasBaixo[0].y >= 0.95 and h[1].y / NotasBaixo[0].y <= 1.18:
					NotasBaixo[0].y += 501
					scorePlayer.increment(10)
					randomNumero = random.randint(1, 38)
					personagem.file = f'Personagem{randomNumero}.png'
				else:
					NotasBaixo[0].y += 501
					scorePlayer.decrement(5)

		## modo dificil
		if menu._end == True and menu._hard == True:
			""" o _show() é para mostrar as 4 hitboxs do modo fácil """
			h[0]._show()
			h[1]._show()
			h[2]._show()
			h[3]._show()
			global NotasCima
			for i in NotasEsquerda:
				""" Função para deletar nota ao passar de y 450 e decrementa o score em 5 """
				if i.y > 450:
					NotasEsquerda.remove(i)
					i.destroy()
					scorePlayer.decrement(5)
				if i.update():
					NotasEsquerda.remove(i)
					i.destroy()
			for i in NotasDireita:
				""" Função para deletar nota ao passar de y 450 e decrementa o score em 5 """
				if i.y > 450:
					NotasDireita.remove(i)
					i.destroy()
					scorePlayer.decrement(5)
				if i.update():
					NotasDireita.remove(i)
					i.destroy()
			for i in NotasBaixo:
				""" Função para deletar nota ao passar de y 450 e decrementa o score em 5 """
				if i.y > 450:
					NotasBaixo.remove(i)
					i.destroy()
					scorePlayer.decrement(5)
				if i.update():
					NotasBaixo.remove(i)
					i.destroy()
			for i in NotasCima:
				""" Função para deletar nota ao passar de y 450 e decrementa o score em 5 """
				if i.y > 450:
					NotasCima.remove(i)
					i.destroy()
					scorePlayer.decrement(5)
				if i.update():
					NotasCima.remove(i)
					i.destroy()
			#Partitura para mais à esquerda
			if keyboard.is_key_just_down('Left') and len(NotasEsquerda) != 0:
				if h[0].y / NotasEsquerda[0].y >= 0.95 and h[0].y / NotasEsquerda[0].y <= 1.18:
					NotasEsquerda[0].y += 501
					scorePlayer.increment(10)
					randomNumero = random.randint(1, 38)
					personagem.file = f'Personagem{randomNumero}.png'
				else:
					NotasEsquerda[0].y += 501
					scorePlayer.decrement(5)
		
			#Partitura para mais à direita
			if keyboard.is_key_just_down('Right') and len(NotasDireita) != 0:
				if h[1].y / NotasDireita[0].y >= 0.95 and h[1].y / NotasDireita[0].y <= 1.18:
					NotasDireita[0].y += 501
					scorePlayer.increment(10)
					randomNumero = random.randint(1, 38)
					personagem.file = f'Personagem{randomNumero}.png'
				else:
					NotasDireita[0].y += 501
					scorePlayer.decrement(5)
     
			#Partitura para baixo
			if keyboard.is_key_just_down('Down') and len(NotasBaixo) != 0:
				if h[1].y / NotasBaixo[0].y >= 0.95 and h[1].y / NotasBaixo[0].y <= 1.18:
					NotasBaixo[0].y += 501
					scorePlayer.increment(10)
					randomNumero = random.randint(1, 38)
					personagem.file = f'Personagem{randomNumero}.png'
				else:
					NotasBaixo[0].y += 501
					scorePlayer.decrement(5)
     
			#Partitura para cima
			if keyboard.is_key_just_down('Up') and len(NotasCima) != 0:
				if h[1].y / NotasCima[0].y >= 0.95 and h[1].y / NotasCima[0].y <= 1.18:
					NotasCima[0].y += 501
					scorePlayer.increment(10)
					randomNumero = random.randint(1, 38)
					personagem.file = f'Personagem{randomNumero}.png'
				else:
					NotasCima[0].y += 501
					scorePlayer.decrement(5)


	"""
		É possível fazer notas aleatórias usando randomint e definindo um intervalo de x à y pra cada Nota.
		Lembrando que o código funciona por ordem, então a nota de posição 1 no array NÃO PODE estar em uma
		Posição maior que a nota de posição 0.
	"""
	
	#Partitura para mais à esquerda
	NotasEsquerda = []
	ValorPartituraEsquerda = -50

	for i in range(30):
		varIntermediaria = ValorPartituraEsquerda -100
		random1 = random.randint(varIntermediaria, ValorPartituraEsquerda)
		NotasEsquerda.append(Notes(100, random1, 'Notes.png',0, 2.5))
		ValorPartituraEsquerda -= 100

	#Partitura para mais à direita
	NotasDireita = []
	ValorPartituraDireita = -50

	for i in range(60):
		varIntermediaria = ValorPartituraDireita -75
		random1 = random.randint(varIntermediaria, ValorPartituraDireita)
		NotasDireita.append(Notes(200, random1, 'Notes2.png',180, 3.5))
		ValorPartituraDireita -= 75
  
	#Partitura para baixo
	NotasBaixo = []
	ValorPartituraBaixo = -50

	for i in range(75):
		varIntermediaria = ValorPartituraBaixo -75
		random1 = random.randint(varIntermediaria, ValorPartituraBaixo)
		NotasBaixo.append(Notes(300, random1, 'Notes.png', 90, 4))
		ValorPartituraBaixo -= 75

	#Partitura para cima
	NotasCima = []
	ValorPartituraCima = -50

	for i in range(90):
		varIntermediaria = ValorPartituraCima -75
		random1 = random.randint(varIntermediaria, ValorPartituraCima)
		NotasCima.append(Notes(400, random1, 'Notes2.png', 270, 6.5))
		ValorPartituraCima -= 75
  
	global personagem
	personagem = PersonagemAssets('Personagem1.png')
	scorePlayer = Score()

run(globals())
