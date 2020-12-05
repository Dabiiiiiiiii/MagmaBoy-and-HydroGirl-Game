"""
Main file for Magma Boy and Hydro Girl game.
"""

# import pygame and orther needed libraries
import sys
import pygame
from pygame.locals import *

# import classes
from game import Game
from board import Level_1
from character import MagmaBoy, HydroGirl
from controller import MagmaBoyController, HydroGirlController


def main():
    # inialize pygame
    pygame.init()
    clock = pygame.time.Clock()
    
    # initialize all classes used in game
    game = Game()
    
    board = Level_1()

    hydro_girl = HydroGirl()
    magma_boy = MagmaBoy()

    magma_boy_controller = MagmaBoyController(magma_boy)
    hydro_girl_controller = HydroGirlController(hydro_girl)

    # main game loop
    while True:
        game.draw_board(board)

        events = pygame.event.get()

        magma_boy_controller.get_user_input(events)
        hydro_girl_controller.get_user_input(events)
        
        magma_boy.calc_movement()
        hydro_girl.calc_movement()
        
        game.move_player(board, magma_boy)
        game.move_player(board, hydro_girl)

        game.draw_player(magma_boy)
        game.draw_player(hydro_girl)

        game.refresh_window()

        clock.tick(60)


if __name__ == '__main__':
    main()
