#coding: latin-1

import pygame
import constants
from block import Block
from Obj import Obj
from Obs import Obs


pygame.init()

clock = pygame.time.Clock()

done = False

drawables_list = pygame.sprite.Group()

animated_list = pygame.sprite.Group()

screen = pygame.display.set_mode([constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT])

player = Obj((constants.SCREEN_WIDTH/2-(constants.Height1/2)),(constants.SCREEN_HEIGHT*4/6-(constants.Height1/2)),constants.Height1,constants.Height1, constants.BLACK)
drawables_list.add(player)
animated_list.add(player)

cannon = Block(0, 0, 70, constants.SCREEN_HEIGHT, constants.LBLUE)
for i in range(0,constants.SCREEN_HEIGHT,50):
	subcanon = Block(70, i+10 , 40, 30, constants.GREY)
	drawables_list.add(subcanon)
wall = Block((constants.SCREEN_WIDTH - 70), 0, 70, constants.SCREEN_HEIGHT, constants.CYAN)
drawables_list.add(wall)
drawables_list.add(cannon)

#-----------------------------------Constantes----------------------------------
Intro = False
Ready = False
Gameover = False
bullet = False
Player = False
pause = False


miss = 0
lifes = 3
point = 0
deco = Obs(0,0,constants.WHITE)
Snack = Obs(0,0,constants.WHITE)
Snackcount = 0
fire_count = 0

#---------------------------------Lógica--------------------------
while not done:	
	
	if Ready == True:
		if Player==False:
			player.kill()
			player = Obj((constants.SCREEN_WIDTH/2-(constants.Height1/2)),(constants.SCREEN_HEIGHT*4/6-(constants.Height1/2)),constants.Height1,constants.Height1, constants.BLACK)
			drawables_list.add(player)
			animated_list.add(player)		
			Player = True
		lifes = 3 - miss
		if lifes <= 0:
			Gameover = True	
	
		if bullet == False:
			Snack = Obs(110,70,constants.YELLOW)
			drawables_list.add(Snack)
			animated_list.add(Snack)
			Snack.generate()
			Snack.change_x= Snack.change_x*(Snackcount/25) + 2
			bullet = True
			Snackcount += 1
			
		if Snack.rect.x >= constants.SCREEN_WIDTH - constants.ObsSize - 70:
			Snack.kill()
			bullet = False
			miss += 1
	#fire_list=[]		
	#if bullet == True:
		#if len(fire_list) != 0:
			#for f in range[0, fire_count-1]:
				#fire_list[f].kill()
		
		#Fire = Block(Snack.rect.x-1,Snack.rect.y,Snack.change_x,15,constants.RED)
		#drawables_list.add(Fire)
		#fire_list.append(Fire)
		#fire_count += 1
		#print(len(fire_list))
		
		
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		
		elif event.type == pygame.KEYDOWN:
			if Ready == True and pause == False:
				if event.key == pygame.K_UP:
					player.move_up()
	
				elif event.key == pygame.K_DOWN:
					player.move_down()
	
				elif event.key == pygame.K_LEFT:
					player.move_left()
	
				elif event.key == pygame.K_RIGHT:
					player.move_right()
	
				elif event.key == pygame.K_g:
					player.image.fill(constants.GREEN)
					Snack.image.fill(constants.GREENISH)
					if Intro == True:
						if Snack.rect.x>= player.rect.x and Snack.rect.x<= player.rect.x + constants.Height1 - constants.ObsSize and Snack.rect.y >= player.rect.y and Snack.rect.y <= player.rect.y + constants.Height1 - constants.ObsSize:
							point += 1
							Snack.kill()
							bullet = False
						else:
							point -= 1
		
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_y:
				if pause == False:
					pause = True
				elif pause == True:
					pause = False
			if event.key == pygame.K_UP:
				player.dont_move()

			elif event.key == pygame.K_DOWN:
				player.dont_move()

			elif event.key == pygame.K_LEFT:
				player.dont_move()

			elif event.key == pygame.K_RIGHT:
				player.dont_move()			

			elif event.key == pygame.K_g:
				player.image.fill(constants.BLACK)
				Snack.image.fill(constants.YELLOW)
				
	
	
	if player.rect.x <= 110:
		player.rect.x = 110
	if player.rect.x >= constants.SCREEN_WIDTH-constants.Height1:
		player.rect.x = constants.SCREEN_WIDTH-constants.Height1
	if player.rect.y <= 0:
		player.rect.y = 0
	if player.rect.y >= constants.SCREEN_HEIGHT-constants.Height1:
		player.rect.y = constants.SCREEN_HEIGHT-constants.Height1
	
		
		
	if point <= 0:
		point = 0
