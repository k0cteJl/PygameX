from random import randint

import PygameX
from PygameX.all_objects import *
from PygameX.game import *


class MainGame(Game):
    background_color = color.BLUE
    object_render_mode = True

    def ready(self):
        player = Circle(
            position=(50, 50),
            radius=25,
            color=(0, 255, 0)
        )
        self.objects["player"] = player

    def on_event(self, event):
        super().on_event(event)

    def on_mouse_pressed(self, mouse):
        if mouse[1] == 1:
            if mouse[2]:
                player = self.objects["player"]
                if PygameX.math.is_point_inside_circle(mouse[0], player):
                    player.color = (randint(0, 255), randint(0, 255), randint(0, 255))

    def update(self):
        player = self.objects["player"]
        keys = PygameX.key.get_pressed()
        if keys[PygameX.key.LEFT]:
            player.position = (player.position[0] - 3, player.position[1])
        if keys[PygameX.key.RIGHT]:
            player.position = (player.position[0] + 3, player.position[1])
        if keys[PygameX.key.UP]:
            player.position = (player.position[0], player.position[1] - 3)
        if keys[PygameX.key.DOWN]:
            player.position = (player.position[0], player.position[1] + 3)


MainGame(width=500, height=300, max_fps=60)
