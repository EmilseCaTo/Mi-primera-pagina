# Tarea 2 – Ejercicios Unidad 1  
## Pensamiento Algorítmico – IUDigital

<p align="justify">
En esta entrada presento las soluciones correspondientes a los ejercicios de la Unidad 1, donde se trabaja el pensamiento algorítmico básico mediante el uso de instrucciones, simulación y programación en Python. Los retos se resolvieron aplicando conceptos como entrada de datos, ciclos, funciones y representaciones simples del movimiento.
</p> 

---

# Reto 1 – Simular comportamiento de la tortuga

<p align="justify">
En este ejercicio se debe simular el movimiento hacia adelante de una tortuga utilizando únicamente instrucciones de impresión <code>print()</code> y lectura de datos con <code>input()</code>. El objetivo es representar el movimiento con símbolos en pantalla.
</p>

### Mi solución en Python 

```python 

# Reto 1: Tortuga avanzando con print e input

pasos = int(input("¿Cuántos pasos avanza la tortuga? "))

print("Movimiento:")
print("-" * pasos + ">")   # Representa el movimiento hacia adelante
```

---

 # Reto 2 - Tortuga bajando

<p align="justify"> El objetivo es simular el movimiento descendente de la tortuga. Para lograrlo se imprime una línea vertical por cada paso hacia abajo, finalizando con una flecha que indica dirección. </p>

### ✔ Mi solución en Python 

```python 

# Reto 2: Tortuga bajando

pasos = int(input("¿Cuántos pasos baja la tortuga? "))

print("Tortuga bajando:")
for i in range(pasos):
    print("  |")
print("  v")
```
---

# Reto 3 – Giros y movimientos

<p align="justify"> En este reto se integra un giro a la derecha y se continúa el trazo horizontal. Se busca representar un movimiento combinado simulando un cambio de orientación. </p>

### ✔ Mi solución en Python
```python
# Reto 3: Giro y trazo horizontal

horizontal = int(input("¿Cuántos pasos avanza horizontalmente? "))
vertical = int(input("¿Cuántos pasos baja la tortuga? "))

# Movimiento horizontal
print("-" * horizontal + ">")

# Giro hacia abajo
for i in range(vertical):
    print(" " * horizontal + "|")

print(" " * horizontal + "v")
```
---

# Reto 4 – Movimientos usando funciones

<p align="justify"> En este último ejercicio se pide modular el programa mediante el uso de funciones. La idea es que los movimientos hacia adelante y hacia abajo sean reutilizables, mejorando la organización y legibilidad del código. </p>

### ✔ Mi solución en Python
```python
# Reto 4: Movimientos usando funciones

def adelante(n):
    print("-" * n + ">")

def abajo(n, offset=0):
    for i in range(n):
        print(" " * offset + "|")
    print(" " * offset + "v")

# Solicitar datos
h = int(input("¿Cuántos pasos avanza la tortuga? "))
v = int(input("¿Cuántos pasos baja luego de girar? "))

# Ejecutar movimientos
adelante(h)
abajo(v, offset=h)
```
---

## Reflexión sobre lo aprendido
<p align="justify"> Resolver estos retos permitió fortalecer la comprensión del uso de variables, ciclos, entrada de datos y funciones en Python. Además, el uso de representaciones mediante caracteres ayuda a visualizar el flujo de control y la lógica detrás de cada algoritmo. Estas actividades son fundamentales para el desarrollo de habilidades de pensamiento algorítmico. </p>




