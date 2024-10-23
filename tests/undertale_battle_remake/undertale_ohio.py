# pgX 0.2 сломался на pypi

from PygameX import *

import attack_moves

class UndertaleGame(Game):

    #object_render_mode = True # На случай если 0.2 не скачивается стабильно.

    def init(self):
        # only visual
        battle_area = Rect(
            size=(300, 300),
            color=(255, 255, 255),
            position=(200, 50),
            thickness=5
        )
        self.objects["battle_area"] = battle_area

        # not visual
        player = Player(
            size = (30, 30),
            color = (255, 0, 0),
            position = (335, 185),
            position_limits = math.get_global_rect_inner_limits(self, battle_area) # эта функция не вписывается, из-за чего я её удалю позже
        )
        self.objects["player"] = player

        attack_moves.ball_shoot(self)

    def update(self):
        player_speed = 2.5
        player = self.objects["player"]
        keys = key.get_pressed()
        if keys[key.LEFT]:
            player.save_move(-player_speed,0) # а эту нужно доработать
        if keys[key.RIGHT]:
            player.save_move(player_speed,0)
        if keys[key.UP]:
            player.save_move(0,-player_speed)
        if keys[key.DOWN]:
            player.save_move(0,player_speed)

UndertaleGame(max_fps=60, width=700, height=400, caption="Undertale Remake")