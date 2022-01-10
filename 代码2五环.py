Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> turtle.showturtle()
>>> turtle.color("blue")
>>> turtle.circle(50)
>>> turtle.penup()
>>> turtle.goto(120,0)
>>> turtle.color("black")
>>> turtle.circle(50)
>>> turtle.pendown()
>>> turtle.circle(50)
>>> turtle.penup()
>>> turtle.goto(240,)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    turtle.goto(240,)
  File "<string>", line 8, in goto
  File "C:\Users\董祥兆\AppData\Local\Programs\Python\Python38\lib\turtle.py", line 1774, in goto
    self._goto(Vec2D(*x))
TypeError: type object argument after * must be an iterable, not int
>>> turtle.goto(240)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    turtle.goto(240)
  File "<string>", line 8, in goto
  File "C:\Users\董祥兆\AppData\Local\Programs\Python\Python38\lib\turtle.py", line 1774, in goto
    self._goto(Vec2D(*x))
TypeError: type object argument after * must be an iterable, not int
>>> turtle.goto(240,0)
>>> turtle.color("red")
>>> turtle.pendown()
>>> turtle.circle(50)
>>> turtle.penup()
>>> turtle.goto(60,-50)
>>> turtle.color("yellow")
>>> turtle.circle(50)
>>> turtle.pendown()
>>> turtle.circle()
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    turtle.circle()
TypeError: circle() missing 1 required positional argument: 'radius'
>>> turtle.circle(50)
>>> turtle.penup()
>>> turtle.goto(180,-50)
>>> turtle.pendown()
>>> turtle.color("green")
>>> turtle.circle(50)
>>> 