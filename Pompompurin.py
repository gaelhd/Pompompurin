import turtle as p

# Configuraciones iniciales
p.turtlesize(2)  # Tamaño de la turtle
p.bgcolor("white")
p.color("yellow")

# Ubicar la turtle en las coordenadas (x, y)
x = 10
y = 0
altura_circulo = 130  # Ajuste la altura del círculo
p.penup()  # Levanta el lápiz para mover la turtle sin dibujar
p.goto(x, y - altura_circulo)  # Ajusta la posición y para bajar la altura del círculo
p.pendown()  # Baja el lápiz para comenzar a dibujar

# Dibujar el círculo
p.begin_fill()
p.circle(200)
p.end_fill()

# Dibujar ojo izquierdo
separacion_ojos = 50  # Ajuste la separación entre los ojos
radio_ojos = 15  # Ajusta el radio de los ojos
p.penup()
p.goto(x - separacion_ojos, y + 30)
p.pendown()
p.color("black")
p.begin_fill()
p.circle(radio_ojos)
p.end_fill()

# Dibujar ojo derecho
p.penup()
p.goto(x + separacion_ojos, y + 30)
p.pendown()
p.begin_fill()
p.circle(radio_ojos)
p.end_fill()

# Ubicar la turtle para el triángulo entre los ojos y arriba de la nariz
x_triangulo = x - 10  # Ajuste adicional a la izquierda
y_triangulo = y + 50  # Ajusta la posición y para ubicar el triángulo entre los ojos y arriba de la nariz
p.penup()
p.goto(x_triangulo, y_triangulo)
p.pendown()

# Llamar a la función para dibujar el triángulo curveado con línea
def dibujar_triangulo_curveado_con_linea():
    p.speed(2)  # Establecer la velocidad de dibujo

    # Dibujar el triángulo curveado
    longitud_lado = 20
    curvatura = 60
    
    p.begin_fill()  # Iniciar el relleno
    p.forward(longitud_lado)
    p.right(180 - curvatura)
    p.forward(longitud_lado)
    p.right(180 - curvatura)
    p.forward(longitud_lado)
    p.end_fill()  # Finalizar el relleno
    
    # Agregar una línea hacia el negativo en la segunda esquina del triángulo
    p.right(-180)
    p.forward(longitud_lado)
    p.right(-330)  # Gira la tortuga 90 grados hacia la izquierda (hacia arriba en el eje y)
    p.forward(25)  # Dibuja una línea vertical de 30 unidades

# Llamar a la función para dibujar el triángulo curveado con línea
dibujar_triangulo_curveado_con_linea()

# Ocultar la turtle antes de dibujar la nariz
p.hideturtle()

# Dibujar nariz de perrito (medio círculo inclinado a 45 grados)
p.penup()
p.goto(x, y + 10)  # Ajusta la posición de la nariz
p.pendown()
p.color("black")        
p.setheading(-45)  # Establece la dirección de la turtle a -45 grados
p.circle(20, 180)  # Dibujar medio círculo
p.end_fill()

# Ocultar la turtle antes de dibujar la otra parte de la nariz
p.hideturtle()

# Dibujar la otra parte de la nariz (medio círculo inclinado a -45 grados)
p.penup()
p.goto(x, y + 10)  # Ajusta la posición de la otra parte de la nariz
p.pendown()
p.color("black")        
p.setheading(45)  # Establece la dirección de la turtle a 45 grados
p.circle(20, -180)  # Dibujar medio círculo en dirección opuesta
p.end_fill()

# Mover la turtle al extremo izquierdo del círculo antes de dibujar el óvalo
p.penup()
p.goto(x - 180, y )
p.pendown() 
p.setheading(-380)
p.speed(2)
p.circle(70, 160)  
p.left(-20)     
p.forward(20)
p.left(-50)     
p.forward(30)

# Ocultar la tortuga
p.hideturtle()


x = 190
y = 0  # Ajusta la posición inicial en el eje y

p.penup()
p.goto(x, y)  # Ajusta la posición inicial
p.pendown() 
p.setheading(-350)  # Cambia la orientación inicial a arriba
p.speed(2)
p.circle(70, -160)  

p.left(-170)     
p.forward(20)
p.left(-270)     
p.forward(30)

# Ocultar la tortuga
p.hideturtle()

p.penup()
p.goto(-117, 195)  # Nuevas coordenadas x e y
p.pendown()
p.left(45)  # Ajusta la orientación inicial del óvalo
p.left(140)  # Rota el óvalo en 45 grados
p.color("saddle brown")  # Puedes cambiar el color según tus preferencias
p.begin_fill()

# Dibuja el óvalo mediante rotaciones
for _ in range(2):  
    p.circle(180, 90)
    p.circle(20, 90)

p.end_fill()

# Coordenadas para ubicar el rectángulo
x = 100
y = 50

p.setheading(25)

p.penup()
p.goto(x - 117, y + 195)  # Ajusta las coordenadas para el centro del rectángulo
p.pendown()
p.color("black")
p.forward(20) 
p.right(90)
p.forward(25) 
p.left(180)
p.forward(25)  
p.left(90)
p.forward(20)    
p.left(90)
p.forward(25) 
p.hideturtle()


def write_love_phrase():
    p.penup()
    p.goto(0, -200)
    p.color("black")
    p.write("I love you ratita", align="center", font=("Arial", 16, "normal"))

p.color("red")
write_love_phrase()
p.hideturtle()
p.done()
# Mantener la ventana abierta
p.mainloop()


