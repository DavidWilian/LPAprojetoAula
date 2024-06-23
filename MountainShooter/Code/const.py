# C
import pygame

COLOR_ORANGE = (255, 128, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_YELLOW = (241, 255, 4)

# E
ENTITY_SPEED = {'Level1BG0': 0,
                'Level1BG1': 1,
                'Level1BG2': 2,
                'Level1BG3': 3,
                'Level1BG4': 4,
                'Level1BG5': 5,
                'Level1BG6': 6,
                'Player1': 3,
                'Player2': 3,
                'Enemy1': 3,
                'Enemy2': 2,
                'Enemy3': 2,
                }
EVENT_ENEMY = pygame.USEREVENT + 1

# M
MENU_OPTION = ('New Game 1P',
               'New Game 2P - Cooperative',
               'New Game 2P - Competitive',
               'Exit')

# P
PLAYER_KEY_UP = {'Player1': pygame.K_UP,
                 'Player2': pygame.K_w
                 }
PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN,
                   'Player2': pygame.K_s
                   }
PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT,
                   'Player2': pygame.K_a
                   }
PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT,
                    'Player2': pygame.K_d
                    }

# W
WIN_WIDTH = 576
WIN_HEIGHT = 324
