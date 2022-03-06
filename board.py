#board 
import pygame

pygame.init()

backgrounds= {(1,1):(0,0,0), (1,2):'map12.jpg', (1,3):(67, 190, 11), (2,1):(), (2,2):'map22.jpg', (2,3):(232, 199, 181), (3,1):(193, 158, 14), (3,2):(229, 97, 89), (3,3):(203, 175, 165)}

class screen():
    def __init__(self, width=800, height=800, location = (2,2)):
        #self.title = backgrounds[location][1]
        self.width = 800
        self.height = 800
        self.location = location
        bg = pygame.image.load(backgrounds[location])
        self.background = pygame.image.load(backgrounds[location])
        self.screen = pygame.display.set_mode((self.width, self.height))
        
    def update_background(selfdoor_entered):
        current_location = self.location
        new_location = ()
        if(door_entered == 'N'):
            new_location = (current_location[0]-1, current_location[1]) 
        elif(door_entered == 'S'):
            new_location = (current_location[0]+1, current_location[1])
        elif(door_entered == 'E'):
            new_location = (current_location[0], current_location[1]-1)
        elif door_entered == 'W':
            new_location = (current_location[0]-1, current_location[1]+1)
        self.location = new_location
        bg = pygame.image.load(backgrounds[new_location])
        self.background = pygame.transform.scale(bg, (self.width, self.height))
        
    #def update_doors(self):
        #if 
        
scr = screen("start")
#pygame.display.set_mode((self.width, self.height))
run = True
while(run):
    scr.screen.blit(scr.background,(0,0))
    #direction = ''
    #for event in pygame.event.get():
        #if event.type == SPACE:
            #get direction
            #scr.update_screen('N')
    pygame.display.update()
    #scr.update_background(direction)
    #scr.update_doors()
#scr.display_screen()
                                            