from PygameX import *

class FlappyBird(Game):

    background_color = color.LIGHT_BLUE

    def init(self):
        self.score = 0
        self.colons: list[str] = []
        self.in_pause = False
        self.bird_y_dir = 0

        for i in range(1, 5):
            upper_colon = Rect(
                color=color.GREEN,
                position=(500 + 200 * i, 0),
                size=(60, 120)
            )
            bottom_colon = Rect(
                color=color.GREEN,
                position=(500 + 200 * i, 280),
                size=(60, 120)
            )
            self.objects[f"upper_colon_{i}"] = upper_colon
            self.objects[f"bottom_colon_{i}"] = bottom_colon
            self.colons.append(f"upper_colon_{i}")
            self.colons.append(f"bottom_colon_{i}")

        bird = Circle(
            radius=25,
            color=color.YELLOW,
            position=(50,200)
        )
        self.objects["bird"] = bird

        score_text = TextDisplay(
            text=f"Score: {self.score}",
            size=70,
            position=(300, 30),
            color=(0,0,0)
        )
        self.objects["score_text"] = score_text

        defeat_text1 = TextDisplay(
            text=f"Defeat! Score: {self.score}",
            size=70,
            position=(300, 170),
            color=(0,0,0)
        )
        self.objects["defeat_text1"] = defeat_text1
        self.invisible_objects.append("defeat_text1")

        defeat_text2 = TextDisplay(
            text="Press SPACE to restart...",
            size=30,
            position=(300, 220),
            color=(0,0,0)
        )
        self.objects["defeat_text2"] = defeat_text2
        self.invisible_objects.append("defeat_text2")

    def update(self):
        if not self.in_pause:
            self.bird_y_dir += 0.18

            if key.get_pressed()[key.SPACE]:
                self.bird_y_dir = -3.75

            bird = self.objects["bird"]
            bird.position = (bird.position[0], bird.position[1] + self.bird_y_dir)

            if bird.position[1] < 25 or bird.position[1] > 375:
                self.defeat()

            for colon_id in self.colons:
                colon = self.objects[colon_id]
                colon.position = (colon.position[0] - 2.4, colon.position[1])
                if colon.position[0] < -100:
                    colon.position = (700, colon.position[1])
                    if colon_id.startswith("upper"):
                        self.score += 1
                        self.objects["score_text"].set_text(f"Score: {self.score}")

                if 5 < colon.position[0] < 70:
                    colonX = colon.position[0]
                    colonY = colon.position[1]
                    colonW = colon.size[0]
                    colonH = colon.size[1]

                    bird = self.objects["bird"]
                    birdX = bird.position[0] - bird.radius + 5
                    birdY = bird.position[1] - bird.radius + 5
                    birdW = bird.radius * 2 - 5
                    birdH = bird.radius * 2 - 5

                    if (colonX < birdX + birdW and
                        colonX + colonW > birdX and
                        colonY < birdY + birdH and
                        colonY + colonH > birdY):
                            self.defeat()

        else:
            if key.get_pressed()[key.SPACE]:
                self.restart()

    def update_colons(self):
        self.colons.clear()
        for i in range(1, 5):
            upper_colon = Rect(
                color=color.GREEN,
                position=(500 + 200 * i, 0),
                size=(60, 120)
            )
            bottom_colon = Rect(
                color=color.GREEN,
                position=(500 + 200 * i, 280),
                size=(60, 120)
            )
            self.objects[f"upper_colon_{i}"] = upper_colon
            self.objects[f"bottom_colon_{i}"] = bottom_colon
            self.colons.append(f"upper_colon_{i}")
            self.colons.append(f"bottom_colon_{i}")

    def defeat(self):
        self.in_pause = True
        self.invisible_objects.clear()
        self.invisible_objects.append("score_text")

        self.objects["defeat_text1"].set_text(f"Defeat! Score: {self.score}")

        self.score = 0

    def restart(self):
        self.in_pause = False
        self.invisible_objects.clear()
        self.invisible_objects.append("defeat_text1")
        self.invisible_objects.append("defeat_text2")
        self.objects["bird"].position = (50,200)
        self.bird_y_dir = 0
        self.objects["score_text"].set_text(f"Score: {self.score}")

        self.update_colons()

FlappyBird(width=600, height=400, max_fps=60)