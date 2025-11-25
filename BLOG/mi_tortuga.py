import turtle

# Configurar pantalla
pantalla = turtle.Screen()
pantalla.title("Tortuga simulada con guiones y flecha final")

# Crear tortuga
t = turtle.Turtle()
t.hideturtle()      # No mostrar la tortuga real
t.penup()           # No dibujar líneas
t.goto(-350, 0)     # Posición inicial

pasos_totales = 50
paso = 10           # avance en píxeles

for i in range(pasos_totales):
    
    if i < pasos_totales - 1:
        # Dibujar guion
        t.write("-", font=("Arial", 16, "normal"))
    else:
        # Último paso: dibujar flecha
        t.write("→", font=("Arial", 16, "normal"))
    
    # Mover a la derecha
    t.forward(paso)

# Mantener ventana abierta
turtle.done()

