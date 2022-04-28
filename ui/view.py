# Interfaz por consola

# Encabezado APP
HEADER = """
╔═╗┌─┐┬─┐┬┌─┐┌─┐  ┌─┐┌┐┌┌┬┐  ╔╦╗┌─┐┬  ┬┬┌─┐┌─┐  ╔╦╗┬─┐┌─┐┌─┐┬┌─┌─┐┬─┐
╚═╗├┤ ├┬┘│├┤ └─┐  ├─┤│││ ││  ║║║│ │└┐┌┘│├┤ └─┐   ║ ├┬┘├─┤│  ├┴┐├┤ ├┬┘
╚═╝└─┘┴└─┴└─┘└─┘  ┴ ┴┘└┘─┴┘  ╩ ╩└─┘ └┘ ┴└─┘└─┘   ╩ ┴└─┴ ┴└─┘┴ ┴└─┘┴└─
"""

# Menu principal
MAIN_MENU = """

1 --> Hacer un registro nuevo
2 --> Mostrar los registros actuales
3 --> Actualizar registro existente
4 --> Eliminar un registro
5 --> Película con la menor duración
6 --> Película con la mayor duración
7 --> Duración promedio de las películas
8 --> Películas/series pendientes
9 --> Películas/series vistas
0 --> Salir

"""


# ***** CORE *****

def showHeader():
    """Mostrar el Encabezado de la App"""
    print(HEADER)


def mainMenu():
    """Mostra el menu principal y obtener
    la elección del usuario"""
    print(MAIN_MENU)
    user_choise = validateNumberInput(':: Ingrese una opción: ', '¡CARACTER INVÁLIDO!')
    return user_choise


# CREATE
def CreateRegisterForm():
    """Registar una película/serie"""
    showSectionHeader('Registrar Película/Serie')
    
    print("""
    A --> Registrar Película
    B --> Registrar Serie
    """)
    user_choise = input(':: Ingresa una opción: ').upper()
    if user_choise == 'A':
        title = input(':: Ingrese el título: ').capitalize()
        streaming_platform = input(':: Ingrese la plataforma: ')
        duration = int(input(':: Ingrese la duración (min): '))
        status = input(':: Ingresa el estado (Pendiente/vista): ').capitalize()
        return (0, {'title': title, 'streaming_platform': streaming_platform, 'duration': duration, 'status': status})

    elif user_choise == 'B':
        title = input(':: Ingrese el título: ').capitalize()
        streaming_platform = input(':: Ingrese la plataforma: ')
        season = int(input(':: Temporada: '))
        episode = int(input(':: Último episodio visto: '))
        status = input(':: Ingresa el estado (Pendiente/Finalizada/En curso): ').capitalize()
        return (1, {'title': title, 'streaming_platform': streaming_platform, 'season': season, 'episode': episode, 'status': status})
    else:
        print('Ingresaste una opción incorrecta!')


# READ
def readData(db):
    """Listar las películas/series guardadas"""
    showSectionHeader('Elementos guardados')

    # Mostrar películas
    showMovies(db)

    # Mostrar Series
    showSeries(db)


# UPDATE
def updateForm(db):
    showSectionHeader('Actualizar registro')
    print("""
    :: Quieres actualizar una película o una serie?
    A --> Película
    B --> Serie
    """)

    update_type = input('::Ingresa una opción: ').upper()

    if update_type == 'A':
        # Mostrar elementos
        showMovies(db)

        # Obtener índice del elemento a actualizar
        index = validateNumberInput(':: Ingresa el índice de la película a actualizar: ', 'Ingresa un índice!')

        # obtener información nueva
        print('-- Ingresa la información nueva --')
        title = input(':: Ingrese el título: ').capitalize()
        streaming_platform = input(':: Ingrese la plataforma: ')
        duration = int(input(':: Ingrese la duración (min): '))
        status = input(':: Ingresa el estado (Pendiente/Vista): ').capitalize()
        item_updated = {'title': title, 'streaming_platform': streaming_platform, 'duration': duration, 'status': status}

        # Retorna índice del elemento a actualizar, el imtem actualizado, 0 -> Actualizar película
        return (index, item_updated, 0)

    elif update_type == 'B':
        # Mostrar elementos
        showSeries(db)

        # Obtener índice del elemento a actualizar
        index = validateNumberInput(':: Ingresa el índice de la serie a actualizar: ', 'Ingresa un índice!')

        # Obtener información nueva
        print('-- Ingresa la información nueva --')
        title = input(':: Ingrese el título: ').capitalize()
        streaming_platform = input(':: Ingrese la plataforma: ')
        season = int(input(':: Temporada: '))
        episode = int(input(':: Último episodio visto: '))
        status = input(':: Ingresa el estado (Pendiente/Finalizada/En curso): ').capitalize()
        item_updated = {'title': title, 'streaming_platform': streaming_platform, 'season': season, 'episode': episode, 'status': status}

        # Retorna índice del elemento a actualizar, el imtem actualizado, 1 -> Actualizar serie
        return (index, item_updated, 1)

    else:
        print('Ingresaste una opción incorrecta!')



# DELETE
def deleteForm(db):
    showSectionHeader('Borrar Registro')
    print("""
    :: Qué quieres borrar?
    A --> Borrar película
    B --> Borrar Serie
    """)

    delele_type = input(':: Ingresa una opción: ').upper()

    if delele_type == 'A':
        showMovies(db)
        index = validateNumberInput(':: Ingresa el índice de la película a borrar: ', 'Ingresa un índice!')
        # Retorna índice del elemento a eliminar, 0 -> Borrar película
        return (index, 0)

    elif delele_type == 'B':
        showSeries(db)
        index = validateNumberInput(':: Ingresa el índice de la serie a borrar: ', 'Ingresa un índice!')
        # Retorna índice del elemento a eliminar, 1 -> Borrar serie
        return (index, 1)
    else:
        print('Ingresaste una opción incorrecta!')

    readData(db)
    index = validateNumberInput(':: Ingresa el índice:')


# ***** UTILIDADES *****

def validateNumberInput(label, errorReport='Este campo es obligatorio!'):
    """Validar un campo numérico"""
    numberInput = None
    while numberInput == None:
        try:
            numberInput = int(input(label))
        except:
            print(errorReport)
    return numberInput


def showSectionHeader(header):
    """Dar formato de Encabezado de sección"""
    print()
    print(''.join(['*'] * (len(header) + 4)))
    print(f'* {header.upper()} *')
    print(''.join(['*'] * (len(header) + 4)))


def showMovies(db):
    print('-- PELICULAS --')
    print('| INDICE | NOMBRE | PLATAFORMA | DURACIÓN MIN | ESTADO |')
    for index, movie in enumerate(db[0]):
        print(f'| {index} | {movie["title"]} | {movie["streaming_platform"]} | {movie["duration"]} | {movie["status"]} |')


def showSeries(db):
    print('-- SERIES --')
    print('| INDICE | NOMBRE | PLATAFORMA | TEMPORADA | EPISODIO | ESTADO |')
    for index, serie in enumerate(db[1]):
        print(f'| {index} | {serie["title"]} | {serie["streaming_platform"]} | {serie["season"]} | {serie["episode"]} | {serie["status"]} |')


def showSingleItem(item):
    print(f'|-> {item}')


def showMultipleItems(items):
    for item in items:
        print(f'|-> {item}')
