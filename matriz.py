class Matriz:
    def __init__(self, filas, columnas, valor=0):
        self.filas = filas
        self.columnas = columnas
        self.matriz = [[]]
        for fila in range(filas):
            for _ in range(columnas):
                self.matriz[fila].append(valor)
            self.matriz.append([])

    def __str__(self):
        cadena = ''
        for fila in range(self.filas):
            cadena += str(self.matriz[fila]) + '\n'
        return cadena