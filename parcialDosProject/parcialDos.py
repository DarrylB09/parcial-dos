# Entradas del usuario
salario_base = int(input("Salario base mensual $: "))
cargo = input("Cargo empleado : ")
desempeño = input("Nivel de desempeño: ")


# Función para calcular la bonificación
def calcular_bonificacion(salario_base, cargo, desempeño):
    cargo = cargo.lower()
    desempeño = desempeño .lower()

    # Porcentaje de bonificación segun el cargo y el desempeño
    if cargo == "directivo":
        if desempeño == "alto":
            porcentaje_bonificacion = 0.20
        elif desempeño == "medio":
            porcentaje_bonificacion = 0.10
        else:
            porcentaje_bonificacion = 0.0
    elif cargo == "operativo":
        if desempeño == "alto":
            porcentaje_bonificacion = 0.15
        elif desempeño == "medio":
            porcentaje_bonificacion = 0.05
        else:
            porcentaje_bonificacion = 0.0
    else:
        porcentaje_bonificacion = 0.0


    # Calcular la bonificación y el total
    bonificacion = round(salario_base * porcentaje_bonificacion)
    total_a_recibir = salario_base + bonificacion

    return bonificacion, total_a_recibir


# Función para generar el mensaje de salida
def generar_resumen(cargo, desempeño, salario_base, bonificacion, total_a_recibir):
    return (f"-----Resumen del Pago-----\n"
            f"Cargo: {cargo.capitalize()}\n"
            f"Nivel de Desempeño: {desempeño.capitalize()}\n"
            f"Salario Base: ${salario_base}\n"
            f"Bonificación: ${bonificacion}\n"
            f"Total a Recibir: ${total_a_recibir}\n"
            f"------------------------------------\n")


# Función para validar los datos y mostrar el resumen
def validar_datos(salario_base, cargo, desempeño):
    # Calcular bonificación y total
    bonificacion, total_a_recibir = calcular_bonificacion(salario_base, cargo, desempeño)
    # Generar y mostrar el resumen
    resumen = generar_resumen(cargo, desempeño, salario_base, bonificacion, total_a_recibir)
    print(resumen)



# Validar y mostrar los resultados
validar_datos(salario_base, cargo, desempeño)































