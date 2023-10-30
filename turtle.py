from pyscript import document, window

class Turtle:
    def __init__(self):
        canvas = document.createElement("canvas")
        canvas.id = "canvas"
        document.body.appendChild(canvas)
        self.turtle = window.getTurtle("canvas")

    async def forward(self, distance):
        await self.turtle.forward(distance)

    async def backward(self, distance):
        await self.turtle.backward(distance)

    async def left(self, angle):
        await self.turtle.left(angle)

    async def right(self, angle):
        await self.turtle.right(angle)

    async def goto(self, x, y):
        await self.turtle.goto(x, y)

    async def circle(self, radius):
        await self.turtle.circle(radius, 360)

    async def width(self, width):
        self.turtle.width(width)

    async def color(self, *args):
        self.turtle.color(*args)

    async def pencolor(self, *args):
        self.turtle.color(*args)

    async def fillcolor(self, *args):
        self.turtle.fillcolor(*args)

    async def begin_fill(self):
        self.turtle.begin_fill()

    async def end_fill(self):
        self.turtle.end_fill()

    async def penup(self):
        self.turtle.penup()

    async def pendown(self):
        self.turtle.pendown()

    async def speed(self, speed):
        self.turtle.speed(speed)

    async def shape(self, shape):
        self.turtle.shape(shape)

class Screen:
    def __init__(self):
        self.turtle = window.getTurtle("canvas")
        
    def bgcolor(self, *args):
        self.turtle.bgcolor(*args)