numeroSecreto = 777
count = 0

print(
"""
+==================================+
| Bienvenido a mi juego, muggle!   |
| Introduce un número entero       |
| y adivina qué número he          |
| elegido para ti.                 |
| Entonces,                        |
| ¿Cuál es el número secreto?      |
+==================================+
""")

entrada = int(input('Ingrese un numero: '))

while entrada != numeroSecreto:
    if entrada != numeroSecreto:
        print('¡Ja, ja! ¡Estás atrapado en mi ciclo!')
        entrada = int(input('Ingrese un numero: '))
        count += 1

print('¡Bien hecho, muggle! Eres libre ahora')