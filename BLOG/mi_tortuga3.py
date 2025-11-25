import turtle

# Configurar pantalla
pantalla = turtle.Screen()
pantalla.title("4 Escalones: 5 derecha + 3 abajo")

# Crear tortuga
t = turtle.Turtle()
t.hideturtle()      # No mostrar la tortuga real
t.penup()           # No dibujar líneas
t.goto(-200, 150)   # Posición inicial

# Configuración
pasos_derecha = 5
pasos_abajo = 3
escalones = 4
paso = 30           # Distancia entre guiones

for escalon in range(escalones):
    # PASOS HACIA LA DERECHA (horizontal)
    for i in range(pasos_derecha):
        if i < pasos_derecha - 1:
            # Dibujar guion horizontal
            t.write("-", align="center", font=("Arial", 16, "normal"))
        else:
            # Último paso: dibujar flecha derecha
            t.write("→", align="center", font=("Arial", 16, "normal"))
        
        # Mover a la derecha
        t.forward(paso)
    
    # PASOS HACIA ABAJO (vertical)
    for i in range(pasos_abajo):
        # Mover hacia abajo primero
        t.sety(t.ycor() - paso)
        
        if i < pasos_abajo - 1:
            # Dibujar guion vertical
            t.write("|", align="center", font=("Arial", 16, "normal"))
        else:
            # Último paso: dibujar flecha abajo
            t.write("↓", align="center", font=("Arial", 16, "normal"))

# Mantener ventana abierta
turtle.done()