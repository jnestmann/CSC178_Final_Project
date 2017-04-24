import GameObjects
import pygame
import sys
import random

pygame.init()
clock = pygame.time.Clock()


# delete as soon as possible
obstacle_height = 52
obstacle_width = 57


bg_filenames = ('assets/images/bg_title.jpg',
                'assets/images/bg_game.jpg',
                'assets/images/bg_credits.jpg'
                )


# setup game display
bg_northpole = pygame.image.load(bg_filenames[1])
size = width, height = 620,320
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Penguin')
pygame.display.set_icon(pygame.image.load('assets/images/penguin_icon.png').convert_alpha())

# Set Color Constants
PALE_BLUE = 208, 236, 253
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 2, 2)


penguin_img = pygame.image.load('assets/images/small_penguin.png')
penguin = GameObjects.Penguin(width=34,height=34,img=penguin_img)

obstacle_img = pygame.image.load('assets/images/obstacle1.png')
obstacle = GameObjects.Obstacle(width=57, height=52, img=obstacle_img)

snowball_img = pygame.image.load('assets/images/small_snowball.png').convert_alpha()
snowball = GameObjects.Snowball(width=34, height=34, img=snowball_img)



#obstacle
#obstaclerect= smallobstacle.get_rect()

#snowball= pygame.image.load("assets/images/snowball-icon.png")
#smallball = pygame.transform.scale(snowball,(snowball_width,snowball_height))
#snowballrect = smallball.get_rect()
#snowball.set_colorkey(BLACK)

def pquit():
    pygame.quit()
    exit()

def background(xpol,ypol):
    screen.blit(bg_northpole,(xpol,ypol))

def ball(x1,y2):
    screen.blit(snowball_img,(x1,y2))

def game_over():
    font = pygame.font.SysFont(None,80)
    fcolor = pygame.color.Color(5, 5, 5, 100)
    message = font.render("Game over",True,fcolor)
    screen.blit(message,(165,100))

def obstacles(xloc,yloc):
    screen.blit(obstacle.img,(xloc,yloc))
    
def pin(x,y):
    screen.blit(penguin.img,(penguin.x, penguin.y))

def game_loop():
    
    #penguin position
    x = (640*0.45)
    y = (340*0.8)
    
    #update penguin posiotion with keyboard 
    x_change = 0
    y_change = 0
    
    #ballposition 
    x1 = random.randint(0,640) 
    y2 = random.randint(0,320)
    
    #background position 
    xpol = 0
    ypol= 0

    #obstacle position
    xloc = 0
    yloc= random.randint(0,300)
    obspeed = 5.2
    ballspeed = 10
    
    finish = False
    
    while not finish:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pquit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pquit()
                elif event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
                elif event.key == pygame.K_UP:
                    y_change = -5
                elif event.key == pygame.K_DOWN:
                    y_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0
                
         
        penguin.x += x_change
        penguin.y += y_change


        
        screen.fill(PALE_BLUE)
        background(xpol,ypol)
        pin(x,y)
        ball(x1,y2)
        obstacles(xloc,yloc)
        y += 0
        xloc -= obspeed
        y2 -= ballspeed
        
        #check if penguin crashes on top or at the bottom
        if penguin.y > 323 - penguin.height or penguin.y < 0:
            game_over()
            y_change = 0
            obspeed = 0
            ballspeed = 0
        #check for obstacles
        if y > yloc-obstacle_height:
            if (x > xloc and x<xloc-obstacle_width) or (x + penguin.width > xloc - penguin.width < xloc - obstacle_width):
                game_over()

        
        if y2 < -80:
            y2 = 300
            x1 = random.randint(0,610)
        if xloc <-80:
            xloc = 600
            yloc = random.randint(0,280)
        clock.tick(60)
        pygame.display.flip()

    pquit()

game_loop()







