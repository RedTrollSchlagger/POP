import game_process
import pygame
import shop_screen
from parameters import *


def menu_screen(surface, clock):
	active_zone = [510, screen_height / 2 - 40, 180, 30]
	font = pygame.font.SysFont('serif', 24)
	start_button = font.render("Начать игру", True, (255, 255, 255))
	top_button = font.render("Рекорды", True, (255, 255, 255))
	store_button = font.render("Магазин", True, (255, 255, 255))

	done = False
	while not done:

		clock.tick(fps)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

			if event.type == pygame.KEYDOWN:
				keystate = pygame.key.get_pressed()
				if keystate[pygame.K_DOWN]:
					active_zone[1] += 40
				if keystate[pygame.K_UP]:
					active_zone[1] -= 40
				if keystate[pygame.K_LEFT] and active_zone[1] == screen_height/2+40 and active_zone[0] == 510:
					active_zone[0] -= 500
					active_zone[1] = screen_height / 2 - 80
					active_zone[2] = 450
				if keystate[pygame.K_RIGHT] and active_zone[0] == 10:
					active_zone[0] += 500
					active_zone[1] = screen_height / 2 + 40
					active_zone[2] = 180
				if keystate[pygame.K_RETURN]:
					if active_zone[1] == screen_height/2-40:
						game_process.game_process(surface, clock)

		if active_zone[0] == 510:
			if active_zone[1] > screen_height/2+40:
				active_zone[1] -= 120
			if active_zone[1] < screen_height/2-40:
				active_zone[1] += 120
		if active_zone[0] == 10:
			if active_zone[1] > screen_height/2+80:
				active_zone[1] -= 200
			if active_zone[1] < screen_height/2 - 80:
				active_zone[1] += 200

		surface.fill((0, 0, 0))

		pygame.draw.rect(surface, (255, 255, 255), [0, 0, game_zone_w, screen_height], width=1)
		pygame.draw.rect(surface, (255, 255, 255), [game_zone_w + 20, 0, 240, screen_height], width=1)

		surface.blit(start_button, (520, screen_height / 2 - 40))
		surface.blit(top_button, (520, screen_height / 2))
		surface.blit(store_button, (520, screen_height / 2 + 40))

		if active_zone[1] == screen_height/2 + 40 or active_zone[0] == 10:
			shop_screen.shop(surface)

		pygame.draw.rect(surface, (255, 255, 255), [active_zone[0], active_zone[1], active_zone[2], 30], width=1)
		pygame.display.flip()
