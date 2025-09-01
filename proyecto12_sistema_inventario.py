#Gestión de inventario

inventario = [{'nombre': 'camisa', 'precio': 30, 'cantidad': 20}, {'nombre': 'gorro', 'precio': 30, 'cantidad': 20}, {'nombre': 'chaqueta', 'precio': 30, 'cantidad': 20}]

def inicio():
    while True:
        print(f'========== Pinun Logistics ==========')
        print('''Bienvenido al sistema de inventario:
    1 - Ver Inventario
    2 - Añadir Productos
    3 - Salir''')
        eleccion_menu_inicio = int(input('Indique una opción: '))
        if eleccion_menu_inicio == 1:
            ver_inventario()
        elif eleccion_menu_inicio == 2:
            anadir_producto()
        elif eleccion_menu_inicio == 3:
            print('Apagando el sistema...')
            exit()
        else:
            print('Opción invalida, vuelva a intentarlo')

def ver_inventario():
    while True:
        print(f'\n========== Pinun Logistics ==========')
        print('1 - Buscador por id')
        print('2 - Ver todo el inventario')
        print('3 - Volver')
        eleccion = int(input('Indique una opción: '))
        if eleccion == 1:
            id_buscado = int(input('Ingresa el ID del producto a buscar: '))
            if 0 <= id_buscado < len(inventario):
                print(f'ID: {id_buscado}')
                print(f'\t Nombre: {inventario[id_buscado].get('nombre')}')
                print(f'\t Precio: {inventario[id_buscado].get('precio')}')
                print(f'\t Cantidad: {inventario[id_buscado].get('cantidad')}')
        elif eleccion == 2:
            print('\n--Inventario--')
            for contador, producto in enumerate(inventario):
                print(f'ID: {contador}')
                print(f'\t Nombre: {inventario[contador].get('nombre')}')
                print(f'\t Precio: {inventario[contador].get('precio')}')
                print(f'\t Cantidad: {inventario[contador].get('cantidad')}')
                print('---------------------------')
        elif eleccion == 3:
            print('Volviendo al menu de inicio...\n')
            inicio()
        else:
            print('Opción invalida, vuelva a intentarlo')

def anadir_producto():
    print(f'\n========== Pinun Logistics ==========')
    num_productos = int(input('Número de productos para añadir: '))
    while num_productos > 0:
        nombre = input('Nombre: ')
        precio = float(input('Precio: '))
        cantidad = int(input('Cantidad: '))
        inventario.append({'nombre': nombre, 'precio': precio, 'cantidad': cantidad})
        print('---------------------------')
        num_productos -= 1
    print('\nVolviendo al menu principal...\n')
    inicio()

inicio()