import pygame

class Room(pygame.sprite.Sprite):
    room_sprite = None

    pos_x = 0
    pos_y = 0

    #image_char = "assets/player-0.png"

    def __init__(self, size_x:int, size_y:int, sprite:str, display_view:pygame.surface.Surface):
        self.surf = pygame.Surface([size_x, size_y])
        self.texture = pygame.transform.scale(pygame.image.load(sprite), (size_x, size_y))
        self.sprite = self.texture

        # self.surf.blit(self.icon, (x,y))
        # surf.blit(icon, (0,0))
        self.rect = self.surf.get_rect()

        # print('Room initialised')

    # TODO: animation pass 
    def update(self):
        pass


    def render(self, display_view : pygame.surface.Surface):
        display_view.blit(self.texture, (self.pos_x, self.pos_y))

    # TODO: implement room interactions
    def interact(self):
        pass
