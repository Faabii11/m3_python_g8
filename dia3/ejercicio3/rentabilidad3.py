#datos
precio_suscripcion = float(input('Ingrese el Precio de Suscripción:\n>'))
numero_usuarios = float(input('Ingrese el Número de Usuarios:\n>'))
gastos_totales = int(input('Ingrese los Gastos Totales:\n>'))

#advertir que u_anterior debe ser distinto de cero
u_anterior = float(input('Ingrese las utilidades anteriores. Este valor debe ser distinto de 0:\n>'))

#Cálculo utilidades
utilidades_actuales = precio * usuarios - gastos
#Razón
ratio = utilidades_actuales / u_anterior

# imprimiendo
print(f'Las utilidades son: {utilidades_actuales}' )
print(f'La razón de utilidades es de un: {ratio:.2f}%')