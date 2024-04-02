import pygame
from framework import *
import rps
import matchingpennies as mp
pygame.init()
pygame.font.init()
menuScreen = Screen("Main", WHITE)
screen = menuScreen

def play():
    game_over = False
    while not game_over:
        for event in pygame.event.get():
            #Quite game
            if event.type == pygame.QUIT:
                game_over=False
                return pygame.QUIT
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                for button in screen.buttons:
                    if button.checkClicked(x,y):
                        if type(button) is NavButton:
                            game_over=False
                            screen = button.changeScreen(screen)
        screen.screenUpdate()
menuScreen.play = play

rpsscreen = rps.screen
penniesscreen = mp.screen

menuScreen.makeCurrentScreen()

penniesbutton = NavButton((200,100),"Matching Pennies", BLUE, penniesscreen,"penniesBtn", ((GRID_WIDTH-200)/2,100))
rpsbutton = NavButton((200,100), "RPS",GREEN, rpsscreen,"rpsBtn",((GRID_WIDTH-200)/2, 250))
homebutton = NavButton((100,100), "Home",GREY, menuScreen,"homeBtn",((0,0)))
menuScreen.addButtons([penniesbutton, rpsbutton,homebutton])
rpsscreen.addButton(homebutton)
penniesscreen.addButton(homebutton)


running = True
while running:
    result = screen.play()
    if result == pygame.QUIT:
        pygame.quit()

    
    
    
