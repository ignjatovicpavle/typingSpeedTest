import pygame as pg
import time
from random import randint

pg.init()
pg.event.clear()
width, height = 1000, 600
text_x, text_y = 20, 250
background_color = (250, 242, 220)
text_color = (138, 130, 109)
correct_color = (0,255,0)
incorrect_color = (255,0,0)
screen = pg.display.set_mode((width, height))
pg.display.set_caption("The project")
font = pg.font.Font(None, 32)

special_characters = {'.', ',', ';', ':', '$', '#', '%', '&', '!', '@', '^', '*', '(', ')' }

def setTarget(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
        for s in lines:
            r = randint(0, 1)
            if r == 1:
                return s.strip()
        return lines[0].strip()


def main(screen):

    t0 = 0
    t1 = 0

    running = True
    started = False
    ended = False
    exit = False

    target = setTarget("targets.txt")
    n = len(target)

    target_l = [char for char in target]
    userText = []

    outputText_l = target_l
    outputText = ""

    while running:
        if len(userText) >= n:
            ended = True

        if not ended:

            screen.fill(background_color)

            event = pg.event.wait()
            if event.type == pg.QUIT:
                return
            elif event.type == pg.KEYDOWN: 
                if event.key == pg.K_TAB:
                    main(screen)
                    return
                else:
                    if not started:
                        started = True
                        t0 = time.time()

                    if event.key == pg.K_BACKSPACE:
                        if len(userText) > 0:
                            userText = userText[:-1]
                    elif (
                    event.unicode.isalpha() 
                    or event.unicode.isdigit() 
                    or event.key == pg.K_LSHIFT 
                    or event.key == pg.K_RSHIFT 
                    or event.key == pg.K_SPACE
                    or event.unicode in special_characters
                    ):
                        userText.append(event.unicode)

            
            w = text_x

            for i in range (len(userText)):
                char = userText[i]
                if char == target[i]:
                    color = correct_color
                else:
                    color = incorrect_color

                t = font.render(char, True, color)
                screen.blit(t, (w, text_y))
                w+=t.get_rect().width

            userText_str = ''.join(userText)
            text2 = font.render(target[len(userText_str):], True, text_color)
            
            
            screen.blit(text2, (w, text_y))

        else:
            t1 = time.time()
            wpm = round((n / 5) / (t1-t0) * 60)

            print(f"Ended. {wpm} WPM")
            text = font.render(f"Test ended. Result: {wpm} WPM", True, text_color)
            screen.blit(text, (text_x, text_y + 50))
            running = False

        pg.display.flip()


    while not exit:
        event = pg.event.wait()
        if event.type == pg.QUIT:
            exit = True
            break
        else:
            if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                main(screen)
                return
    return

if __name__ == "__main__":
    screen.blit(font.render("Press SPACE to start the test...", True, text_color), (text_x, text_y + 50))
    screen.blit(font.render("Good luck!", True, text_color), (text_x, text_y + 80))
    pg.display.flip()
    while True:
        event = pg.event.wait()
        if event.type == pg.QUIT:
            break
        else:
            if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                main(screen)
                break
    pg.quit()