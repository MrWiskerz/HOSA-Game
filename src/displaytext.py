import pygame


pygame.init()
WINDOW_SIZE = WIDTH, HIEGHT = 800, 600
display_surface = pygame.display.set_mode(WINDOW_SIZE)


def display_text(surface, text, pos, font, color, limit_right):
    collection = [word.split(' ') for word in text.splitlines()]
    space = font.size(' ')[0]
    x, y = pos
    for lines in collection:
        for words in lines:
            word_surface = font.render(words, True, color)
            word_width, word_height = word_surface.get_size()
            if limit_right != "null":
                if x + word_width >= limit_right: #if the next word surpases 0.675*WIDTH, add "word_height" to y coordinate of next word
                    x = pos[0]
                    y += word_height
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]
        y += word_height