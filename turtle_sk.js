import "https://skulpt.org/js/skulpt.min.js";
import "https://skulpt.org/js/skulpt-stdlib.js";

class Turtle {
    setup() {
        const canvas = document.createElement("div");
        canvas.id = "canvas";
        document.body.prepend(canvas);

        Sk.configure({
            __future: Sk.python3,
            retainglobals: true
        });
        
        (Sk.TurtleGraphics || (Sk.TurtleGraphics = {})).target = 'canvas';
        
        Sk.importMainWithBody("repl", false, "from turtle import *", true);
    }

    async execute(code){
        await Sk.misceval.asyncToPromise(function() {
            return Sk.importMainWithBody("repl", false, code, true);
        });
    }
}

window.turtle = new Turtle()