import pygame
import sys
import random
from src.mcq_button import mcq_Button
from src.displaytext import display_text
from src.Room import Room

pygame.init()
WINDOW_SIZE = WIDTH, HIEGHT = 800, 600
display_surface = pygame.display.set_mode(WINDOW_SIZE)
clock = pygame.time.Clock()
FPS = 60

classroom = Room(WIDTH, HIEGHT, "assets/classroom.png", display_surface)

font_answer = pygame.font.Font('assets/Minecraftia.ttf', round(HIEGHT * 0.021667))
font_question = pygame.font.Font('assets/Minecraftia.ttf', round(HIEGHT * 0.028))
wrong_img = pygame.transform.scale(pygame.image.load("assets/wrong.png"),
                                   (round(0.04 * WIDTH), round(0.055 * HIEGHT)))
check_img = pygame.transform.scale(pygame.image.load("assets/check.png"),
                                   (round(0.04 * WIDTH), round(0.055 * HIEGHT)))
A_button = mcq_Button('assets/A_answerChoice.png', round(WIDTH * 0.26125), round(HIEGHT * 0.351667))
B_button = mcq_Button('assets/B_answerChoice.png', round(WIDTH * 0.26125), round(HIEGHT * 0.418333))
C_button = mcq_Button('assets/C_answerChoice.png', round(WIDTH * 0.26125), round(HIEGHT * 0.485))
D_button = mcq_Button('assets/D_answerChoice.png', round(WIDTH * 0.26125), round(HIEGHT * 0.551667))


class Button:
    def __init__(self, image, x, y, scale):
        img = pygame.image.load(image)
        width = img.get_width()
        height = img.get_height()
        self.image = pygame.transform.scale(img, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def draw(self, npc, timer):
        display_surface.blit(self.image, (self.rect.x, self.rect.y))
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            for i in pygame.event.get():
                if i.type == pygame.MOUSEBUTTONUP:
                    return prompt(npc, timer)

    def drawtwo(self):
        display_surface.blit(self.image, (self.rect.x, self.rect.y))
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            for i in pygame.event.get():
                if i.type == pygame.MOUSEBUTTONUP:  # checks for left click
                    return "restart"


picker = -1
questions = open("assets/questions.csv", "r")
subject_list = questions.readlines()
random.shuffle(subject_list)
questions.close()
boardd = pygame.transform.scale(pygame.image.load("assets/board.png"), (WIDTH, HIEGHT))
chalk_outline = pygame.transform.scale(pygame.image.load("assets/chalk_outline.png"), (round(WIDTH * 0.6475), round(HIEGHT * 0.515)))

def prompt(npc, timer):
    global picker
    if picker < 24:
        picker = picker + 1
    else:
        picker = -1
    n_p_c = pygame.transform.scale(npc, (round(WIDTH * 0.39667), round(HIEGHT * 0.58333)))
    q_a_list = subject_list[picker].split(",")
    q_a = q_a_list[0].split(";")
    question = str(q_a[0])
    ans_choices = q_a[1].split(":")
    ans = ans_choices[0]
    random.shuffle(ans_choices)  # shuffles list of answers choices
    ans_x = round(WIDTH * 0.285)  # position of where intial answer choice will print
    ans_y = round(HIEGHT * 0.335)
    a = str(ans_choices[0]) == str(ans)  # gives true or false depending on if its correct
    b = str(ans_choices[1]) == str(ans)
    c = str(ans_choices[2]) == str(ans)
    d = str(ans_choices[3]) == str(ans)
    a_x = False
    b_x = False
    c_x = False
    d_x = False

    tries = 0
    run = True  # variable to see when to close question pop up
    correct = False
    first_try = 0
    timer.change_position((450, 545))
    while run:
        # pos = pygame.mouse.get_pos()
        # print(pos)
        # Timer
        timer.current_tick += 1 / (FPS / 1.75)
        if timer.current_tick >= 1:
            timer.current_tick = 0
            timer.tick(1)

        classroom.render(display_surface)
        timer.render(display_surface)

        for i in pygame.event.get():
            clock.tick(FPS)
            if i.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            pos = pygame.mouse.get_pos()
            if A_button.rect.collidepoint(pos) and i.type == pygame.MOUSEBUTTONUP and not a_x:  # checks for left click on a
                if a:  # a will be true or false according to line 130
                    correct = True
                    run = False  # ends code if right
                    if tries == 0:
                        first_try += 1
                else:
                    tries += 1
                    # print('ran')
                    a_x = True  # makes a_x true if it is a chosen wrong answer (relates to line 205)
                    # print(tries)
                    if tries >= 4:  # ends code if surpass 3 tries
                        correct = False
                        run = False
            if B_button.rect.collidepoint(pos) and i.type == pygame.MOUSEBUTTONUP and not b_x:  # checks for left click RELEASE on b
                if b:
                    correct = True
                    run = False
                    if tries == 0:
                        first_try += 1
                else:
                    tries += 1
                    # print('ran')
                    b_x = True
                    # print(tries)
                    if tries >= 4:
                        correct = False
                        run = False
            if C_button.rect.collidepoint(pos) and i.type == pygame.MOUSEBUTTONUP and not c_x:  # checks for left click on c
                if c:
                    correct = True
                    run = False
                    if tries == 0:
                        first_try += 1
                else:
                    tries += 1
                    # print('ran')
                    c_x = True
                    # print(tries)
                    if tries >= 4:
                        correct = False
                        run = False
            if D_button.rect.collidepoint(pos) and i.type == pygame.MOUSEBUTTONUP and not d_x:  # checks for left click on d
                if d:
                    correct = True
                    run = False
                    if tries == 0:
                        first_try += 1
                else:
                    tries += 1
                    # print('ran')
                    d_x = True
                    # print(tries)
                    if tries >= 4:
                        correct = False
                        run = False
        display_surface.blit(boardd, (0,0))  # blits board
        display_surface.blit(chalk_outline, (round(WIDTH * 0.19625), round(HIEGHT * 0.14666)))
        display_surface.blit(n_p_c, (round(WIDTH * 0.0125), round(HIEGHT * 0.58333)))
        for i in range(len(ans_choices)):
            display_text(display_surface, str(ans_choices[i]), (ans_x, ans_y), font_answer, (255, 255, 255), round(WIDTH * 0.78125))
            ans_y += round(HIEGHT * 0.066667)  # for loop blits next answer choices below the first
        ans_y = round(ans_y - (HIEGHT * 0.26667))
        A_button.draw1()  # draws the answer bubbles
        B_button.draw1()
        C_button.draw1()
        D_button.draw1()

        if a_x:
            display_surface.blit(wrong_img, (
            round(WIDTH * 0.24375), round(HIEGHT * 0.33)))  # if player chooses wrong anser, put x image over it
        if b_x:
            display_surface.blit(wrong_img, (round(WIDTH * 0.24375), round(HIEGHT * 0.39667)))
        if c_x:
            display_surface.blit(wrong_img, (round(WIDTH * 0.24375), round(HIEGHT * 0.46333)))
        if d_x:
            display_surface.blit(wrong_img, (round(WIDTH * 0.24375), round(HIEGHT * 0.53)))

        display_text(display_surface, question, (round(WIDTH * 0.25), round(HIEGHT * 0.21)), font_question,
                     (255, 255, 255), round(WIDTH * 0.78125))

        pygame.display.flip()
        clock.tick(60)

    if correct:
        # print(first_try)
        x, y = pygame.mouse.get_pos()
        display_surface.blit(check_img, (x - 15, y - 15))
        return (["correct", first_try])  # returns to draw function line 32
    else:
        return ("wrong")