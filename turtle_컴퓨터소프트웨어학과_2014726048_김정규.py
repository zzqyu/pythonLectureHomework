Python 2.7.7 |Anaconda 2.0.1 (64-bit)| (default, Jun 11 2014, 10:40:02) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
==== No Subprocess ====
>>> import turtle

>>> import sys

>>> def modify(n):
    rules={'X':'F-[[X]+X]+F[+FX]-X','F':'FF'}
    start='X'
    s=start

    for k in range(n):
        s=''.join([rules.get(v,v) for v in s])

    return s

>>> def FractalPlant(s):
    stack = []
    for cmd in s:
        if cmd=='F':
            turtle.forward(2)
        elif cmd=='-':
            turtle.left(25)
        elif cmd=='+':
            turtle.right(25)
        elif cmd=='X':
            pass
        elif cmd=='[':
            stack.append((turtle.position(), turtle.heading()))
        elif cmd==']':
            position, heading = stack.pop()
            turtle.up()
            turtle.setposition(position)
            turtle.setheading(heading)
            turtle.down()

            
>>> def setup():
    turtle.hideturtle()
    turtle.tracer(False)
    turtle.left(90)
    turtle.up()
    turtle.goto(0,-250)
    turtle.down()

    
>>> setup()
>>> FractalPlant(modify(6))
>>> 
