#coding: latin-1


import pygame
import random
from block import Block

from paddle import Paddle
from wall import Wall
from ball import Ball

import constants



# Inicializao da biblioteca pygame
pygame.init()

# Criação da janela com a resolução indicada
screen = pygame.display.set_mode([constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT])

# Definição do título da janela
pygame.display.set_caption('Pong')



# inicializar o relógio
clock = pygame.time.Clock()


# variável usada para assinalar que o jogo terminou
done = False

# criar a(s) raquete(s)


# criar as paredes
top_wall = Wall(0,0,constants.SCREEN_WIDTH,constants.CWALLS)
bottom_wall = Wall(0,constants.SCREEN_HEIGHT-15,constants.SCREEN_WIDTH,constants.CWALLS)

#todo -paredes
walls_list = pygame.sprite.Group()

walls_list.add(top_wall)
walls_list.add(bottom_wall)


#todo

ball = None
player = False

""" listas para gerir os vários objetos do jogo """
# criação do grupo dos objetos que necessitam ser redesenhados (todos)
drawables_list = pygame.sprite.Group()

#criação do grupo dos objetos que colidem com a bola
colliders_list = pygame.sprite.Group()

#criação do grupo dos objetos animados
animated_list = pygame.sprite.Group()



# adicionar as paredes superior e inferior aos objetos que colidem com a bola
colliders_list.add(top_wall)
colliders_list.add(bottom_wall)

# adicionar a(s) raquete(s) à lista de objetos que colidem com a bola


# adicionar os objetos que necessitam ser desenhados
drawables_list.add(top_wall)
drawables_list.add(bottom_wall)

# criar a rede e adicionar os objetos à lista de objetos que necessitam ser redesenhados
for i in range(0,constants.SCREEN_HEIGHT,30):
	net = Block(constants.SCREEN_WIDTH//2-7,i+15,14,15,constants.CWALLS)
	drawables_list.add(net)

# adicionar a(s) raqueta(s)


# adicionar os objetos que necessitam ser atualizados à lista respetiva


#---------coisas:tipo de jogo, pontuações, o resultado para ganhar, cores--------------------
style =	0 					#tipo de jogo
score1 = 0 					#score player 1
score2 = 0					#score player 2
winplayer = 0					#que jogador ganhou
scoreTot = str(score1) + "   " + str(score2) 	#string que comporta o score
maxscore = 1					#pontos máximos (até aos maxscore pontos) 
Intro = False
match =	False					
single = False
pause = False

#------------------------------ciclo principal---------------------------------------------
while not done:
	
	
	
	if match == False: 
		Height1 = constants.Height1
		Height2 = constants.Height2	
	elif match == True:	
		if score1 >= score2:
			Height1 = constants.Height1*2/3
		if score2 >= score1:
			Height2 = constants.Height2*2/3

	
	
	if player == False:
		if match == False:	
			

			player_one = Paddle(30,constants.SCREEN_HEIGHT//2-30,Height1,constants.CPLAYER1)
			player_two = Paddle(constants.SCREEN_WIDTH-30-15,constants.SCREEN_HEIGHT//2-30,Height2,constants.CPLAYER2)		
			
			player_one.set_walls(walls_list)
			player_two.set_walls(walls_list)		
			colliders_list.add(player_one)
			colliders_list.add(player_two)		
			drawables_list.add(player_one)
			drawables_list.add(player_two)		
			animated_list.add(player_one)
			animated_list.add(player_two)	
			player = True
	
		if match == True:
			player_one.kill()
			player_two.kill()
			
			
			player_one = Paddle(30,constants.SCREEN_HEIGHT//2-30,Height1,constants.CPLAYER1)
			player_two = Paddle(constants.SCREEN_WIDTH-30-15,constants.SCREEN_HEIGHT//2-30,Height2,constants.CPLAYER2)		
			
			player_one.set_walls(walls_list)
			player_two.set_walls(walls_list)		
			colliders_list.add(player_one)
			colliders_list.add(player_two)		
			drawables_list.add(player_one)
			drawables_list.add(player_two)		
			animated_list.add(player_one)
			animated_list.add(player_two)	
			player = True	
	
	
	
	
	# Verificar se é necessário criar uma nova bola e players?
	if ball == None:
		ball = Ball(constants.SCREEN_WIDTH//2-7,constants.SCREEN_HEIGHT//2-7,constants.CBALL)
		ball.set_colliders(colliders_list)
		# adicionar a bola à lista de objetos a atualizar
		animated_list.add(ball)
		drawables_list.add(ball)
		
		if score1 == 0 and score2 == 0:
			ball.dir_x = ball.dir_x
			ball.dir_y = 0
			player_one.rect.y = constants.SCREEN_HEIGHT//2-30
			player_two.rect.y = constants.SCREEN_HEIGHT//2-30

	

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		elif event.type == pygame.KEYDOWN:		
			if pause == False:
				if event.key == pygame.K_q or event.key == pygame.K_UP and single == True:
					player_one.move_up()
				elif event.key == pygame.K_a or event.key == pygame.K_DOWN and single == True:
					player_one.move_down()
				elif event.key == pygame.K_p and single == False or event.key == pygame.K_UP and single == False:
					player_two.move_up()
				elif event.key == pygame.K_l and single == False or event.key == pygame.K_DOWN and single == False:
					player_two.move_down()
			
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_y:
				if pause == False:
					paus
