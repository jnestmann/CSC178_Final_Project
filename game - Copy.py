import time
import pygame, sys
import random
pygame.init()

size = width, height = 590,612
color = 208,236,253
black = 0,0,0
white = 255,255,255
red = 255,2,2
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

penguin_width = 34
penguin_height = 34
obstacle_width = 77
obstacle_height = 72
snowball_width = 54
snowball_height = 54

pygame.display.set_caption('Penguin')

#background
#northpole = pygame.image.load("polar.png")
pinetree1 = pygame.image.load("hut in the mountains.png").convert()
#pinetree = pygame.image.load("pinetrees.png").convert()
pinetree = pygame.transform.scale(pinetree1,(width,height)).convert()


#obstacle
obstacle = pygame.image.load("Marshmallow.png")
smallobstacle = pygame.transform.scale(obstacle,(obstacle_width,obstacle_height))
obstaclerect= smallobstacle.get_rect()
#SNOW BALL
snowball= pygame.image.load("snowball-icon.png")
smallball = pygame.transform.scale(snowball,(snowball_width,snowball_height))
snowballrect = smallball.get_rect()
#snowball.set_colorkey(black)

#penguin 
penguin = pygame.image.load('penguin2.png')
smallpenguin= pygame.transform.scale(penguin,(penguin_width,penguin_height))
penguinrect = smallpenguin.get_rect().width
smallpenguin.set_colorkey(white)


def score(count):
    font = pygame.font.SysFont(None,35)
    text = font.render('Score: ' + str(count), True, black)
    screen.blit(text,(1,1))
    
def background(xpol,ypol):
    screen.blit(pinetree,(xpol,ypol))

def ball(x1,y2):
    screen.blit(smallball,(x1,y2))

def game_over():
    font = pygame.font.SysFont(None,80)
    message = font.render("Game over",True,red)
    screen.blit(message,(165,100))
    

def obstacles(xloc,yloc):
    screen.blit(smallobstacle,(xloc,yloc))
    
def pin(x,y):
    screen.blit(smallpenguin,(x,y))

def game_loop():
    
    #penguin position
    x = (width*0.45)
    y = (height*0.80)
    
    #update penguin posiotion with keyboard 
    x_change = 0
    y_change = 0
    
    #ballposition 
    x1 = random.randint(0,width) 
    y2 = height*0.83
    
    #background position
    xpol = 0
    ypol= 0
    
    #obstacle position
    xloc = width + 10
    yloc= height*0.75
    obspeed = 3
    ballspeed = 7

    count = 0
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
                    y_change = 4 

        #position bacground
        real_x = xpol % pinetree.get_rect().width
        x += x_change
        y += y_change

        # move the background
        screen.fill(color)
        background(real_x - pinetree.get_rect().width,ypol)
        if real_x<width:
            background(real_x,0)
        xpol -=1
            
        # diplay the penguin, ball and obstacles positions
        pin(x,y)
        ball(x1,y2)
        obstacles(xloc,yloc)
        y += 0
        xloc -= obspeed
        x1 -= ballspeed
        
        # display score
        score(count)
        
        #check if penguin crashes on top or at the bottom
        if y> height - penguin_height or y<0:
            game_over()
            y_change = 0
            obspeed = 0
            ballspeed = 0
            xpol += 0
            

        #check for obstacles and then stop everything
        if x + penguin_width >xloc and x-obstacle_height<xloc and y+penguin_height > yloc and y-obstacle_width < yloc:
            game_over()
            y_change = 0
            obspeed = 0
            ballspeed = 0
            xpol = 0
            
        #check if the penguin hits the ground then x_change=0
        if y >= (height*0.80):
            y_change = 0
        # make the ball and obstacles to appear randomly in the screen 
        if x1 <-10:
            x1 =630
            y2 = height*0.85
        if xloc <-40:
            xloc = 600
            yloc = height*0.75
            count +=1
        clock.tick(60)
        pygame.display.flip()

game_loop()
pygame.quit()
quit()







