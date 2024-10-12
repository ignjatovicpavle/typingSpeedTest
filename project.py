import pygame as pg

def main():

    pg.init()
    width, height = 1000, 600
    background_color = (0, 0, 255)
    text_color = (0,0,0)
    correct_color = (0,255,0)
    incorrect_color = (255,0,0)
    screen = pg.display.set_mode((width, height))
    pg.display.set_caption("The project")

    running = True

    target = "The quick brown fox jumps over the lazy dog"

    target_l = [char for char in target]
    userText = []

    outputText_l = target_l
    outputText = ""

    while running:
        screen.fill(background_color)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
            else:
                if event.type == pg.KEYDOWN:
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

        pg.display.update()

if __name__ == "__main__":
    main()