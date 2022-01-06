import pygame
import random
import math

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
alienImg = []
alienX = []
alienY = []
alienX_change = []
alienY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):                                 #creating enemies in loop

    alienImg.append(pygame.image.load('alien.png'))
    alienX.append(random.randint(0, 800))
    alienY.append(random.randint(50, 100))
    alienX_change.append(0.2)
    alienY_change.append(40) 

# Bullet
bulletImg = pygame.image.load('bullet.png')                     # Ready state - when bullets will not be fired
bulletX = 0                                                     #Fire state - when bullets will be fired
bulletY = 480
bulletX_change = 0
bulletY_change = 1
bullet_state = "ready"

# Score

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)                 # score value

textX = 10
textY = 10

# Game Over
over_font = pygame.font.Font('freesansbold.ttf', 64)

def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))

def player(x, y):
    screen.blit(playerImg, (x, y))                              # blit means draw

def alien(x, y, i):
    screen.blit(alienImg[i], (x, y))   

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))

def isCollision(alienX, alienY, bulletX, bulletY):                                         
    distance = math.sqrt(math.pow(alienX - bulletX, 2) + (math.pow(alienY - bulletY, 2)))  #distance formula 
    if distance < 27:                                              # considering 27 becuase of the size of the alien
        return True                                                # boolean function
    else:
        return False


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
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
               



        if event.type == pygame.KEYUP:         # to check if we released any button
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0             # keep the incrementer constant

     
    playerX += playerX_change                  # boundary check for spaceship

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # Enemy Movement
    for i in range(num_of_enemies):

        # Game Over
        if alienY[i] > 440:                    # if the alien reaches the spaceship then GAME OVER
            for j in range(num_of_enemies):
                alienY[j] = 2000
            game_over_text()
            break

        alienX[i] += alienX_change[i]          #if aliens collide to the leftmost and rightmost side of the screen
        if alienX[i] <= 0:                     #then we will just increase/decrease the alienX_change accordinly
            alienX_change[i] = 0.2
            alienY[i] += alienY_change[i]
        elif alienX[i] >= 736:
            alienX_change[i] = -0.2
            alienY[i] += alienY_change[i]

        # Collision
        collision = isCollision(alienX[i], alienY[i], bulletX, bulletY)   #when the bullet hits the alien
        if collision:
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            alienX[i] = random.randint(0, 736)                            #sprawning new alien
            alienY[i] = random.randint(50, 150)

        alien(alienX[i], alienY[i], i)                                    #initiating it's movement


    #Bullet Movement

    if bulletY <= 0:                                                      #when the bullet reaches the top most of the screen
        bulletY = 480                                                     # we will change it's state
        bullet_state = "ready"

    if bullet_state == "fire":                                             
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)                                   #calling the player function to draw space ship on the window
    show_score(textX, textY)
    pygame.display.update()                    #The display will only change when we update it
