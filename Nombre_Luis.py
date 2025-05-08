import turtle
import random
import colorsys

def random_rgb():
    return (random.random(), random.random(), random.random())


t = turtle.Turtle()
turtle.bgcolor("black") 
t.speed(0)
t.color("black")
h = 0

for i in range(360):
    c = colorsys.hsv_to_rgb(h, 1, 1)
    t.pencolor(c)
    t.forward(i)
    t.right(59)
    h += 1 / 360  
t.penup()
t.goto(-100, 60)  
t.pendown()


import turtle

# Configurar pantalla para usar colores RGB
turtle.colormode(255)
pantalla = turtle.Screen()
pantalla.bgcolor("black")  # Fondo negro

# Crear turtle
t = turtle.Turtle()
t.pensize(5)
t.speed(2)

# Función para escribir una letra en cierta posición y color
def escribir_letra(letra, x, y, color_rgb):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color_rgb)
    t.write(letra, font=("Algerian", 120, "bold"))

# Escribir cada letra con color blanco
blanco = (255, 255, 255)
escribir_letra("L", -200, 0, blanco)
escribir_letra("U", -120, 0, blanco)
escribir_letra("I", -40, 0, blanco)
escribir_letra("S", 40, 0, blanco)

t.hideturtle()
turtle.done()

