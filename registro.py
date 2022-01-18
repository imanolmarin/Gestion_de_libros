class Libros:
    def __init__(self, titulo, revisiones, anio, idioma, rating, isbn):
        self.titulo = titulo
        self.revisiones = revisiones
        self.anio = anio
        self.idioma = idioma
        self.rating = rating
        self.isbn = isbn

    def __str__(self):
        return ' Titulo del libro: ' + str(self.titulo) + \
               " | Cantidad de revisiones : " + str(self.revisiones) + \
               " | Año de publicacion: " + str(self.anio) + \
               " | Codigo de idioma: " + str(self.idioma) + \
               " | Rating: " + str(self.rating) + \
               " | Codigo ISBN: " + str(self.isbn)




