def autores():
    print("Programa hecho por Calderon Romero Alberto Arphaxad,")
    print("Rios Serrano Asis Gamaliel y")
    print("Vergara Lorenzo Santiago Alonso")

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

    def rellenarMatrizDados(self):
        for i in range(self.filas):
            for j in range(self.columnas):
                nuevonum = int(input(f"Numero a ingresar en la posicion {i}, {j}: "))
                self.matriz[i][j] = nuevonum

    def rellenarMatrizEspecifico(self, num):
        for i in range(self.filas):
            for j in range(self.columnas):
                self.matriz[i][j] = num

autores()
a = Matriz(3, 3)
a.rellenarMatrizDados()
print(a)
