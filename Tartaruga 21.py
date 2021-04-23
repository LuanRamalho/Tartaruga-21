import turtle

FONT_SIZE = 32


class Tile(turtle.Turtle):
    def __init__(self):
        super().__init__(shape="square")
        self.penup()

    def show_value(self, val):
        self.write(val, font=("Arial", FONT_SIZE, "bold"), align="center")


screen = turtle.Screen()
vals = [5, 7, 8, 2, 6 , 10]
for i in range(len(vals)):
    tile = Tile()
    tile_size = (FONT_SIZE / 20)
    tile.shapesize(tile_size)
    tile.fillcolor("red" if i % 2 == 0 else "blue")
    tile.setx(i * FONT_SIZE)
    tile.show_value(vals[i])
turtle.done()