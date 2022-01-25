import math

def sumacplx(a, b):
    real = a[0] + b[0]
    img = a[1] + b[1]
    return (real, img)

def multcplx(a, b):
    real = (a[0] * b[0]) - (a[1] * b[1])
    img = (a[0] * b[1]) + (a[1] * b[0])
    return (real, img)

def divcplx(a, b):
    real = ((a[0] * b[0]) + (a[1] * b[1]))/((b[0]^2) + (b[1]^2))
    img = ((b[0] * a[1])-(a[0] * b[1]))/((b[0]^2) + (b[1]^2))
    return (real, img)

def modulocplx(a):
    return math.sqrt((a[0])^2 + (a[1])^2)

def conjugadocplx(a):
    return (a[0], (-1*a[1]))

def prettyprinting(c):
    if c[1] > 0:
        print(str(c[0]) + " + " + str(c[1]) + "i")
    else:
        print(str(c[0]) + " " + str(c[1]) + "i")


#if __name__ == '__main__':
prettyprinting(sumacplx((2,3), (4,7)))
prettyprinting(multcplx((2,3), (4,7)))
prettyprinting(divcplx((2,3), (4,7)))
print(modulocplx((2,3)))
prettyprinting(conjugadocplx((2,3)))
