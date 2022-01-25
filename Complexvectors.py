import Complejos as lc

def sumavec(v,w):
    tamano = len(v)
    suma = [lc.sumacplx(v[j],w[j]) for j in range(tamano)]
    return suma

def main():
    v = [(5,3), (8,2)]
    w = [(3,4), (9,3)]
    resp = sumavec(v, w)
    for i in resp:
        lc.prettyprinting(i)

main()