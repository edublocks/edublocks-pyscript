from pyscript import window

window.turtle.setup()

turtles = []
screens = []

def get_color(args):
    if len(args) == 3:
        return "#%02x%02x%02x" % (args[0], args[1], args[2])
    else:
        return args[0]

class Turtle:
    def __init__(self):
        length = len(turtles)
        if length == 1:
            self.reference = turtles[0]
            turtles.append(f"turtle{length+1}")
        else:
            self.reference = f"turtle{length+1}"
            turtles.append(self.reference)
            window.turtle.execute(f'{self.reference} = Turtle()')

    async def forward(self, distance):
        await window.turtle.execute(f'{self.reference}.forward({distance})')

    async def left(self, angle):
        await window.turtle.execute(f'{self.reference}.left({angle})')

    async def backward(self, distance):
        await window.turtle.execute(f'{self.reference}.backward({distance})')

    async def right(self, angle):
        await window.turtle.execute(f'{self.reference}.right({angle})')

    async def goto(self, x, y):
        await window.turtle.execute(f'{self.reference}.goto({x}, {y})')

    async def circle(self, radius):
        await window.turtle.execute(f'{self.reference}.circle({radius})')

    async def width(self, width):
        await window.turtle.execute(f'{self.reference}.width({width})')

    async def color(self, *args):        
        await window.turtle.execute(f'{self.reference}.color("{get_color(args)}")')

    async def pencolor(self, *args):
        await window.turtle.execute(f'{self.reference}.pencolor("{get_color(args)}")')

    async def fillcolor(self, *args):
        await window.turtle.execute(f'{self.reference}.fillcolor("{get_color(args)}")')

    async def begin_fill(self):
        await window.turtle.execute(f'{self.reference}.begin_fill()')

    async def end_fill(self):
        await window.turtle.execute(f'{self.reference}.end_fill()')

    async def penup(self):
        await window.turtle.execute(f'{self.reference}.penup()')

    async def pendown(self):
        await window.turtle.execute(f'{self.reference}.pendown()')

    async def speed(self, speed):
        await window.turtle.execute(f'{self.reference}.speed({speed})')

    async def shape(self, shape):
        await window.turtle.execute(f'{self.reference}.shape("{shape}")')

    async def write(self, text, move=False, align="left", font=("Arial", 8, "normal")):
        await window.turtle.execute(f'{self.reference}.write("{text}", move={move}, align="{align}", font=("{font[0]}", {font[1]}, "{font[2]}"))')

class Screen:
    def __init__(self):
        length = len(screens)
        if length == 1:
            self.reference = screens[0]
            turtles.append(f"screen{length+1}")
        else:
            self.reference = f"screen{length+1}"
            screens.append(self.reference)
            window.turtle.execute(f'{self.reference} = Screen()')

        
    async def bgcolor(self, *args):
        await window.turtle.execute(f'{self.reference}.bgcolor("{get_color(args)}")')
        
    async def setup(self, w, h):
        await window.turtle.execute(f'{self.reference}.setup({w}, {h})')

_classes = [
    "Turtle",
    "Screen"
]

_turtle_functions = [
    "forward",
    "left",
    "backward",
    "right",
    "goto",
    "circle",
    "width",
    "color",
    "pencolor",
    "fillcolor",
    "begin_fill",
    "end_fill",
    "penup",
    "pendown",
    "speed",
    "shape",
    "write"
]

_screen_functions = [
    "bgcolor",
    "setup"
]

default_turtle = Turtle()
default_screen = Screen()
__all__ = _classes + _turtle_functions + _screen_functions

def _make_global_funcs(functions, cls):
    for func in functions:
        globals()[func] = getattr(cls, func)

_make_global_funcs(_turtle_functions, default_turtle)
_make_global_funcs(_screen_functions, default_screen)