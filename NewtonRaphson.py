import numpy as np
import sympy as sp
from sympy.functions import exp,log
from sympy import cos,sin,pi
from sympy.abc import x

class NewtonRaphson :
    
    def __init__(self):
        pass
    
    def newtonraphson(xk : float,f ,tole : float,nbrIter : int):
        xmoins = xk - 1
        xkplus = 0
        def func(x):
            func = eval(f)
            return func
        x = sp.Symbol('x')
        deriv1 = sp.diff(func(x),x)
        deriv2 = sp.diff(func(x),x,x)
        def deriv1er(x):
            deriv1er = eval(str(deriv1))
            return deriv1er
        def deriv2eme(x):
            deriv2eme = eval(str(deriv2))
            return deriv2eme
        for n in range(0,nbrIter):
            f1 = deriv1er(xk)
            f2 = deriv2eme(xk)
            if(f2 == 0):
                print("Impossible la derivee seconde egale à 0")
                break
            else :
                dist = xk - xmoins
                if(abs(dist)>=tole):
                    direction = -1 * f1/f2
                    xkplus = xk + direction
                    xmoinx = xk
                    xk = xkplus 
                else:
                    #print("La valeur apres ",n," iteration")
                    #print(xk)
                    break
                    return xk
        if(f2 > 0):
            #print("apres ",n," iteration le minimum est ",xk)
            return xk
        elif(f2 < 0):
            #print("apres ",n," iteration le maximum est ",xk)
            return xk
    
