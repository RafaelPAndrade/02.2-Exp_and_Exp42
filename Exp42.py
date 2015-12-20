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

player1 = Obj((constants.SCREEN_WIDTH/2-(constants.Height1/2)),(constants.SCREEN_HEIGHT*4/6-(constants.Height1/2)),constants.Height1,constants.Height1, constants.BLUE)
drawables_list.add(player1)
animated_list.add(player1)

player2 = Obj((constants.SCREEN_WIDTH/2-(constants.Height1/2)),(constants.SCREEN_HEIGHT*4/6-(constants.Height1/2)),constants.Height1,constants.Height1, constants.RED)
drawables_list.add(player2)
animated_list.add(player2)

cannon = Block(0, 0, 70, constants.SCREEN_HEIGHT, constants.LBLUE)
for i in range(0,constants.SCREEN_HEIGHT,50):
	subcanon = Block(70, i+10 , 40, 30, constants.GREY)
	drawables_list.add(subcanon)
wall = Block((constants.SCREEN_WIDTH - 70), 0, 70, constants.SCREEN_HEIGHT, constants.CYAN)
drawables_list.add(wall)
drawables_list.add(cannon)

#-----------------------------------Constants----------------------------------
Intro = False
Ready = False
Gameover = False
bullet1 = False
bullet2 = False
Player1 = False
Player2 = False
pause = False



miss = 0
lifes = 10
point1 = 0
point2 = 0
deco = Obs(0,0,constants.WHITE)
Snack = Obs(0,0,constants.WHITE)
Snack2 = Obs(0,0,constants.WHITE)
Snackcount = 0

while not done:
#---------------------------------Lógica--------------------------
	
	
	if Ready == True:
		if Player1==False:
			player1.kill()
			player1 = Obj((constants.SCREEN_WIDTH/2-(constants.Height1/2)),(constants.SCREEN_HEIGHT*4/6-(constants.Height1/2)),constants.Height1,constants.Height1, constants.RED)
			drawables_list.add(player1)
			animated_list.add(player1)		
			Player1 = True
		
		
		if Player2==False:
			player2.kill()
			player2 = Obj((constants.SCREEN_WIDTH/2-(constants.Height1/2)),(constants.SCREEN_HEIGHT*4/6-(constants.Height1/2)),constants.Height1,constants.Height1, constants.BLUE)
			drawables_list.add(player2)
			animated_list.add(player2)		
			Player2 = True		
		
		
		lifes = 10 - miss
		if lifes <= 0:
			Gameover = True	
	
		if bullet1 == False:
			Snack = Obs(110,70,constants.YELLOW)
			drawables_list.add(Snack)
			animated_list.add(Snack)
			Snack.generate()
			Snack.change_x= Snack.change_x*(Snackcount/40) + 2
			bullet1 = True
			Snackcount += 1
			
		if Snack.rect.x >= constants.SCREEN_WIDTH - constants.ObsSize - 70:
			Snack.kill()
			bullet1 = False
			miss += 1
			
		#if bullet2 == False:
			#Snack2 = Obs(110,70,constants.YELLOW)
			#drawables_list.add(Snack2)
			#animated_list.add(Snack2)
			#Snack2.generate()
			#Snack2.change_x= Snack2.change_x*(Snackcount/30) + 2
			#bullet2 = True
						
		if Snack2.rect.x >= constants.SCREEN_WIDTH - constants.ObsSize - 70:
			Snack2.kill()
			bullet2 = False
			miss += 1		
		
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		
		elif event.type == pygame.KEYDOWN:
			if Ready == True:
				if event.key == pygame.K_UP:
					player1.move_up()
				if event.key == pygame.K_DOWN:
					player1.move_down()
				if event.key == pygame.K_LEFT:
					player1.move_left()
				if event.key == pygame.K_RIGHT:
					player1.move_right()
				if event.key == pygame.K_l:
					player1.image.fill(constants.GREEN)
					Snack.image.fill(constants.GREENISH)
					Snack2.image.fill(constants.GREENISH)
					if Intro == True:
						if Snack.rect.x>= player1.rect.x and Snack.rect.x<= player1.rect.x + constants.Height1 - constants.ObsSize and Snack.rect.y >= player1.rect.y and Snack.rect.y <= player1.rect.y + constants.Height1 - constants.ObsSize:
							point1 += 1
							Snack.kill()
							bullet1 = False					
											
						if Snack2.rect.x>= player1.rect.x and Snack2.rect.x<= player1.rect.x + constants.Height1 - constants.ObsSize and Snack2.rect.y >= player1.rect.y and Snack2.rect.y <= player1.rect.y + constants.Height1 - constants.ObsSize:
							point1 += 2
							Snack2.kill()
							bullet2 = False						
						
												
						
				if event.key == pygame.K_w:
					player2.move_up()
				if event.key == pygame.K_s:
					player2.move_down()
				if event.key == pygame.K_a:
					player2.move_left()
				if event.key == pygame.K_d:
					player2.move_right()
				if event.key == pygame.K_c:
					player2.image.fill(constants.GREEN)
					Snack.image.fill(constants.GREENISH)
					Snack2.image.fill(constants.GREENISH)
					if Intro == True:
						if Snack.rect.x>= player2.rect.x and Snack.rect.x<= player2.rect.x + constants.Height1 - constants.ObsSize and Snack.rect.y >= player2.rect.y and Snack.rect.y <= player2.rect.y + constants.Height1 - constants.ObsSize:
							point2 += 1
							Snack.kill()
							bullet1 = False					
							
						if Snack2.rect.x>= player2.rect.x and Snack2.rect.x<= player2.rect.x + constants.Height1 - constants.ObsSize and Snack2.rect.y >= player2.rect.y and Snack2.rect.y <= player2.rect.y + constants.Height1 - constants.ObsSize:
							point2 += 1
							Snack2.kill()
							bullet2 = False	
															
				
				
				
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_y:
				if pause == False:
					pause = True
				elif pause == True:
					pause = False
			if event.key == pygame.K_UP:
				player1.dont_move()

			if event.key == pygame.K_DOWN:
				player1.dont_move()

			if event.key == pygame.K_LEFT:
				player1.dont_move()

			if event.key == pygame.K_RIGHT:
				player1.dont_move()			

			if event.key == pygame.K_l:
				player1.image.fill(constants.RED)
				Snack.image.fill(constants.YELLOW)
				Snack2.image.fill(constants.YELLOW)
			if event.key == pygame.K_w:
				player2.dont_move()

			if event.key == pygame.K_s:
				player2.dont_move()

			if event.key == pygame.K_a:
				player2.dont_move()

			if event.key == pygame.K_d:
				player2.dont_move()			

			if event.key == pygame.K_c:
				player2.image.fill(constants.BLUE)
				Snack.image.fill(constants.YELLOW)				
				Snack2.image.fill(constants.YELLOW)
	
	if player1.rect.x <= 110:
		player1.rect.x = 110
	if player1.rect.x >= constants.SCREEN_WIDTH-constants.Height1:
		player1.rect.x = constants.SCREEN_WIDTH-constants.Height1
	if player1.rect.y <= 0:
		player1.rect.y = 0
	if player1.rect.y >= constants.SCREEN_HEIGHT-constants.Height1:
		player1.rect.y = constants.SCREEN_HEIGHT-constants.Height1
	
	if player2.rect.x <= 110:
		player2.rect.x = 110
	if player2.rect.x >= constants.SCREEN_WIDTH-constants.Height1:
		player2.rect.x = constants.SCREEN_WIDTH-constants.Height1
	if player2.rect.y <= 0:
		player2.rect.y = 0
	if player2.rect.y >= constants.SCREEN_HEIGHT-constants.Height1:
		player2.rect.y = constants.SCREEN_HEIGHT-constants.Height1	
		
	if point1 <= 0:
		point1 = 0
	if point2 <= 0:
		point2 = 0
