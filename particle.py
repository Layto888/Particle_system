"""
A simple 2D particle engine.
Author: Amardjia Amine
"""
import pygame as pg
from random import uniform
from random import randint
from laylib import util

"""
Parameters:
1. The number of paticles
2. speed of particles on move
3. the duration of each particle between creation and death
4. the radius of each particle
5. the field of generated particle
6. the particles colors.
"""
PARTICLES_NUM = 1000
PARTICLE_MAX_SPEED = 0.9
PARTICLE_DURATION = 500
PARTICLE_RADIUS = 9
THIKNESS = 15
COLOR_RANGE = (80, 255)


class Particle(object):
    """
    particle class
    """

    def __init__(self, pos, vel, radius, color):
        self.x, self.y = pos
        self.y_vel = vel
        self.x_vel, self.y_vel = vel
        self.radius = radius
        self.color = color
        # in ms.
        self.duration = uniform(
            PARTICLE_DURATION / 3, PARTICLE_DURATION)
        self.startTime = util.get_time()
        self.screen = pg.display.get_surface()
        self.boundary = self.screen.get_rect()
        # rot & rot_speed:

    def update(self, dt):
        # update the move of particles
        self.x += uniform(-0.5, 2.5) * dt
        self.y += self.y_vel * dt
        self.x = int(self.x)
        self.y = int(self.y)

    def draw(self):
        # draw particle
        pg.draw.circle(self.screen, self.color,
                       (self.x, self.y), int(self.radius), 0)

    def is_dead(self):
        # tell if the elapsed time of particle is greater than  duration or not
        return util.get_time() - self.startTime > self.duration


class ParticlesEngine(object):
    # class: manage a groupe of particles
    def __init__(self, pos):
        self.particles = []
        self.pos = pos
        self.done = False
        self.screen = pg.display.get_surface()
        self.boundary = self.screen.get_rect()
        for _ in range(PARTICLES_NUM):
            self.particles.append(self.generate_particle(pg.mouse.get_pos()))

    @staticmethod
    def generate_particle(pos):
        # generate a group of particles using the defined parameters
        this_pos = (pos[0] + uniform(-THIKNESS, THIKNESS * 2),
                    pos[1] + uniform(-THIKNESS, THIKNESS * 0.5))
        this_vel = (uniform(-0.15, 0.15),
                    uniform(-PARTICLE_MAX_SPEED, 0.05))
        this_radius = uniform(0.1, PARTICLE_RADIUS)
        color_choice = randint(*COLOR_RANGE)
        this_color = (color_choice, color_choice, color_choice)
        return Particle(this_pos, this_vel, this_radius, this_color)

    def update(self, dt):
        # update all the group of particles
        for particle in self.particles:
            if particle.is_dead():
                # remove the dead particles
                self.particles.remove(particle)
                # here append new particle to replace the dead one
                self.particles.append(
                    self.generate_particle(pg.mouse.get_pos()))

            particle.update(dt)

    def draw(self):
        # draw all stuffs
        self.screen.fill((0, 0, 0))
        for particle in self.particles:
            particle.draw()
        pg.display.update()

    def event_listener(self):
        # mouse event managing
        ev = pg.event.poll()
        if ev.type == pg.QUIT:
            self.done = True

    def main_loop(self):
        # the main loop of program
        while not self.done:
            self.event_listener()
            self.update(0.5)
            self.draw()
