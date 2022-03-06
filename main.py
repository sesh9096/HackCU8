# import pygame module in this program 
import pygame
import board
  
# activate the pygame library .  
# initiate pygame and give permission  
# to use pygame's functionality.  
pygame.init()

# create the display surface object  
# of specific dimension..e(500, 500).  
XMAX = 1300
YMAX = 700

win = pygame.display.set_mode((XMAX, YMAX))



# set the pygame window name 
pygame.display.set_caption("Harry Potter Adaptation")
  
# object current co-ordinates 
x = 200
y = 200
  
# dimensions of the object 
width = 55
height = 77
  
# velocity / speed of movement
vel = 10
  
# Indicates pygame is running
run = True

player = pygame.image.load('playerImage.png')

game = board.screen('Harry Potter Adaptation')


# infinite loop 
while run:
    # creates time delay of 10ms 
    pygame.time.delay(10)
    # iterate over the list of Event objects  
    # that was returned by pygame.event.get() method.  
    for event in pygame.event.get():
          
        # if event object type is QUIT  
        # then quitting the pygame  
        # and program both.  
        if event.type == pygame.QUIT:
              
            # it will make exit the while loop 
            run = False
    # stores keys pressed 
    keys = pygame.key.get_pressed()
      
    if keys[pygame.K_LEFT] and x>0:
          
        # decrement in x co-ordinate
        x -= vel
          
    if keys[pygame.K_LEFT] and x<=0:    
        game.update_background('L')
        x = XMAX-width-5
        
    # if left arrow key is pressed
    if keys[pygame.K_RIGHT] and x < (XMAX-width):
          
        # increment in x co-ordinate
        x += vel
    
    if keys[pygame.K_RIGHT] and x >=(XMAX-width):
        game.update_background('R')
        x = 5
         
    # if left arrow key is pressed   
    if keys[pygame.K_UP] and y>0:
          
        # decrement in y co-ordinate
        y -= vel
          
    # if left arrow key is pressed   
    if keys[pygame.K_DOWN] and y < (YMAX-height):
        # increment in y co-ordinate
        y += vel
        
    game.screen.blit(game.background, (0,0))
    
    game.screen.blit(player, (x, y))
    
    
    pygame.display.update() 
    # closes the pygame window 
pygame.quit()
