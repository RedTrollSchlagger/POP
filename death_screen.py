import pygame


def death_screen(surface, screen_height, fps, clock):
    font1 = pygame.font.SysFont('serif', 24)
    output_result = font1.render("Результат ", True, (255, 255, 255))
    death_ground = pygame.image.load('death_ground.jpeg').convert()
    done = False
    while not done:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True

            if event.type == pygame.KEYDOWN:
                keystate = pygame.key.get_pressed()
                if keystate[pygame.K_SPACE]:
                    return False

        surface.fill((0, 0, 0))
        pygame.draw.rect(surface, (255, 255, 255), [500, 0, 230, screen_height], width=1)
        surface.blit(death_ground, (0, 0))
        surface.blit(output_result, (520, screen_height/2))
        pygame.display.flip()
