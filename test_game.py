import pytest

# import pygame and orther needed libraries
import sys
import pygame
from pygame.locals import *

# import classes
from game import Game
from doors import FireDoor, WaterDoor

#characters at start
magma_boy = pygame.Rect(16,350,16,32)
hydro_girl = pygame.Rect(16,350,16,32)
#characters in goo
magma_boy_goo = pygame.Rect(272,80,16,32)
hydro_girl_goo = pygame.Rect(272,80,16,32)
#characters in lava
magma_boy_lava = pygame.Rect(19*16,23*16,16,32)
hydro_girl_lava = pygame.Rect(19*16,23*16,16,32)
#characters in water
magma_boy_water = pygame.Rect(11*16,23*16,16,32)
hydro_girl_water = pygame.Rect(11*16,23*16,16,32)
#characters at gates
magma_boy_gates = pygame.Rect(285, 128,16,32)
hydro_girl_gates = pygame.Rect(285, 128,16,32)
#characters at fire door
magma_boy_fired = pygame.Rect(64, 48,16,32)
hydro_girl_fired = pygame.Rect(64, 48,16,32)
#characters at water door
magma_boy_waterd = pygame.Rect(128, 48,16,32)
hydro_girl_waterd = pygame.Rect(128, 48,16,32)


collision_cases = [
# Check that if there is nothing, there is no collisions
(magma_boy, [], []),
(hydro_girl, [], []),
# Check for player collisions on floor
(magma_boy, [pygame.Rect(16,350,16,16)], [pygame.Rect(16,350,16,16)]),
(hydro_girl, [pygame.Rect(16,350,16,16)], [pygame.Rect(16,350,16,16)]),
# Check for player collisions on goo
(magma_boy_goo, [pygame.Rect(272,80,16,16)], [pygame.Rect(272,80,16,16)]),
(hydro_girl_goo, [pygame.Rect(272,80,16,16)], [pygame.Rect(272,80,16,16)]),
# Check for player collisions on lava
(magma_boy_lava, [pygame.Rect(19*16,23*16,16,16)], [pygame.Rect(19*16,23*16,16,16)]),
(hydro_girl_lava, [pygame.Rect(19*16,23*16,16,16)], [pygame.Rect(19*16,23*16,16,16)]),
# Check for player collisions on water
(magma_boy_water, [pygame.Rect(11*16,23*16,16,16)], [pygame.Rect(11*16,23*16,16,16)]),
(hydro_girl_water, [pygame.Rect(11*16,23*16,16,16)], [pygame.Rect(11*16,23*16,16,16)]),
# Check for player collisions on gates
(magma_boy_gates, [pygame.Rect(285, 128,16,16)], [pygame.Rect(285, 128,16,16)]),
(hydro_girl_gates, [pygame.Rect(285, 128,16,16)], [pygame.Rect(285, 128,16,16)]),
# Check for player collisions on fire doors
(magma_boy_fired, [pygame.Rect(64, 48,16,16)], [pygame.Rect(64, 48,16,16)]),
(hydro_girl_fired, [pygame.Rect(64, 48,16,16)], [pygame.Rect(64, 48,16,16)]),
# Check for player collisions on water doors
(magma_boy_waterd, [pygame.Rect(128, 48,16,16)], [pygame.Rect(128, 48,16,16)]),
(hydro_girl_waterd, [pygame.Rect(128, 48,16,16)], [pygame.Rect(128, 48,16,16)]),
]

# Define standard testing functions to check functions' outputs given certain
# inputs defined above.
@pytest.mark.parametrize("player,tile,hit_list", collision_cases)
def test_collision(player,tile,hit_list):
    assert Game.collision_test(player, tile) == hit_list

#both doors closed
fire_door = FireDoor((64, 48), (64, 48), (48, 16))
water_door = WaterDoor((128, 48), (128, 48), (112, 16))

# both doors open
fire_door_both = FireDoor((16,350), (16,350), (0, 318))
fire_door_both._door_open = True
water_door_both = WaterDoor((16,350), (16,350), (0, 318))
water_door_both._door_open = True

#fire door open, water door closed
fire_door_magma = FireDoor((16,350), (16,350), (0, 318))
fire_door_magma._door_open = True
water_door_magma = WaterDoor((128, 48), (128, 48), (112, 16))

#water door open, fire door closed
fire_door_hydro = FireDoor((64, 48), (64, 48), (48, 16))
water_door_hydro = WaterDoor((16,350), (16,350), (0, 318))
water_door_hydro._door_open = True

level_done_cases = [
#players not in front of door
([fire_door, water_door], False),
#both players in front of door
([fire_door_both, water_door_both], True),
#only magmaboy in front of door
#players not in front of door
([fire_door_magma, water_door_magma], False),
#both only hydrogirl in front of door
([fire_door_hydro, water_door_hydro], False),
]

@pytest.mark.parametrize("doors,win_status", level_done_cases)
def test_level_is_done(doors,win_status):
    assert Game.level_is_done(doors,doors) == win_status
