from parameters import *
import pygame


def shop(surface):
    font = pygame.font.SysFont('serif', 24)
    skin1 = font.render("Золото Одина", True, (255, 255, 255))
    skin2 = font.render("Дионис", True, (255, 255, 255))
    skin3 = font.render("Лазурь", True, (255, 255, 255))
    skin4 = font.render("Кровь и вино", True, (255, 255, 255))
    ultimate_skin = font.render("Чемпионство мира", True, (255, 255, 255))

    prise1 = font.render("10 $", True, (255, 255, 255))
    prise2 = font.render("20 $", True, (255, 255, 255))
    prise3 = font.render("30 $", True, (255, 255, 255))
    prise4 = font.render("40 $", True, (255, 255, 255))
    ultimate_prise = font.render("Ваша душа...", True, (255, 255, 255))

    surface.blit(skin1, (20, screen_height / 2 - 80))
    surface.blit(skin2, (20, screen_height / 2 - 40))
    surface.blit(skin3, (20, screen_height / 2))
    surface.blit(skin4, (20, screen_height / 2 + 40))
    surface.blit(ultimate_skin, (20, screen_height / 2 + 80))

    pygame.draw.rect(surface, (255, 255, 0), [250, screen_height / 2 - 78, 20, 20])
    pygame.draw.rect(surface, (0, 255, 0), [250, screen_height / 2 - 38, 20, 20])
    pygame.draw.rect(surface, (0, 250, 175), [250, screen_height / 2 + 2, 20, 20])
    pygame.draw.rect(surface, (255, 40, 0), [250, screen_height / 2 + 42, 20, 20])

    surface.blit(prise1, (300, screen_height / 2 - 80))
    surface.blit(prise2, (300, screen_height / 2 - 40))
    surface.blit(prise3, (300, screen_height / 2))
    surface.blit(prise4, (300, screen_height / 2 + 40))
    surface.blit(ultimate_prise, (300, screen_height / 2 + 80))
