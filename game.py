
import pygame, sys
import random
pygame.init()

size = width, height = 620,320
color = 208,236,253
black = 0,0,0
white = 255,255,255
red = 255,2,2
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

penguin_width = 34
penguin_height = 34
obstacle_width = 57
obstacle_height = 52
snowball_width = 34
snowball_height = 34

pygame.display.set_caption('Penguin')

#background
northpole = pygame.image.load("assets/images/polar.png")

#obstacle
obstacle = pygame.image.load("assets/images/obstacle1.png")
smallobstacle = pygame.transform.scale(obstacle,(obstacle_width,obstacle_height))
obstaclerect= smallobstacle.get_rect()
#SNOW BALL
snowball= pygame.image.load("assets/images/snowball-icon.png")
smallball = pygame.transform.scale(snowball,(snowball_width,snowball_height))
snowballrect = smallball.get_rect()
#snowball.set_colorkey(black)

#penguin 
penguin = pygame.image.load('assets/images/penguin2.png')
smallpenguin= pygame.transform.scale(penguin,(penguin_width,penguin_height))
penguinrect = smallpenguin.get_rect()
smallpenguin.set_colorkey(white)

def background(xpol,ypol):
    screen.blit(northpole,(xpol,ypol))

def ball(x1,y2):
    screen.blit(smallball,(x1,y2))

def game_over():
    font = pygame.font.SysFont(None,80)
    fcolor = pygame.color.Color(5, 5, 5, 100)
    message = font.render("Game over",True,fcolor)
    screen.blit(message,(165,100))

def obstacles(xloc,yloc):
    screen.blit(smallobstacle,(xloc,yloc))
    
def pin(x,y):
    screen.blit(smallpenguin,(x,y))

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
                
                pygame.quit()
                sys.exit()

                #check for keys being pressed by user 
            if event.type == pygame.KEYDOWN:
                #check fo the left arrow key
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5 
                if event.key == pygame.K_UP:
                    y_change = -5
                if event.key == pygame.K_DOWN:
                    y_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0
                
         
        x += x_change
        y += y_change


        
        screen.fill(color)
        background(xpol,ypol)
        pin(x,y)
        ball(x1,y2)
        obstacles(xloc,yloc)
        y += 0
        xloc -= obspeed
        y2 -= ballspeed
        
        #check if penguin crashes on top or at the bottom
        if y > 323 - penguin_height or y<0:
            game_over()
            y_change = 0
            obspeed = 0
            ballspeed = 0
        #check for obstacles
        if y > yloc-obstacle_height:
            if (x > xloc and x<xloc-obstacle_width) or (x + penguin_width > xloc -penguin_width<xloc - obstacle_width):
                game_over()

        
        if y2 < -80:
            y2 = 300
            x1 = random.randint(0,610)
        if xloc <-80:
            xloc = 600
            yloc = random.randint(0,280)
        clock.tick(60)
        pygame.display.flip()

game_loop()
pygame.quit()
quit()







