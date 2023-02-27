import pygame
import sys
from src.displaytext import display_text
from src.Buttons import Button

pygame.init()
WINDOW_SIZE = WIDTH, HIEGHT = 800, 600
display_surface = pygame.display.set_mode(WINDOW_SIZE)
stall = True
board = pygame.transform.scale(pygame.image.load("assets/board.png"), (round(0.3875*WIDTH), round(0.35*HIEGHT)))
clock = pygame.time.Clock()
FPS = 60
font_end = pygame.font.Font(None, round(30))
board = pygame.transform.scale(pygame.image.load("assets/board.png"), (round(0.3875*WIDTH), round(0.35*HIEGHT)))
classroom = pygame.transform.scale(pygame.image.load("assets/classroom.png"), (WIDTH, HIEGHT))
play_again = Button('assets/play_again_button.png', round(390), round(290), (0.0012 * HIEGHT))
pixel_font = pygame.font.Font('assets/Minecraftia.ttf', 20)

def end_menu(total_first_try, timer):
    total_ft = total_first_try
    while stall:
        for i in pygame.event.get():
            clock.tick(FPS)
            if i.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # pos = pygame.mouse.get_pos()
            # print(pos)
        display_surface.blit(classroom, (0, 0))
        display_surface.blit(board, (round(0.3 * WIDTH), round(0.325 * HIEGHT))) #blits board
        score = int(((10000 / (int(timer.time) + 100)) + (int(total_ft) * 3)))
        display_text(display_surface, "GREAT JOB!!! ", (round(0.4 * WIDTH), round(0.3575 * HIEGHT)), pixel_font,
                     (255, 255, 255), "null")
        display_text(display_surface, "Score: " + str(score), (round(0.412 * WIDTH), round(0.4 * HIEGHT)),
                     pixel_font,
                     (255, 255, 255), "null")
        timer.change_position((round(0.4 * WIDTH)-60, round(0.3575 * HIEGHT)+125))
        timer.render(display_surface)
        if play_again.drawtwo() == "restart":
            return "restart"
        pygame.display.flip()
        clock.tick(60)