#-----------------------------Desenhos------------------------------------------
	if pause == False:
		animated_list.update()	
			
	screen.fill(constants.WHITE)

	drawables_list.draw(screen)
	

#-------------------------------Introdução--------------------------------------
	if Intro == False:
		Snack.kill()		
		Snack2.kill()
		
		font = pygame.font.Font(None, 45)
		text = font.render("Press [H] to continue", 1, constants.BLACK)
		textpos = text.get_rect()
		textpos.centerx = constants.SCREEN_WIDTH/2
		textpos.centery = constants.SCREEN_HEIGHT*6/7
		screen.blit(text, textpos)	
					
					
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True		
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_h:
					Intro = True		
			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_h:
					Intro = True				
		
		
		for i in range(1201):
			if i%600 == 0: 
				deco = Obs(110,70,constants.MAGENTA)
				drawables_list.add(deco)
				animated_list.add(deco)
				deco.generate()				
				
#--------------------------------Instruções-------------------------------------		
	if Intro == True and Ready == False:	
		for i in range(1201):
			if i%600 == 0: 						
				deco.kill()
		
		
		font = pygame.font.Font(None, 55)
		text = font.render("Keys: Arrows/[W][A][S][D] to move, [L]/[C] to catch", 1, constants.BLACK)
		textpos = text.get_rect()
		textpos.centerx = constants.SCREEN_WIDTH/2
		textpos.centery = constants.SCREEN_HEIGHT*1/6
		screen.blit(text, textpos)
		
		font = pygame.font.Font(None, 55)
		text = font.render("the targets, [Y] to pause", 1, constants.BLACK)	
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
		text = font.render("Press [H] to continue", 1, constants.BLACK)
		textpos = text.get_rect()
		textpos.centerx = constants.SCREEN_WIDTH/2
		textpos.centery = constants.SCREEN_HEIGHT*5/6
		screen.blit(text, textpos)	
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True		
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_h:
					Ready = True			
			
		
#---------------------------Jogo--------------------------------------------------
	if Intro == True and Ready == True:
		font = pygame.font.Font(None, 30)
		text = font.render(str(point1)+"-"+str(point2), 1, constants.WHITE)
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
					deco = Obs(110,70,constants.MAGENTA)
					drawables_list.add(deco)
					animated_list.add(deco)
					deco.generate()		
		
		Snack.kill()
		Snack2.kill()
		player1.kill()
		player2.kill()
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
					Player1 = False
					Player2 = False
					bullet1 = False
					bullet2 = False
					point1 = 0
					point2 = 0
					miss = 0
					Snackcount = 0
					#screen.fill(constants.WHITE)
					#drawables_list.draw(screen)					
				elif event.key == pygame.K_v:
					Intro = False
					Ready = False
					Gameover = False
					Player1 = False
					Player2 = False
					bullet1 = False
					bullet2 = False
					point1 = 0
					point2 = 0
					miss = 0
					Snackcount = 0
					#screen.fill(constants.WHITE)
					#drawables_list.draw(screen)
				elif event.key == pygame.K_b:
					done = True				
															
	
	pygame.display.flip()

	clock.tick(constants.FPS)

pygame.quit()
