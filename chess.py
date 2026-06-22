import pygame #imports pygame
import pygame_gui as gui #imports pygame gui as gui
import pygame.rect as Rect

#choose res for debugging
windowx = 1920
windowy = 1080
ratiox = 800/windowx
ratioy = 800/windowy

pygame.font.init()
pygame.init() # start the library
clock = pygame.time.Clock() # start the cock that in in discharge of the ticks
pygame.display.set_caption("Chess") # sets the captan as chess
window_surface = pygame.display.set_mode((windowx, windowy), pygame.SCALED) #sets the window size

background = pygame.Surface((windowx, windowy)) # change color of the surface 
background.fill((pygame.Color("Black"))) # colors the background to white

is_running = True # boleen to make run true

while is_running: #begin wile loop
    
    for event in pygame.event.get(): # start for loop for pygane gevents
        if event.type == pygame.QUIT: # if then statement
            is_running = False # set is run to false
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                print("left click")
                if versusButton_rect.collidepoint(event.pos):
                    print("versus button clicked")
                if botButton_rect.collidepoint(event.pos):
                    print("bot button clicked")
                if settingsButton_rect.collidepoint(event.pos):
                    print("settings button clicked")
    window_surface.blit(background, (0, 0, windowx, windowy)) # surface color change 
    

# MENU DEISEN STARTS HERE \/\/\/\/ 


    versusButton_rect = pygame.draw.rect(window_surface, "blue", (250/ratiox, 350/ratioy, 300/ratiox, 100/ratioy)) #
    botButton_rect = pygame.draw.rect(window_surface, "blue", (250/ratiox, 500/ratioy, 300/ratiox, 100/ratioy)) #
    settingsButton_rect = pygame.draw.rect(window_surface, "blue", (250/ratiox, 650/ratioy, 300/ratiox, 100/ratioy)) #
    mainTitleSurface = pygame.font.SysFont("Arial", 100)
    MainTitleButtonSurface = pygame.font.SysFont("Arial", 60)
    mainTitle = mainTitleSurface.render("Chess but gay", False, "White")
    versusButton = MainTitleButtonSurface.render("Play", False, "Black")
    botButton = MainTitleButtonSurface.render("Go against a bot", False, "Black")
    settingsButton = MainTitleButtonSurface.render("Settings/Privacy", False, "Black")
    #main title surface merge
    window_surface.blit(mainTitle, (250/ratiox, 200/ratioy))
    #buttons text surface merge
    window_surface.blit(versusButton, (300/ratiox, 375/ratioy))
    window_surface.blit(botButton, (275/ratiox, 525/ratioy))
    window_surface.blit(settingsButton, (275/ratiox, 675/ratioy))
    
    
    #menu mouse interactions.
   
    mousex, mousey = pygame.mouse.get_pos()
    print(mousex, mousey)
    
    
    
    clock.tick(10)
    
    pygame.display.update() #updates te display 
