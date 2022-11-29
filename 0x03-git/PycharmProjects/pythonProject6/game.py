from ursina import *

app = Ursina()

for z in range(10):
    for x in range(10):
        Entity(
            model="cube", color=color.dark_gray, collider="box", igmore=True,
            position = (x, 0, z),
            parent=scene,
            origin_y = 0.5,
            text = "White_cube"
        )

class TextureBox(Button):
    def __init__(self, position=(5,2,5)):
        super().__int__(
            parent= scene,
            position=position,
            model="cube",
            origin_y=0.5,
            texture = "texture.jpg",
            color= color.color(0,0,1)
)
        self.texture_choice= 0
        self.texture = ["texture.jpg"]
    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                self.texture_choice += 1
                self.texture_choice %= len[self.textures]
                self.texture = self.texture[self.texture_choice]

app.run()