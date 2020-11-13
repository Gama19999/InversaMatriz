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
        if ((posf + posc) % 2) == 0:
            return "+"
        else:
            return "-"

    def obtenerDeterminante(self):
        acumSumas1 = 0
        acumSumas2 = 0
        auxIterador = 0
        if tamaño == 2:
            determinante = (self.matriz[0][0] * self.matriz[1][1]) - (self.matriz[1][0] * self.matriz[0][1])
            print(f"El determinante de la matriz es {determinante}")
        elif tamaño == 3:
            self.matriz.append(self.matriz[0])
            self.matriz.append(self.matriz[1])
            for j in range(3):
                acumMulti1 = 1
                for i in range(j, j+3):
                    acumMulti1 *= self.matriz[i][j]
                acumSumas1 += acumMulti1

            for k in range(2,0,-1):
                acumMulti2 = 1
                for l in range(auxIterador, auxIterador+2):
                    acumMulti2 *= self.matriz[l][k]
                auxIterador += 1
                acumSumas2 += acumMulti2

            print(f"El determinante de la matriz es {acumSumas1 - acumSumas2}")
                

        else:
            print("Con ese tamaño no podemos hacer este metodo, una disculpa")


autores()
tamaño = int(input("Tamaño de la matriz: "))
a = Matriz(tamaño, tamaño)
a.rellenarMatrizEspecifico(5)

print(a)
print(a.signos())
print(a.possigno())

a.obtenerDeterminante()