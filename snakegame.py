import random
import pygame
import os
pygame.init()

pygame.mixer.init()
# colours
white = (255,255,255)
red = (255,0,0)
black = (0,0,0)

screen_width = 900
screen_height = 600

image = pygame.image.load("C:\\Users\\Shree\\Downloads\\Background texture for a board game.jpg")
image = pygame.transform.scale(image, (screen_width,screen_height))

image_2 = pygame.image.load("C:\\Users\\Shree\\Downloads\\Free Vector _ Game over with glitch effect.jpg")
image_2 = pygame.transform.scale(image_2, (screen_width,screen_height))
# clock
clock = pygame.time.Clock()

gamewindow = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("My first Game")

font = pygame.font.SysFont(None, 55)



def plot_snake(gamewindow, colour, snk_l, size):
    for x,y in snk_l:
        pygame.draw.rect(gamewindow, colour, [x,y,size,size])


def text_screen(text, colour, x, y):
    screen_text = font.render(text, True, colour )
    gamewindow.blit(screen_text, [x,y])

def welcome():
    exit_game = False
    
    while not exit_game:
        gamewindow.fill((230,220,230))
        text_screen("WELCOME! TO SNAKES GAME", black,50,50)
        text_screen("PRESS SPACE TO ENTER THE GAME", black,50,110)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load("C:\\Users\\Shree\\Downloads\\3-egg-shaker-rolls-32718.mp3")
                    pygame.mixer.music.play()
                    game_loop()
        pygame.display.update()
        clock.tick(60)

def game_loop():
    exit_game = False
    game_over = False
    score = 0
    x = 100
    y = 100
    size = 10
    vel_x = 0
    vel_y = 0
    food_x = random.randint(0,800)
    food_y = random.randint(0,500)
    fps = 60
    snk_l = []
    snk_length = 1
    if not os.path.exists("highscore.txt"):
        with open("highscore.txt", "w") as f:
            f.write("0")
    with open("highscore.txt", "r") as f:
        highscore = f.read()
    

    while not exit_game:
        
        if game_over:
            with open("highscore.txt", "w") as f:
                f.write(str(highscore))
            gamewindow.fill(white)
            gamewindow.blit(image_2, (0,0))
            text_screen("PRESS ENTER TO RESTART THE GAME!!!", (white), 90,450)    
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        pygame.mixer.music.load("C:\\Users\\Shree\\Downloads\\3-egg-shaker-rolls-32718.mp3")
                        pygame.mixer.music.play()
                        game_loop()

        else:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        vel_x += 5
                        vel_y = 0
                    if event.key == pygame.K_LEFT:
                        vel_x += -5
                        vel_y = 0
                    if event.key == pygame.K_UP:
                        vel_y += -5
                        vel_x = 0
                    if event.key == pygame.K_DOWN:
                        vel_y += 5
                        vel_x = 0

            x += vel_x
            y += vel_y
            if abs(x - food_x)<10 and abs(y - food_y)<10:
                score += 1
                food_x = random.randint(0,800)
                food_y = random.randint(0,500)
                snk_length+=5
                if score>int(highscore):
                    highscore = score

            if x>screen_width or x<0 or y>screen_height or y<0:
                    game_over = True  
                    pygame.mixer.music.load("C:\\Users\\Shree\\Downloads\\mixkit-drums-of-war-call-2780.wav")
                    pygame.mixer.music.play()  
            gamewindow.fill(black)
            gamewindow.blit(image, (0, 0))
            text_screen("Score:"+str(score), white, 5, 5)
            text_screen("Highscore:"+str(highscore), white, 150, 5)
            plot_snake(gamewindow, black, snk_l, size)
            pygame.draw.rect(gamewindow, red, [food_x,food_y,size,size])
            head = []
            head.append(x)
            head.append(y)
            snk_l.append(head)
            
            if len(snk_l)>snk_length:
                del snk_l[0]
            if head in snk_l[:-1]:
                pygame.mixer.music.load("C:\\Users\\Shree\\Downloads\\mixkit-drums-of-war-call-2780.wav")
                pygame.mixer.music.play() 
                game_over = True

            plot_snake(gamewindow, black, snk_l, size)

        pygame.display.update()
        clock.tick(fps)
            

    pygame.quit()
    quit()
welcome()
