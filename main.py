# import pygame module in this program 
import pygame
from random import randint
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

class Item(pygame.sprite.Sprite):
    def __init__(self, image, height=50,width=50):
        super(Item, self).__init__()
        self.surf = pygame.image.load(image).convert()
        self.surf = pygame.transform.scale(self.surf,(width,height))  #self.surf.set_colorkey((255,255,255),pygame.RLEACCEL)
        self.xloc =  randint(0,XMAX)
        self.yloc = randint(0,YMAX)
        self.rect = self.surf.get_rect(center=(self.xloc,self.yloc))        
        
    def remove_item(self):
        self.remove()

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

backgrounds={1:'map12.jpg',2:'map22.jpg',3:'map12.jpg',4:'map22.jpg',5:'map12.jpg',6:'map22.jpg',7:'map12.jpg',8:'map22.jpg',9:'map12.jpg'}

horcrux_list = ['h1.png','h2.png','h3.png','h4.png','h5.png','h6.jpg','h7.png']

location = 5

def message(fontName, size,text, location, color = (0,200,0)):
    fontObj = pygame.font.Font(fontName,size)
    textSurface = fontObj.render(text, True, color)
    scr.blit(textSurface, location)

player = pygame.image.load('playerImage.png')

scr = pygame.display.set_mode((XMAX, YMAX))

i = 5000
count=0

#startup

message('arial.ttf' ,50 ,"Time: " + str(int(i/10)), (10, 10))

message('arial.ttf' ,40 ,"Welcome to Harry Potter Adaptation" , (50, 100), (200, 200, 200))
message('arial.ttf' ,38 ,"Your nemesis has scattered the 7 horcruxes throughout the 9 worlds", (50, 150), (200, 200, 200))
message('arial.ttf' ,40 ,"To win, you must gather all 7 before time runs out" , (50, 200), (200, 200, 200))
message('arial.ttf' ,40 ,"Good Luck!" , (100, 250), (200, 200, 200))

pygame.display.flip()
pygame.display.update()
pygame.time.delay(5000)

# game = board.screen('Harry Potter Adaptation')
rand_location = randint(1,9)
current_item = None #False
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
        if location == rand_location:
            print('placing item')
            current_item = Item(horcrux_list.pop())#True
            
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
        if location == rand_location:
            print('placing item')
            current_item = Item(horcrux_list.pop())#True
            
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
    if current_item!=None:
        scr.blit(current_item.surf, current_item.rect)
    
    scr.blit(player, (x, y))
    
    if(i <= 0):
        run = False
        message('Inkfree.ttf' ,100 ,'You Have Failed', (300, 200), (200, 50, 50))
    else:
        message('Inkfree.ttf',50 ,"Time: " + str(int(i/10)), (10, 10))
        i-=1
    
    pygame.display.flip()

    
    if (current_item is not None) and (x>=current_item.xloc-25 and x<=current_item.xloc+100) and (y>=current_item.yloc-25 and y<=current_item.yloc+100):
        current_item.remove_item()
        current_item = None
        rand_location = randint(1,9)
        count+=1
        
    message('Inkfree.ttf',50 ,f"Items found: {count} of 7", (10, 60),(0,0,0))
    if not horcrux_list:
        message('arial.ttf' ,40 ,"You found all the horcurxes. Congrats" , (50, 100), (200, 200, 200))
        run = False
       
    pygame.display.update()
    
    if(run==False):
        pygame.time.delay(2000)
    # closes the pygame window 
pygame.quit()