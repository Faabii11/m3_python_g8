#paso 1: capturar los datos (string), y conversion 
#radio = float(input("Ingrese el radio en kilometros")) * 1000

radio_kilometros = input("Ingrese el radio en kilometros")
radio_kilometros = float(radio_kilometros)
radio_metros = radio_kilometros * 1000

constante_gravitacional = input("Ingrese la constante de gravedad del planeta en [mt/s]")
constante_gravitacional = float(constante_gravitacional)#conversion de string a float

#paso 2: resolver formula velocidad_escape =  raiz_cuadrada(2 * constante_gravitacional * radio_metros)
multiplacion = 2 * constante_gravitacional * radio_metros
velocidad_escape = sqrt(multiplacion)

#paso 3: mostrar el resultado final
print(f"La velocidad de Escape es {round(velocidad_escape,1)} [m/s]")