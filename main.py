# import pygame module in this program 
import pygame

  
# activate the pygame library .  
# initiate pygame and give permission  
# to use pygame's functionality.  
pygame.init()
  
# create the display surface object  
# of specific dimension..e(500, 500).


# set the pygame window name 
pygame.display.set_caption("Harry Potter Adaptation")

XMAX = 1200
YMAX = 600


# object current co-ordinates 
x = 200
y = 200
  
# dimensions of the object 
width = 55
height = 77
  
# velocity / speed of movement
vel = 20
  
# Indicates pygame is running
run = True

backgrounds={1:'map1.jpg',2:'map2.jpg',3:'map3.jpg',4:'map4.jpg',5:'map5.jpg',6:'map6.jpg',7:'map7.jfif',8:'map8.jpg',9:'map9.jfif'}
location = 5


player = pygame.image.load('playerImage.png')

scr = pygame.display.set_mode((XMAX, YMAX))

# game = board.screen('Harry Potter Adaptation')

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
        if location!=9:
            location+=1
        else:
            location = 1
        x = XMAX-width-5
        
    # if left arrow key is pressed
    if keys[pygame.K_RIGHT] and x < (XMAX-width):
          
        # increment in x co-ordinate
        x += vel
    
    if keys[pygame.K_RIGHT] and x >=(XMAX-width):
        x = 5
        if location!=1:
            location-=1
        else:
            location = 9
    # if left arrow key is pressed   
    if keys[pygame.K_UP] and y>0:
          
        # decrement in y co-ordinate
        y -= vel
          
    # if left arrow key is pressed   
    if keys[pygame.K_DOWN] and y < (YMAX-height):
        # increment in y co-ordinate
        y += vel
    background = pygame.image.load(backgrounds[location])
    scr.blit(background, [0,0])
    
    scr.blit(player, (x, y))
    
    pygame.display.flip()
    
    pygame.display.update() 
    # closes the pygame window 
pygame.quit()
