import pygame, os
import numpy as np
import config as c

class enemy():
  def __init__(self, pos):
    #initialize object
    self.position = pos
    self.x = np.array([75, 72, 77, 83, 88, 85, 83, 77])
    self.y = np.array([37, 32, 27, 27, 32, 37, 35, 35])

    self.x += 40*(pos % 7)
    self.y += 30*((pos+7)/7)

    self.isAlive = True
    self.state = 0
    self.dying_time = 6*10
    self.di = 0.15
    self.k0 = 0.0
    self.k1 = 0


    self.sound_expl = pygame.mixer.Sound(c.explosion)
    self.dx = -1 if np.random.uniform() < 0.5 else 1
    font = pygame.font.Font(None, c.font_size_enemy)
    self.texto = font.render(c.death_msg.strip(), True, self.color)
    self.r = self.texto.get_rect()
    self.ammo = []
    for i in np.arange(self.n_ammo):
      self.ammo.append(bullet())
  def checkLimits(self):
    if self.x[4] < -1:
      self.x -= self.x[4] - 1
      self.dx = -self.dx
    elif self.x[1] > c.screen_size[0] + 1:
      self.x -= self.x[1] - (c.screen_size[0] + 1)
      self.dx = -self.dx

  def update:
    if self.isAlive:
      if self.state == 0:
        self.k0 += self.di
        if np.abs(self.k0) >= 1:
          self.x += int(self.k0)
          self.k1 += 1
          self.k0 = 0.0
          if self.k1 == 10:
            self.di = -self.di
            self.k1 -= self.k1
        elif self.state == 1:
          if np.random.uniform() >= 0.98:
            self.dx = -self.dx
          self.x += self.dx
          self.y += 1
          self.checkLimits()
          if self.y[2] > 450:
            self.y -= 466


       for weapon in self.ammo:
         if weapon.isAlive:
           weapon.move()

  def shoot(self, prob):
    for i in np.arange(self.n_ammo)                          
