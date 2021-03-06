def autores():
    print()
    print("Programa hecho por Vergara Lorenzo Santiago Alonso")
    print("Rios Serrano Asis Gamaliel y")
    print("Calderon Romero Alberto Arphaxad,")


class Matriz:
    def __init__(self, filas, columnas, valor=0):
        self.filas = filas
        self.columnas = columnas
        self.matriz = []
        for fila in range(filas):
            self.matriz.append([])
            for _ in range(columnas):
                self.matriz[fila].append(valor)

    def __str__(self):
        cadena = ''
        for fila in range(self.filas):
            cadena += str(self.matriz[fila]) + '\n'
        return cadena

    def rellenarConListaDeLista(self, lis):
        for i in range(self.filas):
            for j in range(self.columnas):
                self.matriz[i][j] = lis[i][j]

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

    # Método que devuelve el signo que posee cierta posición en la matriz de signos
    def possigno(self, posf, posc):
        # posf = int(input("Posicion fila ")) - 1
        # posc = int(input("Posicion columna ")) - 1
        if ((posf + posc) % 2) == 0:
            return 1
        else:
            return -1

    # Método que obtiene el determinante de la matriz de tamaño 2 y tamaño 3 por método de Sarus
    def obtenerDeterminante(self):
        acumSumas1 = 0
        acumSumas2 = 0
        determinante = 0

        if self.filas == 2:   # Condición para obtener determinante de matriz tamaño 2
            determinante = (self.matriz[0][0] * self.matriz[1][1]) - (self.matriz[1][0] * self.matriz[0][1])
            # print(f"El determinante de la matriz es {determinante}")
            return determinante
        elif self.filas == 3:   # Condición para obtener matriz de tamaño 3
            self.matriz.append(self.matriz[0])
            self.matriz.append(self.matriz[1])

            # Proceso que inicia la obtención del determinante
            for j in range(3):
                acumMulti1 = 1
                for i in range(j, j+3):
                    acumMulti1 *= self.matriz[i][i - j]
                acumSumas1 += acumMulti1
            for j in range(3):
                acumMulti2 = 1
                for i in range(j + 2, j - 1, -1):
                    acumMulti2 *= self.matriz[i][j + 2 - i]
                acumSumas2 += acumMulti2
            determinante = acumSumas1 - acumSumas2
            # print(f"El determinante de la matriz es {determinante}")
            return determinante
        else:
            print("Con ese tamaño no podemos hacer este metodo, una disculpa")

    # Método que obtiene el determiante de la matriz por método Laplace
    def determinanteLaplace(self):
        lisCeros = []
        lisPivotes = []
        lisObjetos = []
        acumSumas = 0

        # Ciclos for que iteran en la matriz para obtener la fila con mayor número de ceros
        for i in range(self.filas):
            lisCeros.append(0)
            for j in range(self.columnas):
                if self.matriz[i][j] == 0:
                    lisCeros[i] += 1

        filMasCeros = lisCeros.index(max(lisCeros))
        # print(f"fila con más ceros {filMasCeros}")

        for j in range(self.filas):
            valor = self.matriz[filMasCeros][j] * self.possigno(filMasCeros + 1, j + 1)
            # print(valor)
            lisPivotes.append(valor)

        # Proceso que comienza con la obtención de los cofactores para el determinante
        for k in range(self.filas):
            # if lisPivotes[k] == 0:
                # continue
            matrizAceptados = []
            filaActual = -1
            for i in range(self.filas):
                if i != filMasCeros:
                    matrizAceptados.append([])
                    filaActual += 1
                    for j in range(self.columnas):
                        if j != k:
                            matrizAceptados[filaActual].append(self.matriz[i][j])
            obj = Matriz(self.filas - 1, self.columnas - 1)
            obj.rellenarConListaDeLista(matrizAceptados)
            # print(obj)
            lisObjetos.append(obj)

        for i in range(len(lisObjetos)):
            acumSumas += lisObjetos[i].obtenerDeterminante() * lisPivotes[i]

        return acumSumas

    # Método que obtiene la matriz inversa de otra matriz utilizando sus cofactores y el método transpuesta
    def obtenerInversa(self):
        determinante = self.determinanteLaplace()
        lisObjetos = []
        lisDeterminantes = []   # Matriz adjunta
        auxMatriz = 0
                
        if determinante != 0:   # Condición que excluye el método si el determinante es cero
            for i in range(self.filas):
                for j in range(self.columnas):
                    obj = Matriz(self.filas - 1, self.columnas - 1)
                    lisAux1 = []
                    aux1 = 0
                    for k in range(self.filas):
                        if i != k:
                            lisAux1.append([])
                            for l in range(self.columnas):
                                if j != l:
                                    lisAux1[aux1].append(self.matriz[k][l])
                            aux1 += 1
                    obj.rellenarConListaDeLista(lisAux1)
                    lisObjetos.append(obj)
        
            for i in range(self.filas):
                lisDeterminantes.append([])
                for j in range(self.columnas):
                    signo = self.possigno(i + 1, j + 1)
                    deter = lisObjetos[auxMatriz].obtenerDeterminante()
                    lisDeterminantes[i].append(deter * signo)
                    auxMatriz += 1

            lisMatrices = Matriz(self.filas, self.columnas)
            lisMatrices.rellenarConListaDeLista(lisDeterminantes)
            matTranspuesta = self.transpuesta(lisMatrices)

            matInversa = Matriz(self.filas, self.columnas)
            for i in range(matTranspuesta.filas):
                for j in range(matTranspuesta.columnas):
                    matInversa.matriz[i][j] = matTranspuesta.matriz[i][j] / determinante

            print("La matriz inversa es: ")
            print(matInversa)
            return matInversa
        else:
            print("El determinantes de la matriz es 0, no podemos realizar el metodo :(")

    # Método que devuelve la matriz transpuesta de otro objeto matriz
    def transpuesta(self, mat):
        transp = Matriz(mat.columnas, mat.filas)
        for i in range(mat.filas):
            for j in range(mat.columnas):
                transp.matriz[i][j] = mat.matriz[j][i]
        return transp


autores()
tam = int(input("Tamaño de la matriz: "))
a = Matriz(tam, tam)
a.rellenarMatrizDados()

print(a)

# print(a.signos())
# print(a.possigno())

a.obtenerInversa()