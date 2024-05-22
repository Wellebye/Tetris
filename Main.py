import pygame, sys
from game import Game
from colors import Colors

pygame.init()

# Initialize fonts and surfaces
title_font = pygame.font.Font(None, 40)
score_surface = title_font.render("Score", True, Colors.white)
next_surface = title_font.render("Next", True, Colors.white)
game_over_surface = title_font.render("GAME OVER", True, Colors.white)
Restart1 = title_font.render("Press R", True, Colors.white)
Restart2 = title_font.render("To", True, Colors.white)
Restart3 = title_font.render("Restart", True, Colors.white)

# Initialize rectangles
score_rect = pygame.Rect(320, 55, 170, 60)
next_rect = pygame.Rect(320, 215, 170, 180)

# Initialize screen and caption
screen = pygame.display.set_mode((500, 620))
pygame.display.set_caption("Python Tetris")

# Initialize clock and game
clock = pygame.time.Clock()
game = Game()

# Initialize lives variable to 3
lives = 0

# Set up game update event
GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 200)

# Game loop
while True:
	# Handle events
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if game.game_over == True:
				if lives > 1:
					lives -= 1
					game.game_over = False
					game.reset()
				elif event.key == pygame.K_r and game.game_over == True:
					game.game_over = False
					game.score = 0
					lives = 3
					game.reset()
			if event.key == pygame.K_LEFT and game.game_over == False:
				game.move_left()
			if event.key == pygame.K_RIGHT and game.game_over == False:
				game.move_right()
			if event.key == pygame.K_DOWN and game.game_over == False:
				game.move_down()
				game.update_score(0, 1)
			if event.key == pygame.K_UP and game.game_over == False:
				game.rotate()
		if event.type == GAME_UPDATE and game.game_over == False:
			game.move_down()

	# Drawing
	score_value_surface = title_font.render(str(game.score), True, Colors.white)

	screen.fill(Colors.dark_blue)
	screen.blit(score_surface, (365, 20, 50, 50))
	screen.blit(next_surface, (375, 180, 50, 50))

	if game.game_over == True:
		screen.blit(game_over_surface, (320, 450, 50, 50))
		screen.blit(Restart1, (360, 490, 50, 50))
		screen.blit(Restart2, (390, 520, 50, 50))
		screen.blit(Restart3, (360, 550, 50, 50))
  
	pygame.draw.rect(screen, Colors.light_blue, score_rect, 0, 10)
	screen.blit(score_value_surface, score_value_surface.get_rect(centerx=score_rect.centerx,
																  centery=score_rect.centery))
	pygame.draw.rect(screen, Colors.light_blue, next_rect, 0, 10)
	game.draw(screen)

	# Display remaining lives
	lives_surface = title_font.render("Lives: " + str(lives), True, Colors.white)
	screen.blit(lives_surface, (20, 20))

	pygame.display.update()
	clock.tick(60)