import menu
import pygame

pygame.init()
screen = pygame.display.set_mode((740, 640))
pygame.display.set_caption("testing")
clock = pygame.time.Clock()

main = False
while not main:
	menu.menu_screen(screen, clock)

pygame.quit()