#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import ENTITY_SPEED, ENTITY_SHOT_DELAY, WIN_HEIGHT
from code.EnemyShot import EnemyShot
from code.Entity import Entity

class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]
        self.vertical_direction = 1  # Direção vertical inicial: 1 para baixo, -1 para cima

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]  # Movimento horizontal da direita para a esquerda

        if self.name == 'Enemy3':
            self.rect.centery += ENTITY_SPEED[self.name] * self.vertical_direction
            
            if self.rect.bottom >= WIN_HEIGHT:  # Se bater na borda inferior, sobe com velocidade normal
                self.vertical_direction = -1
            if self.rect.top <= 0:  # Se bater na borda superior, desce com o dobro da velocidade
                self.vertical_direction = 2

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))

    def update(self):
        return []

    def take_damage(self, amount):
        self.health -= amount
        return self.update()
