import turtle

# Configurar pantalla
pantalla = turtle.Screen()
pantalla.title("Tortuga simulada con guiones y flecha final")

# Crear tortuga
t = turtle.Turtle()
t.hideturtle()      # No mostrar la tortuga real
t.penup()           # No dibujar líneas
t.goto(0, 0)        # Posición inicial centrada

# Configurar para moverse hacia abajo
pasos_abajo = 3
paso = 30           # Paso más grande para buena separación
t.setheading(270)   # Apuntar hacia abajo

for i in range(pasos_abajo):
    # Mover primero y luego dibujar (como en el primer reto)
    t.forward(paso)
    
    # Dibujar el símbolo en la nueva posición
    if i < pasos_abajo - 1:
        # Dibujar guion vertical
        t.write("|", align="center", font=("Arial", 16, "normal"))
    else:
        # Último paso: dibujar flecha hacia abajo
        t.write("↓", align="center", font=("Arial", 16, "normal"))

# Mantener ventana abierta
turtle.done()