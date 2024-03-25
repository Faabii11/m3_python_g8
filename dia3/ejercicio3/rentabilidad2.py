#Inputs
precio_suscripcion = int(input("Ingrese el Precio de Suscripción"))
usuarios_normal = int(input("Ingrese el Número de Usuarios Normales"))
usuarios_premium = int(input("Ingrese el Número de Usuarios Premium"))
gastos_totales = int(input("Ingrese los Gastos Totales"))


#Cálculo utilidades
utilidades = precio_suscripcion * usuarios_normal + (1.5 * precio_suscripcion) * usuarios_premium - gastos_totales

# Output
print(f'Las utilidades son $ {utilidades}.-')
