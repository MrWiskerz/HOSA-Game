import pygame
import sys
import random
from src.Buttons import Button

# from src.Buttons import mcq_Button
# from main import constants

screen_WIDTH = 800
screen_HIEGHT = 600

prompt_button = Button('assets/question.png', round(screen_WIDTH / 8), round(screen_HIEGHT / 6),
                       round(0.0016667 * screen_HIEGHT))


class Player(pygame.sprite.Sprite):
    player_pos_x = 0
    player_pos_y = 0

    player_size_x = 0
    player_size_y = 0
    player_move_speed = 0

    player_sprite = None

    hitbox_displacement_y = 2
    flipped = False

    # image_char = "assets/player-0.png"

    def __init__(self, pos_x, pos_y, size_x, size_y, move_speed, sprite, sprite_2, display_surface: pygame.surface.Surface,
                 Objects):

        self.Objects = Objects

        self.player_pos_x = pos_x
        self.player_pos_y = pos_y
        self.player_size_x = size_x
        self.player_size_y = size_y
        self.hitbox = pygame.draw.rect(display_surface, (0, 255, 0), (pos_x, pos_y, size_x, size_y))
        self.trigger = pygame.draw.rect(display_surface, (0, 255, 0), (pos_x - 2, pos_y - 2, size_x + 4, size_y + 4))
        self.texture = pygame.transform.scale(pygame.image.load(sprite), (size_x, size_y))

        self.move_speed = move_speed

        # self.hitbox = Collider(self.player_pos_x, self.player_pos_y, size_x, size_y)
        print('Player initialised')

    def set_position(self, pos_x, pos_y):
        self.player_pos_x = pos_x
        self.player_pos_y = pos_y

    # def update_input(self, display_surface : pygame.surface.Surface):
    #     keys = pygame.key.get_pressed()
    #     test_x = (-keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]) * self.move_speed
    #     test_y = (-keys[pygame.K_UP] or keys[pygame.K_DOWN]) * self.move_speed
    #     for object in self.Objects:
    #         rect = pygame.Rect(object.hb_pos_x, object.hb_pos_y, object.x_hitbox, object.y_hitbox)
    #         if rect.colliderect((self.player_pos_x+test_x, (self.player_pos_y+test_y), self.player_size_x, self.player_size_y)):
    #             print("no!")
    #             return

    #     print("yes")
    #     self.player_pos_x += test_x
    #     self.player_pos_y += test_y

    def update_input(self, display_surface: pygame.surface.Surface, timer):
        keys = pygame.key.get_pressed()
        test_x = (-keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]) * self.move_speed
        test_y = (-keys[pygame.K_UP] or keys[pygame.K_DOWN]) * self.move_speed

        if test_x < 0 and not self.flipped:
            self.texture = pygame.transform.flip(self.texture, True, False)
            self.flipped = True
        elif test_x > 0 and self.flipped:
            self.texture = pygame.transform.flip(self.texture, True, False)
            self.flipped = False
        for object in self.Objects:
            rect = pygame.Rect(object.hb_pos_x - 5, object.hb_pos_y - 5, object.x_hitbox + 10, object.y_hitbox + 10)
            if object.name == "desk_small" and object.status == "incomplete":
                if rect.colliderect((self.player_pos_x + test_x,
                                     (self.player_pos_y + test_y) + self.hitbox_displacement_y, self.player_size_x,
                                     self.player_size_y)):
                    for objec in self.Objects:
                        rec = pygame.Rect(objec.hb_pos_x - 5, objec.hb_pos_y - 5, objec.x_hitbox + 10,
                                          objec.y_hitbox + 10)
                        if rec.colliderect(rect):
                            desk_npc = objec
                    result = prompt_button.draw(desk_npc.texture_original, timer)
                    if result != None:
                        if result[0] == "correct":
                            object.status = "complete"
                            return (["correct", result[1]])
                        elif result == "wrong":
                            return "wrong"
        for object in self.Objects:
            rect = pygame.Rect(object.hb_pos_x, object.hb_pos_y, object.x_hitbox, object.y_hitbox)
            if rect.colliderect((self.player_pos_x + test_x, (self.player_pos_y + test_y) + self.hitbox_displacement_y,
                                 self.player_size_x, self.player_size_y)):
                return

        # print("yes")
        self.player_pos_x += test_x
        self.player_pos_y += test_y

    def update(self, display_surface: pygame.surface.Surface, timer):
        # self.hitbox.set_position(self.player_pos_x, self.player_pos_y)
        # self.hitbox.update_collision(display_surface)

        outcome = self.update_input(display_surface, timer)
        if outcome != None:
            if outcome[0] == "correct":
                return (["correct", outcome[1]])
            if outcome == "wrong":
                return "wrong"

    def render(self, display_surface: pygame.surface.Surface):
        # self.hitbox.render(display_surface)
        display_surface.blit(self.texture, (self.player_pos_x, self.player_pos_y))

    def collide_check(self, obj_rect):
        pass

    def interact(self, type):
        pass