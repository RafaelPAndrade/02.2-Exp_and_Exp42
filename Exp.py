#coding: utf-8

import pygame
import constants
from block import Block
from Obj import Obj
from Obs import Obs


#-----Writes text, using 5 arguments: position of center x, position of center y, size, color(RGB), wording
def words(x, y, size, color, string):
    font = pygame.font.Font(None, size)
    text = font.render(string, 1, color) #color may refer to the constants.py file
    textpos = text.get_rect()
    textpos.centerx = x
    textpos.centery = y
    screen.blit(text, textpos)
    
    return True



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
ate = 0
deco_count=0
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
				
				elif event.key == pygame.K_a:
					player.kill()	
				elif event.key == pygame.K_g:
					player.image.fill(constants.GREEN)
					Snack.image.fill(constants.GREENISH)
					if Intro == True:
						if Snack.rect.x>= player.rect.x and Snack.rect.x<= player.rect.x + constants.Height1 - constants.ObsSize and Snack.rect.y >= player.rect.y and Snack.rect.y <= player.rect.y + constants.Height1 - constants.ObsSize:
							ate += 1
							Snack.kill()
							bullet = False
						else:
							True
		
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
	
		
#-----------------------------Desenhos(não pôr nada gráfico antes, will be erased)------------------------------------------
	if pause == False:
		animated_list.update()	
			
	screen.fill(constants.WHITE)

	drawables_list.draw(screen)
	words(player.rect.x+(constants.Height1/2), player.rect.y+(constants.Height1/2), 40, constants.RED, str(lifes))

#-------------------------------Introdução--------------------------------------
	if Intro == False:
		Snack.kill()		
		
		
		words(constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT*6/7, 45, constants.BLACK, "Press [G] to continue")
		
	    
					
					
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
			    #deco.generate()
			    deco_list.append(deco)
			    deco_count += 1
			    print(len(deco_list))
				
#--------------------------------Instruções------------------------------------
	if Intro == True and Ready == False:
	    print(str(deco_count))		
	    
		
		
	    words(constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT*2/6, 60, constants.BLACK, "Keys:Arrows to move, [G] to catch the targets, [Y] to pause")
		
		
	    words(constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT*3/6, 60, constants.BLACK, "Don't let the targets hit the light blue bar")
		
	    words(constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT*6/7, 45, constants.BLACK, "Press [G] to continue")
		
		
		
	    for event in pygame.event.get():
	        if event.type == pygame.QUIT:
		    done = True		
		elif event.type == pygame.KEYDOWN:
		    if event.key == pygame.K_g:
			Ready = True			
	
	
	
		
#---------------------------Jogo--------------------------------------------------
	if Intro == True and Ready == True:
		words(35, 15, 30, constants.WHITE, str(ate))
	
	
	if Gameover == False:
		words(constants.SCREEN_WIDTH -35, 15, 30, constants.WHITE, str(lifes))
		
	if pause == True:		
		words(constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2, 150, constants.BLACK, "GET     READY")
		
		
	
	
	
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

		words(constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2, 150, constants.BLACK, "GAME     OVER")
		
		words(constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT*5/6, 45, constants.BLACK, "Press [G] to restart, [V] for Intro and [B] to quit")
		
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
					ate = 0
					miss = 0					
				elif event.key == pygame.K_v:
					Intro = False
					Ready = False
					Gameover = False
					Player = False
					bullet = False
					Snackcount = 0
					ate = 0
					miss = 0
					
					
				elif event.key == pygame.K_b:
					done = True				
															
	
	pygame.display.flip()

	clock.tick(constants.FPS)

pygame.quit()