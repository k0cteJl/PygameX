from PygameX import *

from time import localtime, sleep

# Функция мусор, как и pgX, потому что его сложно разделять на разные скрипты.
def shoot(game: Game):
    ball_id = f"ball:{localtime().tm_hour}{localtime().tm_min}{localtime().tm_sec}"
    sleep(2)