# Escopo inicial
from tupy import *
from score import Score
from notes import Notes
from menu import Menu

class Star(Image):
	def __init__(self, x: float) -> None:
		self.x = x
	def update(self):
		self.y += 2
		if self.y > 500:
			return True

class Fundo(Image):
    def __init__(self):
        self.y = 250
        self.x = 450
        self.file = 'bg.png'

class HitBox(Image):
	def __init__(self, x: float, y: float, file: str, angle: int) -> None:
		self.x = x
		self.y = y
		self.file = file
		self.angle = angle
  
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

def update():
	global NotasEsquerda
	global NotasDireita
	for i in NotasEsquerda:
		""" Função para deletar nota ao passar de y 450 """
		if i.y > 450:
			NotasEsquerda.remove(i)
			i.destroy()
		if i.update():
			NotasEsquerda.remove(i)
			i.destroy()
	for i in NotasDireita:
		""" Função para deletar nota ao passar de y 450 """
		if i.y > 450:
			NotasDireita.remove(i)
			i.destroy()
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
   


"""
	É possível fazer notas aleatórias usando randomint e definindo um intervalo de x à y pra cada Nota.
	Lembrando que o código funciona por ordem, então a nota de posição 1 no array NÃO PODE estar em uma
	Posição maior que a nota de posição 0.
"""
bg = Fundo()
h = [HitBox(100, 400, 'HitBoxArrow.png', 0), HitBox(200, 400, 'HitBoxArrow.png', 180)]

#Partitura para mais à esquerda
NotasEsquerda = []
ValorPartituraEsquerda = -50

for i in range(30):
    varIntermediaria = ValorPartituraEsquerda -100
    random1 = random.randint(varIntermediaria, ValorPartituraEsquerda)
    NotasEsquerda.append(Notes(100, random1, 'Notes.png',0, 3))
    ValorPartituraEsquerda -= 100

#Partitura para mais à direita
NotasDireita = []
ValorPartituraDireita = -50

for i in range(45):
    varIntermediaria = ValorPartituraDireita -75
    random1 = random.randint(varIntermediaria, ValorPartituraDireita)
    NotasDireita.append(Notes(200, random1, 'Notes2.png',180, 5))
    ValorPartituraDireita -= 75


global personagem
personagem = PersonagemAssets('Personagem1.png')
scorePlayer = Score()
run(globals())