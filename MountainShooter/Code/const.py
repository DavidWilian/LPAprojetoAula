# C
import pygame

COLOR_ORANGE = (255, 128, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_YELLOW = (241, 255, 4)

# E
ENTITY_HEALTH = {'Level1BG0': 999,
                 'Level1BG1': 999,
                 'Level1BG2': 999,
                 'Level1BG3': 999,
                 'Level1BG4': 999,
                 'Level1BG5': 999,
                 'Level1BG6': 999,
                 'Player1': 300,
                 'Player1Shot': 1,
                 'Player2': 300,
                 'Player2Shot': 1,
                 'Enemy1': 200,
                 'Enemy1Shot': 1,
                 'Enemy2': 200,
                 'Enemy2Shot': 1,
                 'Enemy3': 250,
                 'Enemy3Shot': 1,
                 }

ENTITY_SHOT_DELAY = {'Player1': 20,
                     'Player2': 15,
                     'Enemy1': 60,
                     'Enemy2': 70,
                     'Enemy3': 130,
                     }

ENTITY_SPEED = {'Level1BG0': 0,
                'Level1BG1': 1,
                'Level1BG2': 2,
                'Level1BG3': 3,
                'Level1BG4': 4,
                'Level1BG5': 5,
                'Level1BG6': 6,
                'Player1': 3,
                'Player1Shot': 2,
                'Player2': 3,
                'Player2Shot': 3,
                'Enemy1': 2,
                'Enemy1Shot': 3,
                'Enemy2': 2,
                'Enemy2Shot': 3,
                'Enemy3': 1,
                'Enemy3Shot': 7,
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
PLAYER_KEY_SHOOT = {'Player1': pygame.K_KP_ENTER,
                    'Player2': pygame.K_f}

# W
WIN_WIDTH = 576
WIN_HEIGHT = 324
