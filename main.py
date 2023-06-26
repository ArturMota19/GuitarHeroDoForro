# Escopo inicial
from tupy import *
from score import Score
from notes import Notes

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
	def __init__(self, x: float, y: float) -> None:
		self.x = x
		self.y = y
  
class PersonagemAssets(Image):
	def __init__(self, file) -> None:
		self.x = 500
		self.y = 200
		self.file = file


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
	if keyboard.is_key_just_down('q') and len(NotasEsquerdaQ) != 0:
		if h[0].y / NotasEsquerdaQ[0].y >= 0.95 and h[0].y / NotasEsquerdaQ[0].y <= 1.18:
			NotasEsquerdaQ[0].y += 501
			scorePlayer.increment(10)
			randomNumero = random.randint(1, 38)
			personagem.file = f'Personagem{randomNumero}.png'
		else:
			NotasEsquerdaQ[0].y += 501
			scorePlayer.decrement(5)
   
   	#Partitura para mais à direita
	if keyboard.is_key_just_down('w') and len(NotasDireitaW) != 0:
		if h[1].y / NotasDireitaW[0].y >= 0.95 and h[1].y / NotasDireitaW[0].y <= 1.18:
			NotasDireitaW[0].y += 501
			scorePlayer.increment(10)
			randomNumero = random.randint(1, 38)
			personagem.file = f'Personagem{randomNumero}.png'
		else:
			NotasDireitaW[0].y += 501
			scorePlayer.decrement(5)
   


"""
	É possível fazer notas aleatórias usando randomint e definindo um intervalo de x à y pra cada Nota.
	Lembrando que o código funciona por ordem, então a nota de posição 1 no array NÃO PODE estar em uma
	Posição maior que a nota de posição 0.
"""
bg = Fundo()
h = [HitBox(100, 400), HitBox(200, 400)]

#Partitura para mais à esquerda
NotasEsquerdaQ = []
ValorPartituraQ = -50

for i in range(30):
    varIntermediaria = ValorPartituraQ -100
    random1 = random.randint(varIntermediaria, ValorPartituraQ)
    NotasEsquerdaQ.append(Notes(100, random1, '', 0, 3))
    ValorPartituraQ -= 100

#Partitura para mais à direita
NotasDireitaW = []
ValorPartituraW = -50

for i in range(45):
    varIntermediaria = ValorPartituraW -75
    random1 = random.randint(varIntermediaria, ValorPartituraW)
    NotasDireitaW.append(Notes(200, random1, '', 0, 5))
    ValorPartituraW -= 75


global personagem
personagem = PersonagemAssets('Personagem1.png')
scorePlayer = Score()
run(globals())