"""PONG!!!"""

import pygame
from random import randint

# Basic variables being declared
w = 1000
h = 600
center_line = 254, 254, 254
white = 255, 255, 255
blue = 0, 0, 255
red = 255, 0, 0
black = 0, 0, 0


# Class for the two bars
class bars(object):
# Basic class declarations, auto_mate lets us have the AI bar start to move
	def __init__(self,surface, auto_mate):
		self.surface = surface
		self.x = w - w
		self.y = h / 2 - 50
		self.vy = auto_mate
		self.color = 255, 255, 255
		# Controls how wide the bars will be, i.e. 10 wide
		self.locator = [0,1,2,3,4,5,6,7,8,9]
		
	# Draws our bars
	def draw(self, starting_location):
		for i in self.locator:
			pygame.draw.line(self.surface, self.color, ((starting_location + i), self.y), ((starting_location + i), (self.y + 100)))
	
	# Will take in our button presses and sends true if its being pressed down,
	# Else when its up, bar stops moving
	def keyPressed(self, inputKey):
		self.keysPressed = pygame.key.get_pressed()
		if self.keysPressed[inputKey]:
			return True
		else:
			return False
	
	# Controls the down button
	def event(self, event):
		if event.key == pygame.K_DOWN:
			self.vy = 1
		elif event.key == pygame.K_UP:
			self.vy = -1
	
	# Controls the up button
	def event1(self, event1):
		if event1.key == pygame.K_DOWN:
			self.vy = 0
		elif event1.key == pygame.K_UP:
			self.vy = 0
		
	# Controls movement of the bars
	def move(self):
		self.y += self.vy

	# Checks to make sure when it hits the top or bottom it bounces back
	def check(self):
		if self.y + 100 == h - 1:
			self.vy = self.vy * -1
		elif self.y == (1):
			self.vy = self.vy * -1

# Ball class			
class ball(object):
	# Declares the basic variables, also scores are placed in here
	def __init__(self,surface):
		self.current_score = 0
		self.current_score_two = 9
		self.surface = surface
		self.x = w / 2 - 15
		self.y = h / 2 - 15
		self.vx = 1
		self.vy = 1
	
	# Draws the ball
	def draw(self):
		pygame.draw.rect(self.surface, blue, (self.x, self.y, 30, 30))
	
	# Move the ball
	def move(self):
		self.x += self.vx
		self.y += self.vy
	
	# When a player scores, resets the ball
	def reset(self):
		self.set_me = self.crazy_num_gen()
		self.x = w / 2 - 15
		self.y = w / 2 - 15
		self.vx = self.vx * -1
		self.vy = self.vy * self.set_me
		
	# Picks a direction either positive or negative	
	def crazy_num_gen(self):
		self.go_away = randint(0, 1)
		if self.go_away == 0:
			return 1
		else:
			return -1
		
	# will edit this to bounce off the other players bar
	def check(self):
		# left side
		r, g, b, a = self.surface.get_at((self.x - 1, self.y))
		#bottom side
		r1, g1, b1, a1 = self.surface.get_at((self.x, (self.y + 31)))
		#right side
		r2, g2, b2, a2 = self.surface.get_at(((self.x + 31), self.y))
		#up side
		r3, g3, b3, a3 = self.surface.get_at(((self.x + 30), self.y - 1))
		# This checks where the ball is and will either bounce or cause it to score
		if (r, g, b) == (255, 255, 255):
			self.vx = self.vx * -1
		elif (r, g, b) == (red):
			# Will reset toward opponent
			score_board_2.score_setter(self.current_score_two)
			print self.current_score_two
			score_board_2.new_line_drawer(score_board_2.score_outline, black)
			self.current_score_two += 1
			self.reset()
		elif (r1, g1, b1) == (255, 255, 255):
			self.vy = self.vy * -1
		elif (r2, g2, b2) == (255, 255, 255):
			self.vx = self.vx * -1
		elif (r2, g2, b2) == (255, 0, 0):
			print self.current_score
			# Sets score outline to the current number...
			score_board_1.score_setter(self.current_score)
			# So that it can be fillled in black and reset
			score_board_1.new_line_drawer(score_board_1.score_outline, black)
			self.current_score += 1
			self.reset()
		elif (r3, g3, b3) == (255, 255, 255):
			self.vy = self.vy * -1
		
		if self.current_score == 10:
			screen.blit(background, (0, 0))
			pygame.time.delay(100)
			self.current_score = 0
			self.current_score_two = 0
		elif self.current_score_two == 10:
			screen.blit(background_1, (0, 0))
			pygame.time.delay(100)
			self.current_score = 0
			self.current_score_two = 0


