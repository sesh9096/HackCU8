# import pygame module in this program 
import pygame
import board
  
# activate the pygame library .  
# initiate pygame and give permission  
# to use pygame's functionality.  
pygame.init()
  
# create the display surface object  
# of specific dimension..e(500, 500).  
win = pygame.display.set_mode((1300, 700))
  
# set the pygame window name 
pygame.display.set_caption("Harry Potter Adaptation")
  
# object current co-ordinates 
x = 200
y = 200
  
# dimensions of the object 
width = 20
height = 20
  
# velocity / speed of movement
vel = 10
  
# Indicates pygame is running
run = True


game = board.screen('Harry Potter Adaptation')


# infinite loop 
while run:
    # creates time delay of 10ms 
    
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
      
    # if left arrow key is pressed
    if keys[pygame.K_LEFT] and x>0:
          
        # decrement in x co-ordinate
        x -= vel
          
    # if left arrow key is pressed
    if keys[pygame.K_RIGHT] and x<500-width:
          
        # increment in x co-ordinate
        x += vel
         
    # if left arrow key is pressed   
    if keys[pygame.K_UP] and y>0:
          
        # decrement in y co-ordinate
        y -= vel
          
    # if left arrow key is pressed   
    if keys[pygame.K_DOWN] and y<500-height:
        # increment in y co-ordinate
        y += vel
    game.display_screen()
    
    pygame.display.update() 
    # closes the pygame window 
    pygame.time.delay(10)
pygame.quit()
