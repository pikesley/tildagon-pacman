from math import atan2
from random import choice, randint, random

import imu
from events.input import BUTTON_TYPES, Buttons
from system.eventbus import eventbus
from system.patterndisplay.events import PatternDisable
from tildagonos import tildagonos

import app

from .lib.background import Background
from .lib.conf import conf, sprite_data
from .lib.gamma import gamma_corrections
from .lib.sprite_train import SpriteTrain

ghost_data = sprite_data["ghost"]
pacman_data = sprite_data["pacman"]


class Game(app.App):
    """Pacman."""

    def __init__(self):
        """Construct."""
        eventbus.emit(PatternDisable())
        self.button_states = Buttons(self)
        self.ghosts_are_blue = False

        self.scale = conf["player"]["scale"]["default"]
        self.speed = conf["player"]["speed"]

        self.directions = ["up", "down", "left", "right"]

        self.direction = choice(self.directions)

        self.led_colour = pacman_data["colours"]["primary"]
        self.rotation = 0

        self.ghost_skins = ["blocky", "smooth"]
        self.pacman_skins = ["blocky", "smooth"]
        self.sprite_train = SpriteTrain(self.scale, skin=self.pacman_skins[0])
        self.sprite_train.align(self.direction)

    def update(self, _):
        """Update."""
        self.scan_buttons()

        acc = imu.acc_read()
        weighting = min(1.0, int(abs(10 - acc[2])) / 9)
        self.rotation = (atan2(acc[1], acc[0])) * weighting

        if self.sprite_train.off_screen:
            self.direction = choice(self.directions)

            self.sprite_train.chaser = "ghosts"
            if random() > 0.7:
                self.sprite_train.chaser = "pacman"

            self.sprite_train.recolour()
            self.sprite_train.reorder()
            self.sprite_train.align(self.direction)

        for sprite in self.sprite_train.sprites:
            sprite.animate()
            sprite.move(self.direction, conf["player"]["speed"])

        self.light_leds(self.led_colour)

    def draw(self, ctx):
        """Draw."""
        ctx.rotate(-self.rotation)

        self.overlays = []
        self.overlays.append(Background(colour=(0, 0, 0)))

        for sprite in self.sprite_train.sprites:
            self.overlays.extend(sprite.pixels)

        self.draw_overlays(ctx)

    def scan_buttons(self):
        """Buttons."""
        if self.button_states.get(BUTTON_TYPES["CANCEL"]):
            self.button_states.clear()
            self.minimise()

        if self.button_states.get(BUTTON_TYPES["UP"]):
            self.button_states.clear()
            if self.scale < conf["player"]["scale"]["max"]:
                self.scale += 1
                self.sprite_train.rescale(self.scale)

        if self.button_states.get(BUTTON_TYPES["DOWN"]):
            self.button_states.clear()
            if self.scale > conf["player"]["scale"]["min"]:
                self.scale -= 1
                self.sprite_train.rescale(self.scale)

    def light_leds(self, colour):
        """Light the lights."""
        for i in range(18):
            brightness = conf["led-brightness"] + (randint(-1, 1) / 50)

            tildagonos.leds[i + 1] = [
                gamma_corrections[int(i * brightness)] for i in colour
            ]

        tildagonos.leds.write()


__app_export__ = Game