#-----------------------------Desenhos------------------------------------------
	if pause == False:
		animated_list.update()	
			
	screen.fill(constants.WHITE)

	drawables_list.draw(screen)
	

#-------------------------------Introdução--------------------------------------
	if Intro == False:
		Snack.kill()		
		
		font = pygame.font.Font(None, 45)
		text = font.render("Press [G] to continue", 1, constants.BLACK)
		textpos = text.get_rect()
		textpos.centerx = constants.SCREEN_WIDTH/2
		textpos.centery = constants.SCREEN_HEIGHT*6/7
		screen.blit(text, textpos)	
					
					
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True		
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_g:
					Intro = True		
			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_g:
					Intro = True				
		
		deco_list=[]
		for i in range(1201):
			if i%600 == 0: 
				deco = Obs(70,70,constants.MAGENTA)
				drawables_list.add(deco)
				animated_list.add(deco)
				deco.generate()
				deco_list.append(deco)
				#deco_count += 1
				
#--------------------------------Instruções------------------------------------
	if Intro == True and Ready == False:	
		#for d in range(0,deco_count-1):
			#deco_list[d].rect.x = 0
			#deco_list[d].change_x = 0
		font = pygame.font.Font(None, 60)
		text = font.render("Keys:Arrows to move, [G] to catch the targets, [Y] to pause", 1, constants.BLACK)
		textpos = text.get_rect()
		textpos.centerx = constants.SCREEN_WIDTH/2
		textpos.centery = constants.SCREEN_HEIGHT*2/6
		screen.blit(text, textpos)		
	
		font = pygame.font.Font(None, 60)
		text = font.render("Don't let the targets hit the light blue bar", 1, constants.BLACK)
		textpos = text.get_rect()
		textpos.centerx = constants.SCREEN_WIDTH/2
		textpos.centery = constants.SCREEN_HEIGHT*3/6
		screen.blit(text, textpos)	
		
		font = pygame.font.Font(None, 45)
		text = font.render("Press [G] to continue", 1, constants.BLACK)
		textpos = text.get_rect()
		textpos.centerx = constants.SCREEN_WIDTH/2
		textpos.centery = constants.SCREEN_HEIGHT*5/6
		screen.blit(text, textpos)	
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True		
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_g:
					Ready = True			
	
	
	
		
#---------------------------Jogo--------------------------------------------------
	if Intro == True and Ready == True:
		font = pygame.font.Font(None, 30)
		text = font.render(str(point), 1, constants.WHITE)
		textpos = text.get_rect()
		textpos.centerx = 35
		textpos.centery = 15
		screen.blit(text, textpos)	
	
	
	if Gameover == False:
		font = pygame.font.Font(None, 30)
		text = font.render(str(lifes), 1, constants.WHITE)
		textpos = text.get_rect()
		textpos.centerx = constants.SCREEN_WIDTH -35
		textpos.centery = 15
		screen.blit(text, textpos)
		
	if pause == True:
		font = pygame.font.Font(None, 150)
		text = font.render("GET     READY", 1, constants.BLACK)
		textpos = text.get_rect()
		textpos.centerx = constants.SCREEN_WIDTH/2
		textpos.centery = constants.SCREEN_HEIGHT/2
		screen.blit(text, textpos)				
		font = pygame.font.Font(None, 45)
		
		
	
	
	
#--------------------------Fim de jogo------------------------------------------	
	if Gameover == True:
		for i in range(1201):
				if i%600 == 0: 
					deco = Obs(70,70,constants.MAGENTA)
					drawables_list.add(deco)
					animated_list.add(deco)
					deco.generate()		
		
		Snack.kill()
		player.kill()
		font = pygame.font.Font(None, 150)
		text = font.render("GAME     OVER", 1, constants.BLACK)
		textpos = text.get_rect()
		textpos.centerx = constants.SCREEN_WIDTH/2
		textpos.centery = constants.SCREEN_HEIGHT/2
		screen.blit(text, textpos)				
		font = pygame.font.Font(None, 45)

		
		text = font.render("Press [G] to restart, [V] for Intro and [B] to quit", 1, constants.BLACK)
		textpos = text.get_rect()
		textpos.centerx = constants.SCREEN_WIDTH/2
		textpos.centery = constants.SCREEN_HEIGHT*5/6
		screen.blit(text, textpos)	
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True		
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_g:
					Ready = False
					Gameover = False
					Player = False
					bullet = False
					Snackcount = 0
					point = 0
					miss = 0					
				elif event.key == pygame.K_v:
					Intro = False
					Ready = False
					Gameover = False
					Player = False
					bullet = False
					Snackcount = 0
					point = 0
					miss = 0
					
					
				elif event.key == pygame.K_b:
					done = True				
															
	
	pygame.display.flip()

	clock.tick(constants.FPS)

pygame.quit()
