import pygame as pg
import time

def main():

    pg.init()
    pg.event.clear()
    width, height = 1000, 600
    background_color = (0, 0, 255)
    text_color = (0,0,0)
    correct_color = (0,255,0)
    incorrect_color = (255,0,0)
    screen = pg.display.set_mode((width, height))
    pg.display.set_caption("The project")

    running = True
    started = False
    ended = False

    target = "The quick brown fox jumps over the lazy dog"
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
                running = False
            else:
                if event.type == pg.KEYDOWN:

                    if not started:
                        started = True
                        t0 = time.time()

                    if event.key != pg.K_BACKSPACE:
                        userText.append(event.unicode)
                    else:
                        if len(userText) > 0:
                            userText = userText[:-1]

            font = pg.font.Font(None, 32)
            w = 0

            for i in range (len(userText)):
                char = userText[i]
                if char == target[i]:
                    color = correct_color
                else:
                    color = incorrect_color

                t = font.render(char, True, color)
                screen.blit(t, (w + 20,20))
                w+=t.get_rect().width

            userText_str = ''.join(userText)
            text2 = font.render(target[len(userText_str):], True, text_color)
            
            
            screen.blit(text2, (w + 20 ,20))

        else:
            t1 = time.time()
            wpm = round((n / 5) / (t1-t0) * 60)

            print(f"Ended. {wpm} WPM")
            text = font.render(f"Test ended. Result: {wpm} WPM", True, text_color)
            screen.blit(text, (width // 2 - text.get_width() // 2, height // 2 - text.get_height() // 2 ))
            running = False

        pg.display.flip()


    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                break

if __name__ == "__main__":
    main()