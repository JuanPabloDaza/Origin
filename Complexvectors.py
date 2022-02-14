import math
import Complejos as lc

def changeprintcomplex(c):
    if c[1] > 0:
        return str(c[0]) + " + " + str(c[1]) + "i"
    else:
        return str(c[0]) + str(c[1]) + " i"

#1
def sumavec(v,w):
    tamano = len(v)
    suma = [[lc.sumacplx(v[j][0],w[j][0])] for j in range(tamano)]
    return suma

#2
def inversoadvec(v):
    tamano = len(v)
    inverso = [[(-1*v[i][0][0],-1*v[i][0][1])]for i in range(tamano)]
    return inverso

#3
def escalarporvector(a,v):
    tamano = len(v)
    resultado = [(a*v[i][0][0],a*v[i][0][1])for i in range(tamano)]
    return resultado

#4
def adicionmatrices(A, B):
    filas = len(A)
    columnas = len(A[0])
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila = fila + [changeprintcomplex(lc.sumacplx(A[i][j], B[i][j]))]
        matriz = matriz + [fila]
    return matriz

#5
def inversamatriz(A):
    matriz = []
    for i in range(len(A)):
        fila = []
        for j in range(len(A[0])):
            fila = fila + [changeprintcomplex((-1*A[i][j][0],-1*A[i][j][1]))]
        matriz = matriz + [fila]
    return matriz

#6
def multescalarmatriz(c, A):
    matriz = []
    for i in range(len(A)):
        fila = []
        for j in range(len(A[0])):
            fila = fila + [changeprintcomplex((c*A[i][j][0],c*A[i][j][1]))]
        matriz = matriz + [fila]
    return matriz

#7
def traspuestacomplex(A):
    filas = len(A)
    columnas = len(A[0])
    matriz = [[0 for i in range(filas)]for i in range(columnas)]
    for i in range(filas):
        for j in range(columnas):
            matriz[j][i] = changeprintcomplex(A[i][j])
    return matriz

#8
def conjugadamatriz(A):
    matriz = []
    for i in range(len(A)):
        fila = []
        for j in range(len(A[0])):
            fila = fila + [changeprintcomplex(lc.conjugadocplx(A[i][j]))]
        matriz = matriz + [fila]
    return matriz

#9
def adjuntamatriz(A):
    matriz = []
    for i in range(len(A)):
        fila = []
        for j in range(len(A[0])):
            fila = fila + [lc.conjugadocplx(A[i][j])]
        matriz = matriz + [fila]
    return traspuestacomplex(matriz)

#10
def productomatrices(A, B):
    filas = len(A)
    columnas = len(A[0])
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(filas):
            suma = (0,0)
            for k in range(columnas):
                suma = lc.sumacplx(suma, lc.multcplx(A[i][k], B[k][j]))
            fila += [changeprintcomplex(suma)]
        matriz += [fila]
    return matriz

#12
def productointerno(A, B):
    for i in range(len(A)):
        A[i][0] = lc.conjugadocplx(A[i][0])
    filas = len(A)
    matriz = [0 for i in range(filas)]
    for i in range(filas):
        matriz[i] = A[i][0]
    suma = (0,0)
    for i in range(len(matriz)):
        suma = lc.sumacplx(suma, lc.multcplx(matriz[i], B[i][0]))
    return suma
        
#13
def normavector(v):
    resp = productointerno(v,v)
    return math.sqrt(resp[0])
    
#14
def distanciavectores(A, B):
    suma = sumavec(A, inversoadvec(B))
    return normavector(suma)

#15
def matrizunitaria(A):
    filas = len(A)
    columnas = len(A[0])
    if filas != columnas:
        return "No es unitaria"
    B = []
    for i in range(len(A)):
        fila = []
        for j in range(len(A[0])):
            fila = fila + [lc.conjugadocplx(A[i][j])]
        B = B + [fila]
    matriz = [[0 for i in range(filas)]for i in range(columnas)]
    for i in range(filas):
        for j in range(columnas):
            matriz[j][i] = B[i][j]
    unitaria = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            suma = (0,0)
            for k in range(filas):
                suma = lc.sumacplx(suma, lc.multcplx(A[i][j], B[j][k]))
            fila += [suma]
        unitaria += [fila]
    for i in range(filas):
        for j in range(columnas):
            if i == j:
                if unitaria[i][j] != 1:
                    return "No es unitaria"
            else:
                if unitaria[i][j] != 0:
                    return "No es unitaria"
    return "Es unitaria"

