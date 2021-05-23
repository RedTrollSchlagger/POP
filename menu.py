import pygame


def menu_screen(surface, GAME_ZONE_W, SCREEN_HEIGHT, FPS, clock):
	active_zone = [510, SCREEN_HEIGHT/2-40]
	font1 = pygame.font.SysFont('serif', 24)
	start_button = font1.render("Начать игру", True, (255, 255, 255))
	top_button = font1.render("Рекорды", True, (255, 255, 255))
	store_button = font1.render("Магазин", True, (255, 255, 255))

	skin1 = font1.render("Золото Одина", True, (255, 255, 255))
	skin2 = font1.render("Дионис", True, (255, 255, 255))
	skin3 = font1.render("Лазурь", True, (255, 255, 255))
	skin4 = font1.render("Кровь и вино", True, (255, 255, 255))
	ultimate_skin = font1.render("Чемпионство мира", True, (255, 255, 255))

	prise1 = font1.render("10 $", True, (255, 255, 255))
	prise2 = font1.render("20 $", True, (255, 255, 255))
	prise3 = font1.render("30 $", True, (255, 255, 255))
	prise4 = font1.render("40 $", True, (255, 255, 255))
	ultimate_prise = font1.render("Ваша душа...", True, (255, 255, 255))

	done = False
	while not done:

		clock.tick(FPS)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True
				return True

			if event.type == pygame.KEYDOWN:
				keystate = pygame.key.get_pressed()
				if keystate[pygame.K_DOWN]:
					active_zone[1] += 40
				if keystate[pygame.K_UP]:
					active_zone[1] -= 40
				if keystate[pygame.K_RETURN]:
					if active_zone[1] == SCREEN_HEIGHT/2-40:
						done = True
						return False


		if active_zone[1] > SCREEN_HEIGHT/2+40:
			active_zone[1] -= 120
		if active_zone[1] < SCREEN_HEIGHT/2-40:
			active_zone[1] += 120

		surface.fill((0, 0, 0))

		pygame.draw.rect(surface, (255, 255, 255), [0, 0, GAME_ZONE_W, SCREEN_HEIGHT], width=1)
		pygame.draw.rect(surface, (255, 255, 255), [GAME_ZONE_W+20, 0, 230, SCREEN_HEIGHT], width=1)

		surface.blit(start_button, (520, SCREEN_HEIGHT/2 - 40))
		surface.blit(top_button, (520, SCREEN_HEIGHT/2))
		surface.blit(store_button, (520, SCREEN_HEIGHT/2 + 40))

		if active_zone[1] == SCREEN_HEIGHT/2 + 40:
			surface.blit(skin1, (20, SCREEN_HEIGHT/2 - 80))
			surface.blit(skin2, (20, SCREEN_HEIGHT/2 - 40))
			surface.blit(skin3, (20, SCREEN_HEIGHT/2))
			surface.blit(skin4, (20, SCREEN_HEIGHT/2 + 40))
			surface.blit(ultimate_skin, (20, SCREEN_HEIGHT/2 + 80))

			pygame.draw.rect(surface, (255, 255, 0), [250, SCREEN_HEIGHT/2 - 78, 20, 20])
			pygame.draw.rect(surface, (0, 255, 0), [250, SCREEN_HEIGHT/2 - 38, 20, 20])
			pygame.draw.rect(surface, (0, 250, 175), [250, SCREEN_HEIGHT/2 + 2, 20, 20])
			pygame.draw.rect(surface, (255, 40, 0), [250, SCREEN_HEIGHT/2 + 42, 20, 20])

			surface.blit(prise1, (300, SCREEN_HEIGHT/2 - 80))
			surface.blit(prise2, (300, SCREEN_HEIGHT/2 - 40))
			surface.blit(prise3, (300, SCREEN_HEIGHT/2))
			surface.blit(prise4, (300, SCREEN_HEIGHT/2 + 40))
			surface.blit(ultimate_prise, (300, SCREEN_HEIGHT/2 + 80))

		pygame.draw.rect(surface, (255, 255, 255), [active_zone[0], active_zone[1], 180, 30], width=1)
		pygame.display.flip()
