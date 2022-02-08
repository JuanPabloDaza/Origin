import Complejos as lc

def sumavec(v,w):
    tamano = len(v)
    suma = [lc.sumacplx(v[j],w[j]) for j in range(tamano)]
    return suma

def inversoadvec(v):
    tamano = len(v)
    inverso = [(-1*v[i][0],-1*v[i][1])for i in range(tamano)]
    return inverso

def escalarporvector(a,v):
    tamano = len(v)
    resultado = [(a*v[i][0],a*v[i][1])for i in range(tamano)]
    return resultado

def adicionmatrices(A, B):
    filas = len(A)
    columnas = len(A[0])
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila = fila + lc.sumacplx(A[i][j], B[i][j])
        matriz = matriz + fila
    return matriz

def main():
    v = [(5,3), (8,2)]
    w = [(3,4), (9,3)]
    resp = sumavec(v, w) + inversoadvec(v) + escalarporvector(5,v)
    for i in resp:
        lc.prettyprinting(i)
    A = [[(5,3), (8,2)], [(4,8), (6,9)], [(2,5), (3,1)]]
    B = [[(6,4), (4,7)], [(8,3), (9,8)], [(7,1), (9,6)]]

main()


