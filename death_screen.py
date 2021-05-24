import pygame
import game_process
import menu
from parameters import *


def death_screen(surface, clock):
    font1 = pygame.font.SysFont('serif', 24)
    res = open(file_add, "r")
    point = res.readline()
    output_result = font1.render("Результат " + point, True, (255, 255, 255))
    death_ground = pygame.image.load('death_ground.jpeg').convert()
    done = False
    while not done:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                keystate = pygame.key.get_pressed()
                if keystate[pygame.K_SPACE]:
                    game_process.game_process(surface, clock)
                if keystate[pygame.K_ESCAPE]:
                    menu.menu_screen(surface, clock)

        surface.fill((0, 0, 0))
        pygame.draw.rect(surface, (255, 255, 255), [500, 0, 230, screen_height], width=1)
        surface.blit(death_ground, (0, 0))
        surface.blit(output_result, (520, screen_height/2))
        pygame.display.flip()
