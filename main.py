import pygame
import menu
import game_process
import death_screen

pygame.init()
screen = pygame.display.set_mode((740, 660))
pygame.display.set_caption("testing")
clock = pygame.time.Clock()

main = False
while not main:
	if not main:
		main = menu.menu_screen(screen, 480, 640, 120, clock)
	if not main:
		main = game_process.game_process(screen, 480, 640, 120, clock)
	if not main:
		main = death_screen.death_screen(screen, 480, 120, clock)

pygame.quit()