#board 
import pygame

pygame.init()

backgrounds= {(1,1):(0,0,0), (1,2):(110, 77, 209), (1,3):(67, 190, 11), (2,1):'map12.jpg', (2,2):'map22.jpg', (2,3):(232, 199, 181), (1,1):(193, 158, 14), (1,2):(229, 97, 89), (1,3):(203, 175, 165)}

class screen():
    def __init__(self, title, width=800, height=800, location = (2,2)):
        self
        self.width = 800
        self.height = 800
        self.location = location
        self.background = pygame.image.load(backgrounds[location])
        
    def display_screen(self):
        #bg = pygame.image.load("bg.png")
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.screen.blit(self.background, (0, 0))
        
    def update_screen(self, door_entered):
        current_location = self.location
        new_location = ()
        if(door_entered == 'N'):
            new_location = (current_location[0]-1,current_location[1]) 
        elif(door_entered == 'S'):
            new_location = (current_location[0]+1,current_location[1])
        elif(door_entered == 'E'):
            new_location = (current_location[0],current_location[1]-1)
        else:
            new_location = (current_location[0]-1,current_location[1]+1)
        self.location = new_location
        self.background = pygame.image.load(backgrounds[new_location])

#screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

scr = screen("start")
scr.display_screen()
scr.update_screen('N')
scr.display_screen()
                                            