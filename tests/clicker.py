from random import randint

import PygameX
from PygameX.game import *
from PygameX.objects.Circle import Circle
from PygameX.objects.TextDisplay import TextDisplay


class MainGame(Game):
    clicks = 0

    background_color = (randint(0, 255), randint(0, 255), randint(0, 255))

    def init(self):
        click_counter = TextDisplay(
            text="Clicks: ",
            position=(250, 40),
            color=PygameX.math.invert_color(self.background_color)
        )
        self.objects["click_counter"] = click_counter

        clicker = Circle(
            radius=100,
            position=(250, 250),
            color=(randint(0, 255), randint(0, 255), randint(0, 255))
        )
        self.objects["clicker"] = clicker

    def on_mouse_pressed(self, mouse):
        if not mouse[1] == 1:
            return
        if not mouse[2]:
            return

        clicker = self.objects["clicker"]
        if PygameX.math.is_point_inside_circle(mouse[0], clicker):
            self.clicks += 1
            self.objects["click_counter"].set_text(f"Clicks: {self.clicks}")
            clicker.color = (randint(0, 255), randint(0, 255), randint(0, 255))


MainGame(width=500, height=500, max_fps=60)
