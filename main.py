import pygame
import random

# Initiate the pygame 
pygame.init()

# Creating the window
screen = pygame.display.set_mode((800, 600)) #(x, y)top left corner to bottom right corner

# Background
background = pygame.image.load('backgroundimg.png')

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('spaceship.png')    #First load the image
pygame.display.set_icon(icon)                #Then assign it to someone


# Player
playerImg = pygame.image.load('spaceship2.png')
playerX = 370
playerY = 480
playerX_change = 0 

# Alien
alienImg = pygame.image.load('alien.png')
alienX = random.randint(0, 800)
alienY = random.randint(50, 100)
alienX_change = 0.2
alienY_change = 40 

# Bullet
bulletImg = pygame.image.load('bullet.png')
bulletX = random.randint(0, 800)
bulletY = random.randint(50, 100)
bulletX_change = 0.2
bulletY_change = 40 

def player(x, y):
    screen.blit(playerImg, (x, y))                              # blit means draw

def alien(x, y):
    screen.blit(alienImg, (x, y))   

#Game Loop (anything which we want inside the window will be a part of that loop)

running = True
while running:                                #infinite loop, it will display the screen for infinite time
    
    screen.fill((0, 0, 0))                   #changing the style of screen (Line: 7) with rgb parameters
    
    screen.blit(background, (0, 0))
    
    for event in pygame.event.get():          #which we need to stop when someone clicks cross button
        if event.type == pygame.QUIT:         #looping through all the events and check if the cross button is pressed or not, continously
            running = False

        if event.type == pygame.KEYDOWN:      # first we will check if anykind of key is pressed or not
            if event.key == pygame.K_LEFT:     # then we will check if the left key is pressed
                playerX_change = -0.3          # we will decrease the value of X
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3           # increase the value of X
        
        if event.type == pygame.KEYUP:         # to check if we released any button
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0             # keep the incrementer constant

     
    playerX += playerX_change                  # boundary check for spaceship

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    alienX += alienX_change                    # boundary check for alien

    if alienX <= 0:
        alienX_change = 0.2
        alienY+= alienY_change
    elif alienX >= 736:
        alienX_change = -0.2
        alienY+= alienY_change

    player(playerX, playerY)                                   #calling the player function to draw space ship on the window
    alien(alienX, alienY)
    pygame.display.update()                    #The display will only change when we update it