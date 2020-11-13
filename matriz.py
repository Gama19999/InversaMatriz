def autores():
    print()
    print("Programa hecho por Vergara Lorenzo Santiago Alonso")
    print("Rios Serrano Asis Gamaliel y")
    print("Calderon Romero Alberto Arphaxad,")


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

    def signos(self):
        cadena = ""
        for i in range(self.filas):
            cadena += "["
            for j in range(self.columnas):
                if (i + j + 2) % 2 == 0:
                    cadena += '+ ' 
                else:
                    cadena += '- '
            cadena += "]\n"
        return cadena

    def possigno(self):
        posf = int(input("Posicion fila ")) - 1
        posc = int(input("Posicion columna ")) - 1
        if (posf + posc % 2) == 0:
            return "+"
        else:
            return "-"

autores()
tamaño = int(input("Tamaño de la matriz: "))
a = Matriz(tamaño, tamaño)
a.rellenarMatrizEspecifico(5)
print(a)
print(a.signos())
print(a.possigno())