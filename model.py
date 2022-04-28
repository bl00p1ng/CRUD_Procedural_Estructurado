# Modelo de la DB


def load():
    """Inicializar datos"""
    db = [
        # PELICULAS
        [
            {
                'title': 'DeadPool',
                'streaming_platform': 'Netflix',
                'duration': 180,
                'status': 'Vista'
            },
            {
                'title': 'Spiderman No Way Home',
                'streaming_platform': 'Disney+',
                'duration': 136,
                'status': 'Vista'
            },
            {
                'title': 'Thor Love and Thunder',
                'streaming_platform': 'Disney+',
                'duration': 150,
                'status': 'Pendiente'
            }
        ],
        # SERIES
        [
            {
                'title': 'Rick y Morty',
                'streaming_platform': 'HBO Max',
                'season': 5,
                'episode': 10,
                'status': 'En curso'
            },
            {
                'title': 'Breaking Bad',
                'streaming_platform': 'Netflix',
                'season': 5,
                'episode': 4,
                'status': 'En curso'
            },
            {
                'title': 'Bojack Horseman',
                'streaming_platform': 'Netflix',
                'season': 6,
                'episode': 16,
                'status': 'Finalizada'
            }
        ]
    ]
    return db


# CREATE
def create(data_type, item, db):
    # Cargar datos de películas
    if data_type == 0:
        db[0].append(item)
    else:
        db[1].append(item)


def update(index, item_updated, update_type, db):
    if update_type == 0:
        db[0][index] = item_updated
    else:
        db[1][index] = item_updated


# DELETE
def delete(index, delete_type, db):
    # Borrar película
    if delete_type == 0:
        db[0].pop(index)
    # Borrar serie
    else:
        db[1].pop(index)

# Película con menor duración
def findShortestMovie(db):
    shortest_movie = db[0][0]

    for i in range(len(db[0]) - 1):
        if shortest_movie['duration'] > db[0][i + 1]['duration']:
            shortest_movie = db[0][i + 1]

    return shortest_movie


# Película con la mayor duración
def findLongestMovie(db):
    longest_movie = db[0][0]

    for i in range(len(db[0]) - 1):
        if longest_movie['duration'] < db[0][i + 1]['duration']:
            longest_movie = db[0][i + 1]

    return longest_movie


# Calcular duración promedio
def mean_duration(db):
    durations = 0  # Almacena la suma de las duraciones
    
    for movie in db[0]:
        durations += movie['duration']

    return round(durations / len(db[0]), 2)


# Buscar Películas/series pendientes
def findUnfinished(db):
    unfinished_items = []  # Coleccionar elementos pendientes
    
    for section in db:
        for item in section:
            if item['status'] == 'Pendiente':
                unfinished_items.append(item)

    return unfinished_items


# Buscar Películas/series vistas
def findFinished(db):
    finished_items = []  # Coleccionar elementos vistos
    
    for section in db:
        for item in section:
            if item['status'] == 'Vista' or item['status'] == 'Finalizada':
                finished_items.append(item)
    
    return finished_items
