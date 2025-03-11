import pygame, sys
import random
import math
import os
from os.path import join
from random import randint as rnd
from pygame.time import delay as slp

from colors import *
from pygame_config import *
import classes_and_objects.shapes as shapes
import classes_and_objects.boxes as boxes

def init_game():
    pygame.init()
    pygame.display.set_caption(PYGAME_CAPTION) # Window Caption

    #Pygame Window
    window = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    return window

# Draw Function to update graphics
def draw(window,background,textboxes):
    #BACKGROUND
    window.fill(WHITE) # 15

    for background_item in background:
        background_item.draw()
    #FOREGROUND
    
    for tb in textboxes:
        tb.draw_textbox()

    pygame.display.update()

def handle_events(text):
    user_text = text

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # QUIT
            return False, ""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                user_text = "left"
            elif event.key == pygame.K_RIGHT:
                user_text = "right"
            elif event.key == pygame.K_UP:
                user_text = "up"
            elif event.key == pygame.K_DOWN:
                user_text = "down"
            elif event.key == pygame.K_RETURN:
                user_text = "enter"
            elif event.key == pygame.K_BACKSPACE:
                user_text = "backspace"
            elif event.key == pygame.K_RSHIFT:
                user_text = "right shift"
            elif event.key == pygame.K_LSHIFT:
                user_text = "left shift"
            elif event.key == pygame.K_SPACE:
                user_text = "spacebar"
            else:
                user_text = event.unicode
    return True, user_text

def main(): # MAIN FUNCTION
    window = init_game()
    clock = pygame.time.Clock()
    # ADD ALL OBJECTS/CLASSES BELOW HERE
    the_code ="upupdowndownleftrightleftrightabenter"
    lookingforcode = ""
    border = shapes.Rectangle(window, THAYER_GREEN, 10,10,SCREEN_HEIGHT-20,SCREEN_WIDTH-20,5)

    background = [border]

    text = "Type something to change the text!"
    textbox = boxes.Text_box(window,SCREEN_HEIGHT//2,600,100,30,text, BLACK)

    textboxes = [textbox]
    
    # ADD ALL OBJECTS/CLASSES ABOVE HERE
    run = True
    while run: # run set to true, program runs while run is true.

        clock.tick(FPS) # FPS Tick

        run,text = handle_events(text)
        lookingforcode += text

        if the_code[:len(lookingforcode)] == lookingforcode:
            if the_code == lookingforcode:
                print("yippee")

        textbox.update_text(text)
        
        
        draw(window,background,textboxes) # UPDATES SCREEN

    pygame.quit()
    quit()
# ADD CLASSES HERE



# ADD CLASSES ABOVE
if __name__ == "__main__": 
    main()

