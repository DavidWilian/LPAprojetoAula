#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.display
from pygame import Surface

from MountainShooter.Code.Entity import Entity
from MountainShooter.Code.EntityFactory import EntityFactory


class Level:
    def __init__(self, window, name, menu_return):
        self.window: Surface = window
        self.name = name
        self.mode = menu_return  # opção do menu
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1BG'))

    def run(self):
        while True:
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
            pygame.display.flip()
        pass
