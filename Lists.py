#Lists

colores = ['rojo', 'verde', 'Azul']

print(colores)

colores_copy = colores # dont creeate a new list, make reference to same one

print(colores_copy)

colores[0] = 'purple'

print(colores_copy)


for color in colores:
	print(color)

print()

if 'purple' in colores_copy:
	print('color in the list')
