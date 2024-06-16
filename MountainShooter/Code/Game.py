# !/usr/bin/python
# -*- coding: utf-8 -*-
import pygame


from MountainShooter.Code.Menu import Menu
from MountainShooter.Code.const import WIN_WIDTH
from MountainShooter.Code.const import WIN_HEIGHT


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu.run()

