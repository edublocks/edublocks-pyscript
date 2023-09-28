import js

class Turtle:
    def __init__(self):
        canvas = js.document.createElement("canvas")
        canvas.id = "canvas"
        js.document.body.appendChild(canvas)
        self.turtle = js.getTurtle("canvas")

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

    def width(self, width):
        self.turtle.width(width)

    def color(self, *args):
        self.turtle.color(*args)

    def pencolor(self, *args):
        self.turtle.color(*args)

    def fillcolor(self, *args):
        self.turtle.fillcolor(*args)

    def begin_fill(self):
        self.turtle.begin_fill()

    def end_fill(self):
        self.turtle.end_fill()

    def penup(self):
        self.turtle.penup()

    def pendown(self):
        self.turtle.pendown()

    def speed(self, speed):
        self.turtle.speed(speed)

class Screen:
    def __init__(self):
        self.turtle = js.getTurtle("canvas")
        
    def bgcolor(self, *args):
        self.turtle.bgcolor(*args)