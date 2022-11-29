import random

playerhp = 260
enemyatkl = 60
enemyatkh = 80

while playerhp > 0:
    dmg: int = random.randrange(enemyatkl, enemyatkh)
    playerhp = playerhp - dmg

    print("enemy strikes for," dmg, "point of damagr. current Hp is", playerhp)