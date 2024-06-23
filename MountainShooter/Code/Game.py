# !/usr/bin/python
# -*- coding: utf-8 -*-
import sys

import pygame

from MountainShooter.Code.Level import Level
from MountainShooter.Code.Menu import Menu
from MountainShooter.Code.const import WIN_WIDTH, MENU_OPTION
from MountainShooter.Code.const import WIN_HEIGHT


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
                level = Level(self.window, 'Level 1', menu_return)
                level_return = level.run()
            else:
                pygame.quit()
                sys.exit()

