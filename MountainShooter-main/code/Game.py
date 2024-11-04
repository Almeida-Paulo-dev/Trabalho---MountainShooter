#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.Level import Level
from code.Menu import Menu
from code.Score import Score

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            score = Score(self.window)
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
                player_score = [0, 0]  # [Player1, Player2]
                total_time = 0  # Inicializa a contagem do tempo total

                # Level 1
                print('Iniciando Level 1')
                level = Level(self.window, 'Level1', menu_return, player_score)
                level_return, level_time = level.run(player_score)
                total_time += level_time

                if level_return:
                    # Level 2
                    print('Iniciando Level 2')
                    level = Level(self.window, 'Level2', menu_return, player_score)
                    level_return, level_time = level.run(player_score)
                    total_time += level_time

                    if level_return:
                        # Level 3
                        print('Iniciando Level 3')
                        level = Level(self.window, 'Level3', menu_return, player_score)
                        level.timeout = total_time  # Define o tempo do Level 3 como a soma dos tempos dos Levels 1 e 2
                        level_return, _ = level.run(player_score)

                        if level_return:
                            print('Salvando pontuação final.')
                            score.save(menu_return, player_score)
            elif menu_return == MENU_OPTION[3]:
                score.show()
            elif menu_return == MENU_OPTION[4]:
                pygame.quit()  # Fechar Janela
                quit()  # Finalizar pygame
            else:
                pygame.quit()
                sys.exit()
