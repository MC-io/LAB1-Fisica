import math

# Ecuacion 1

def eq1():

    print("Que desea calcular?")
    print("1) Distancia")
    print("2) Velocidad")
    print("3) Tiempo")

    op = input()

    if op == "1":
        v = float(input("Ingrese la velocidad: "))
        delta_t = float(input("Ingrese el tiempo: "))

        delta_x = v * delta_t

        if delta_t < 0:
            print("Error: El valor de delta_t no puede ser negativo")
        else:
            print("La distancia es: " + str(delta_x))

    elif op == "2":
        delta_x = float(input("Ingrese la distancia: "))
        delta_t = float(input("Ingrese el tiempo: "))

        v = delta_x / delta_t

        if delta_t == 0:
            print("Error: El valor de delta_t no puede ser 0")
        elif delta_t < 0:
            print("Error: El valor de delta_t no puede ser negativo")
        else:
            print("La velocidad es: " + str(v))
    else:
        v = float(input("Ingrese la velocidad: "))
        delta_x = float(input("Ingrese la distancia: "))

        delta_t = delta_x / v

        if v == 0:
            print("Error: El valor de v no puede ser 0")
        else:
            print("El tiempo es: " + str(delta_t))

# Ecuacion 2

def eq2():
    print("Que desea calcular?")
    print("1) Distancia")
    print("2) Velocidad Inicial")
    print("3) Tiempo")
    print("4) Aceleracion")

    op = input()

    if op == "1":
        Vi = float(input("Ingrese la velocidad inicial: "))
        delta_t = float(input("Ingrese el tiempo: "))
        a = float(input("Ingrese la aceleracion: "))

        delta_x = Vi * delta_t + (a * (delta_t ** 2)) / 2

        if delta_t < 0:
            print("Error: El valor de delta_t no puede ser negativo")
        else:
            print("La distancia es: " + str(delta_x))
    
    elif op == "2":
        delta_x = float(input("Ingrese la distancial: "))
        delta_t = float(input("Ingrese el tiempo: "))
        a = float(input("Ingrese la aceleracion: "))

        Vi = (delta_x - (a * (delta_t ** 2)) / 2) / delta_t

        if delta_t == 0:
            print("Error: El valor de delta_t no puede ser 0")
        elif delta_t < 0:
            print("Error: El valor de delta_t no puede ser negativo")
        else:
            print("La velocidad inicial es: " + str(Vi))

    elif op == "3":
        delta_x = float(input("Ingrese la distancial: "))
        Vi = float(input("Ingrese la velocidad inicial: "))
        a = float(input("Ingrese la aceleracion: "))

        delta_t = (-2 * Vi + math.sqrt(4 * (Vi ** 2) + 8 * a * delta_x)) / (2 * a)

        if a == 0:
            print("Error: El valor de a no puede ser 0")
        else:
            print("El tiempo es: " + str(delta_t))

    elif op == "4":
        Vi = float(input("Ingrese la velocidad inicial: "))
        delta_t = float(input("Ingrese el tiempo: "))
        delta_x = float(input("Ingrese la distancia: "))

        a = (2 * delta_x - 2 * Vi * delta_t) / (delta_t ** 2) 


        if delta_t == 0:
            print("Error: El valor de delta_t no puede ser 0")
        elif delta_t < 0:
            print("Error: El valor de delta_t no puede ser negativo")
        else:
            print("La aceleracion es: " + str(a))        

# Ecuacion 3

def eq3():
    print("Que desea calcular?")
    print("1) Velocidad Final")
    print("2) Velocidad Inicial")
    print("3) Tiempo")
    print("4) Aceleracion")

    op = input()

    if op == "1":

        Vi = float(input("Ingrese la velocidad inicial: "))
        delta_t = float(input("Ingrese el tiempo: "))
        a = float(input("Ingrese la aceleracion: "))

        Vf = Vi * delta_t + a * delta_t

        if delta_t < 0:
            print("Error: El valor de delta_t no puede ser negativo")
        else:
            print("La velocidad final es: " + str(Vf))

    elif op == "2":

        Vf = float(input("Ingrese la velocidad final: "))
        delta_t = float(input("Ingrese el tiempo: "))
        a = float(input("Ingrese la aceleracion: "))

        Vi = (Vf - a * delta_t) / delta_t

        if delta_t == 0:
            print("Error: El valor de delta_t no puede ser 0")
        elif delta_t < 0:
            print("Error: El valor de delta_t no puede ser negativo")
        else:
            print("La velocidad inicial es: " + str(Vi))

    elif op == "3":
        Vi = float(input("Ingrese la velocidad inicial: "))
        Vf = float(input("Ingrese la velocidad final: "))
        a = float(input("Ingrese la aceleracion: "))

        delta_t = Vf / (Vi + a)

        if Vi + a == 0:
            print("Error: El valor de Vi + a no puede ser 0")
        else:
            print("El tiempo es: " + str(delta_t))

    elif op == "4":
        Vi = float(input("Ingrese la velocidad inicial: "))
        Vf = float(input("Ingrese la velocidad final: "))
        delta_t = float(input("Ingrese el tiempo: "))

        a = (Vf - Vi * delta_t) / delta_t

        if delta_t == 0:
            print("Error: El valor de delta_t no puede ser 0")
        elif delta_t < 0:
            print("Error: El valor de delta_t no puede ser negativo")
        else:
            print("La aceleracion es: " + str(a))

print("Elegir ecuacion a realizar:")
print("1) delta_x = v * delta_t")
print("2) delta_x = Vi * delta_t + (a * (delta_t ** 2)) / 2")
print("3) Vf = Vi * delta_t + a * delta_t")

ope = input()

if ope == "1":
    eq1()
elif ope == "2":
    eq2()
else:
    eq3()