class table(object):
	def __init__(self, screen, side):
		self.surface = screen
		self.score_outline = []
		self.x1 = w / 2 - 60
		self.x2 = w / 2 + 60
		self.y1 = h - 80
		# sets if its right or left of center line for the score
		self.lor = side

		# holds all points for score
		self.d1 = [(w / 2 - 20*(self.lor)), (w / 2 - 20*(self.lor)), (w / 2 - 20*(self.lor)), (w / 2 - 40*(self.lor)), (w / 2 - 40*(self.lor)), (w / 2 - 40*(self.lor)), (w / 2 - 40*(self.lor))]
		self.d2 = [(h - 60), (h - 40), (h - 20), (h - 60), (h - 40), (h - 20), (h - 40)]
		self.d3 = [(w / 2 - 20*(self.lor)), (w / 2 - 20*(self.lor)), (w / 2 - 40*(self.lor)), (w / 2 - 20*(self.lor)), (w / 2 - 40*(self.lor)), (w / 2 - 40*(self.lor)), (w / 2 - 20*(self.lor))]
		self.d4 = [(h - 40), (h - 20), (h - 20), (h - 60), (h - 60), (h - 40), (h - 40)]
		
	#WORKS!!!, we send it the current score then it changes the score outline
	def score_setter(self,sendin_it):
		self.sending_it = sendin_it
		del self.score_outline[:]
		if self.sending_it == 0:
			self.score_outline = [0, 1, 2, 3, 4, 5]
		elif self.sending_it == 1:
			if self.lor == 1:
				self.score_outline = [0, 1]
			else:
				self.score_outline = [4, 5]
		elif self.sending_it == 2:
			if self.lor == 1:
				self.score_outline = [0, 2, 3, 5, 6]
			else:
				self.score_outline = [1, 2, 3, 4, 6]
		elif self.sending_it == 3:
			if self.lor == 1:
				self.score_outline = [0, 1, 2, 3, 6]
			else:
				self.score_outline = [2, 3, 4, 5, 6]
		elif self.sending_it == 4:
			if self.lor == 1:
				self.score_outline = [0, 1, 4, 6]
			else:
				self.score_outline = [0, 4, 5, 6]
		elif self.sending_it == 5:
			if self.lor == 1:
				self.score_outline = [1, 2, 3, 4, 6]
			else:
				self.score_outline = [0, 2, 3, 5, 6]
		elif self.sending_it == 6:
			if self.lor == 1:
				self.score_outline = [1, 2, 3, 4, 5, 6]
			else:
				self.score_outline = [0, 1, 2, 3, 5, 6]
		elif self.sending_it == 7:
			if self.lor == 1:
				self.score_outline = [0, 1, 3]
			else:
				self.score_outline = [3, 4, 5]
		elif self.sending_it == 8:
				self.score_outline = [0, 1, 2, 3, 4, 5, 6]
		elif self.sending_it == 9:
			if self.lor == 1:
				self.score_outline = [0, 1, 3, 4, 6]
			else:
				self.score_outline = [0, 3, 4, 5, 6]
			
	# Draws all score related lines		
	def new_line_drawer(self, passes, line_color):
		pygame.draw.line(self.surface, center_line, (self.x1, (h - 1)), (self.x1, self.y1))
		pygame.draw.line(self.surface, center_line, (self.x1, (self.y1)), (self.x2, self.y1))
		pygame.draw.line(self.surface, center_line, (self.x2, self.y1), (self.x2, (h - 1)))
		
		for i in passes:
			pygame.draw.line(self.surface, line_color, (self.d1[i], self.d2[i]), (self.d3[i], self.d4[i]))
		# 0 is top right, 1 is bottom right, 2 is bottom, 3 is top, 4 is top left, 5 is bottom left, 6 is middle
	
		
		
clock = pygame.time.Clock()
screen = pygame.display.set_mode((w, h))
background = pygame.image.load('you_win.bmp').convert()
background_1 = pygame.image.load('you_lose.bmp').convert()

player1 = bars(screen, 0)
player2 = bars(screen, 1)
target = ball(screen)
target1 = ball(screen)
score_board_1 = table(screen, 1)
score_board_2 = table(screen, -1)


running = True

while running:
	screen.fill((0, 0, 0))
	pygame.draw.line(screen, red, ((w - w), (h - h)), ((w - w), (h - 1)))
	pygame.draw.line(screen, red, ((w - 1), (h - h)), ((w - 1), (h - 1)))
	pygame.draw.line(screen, white, ((w - w), (h - h)), ((w), (h - h)))
	pygame.draw.line(screen, white, ((w - w), (h - 1)), ((w), (h - 1)))
	pygame.draw.line(screen, center_line, ((w / 2), (h - h)), ((w / 2), (h)))
	pygame.draw.line(screen, center_line, ((w / 2 + 1), (h - h)), ((w / 2 +1), (h)))
	pygame.draw.line(screen, center_line, ((w / 2 - 1), (h - h)), ((w / 2 - 1), (h)))
	score_board_1.score_setter(target.current_score)
	score_board_1.new_line_drawer(score_board_1.score_outline, center_line)
	score_board_2.score_setter(target.current_score_two)
	score_board_2.new_line_drawer(score_board_2.score_outline, center_line)
	player1.draw(player1.x)
	player2.draw(w - 11)
	player1.move()
	player2.move()
	player1.check()
	player2.check()
	target.draw()
	target.move()
	target.check()
	
	# Controls the movement, once the button is released it will
	# stop the bar from moving
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		elif event.type == pygame.KEYDOWN:
			player1.event(event)
		elif event.type == pygame.KEYUP:
			player1.event1(event)
		
			
	pygame.display.flip()
	clock.tick(300)