#16
def matrizhermitiana(A):
    filas = len(A)
    columnas = len(A[0])
    if filas != columnas:
        return "No es hermitiana"
    B = [[0 for i in range(filas)]for i in range(columnas)]
    for i in range(filas):
        for j in range(columnas):
            B[j][i] = A[i][j]
    for i in range(filas):
        for j in range(columnas):
            B[i][j] = lc.conjugadocplx(B[i][j])
    for i in range(filas):
        for j in range(columnas):
            if B[i][j] != A[i][j]:
                return "No es hermitiana"
    return "Es hermitiana"

def main():
    v = [[(5,3)], [(8,2)]]
    w = [[(3,4)], [(9,3)]]
    print("---------------Suma vectores---------------")
    resp = sumavec(v, w)
    for i in range(len(resp)):
        lc.prettyprinting(resp[i][0])
    print("---------------Inverso aditivo---------------")
    resp = inversoadvec(v)
    for i in range(len(resp)):
        lc.prettyprinting(resp[i][0])
    print("---------------Escalar por vector---------------")
    resp = escalarporvector(5,v)
    for i in resp:
        lc.prettyprinting(i)
    A = [[(5,3), (8,2)], [(4,8), (6,9)], [(2,5), (3,1)]]
    B = [[(6,4), (4,7)], [(8,3), (9,8)], [(7,1), (9,6)]]
    print("---------------Adicion de matrices complejas---------------")
    resp = adicionmatrices(A,B)       
    for i in range(len(resp)):
        print(resp[i])
    print("---------------Inversa aditiva de una matriz---------------")
    resp = inversamatriz(A)       
    for i in range(len(resp)):
        print(resp[i])
    print("---------------Multiplicacion de un escalar por una matriz compleja---------------")
    c=3
    resp = multescalarmatriz(c,A)
    for i in range(len(resp)):
        print(resp[i])
    print("---------------Transpuesta de una matriz compleja---------------")
    resp = traspuestacomplex(A)
    for i in range(len(resp)):
        print(resp[i])
    print("---------------Conjugada de una matriz compleja---------------")
    resp = conjugadamatriz(A)
    for i in range(len(resp)):
        print(resp[i])
    print("---------------Adjunta de una matriz compleja---------------")
    resp = adjuntamatriz(A)
    for i in range(len(resp)):
        print(resp[i])
    C = [[(5,3), (8,2), (4,8)], [(6,9), (2,5), (3,1)]]
    D = [[(6,4), (4,7)], [(8,3), (9,8)], [(7,1), (9,6)]]
    print("---------------Producto de dos matrices---------------")
    resp = productomatrices(C, D)
    for i in range(len(resp)):
        print(resp[i])
    print("---------------Producto interno de dos vectores---------------")
    resp = productointerno(v, w)
    print(changeprintcomplex(resp))
    print("---------------Norma de un vector---------------")
    resp = normavector(v)
    print(resp)
    print("---------------Distancia entre dos vectores---------------")
    resp = distanciavectores(v, w)
    print(resp)
    print("---------------Comprobacion de una matriz unitaria---------------")
    E = [[(1,0),(2,0),(3,0)],[(3,0),(7,0),(9,0)],[(3,0),(2,0),(1,0)]]
    print(matrizunitaria(E))
    print("---------------Comprobacion de una matriz hermitiana---------------")
    G = [[(3,0),(-2,8),(3,-5)],[(-2,-8),(0,0),(-5,0)],[(3,5),(-5,-7),(1,0)]]
    H = [[(3,0),(-2,8),(3,-5)],[(-2,-8),(0,0),(-5,7)],[(3,5),(-5,-7),(1,0)]]
    print(matrizhermitiana(G))
    print(matrizhermitiana(H))
main()