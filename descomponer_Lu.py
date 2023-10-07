
arrayTrabajar = [3,5,6,1,0,5,7,4,3]

def descomponerLu(fun):
    a11, a12, a13, a21, a22, a23, a31, a32, a33 = arrayTrabajar

    u11 = a11
    u12 = a12
    l21 = a21/u11

    l32 = a22-l21*u12
    

descomponerLu(arrayTrabajar)