from pico2d import load_image


class Grass:
    def __init__(self, width, height):
        self.image = load_image('grass.png')
        self.x=width
        self.y=height

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        pass
