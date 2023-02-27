import pygame, sys
from pygame.locals import *
from src.Entities import Player
from src.Room import Room
from src.Object import Object
from src.game_end import end_menu
from src.displaytext import display_text
from src.room3 import play3
from src.Object import Timer
import random



lock = pygame.transform.scale(pygame.image.load("assets/lock.png"), (round(32), round(38)))
unlock = pygame.transform.scale(pygame.image.load("assets/unlock.png"), (round(32), round(38)))
def play2(first_try1, timer):
    door_open = pygame.Rect(742, 528, 46, 69)
    global WINDOW_SIZE
    WINDOW_SIZE = WINDOW_SIZE_X, WINDOW_SIZE_Y = 800, 600

    REFRESH_RATE = 60

    pygame.init()
    clock = pygame.time.Clock()
    display_surface = pygame.display.set_mode(WINDOW_SIZE)

    classroom = Room(WINDOW_SIZE_X, WINDOW_SIZE_Y, "assets/class2.png", display_surface)
    title_screen = Room(WINDOW_SIZE_X, WINDOW_SIZE_Y, "assets/title_screen.png", display_surface)
    font_answer = pygame.font.Font(None, round(0.026667*WINDOW_SIZE_Y))
    font_next = pygame.font.Font('assets/Minecraftia.ttf', round(0.036667*WINDOW_SIZE_Y))

    #Colors
    yellow = (255, 255, 0)
    cyan = (0, 255, 255)
    magenta = (255, 0, 255)
    red = (255, 0, 0)
    pastelred =(182, 105, 106)
    pastelwhite =(225, 226, 229)
    pastelyellow =(231, 206, 140)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    black = (0, 0, 0)
    gray = (200,200,200)
    white = (255, 255, 255)
    purple = (36, 4, 20)
    lightpurple = ((112, 58, 85))

    start_font = pygame.font.Font('assets/Minecraftia.ttf', 50)
    smallfont = pygame.font.Font('assets/Minecraftia.ttf', 35)

    # "sprite_type": ( size_dimensions ), "desk_size": [ ( size_dimesnsions ), texture, scale_x, scale_y ]
    constants = {
        "teacher": [15,27],
        "player": [18,26],
        "desk_small": [pygame.image.load("assets/desk_small.png").get_rect().size, pygame.image.load("assets/desk_small.png"), 1,.5, "desk_small"],
        "desk_big": [pygame.image.load("assets/desk2.png").get_rect().size, pygame.image.load("assets/desk2.png"), 1,.6, "desk_big"],
        "wall": [None, pygame.image.load("assets/trans_pixel.png"),1,1, "wall"], #No defined size
        "instructions": [pygame.image.load("assets/instructions.png").get_rect().size, pygame.image.load("assets/instructions.png"), 1,1, "instructions"],
        "npc": [(17,25), None, .01,.01, "npc"]
        }
    #(self, pos_x, pos_y, size_x, size_y, move_speed, sprite, display_surface:pygame.surface.Surface)

    #(rect_instance(surface, color, position + size), texture, scale_x, scale_y)
    Obj0 = [
        Object(rect=pygame.draw.rect(display_surface, (255,0,0), (106, 332) + constants["instructions"][0]),
            texture=constants["instructions"][1],
            scale_x=constants["instructions"][2],
            scale_y=constants["instructions"][3],
            name=constants["instructions"][4],
            number="null",
            status="null")
        # Object(rect=pygame.draw.rect(display_surface, (255,0,0), (0,0) + pygame.image.load("assets/title_button.png").get_rect().size),
        #     texture=pygame.image.load("assets/title_button.png"),
        #     scale_x=constants["instructions"][2],
        #     scale_y=constants["instructions"][3],
        #     name=constants["instructions"][4])
    ]

    Obj1 = [

        Object(rect=pygame.draw.rect(display_surface, (255,0,0), (122, 268) + constants["desk_small"][0]),
            texture=constants["desk_small"][1],
            scale_x=constants["desk_small"][2],
            scale_y=constants["desk_small"][3],
            name=constants["desk_small"][4],
            number="1",
            status="incomplete")

        ,

        Object(rect=pygame.draw.rect(display_surface, (255,0,0), (316, 268) + constants["desk_small"][0]),
            texture=constants["desk_small"][1],
            scale_x=constants["desk_small"][2],
            scale_y=constants["desk_small"][3],
            name=constants["desk_small"][4],
            number="2",
            status="incomplete")
        ,

        Object(rect=pygame.draw.rect(display_surface, (255,0,0), (510, 268) + constants["desk_small"][0]),
            texture=constants["desk_small"][1],
            scale_x=constants["desk_small"][2],
            scale_y=constants["desk_small"][3],
            name=constants["desk_small"][4],
            number="3",
            status="incomplete")
        ,
        Object(rect=pygame.draw.rect(display_surface, (255,0,0), (122, 390) + constants["desk_small"][0]),
            texture=constants["desk_small"][1],
            scale_x=constants["desk_small"][2],
            scale_y=constants["desk_small"][3],
            name=constants["desk_small"][4],
            number="4",
            status="incomplete")

        ,
        Object(rect=pygame.draw.rect(display_surface, (255,0,0), (316, 390) + constants["desk_small"][0]),
            texture=constants["desk_small"][1],
            scale_x=constants["desk_small"][2],
            scale_y=constants["desk_small"][3],
            name=constants["desk_small"][4],
            number="5",
            status="incomplete")

        ,
        Object(rect=pygame.draw.rect(display_surface, (255,0,0), (510, 390) + constants["desk_small"][0]),
            texture=constants["desk_small"][1],
            scale_x=constants["desk_small"][2],
            scale_y=constants["desk_small"][3],
            name=constants["desk_small"][4],
            number="6",
            status="incomplete")

        ,



        Object(rect=pygame.draw.rect(display_surface, (255,0,0), (196,142) + constants["desk_big"][0]),
            texture=constants["desk_big"][1],
            scale_x=constants["desk_big"][2],
            scale_y=constants["desk_big"][3],
            name=constants["desk_big"][4],
            number="null",
            status="null")

        ,#walls
        Object(rect=pygame.draw.rect(display_surface, (255,0,0), (-4,-4,8,WINDOW_SIZE_Y)),
            texture=constants["wall"][1],
            scale_x=constants["wall"][2],
            scale_y=constants["wall"][3],
            name=constants["wall"][4],
            number="null",
            status="null"),
        Object(rect=pygame.draw.rect(display_surface, (255,0,0), (0,60,WINDOW_SIZE_X,8)),
            texture=constants["wall"][1],
            scale_x=constants["wall"][2],
            scale_y=constants["wall"][3],
            name=constants["wall"][4],
            number="null",
            status="null"),
        Object(rect=pygame.draw.rect(display_surface, (255,0,0), (-4,WINDOW_SIZE_Y-4,WINDOW_SIZE_X,8)),
            texture=constants["wall"][1],
            scale_x=constants["wall"][2],
            scale_y=constants["wall"][3],
            name=constants["wall"][4],
            number="null",
            status="null"),
        Object(rect=pygame.draw.rect(display_surface, (255,0,0), (WINDOW_SIZE_X-4,-4,8,WINDOW_SIZE_Y)),
            texture=constants["wall"][1],
            scale_x=constants["wall"][2],
            scale_y=constants["wall"][3],
            name=constants["wall"][4],
            number="null",
            status="null"),
        Object(rect=pygame.draw.rect(display_surface, (255,0,0), (0,0,65,70)),
            texture=constants["wall"][1],
            scale_x=constants["wall"][2],
            scale_y=constants["wall"][3],
            name=constants["wall"][4],
            number="null",
            status="null"),
        Object(rect=pygame.draw.rect(display_surface, (255,0,0), (0,WINDOW_SIZE_Y-80) + pygame.image.load("assets/class_bottom.png").get_rect().size),
            texture=pygame.image.load("assets/class_bottom.png"),
            scale_x=1,
            scale_y=.5,
            name="bottom",
            number="null",
            status="null"),
        # Object(rect=pygame.draw.rect(display_surface, (255,0,0), (620,26,40,40)),
        #     texture=pygame.image.load("assets/logo.png"),
        #     scale_x=0,
        #     scale_y=0,
        #     name="logo"),
        Object(rect=pygame.draw.rect(display_surface, (255,0,0), (425,540,140,30)),
            texture=pygame.image.load("assets/Hosa_Logo.png"),
            scale_x=.1,
            scale_y=0,
            name="hosa_logo",
            number="null",
            status="null"),
        Object(rect=pygame.draw.rect(display_surface, (255,0,0), (200,20,140,30)),
            texture=pygame.image.load("assets/board_image.png"),
            scale_x=.1,
            scale_y=0,
            name="board_image",
            number="null",
            status="null"),
        Object(rect=pygame.draw.rect(display_surface, (255,0,0), (310,85,30,60)),
            texture=pygame.image.load("assets/teacher_2.png"),
            scale_x=0,
            scale_y=0,
            name="teacher",
            number="null",
            status="null")

    ]


    for object in Obj1:
        if object.name == "desk_small":
            Obj1.append(Object(rect=pygame.draw.rect(display_surface, (255,0,0), (object.texture_pos_x+random.randint(0,3),object.texture_pos_y-random.randint(12,16))+(26,38)),
                texture=pygame.image.load("assets/npc"+str(random.randint(0,3))+".png"),
                scale_x=constants["npc"][2],
                scale_y=constants["npc"][3],
                name=constants["npc"][4],
                number="null",
                status="null"))

    sheet = pygame.image.load("assets/spritesheet1.png")
    boy_params = (0,236) + tuple(constants["player"])

    girl_params = (76,236) + tuple(constants["player"])
    teacher_params = (0,207) + tuple(constants["teacher"])
    # print(boy_params, girl_params, teacher_params)

    player_surface = pygame.surface.Surface((50,60))
    player_surface.blit(sheet, (76,236), (20,20,20,20))

    player = Player(pos_x=720, pos_y=90, size_x=50, size_y=70, move_speed=5, sprite="assets/player-0.png", sprite_2="assets/player-1.png", display_surface=display_surface, Objects=Obj1)
    Title = "Classroom Hero by UNHP Comp Sci Club"
    Icon = pygame.image.load("assets/logo.png")

    index = [0,0]
    display_surface.blit(sheet, (200,200), ((constants["player"][0]*index[0]), (constants["player"][1]*index[1])) + tuple(constants["player"]))


    def start_button(x, y, width, height, hovercolor, defaultcolor):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed(3)
        startbuttontext = smallfont.render("Start The Game!", True, black)

        if x + width > mouse[0] > x and y + height > mouse[1] > y:
            pygame.draw.rect(display_surface, black, (x-11, y+15, width, height+2), 68, 20)
            pygame.draw.rect(display_surface, hovercolor, (x-3, y+3, width, height), 68, 20)
            display_surface.blit(startbuttontext, (111, 193))
            if click[0] == 1:
                # print("mansa musa")
                return True
        else:
            pygame.draw.rect(display_surface, black, (x-11, y+15, width, height+2), 68, 20)
            pygame.draw.rect(display_surface, defaultcolor, (x, y, width, height), 68, 20)
            display_surface.blit(startbuttontext, (114, 190))

    def update():
        start_value = 1
        right = 0
        door_box = pygame.Rect(742, 528, 46, 69)
        first_try2 = first_try1
        while True:


            if start_value == 0:
                #Title Window

                title_screen.render(display_surface)
                for object in Obj0:
                    object.render(display_surface)


                play_game = start_button(60, 150, 420, 136, gray, white)

                if play_game:
                    start_value = 1

            elif start_value == 1:
                #Game Window

                #Time
                timer.change_position((50,545))
                timer.current_tick += 1/(REFRESH_RATE/1.75)

                if timer.current_tick >= 1:
                    timer.current_tick = 0
                    timer.tick(1)

                pygame.display.set_caption(Title)
                pygame.display.set_icon(Icon)
                classroom.render(display_surface)

                outcome_final = player.update(display_surface, timer)
                if outcome_final != None:
                    if outcome_final[0] == "correct":
                        right += 1
                        if int(outcome_final[1]) == 1:
                            first_try2 += 1
                        # print(right)
                player.render(display_surface)
                if right == 6:
                    display_surface.blit(unlock, (748, 545))
                    if door_box.colliderect(player.player_pos_x, player.player_pos_y, player.player_size_x,
                                            player.player_size_y):
                        if pygame.key.get_pressed()[K_e]:
                            if play3(first_try2, timer) == "restart":
                                return "restart"
                else:
                    display_surface.blit(lock, (748, 545))
                player.render(display_surface)
                for object in Obj1:
                    if object.overlap == 0:
                        object.render(display_surface)
                        # if object.NPC:
                        #     object.NPC.render(display_surface)

                for object in Obj1:
                    if object.overlap != 0:
                        object.render(display_surface)
                        # if object.NPC:
                        #     object.NPC.render(display_surface)

                timer.render(display_surface)

                if right == 6:
                    display_surface.blit(unlock, (748, 545))
                    if door_box.colliderect(player.player_pos_x, player.player_pos_y, player.player_size_x,
                                            player.player_size_y):
                        display_text(display_surface, "Press E to enter", (429, 478), font_next, (25, 25, 25), "null")
                else:
                    display_surface.blit(lock, (748, 545))
                # display_surface.blit(sheet, (200,200), boy_params)
                # display_surface.blit(sheet, (200,150), girl_params)
            #main code
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()

            pygame.display.update()

    if update() == "restart":
        return "restart"