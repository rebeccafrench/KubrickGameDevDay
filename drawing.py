import pygame, sys, random
import pygame.event as GAME_EVENTS
import pygame.locals as GAME_GLOBALS
#import keyboard	#import functions defined in out keyboard.py library script

pygame.init()	#initialize the library

clock = pygame.time.Clock()

blob = pygame.image.load('images/snake.jpg')

#defining flying shape variables
windowwidth = 500
windowheight = 400
rectX = 10.0	#X coordinate of the shape
rectY = 10.0	#Y coordinate of the shape
rectEndX = 148	#X coordinate of the end of the shape
rectEndY = 125	#X coordinate of the end of the shape
xdirection = 1
ydirection = 1
window = pygame.display.set_mode( (windowwidth, windowheight) )	#setting the display variable as 500x400 pixels

#defining Square Variables
playerSize = 20
playerX = (windowwidth / 2) - (playerSize / 2)
playerY = windowheight - playerSize
playerVX = 1.0
playerVY = 0.0
jumpHeight = 40.0
moveSpeed = 1.0
maxSpeed = 10.0
gravity = 1.0

# Keyboard Variables
leftDown = False    #default to false since the player hasn't done these actions yet
rightDown = False   #default to false since the player hasn't done these actions yet
haveJumped = False	#default to false since the player hasn't done these actions yet

pygame.display.set_caption('Becca\'s Game!')

def quitgame():	#defining a function to quit the game - useful as we will call it multiple times
	pygame.quit()
	sys.exit()

def move():	#defining a function to get the player (square) to move/jump

	global playerX, playerY, playerVX, playerVY, haveJumped, gravity	#globally accessible function, not just local

	# Move left 
	if leftDown:
		#If we're already moving to the right, reset the moving speed and invert the direction
		if playerVX > 0.0:
			playerVX = moveSpeed
			playerVX = -playerVX	
		# Make sure our square doesn't leave our window to the left
		if playerX > 0:
			playerX += playerVX	

	# Move right
	if rightDown:
		# If we're already moving to the left reset the moving speed again
		if playerVX < 0.0:
			playerVX = moveSpeed
		# Make sure our square doesn't leave our window to the right
		if playerX + playerSize < windowwidth:
			playerX += playerVX

	if playerVY > 1.0:
		playerVY = playerVY * 0.9
	else :
		playerVY = 0.0
		haveJumped = False

	# Is our square in the air? Better add some gravity to bring it back down!
	if playerY < windowheight - playerSize:
		playerY += gravity
		gravity = gravity * 1.1
	else :
		playerY = windowheight - playerSize
		gravity = 1.0

	playerY -= playerVY

	if playerVX > 0.0 and playerVX < maxSpeed or playerVX < 0.0 and playerVX > -maxSpeed:
		if haveJumped == False:
			playerVX = playerVX * 1.1
			
while True:	#get the game to run indefinitely using this loop
	window.fill((0, 0, 0))	#black background
	
	# drawing the flying shape
	#pygame.draw.rect(window, (114, 233, 255), (rectX, rectY, rectEndX, rectEndY))	#draw a 2D rectangle in the game - RGB colour coords can be found by searching color picker on google
	#pygame.draw.arc(window, (0, 0, 0), (rectX + 10, rectY + 10, 50, 50), 4.71238898038, 1.57079632679, 5)
	#pygame.draw.arc(window, (0, 0, 0), (rectX + 10, rectY + 60, 50, 50), 4.71238898038, 1.57079632679, 5)
	#pygame.draw.line(window, (0, 0, 0), (rectX + 35, rectY + 10), (rectX + 35, rectY + 110), 5)
	#pygame.draw.line(window, (0, 0, 0), (rectX + 90, rectY + 10), (rectX + 90, rectY + 110), 5)
	#pygame.draw.line(window, (0, 0, 0), (rectX + 90, rectY + 10), (rectX + 130, rectY + 10), 5)
	#pygame.draw.line(window, (0, 0, 0), (rectX + 90, rectY + 60), (rectX + 130, rectY + 60), 5)
	
	# flying snake :D
	window.blit(blob, (rectX, rectY, rectEndX, rectEndY))
	
	# if statements to tell the flying shape to bounce back when it reaches the end of the screen
	movement = random.randint(0, 3)
	if rectX > windowwidth - rectEndX:
		xdirection = -1
	if rectX < 0:
		xdirection = 1
	rectX += xdirection * movement	#making the rectangle move by adding pixels to it's position variable
	if rectY > windowheight - rectEndY:
		ydirection = -1
	if rectY < 0:
		ydirection = 1
	rectY += ydirection * movement
	
	# drawing the moving player
	pygame.draw.rect(window, (255,0,0), (playerX, playerY, playerSize, playerSize))
	

	# Get a list of all events that happened since the last redraw
	for event in GAME_EVENTS.get():

		if event.type == pygame.KEYDOWN:

			if event.key == pygame.K_LEFT:
				leftDown = True
			if event.key == pygame.K_RIGHT:
				rightDown = True
			if event.key == pygame.K_UP:
				if not haveJumped:
					haveJumped = True
					playerVY += jumpHeight
			if event.key == pygame.K_ESCAPE:
				quitGame()

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT:
				leftDown = False
				playerVX = moveSpeed
			if event.key == pygame.K_RIGHT:
				rightDown = False
				playerVX = moveSpeed

	move()
	
	for event in GAME_EVENTS.get():	#adding the option to quit
		if event.type == GAME_GLOBALS.QUIT:
			quitgame()
		if event.type == pygame.KEYDOWN:	#if the player hits the escape key, then quit the game
			if event.key == pygame.K_ESCAPE:
				quitgame()
	
	clock.tick(100)
	pygame.display.update()