import pygame

WINDOW_SIZE = WIDTH, HIEGHT = 800, 600
display_surface = pygame.display.set_mode(WINDOW_SIZE)

class mcq_Button:
    def __init__(self, image, x, y):
        img = pygame.image.load(image)
        self.image = pygame.transform.scale(img, (round(25), round(25)))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def draw1(self):
        display_surface.blit(self.image, (self.rect.x, self.rect.y))