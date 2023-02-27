import pygame
# from main import constants
import random

constants = {
    "npc": [17, 25],
    "teacher": [15, 27],
    "player": [18, 26],
    "desk_small": [pygame.image.load("assets/desk_small.png").get_rect().size,
                   pygame.image.load("assets/desk_small.png"), 1, .5, "desk_small"],
    "desk_big": [pygame.image.load("assets/desk_big.png").get_rect().size, pygame.image.load("assets/desk_big.png"), 1,
                 .6, "desk_big"],
    "wall": [None, pygame.image.load("assets/trans_pixel.png"), 1, 1, "wall"],  # No defined size
    "instructions": [pygame.image.load("assets/instructions.png").get_rect().size,
                     pygame.image.load("assets/instructions.png"), 1, 1, "instructions"],
    "start_buttons": [None, None, 1, 1, "start_buttons"]
}

sheet = pygame.image.load("assets/spritesheet1.png")
boy_params = (0, 236) + tuple(constants["player"])

girl_params = (76, 236) + tuple(constants["player"])
teacher_params = (0, 207) + tuple(constants["teacher"])
scale_factor = 2


class Object(pygame.sprite.Sprite):

    def __init__(self, rect, texture, scale_x, scale_y, name, number, status):
        self.texture_rect = rect
        self.texture_pos_x, self.texture_pos_y = rect.x, rect.y
        self.x_size, self.y_size = rect.size
        self.name = name
        self.x_size *= scale_factor
        self.y_size *= scale_factor
        self.number = number
        self.status = status

        self.trigger = pygame.Rect(rect.x - 2, rect.y - 2, self.x_size + 4, self.y_size + 4)

        self.overlap = (scale_x + scale_y) / 2

        self.texture = pygame.transform.scale(texture, (self.x_size, self.y_size))
        self.texture_original = pygame.transform.scale(texture, (self.x_size, self.y_size))

        # new boundries
        self.x_hitbox, self.y_hitbox = self.x_size * scale_x, self.y_size * scale_y
        self.hb_pos_x = rect.x
        self.hb_pos_y = self.texture_pos_y + (self.y_size) - (self.y_hitbox)

        # debugging
        self.rect_surf = pygame.Surface((self.x_hitbox, self.y_hitbox))
        self.rect_surf.fill((250, 0, 0))

        if self.name == "npc":
            # print("siddhant an npc fr")
            bool = random.randint(0, 1)
            if bool == 0:
                bool = False
            elif bool == 1:
                bool = True
            self.texture = pygame.transform.flip(self.texture, bool, False)

        # NPC
        # if name in "desk_small":
        #     displacement_x, displacement_y = (17,3)
        #     increment = (random.randint(0,4)*2)+1

        #     #(pos) + (size_constant)
        #     npc_params = (constants["npc"][0], constants["npc"][1]*increment) + tuple(constants["npc"])
        #     self.NPC = Npc(pygame.rect.Rect((self.texture_pos_x+displacement_x, self.texture_pos_y+displacement_y)+tuple(constants["npc"])), npc_params, 2, 2)

        #     print("NPC for ", self)

        # print("Object: ", self.x_size, self.y_size, self.texture_pos_y, self.texture_pos_y - (self.x_size / 2))

    def render(self, display_surface: pygame.surface.Surface):
        display_surface.blit(self.texture, (self.texture_pos_x, self.texture_pos_y))

        # uncomment to debug
        # display_surface.blit(self.rect_surf, (self.hb_pos_x,self.hb_pos_y))


class Timer():
    current_tick = 0.

    def __init__(self, start_time, text="Time taken: {}" + "s",
                 params={"size": (20, 500), "position": (0, 0), "color": (0, 0, 0), "text_size": 30}):
        self.size_x, self.size_y = params["size"]
        self.pos_x, self.pos_y = params["position"]
        self.color = params["color"]
        self.font = pygame.font.Font('assets/Minecraftia.ttf', 29)
        self.text = text

        self.time = start_time

    def change_position(self, new_pos):
        self.pos_x, self.pos_y = new_pos

    def tick(self, increment, replace=False):
        if replace:
            self.time = increment
        elif not replace:
            self.time += increment

    def render(self, display_surface: pygame.surface.Surface):
        new_text = self.font.render(self.text.format(str(self.time)), False, self.color)
        display_surface.blit(new_text, (self.pos_x, self.pos_y))

# class Npc(pygame.sprite.Sprite):

#     def __init__(self, rect, texture_params, scale_x, scale_y):
#         self.texture_rect = rect
#         self.texture_pos_x, self.texture_pos_y = rect.x, rect.y
#         self.x_size, self.y_size = rect.size
#         self.x_size *= scale_factor
#         self.y_size *= scale_factor

#         surf = pygame.surface.Surface(tuple(constants["npc"]))
#         surf.blit(sheet, (rect.x, rect.y), texture_params)
#         self.texture = pygame.transform.scale(surf, (self.x_size, self.y_size))

#         #new boundries
#         self.x_hitbox, self.y_hitbox = self.x_size*scale_x, self.y_size*scale_y
#         self.hb_pos_x = rect.x
#         self.hb_pos_y = self.texture_pos_y+(self.y_size)-(self.y_hitbox)
#         self.texture = pygame.transform.scale(texture, (self.x_size, self.y_size))

#         #debugging
#         self.rect_surf = pygame.Surface((self.x_hitbox, self.y_hitbox))
#         self.rect_surf.fill((250,0,0))

#         print("Object: ", self.x_size, self.y_size, self.texture_pos_y, self.texture_pos_y-(self.x_size/2))

#     def render(self, display_surface : pygame.surface.Surface):
#         display_surface.blit(self.texture, (self.texture_pos_x, self.texture_pos_y))

#         #uncomment to debug
#         #display_surface.blit(self.rect_surf, (self.hb_pos_x,self.hb_pos_y))
#     def animate(self, type):
#         if type == True:
#             pass


