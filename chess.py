import pygame #imports pygame
import pygame_gui as gui #imports pygame gui as gui
import pygame.rect as Rect
import time

# name = input("Whats your name? \n My name is: ")#asks for the name of the player
# print(name)# prints the name of the player with a message
# time.sleep(2)
# print(f"fuck you {name} i dont give a shit")
pygame.font.init()
pygame.init() # start the library
clock = pygame.time.Clock() # start the cock that in in discharge of the ticks
pygame.display.set_caption("Chess") # sets the captan as chess
window_surface = pygame.display.set_mode((800, 800)) #sets the window size

background = pygame.Surface((800, 800)) # change color of the surface 
background.fill((pygame.Color("#C2C2C2"))) # colors the background to white

is_running = True # boleen to make run true

while is_running: #begin wile loop
    
    for event in pygame.event.get(): # start for loop for pygane gevents
        if event.type == pygame.QUIT: # if then statement
            is_running = False # set is run to false

    window_surface.blit(background, (0, 0, 800, 800)) # surface color change 
    

# MENU DEISEN STARTS HERE \/\/\/\/ ✡️


    button_rect = pygame.draw.rect(window_surface, "blue", (250, 350, 300, 100)) #
    button_rect1 = pygame.draw.rect(window_surface, "blue", (250, 500, 300, 100)) #
    button_rect2 = pygame.draw.rect(window_surface, "blue", (250, 650, 300, 100)) #
    mainTitleSurface = pygame.font.SysFont("Arial", 50)
    MainTitleButtonSurface = pygame.font.SysFont("Arial", 30)
    mainTitle = mainTitleSurface.render("Chess but gay✡️", False, "Black")
    versusButton = MainTitleButtonSurface.render("Play", False, "Black")
    botButton = MainTitleButtonSurface.render("Go against a bot", False, "Black")
    settingsButton = MainTitleButtonSurface.render("Settings✡️", False, "Black")
    window_surface.blit(mainTitle, (250, 200))
    window_surface.blit(versusButton, (300, 375))
    window_surface.blit(botButton, (275, 525))
    window_surface.blit(settingsButton, (275, 675))
    
    
    
    
    
    
    
    
    
    
    pygame.display.update() #updates te display 
