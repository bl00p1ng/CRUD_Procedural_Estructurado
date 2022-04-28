import ui.view as ui
import model as md
import sys


# Precargar datos
db = None
db = md.load()
if db == None:  #Validar que la carga sea exitosa
    print('Error cargando tareas por defecto!')
    sys.exit(1) #Reportar error


# Iniciar App
def main():
    mainloop = True
    while mainloop:
        # Mostar encabezado de la App
        ui.showHeader()

        # Obtener la opción del usuario
        userOption = ui.mainMenu()

        # CREATE
        if userOption == 1:
            # Obtener la data del usuario
            data_type, data_from_user = ui.CreateRegisterForm()
            # Cargar datos en la DB
            md.create(data_type, data_from_user, db)

        # READ
        elif userOption == 2:
            ui.readData(db)

        # UPDATE
        elif userOption == 3:
            index, item_updated, update_type = ui.updateForm(db)
            md.update(index, item_updated, update_type, db)

        # DELETE
        elif userOption == 4:
            # Obtener elemento a eliminar
            item_to_delete, delete_type = ui.deleteForm(db)
            # Eliminar elemento
            md.delete(item_to_delete, delete_type, db)

        # Película con menor duración
        elif userOption == 5:
            # Encontrar la película con menor duración
            movie = md.findShortestMovie(db)
            # Mostrar la película encontrada
            ui.showSingleItem(movie)

        # Película con la mayor duración
        elif userOption == 6:
            # Encontrar la película con mayor duración
            movie = md.findLongestMovie(db)
            # Mostrar la película encontrada
            ui.showSingleItem(movie)

        # Duración promedio de las películas
        elif userOption == 7:
            # Calcular duración promedio
            mean = md.mean_duration(db)
            # Mostrar duración
            ui.showSingleItem(mean)

        # Películas/series pendientes
        elif userOption == 8:
            # Buscar elementos pendientes
            unfinished_items = md.findUnfinished(db)
            # Mostrar elementos encontrados
            ui.showMultipleItems(unfinished_items)

        # Películas/series vistas
        elif userOption == 9:
            # Buscar elementos finalizados
            finished_items = md.findFinished(db)
            # Mostrar elementos encontrados
            ui.showMultipleItems(finished_items)

        # EXIT
        elif userOption == 0:
            mainloop = False
            sys.exit(1) #Reportar error


