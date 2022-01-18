
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

def prettyprinting(c):
    print(str(c[0]) + " + " + str(c[1]) + "i")


#if __name__ == '__main__':
prettyprinting(sumacplx((2,3), (4,7)))
prettyprinting(multcplx((2,3), (4,7)))


