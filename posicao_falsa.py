import math
# Definir um intervalo [a,b] e a tolerancia
a = 0
b = 1
tol = 2e-3
k= 0
xi=0
# Definir uma função
def f(x):
  f = 2**x - 3*x
  return f


if f(a)* f(b) < 0:
    while (math.fabs(f(xi))>tol) or math.fabs(b-a) > tol:
        xi = (a*f(b)-b*f(a))/(f(b)-f(a))
        print("Iteracao ", k , "| x = ", xi ,  "| f(x) = ", f(xi), "| b-a = ", b-a)
        if f(xi)== 0:
            print ("A raiz é : ",xi)
            break
        else:
            if f(a)* f(xi) < 0:
                b = xi
            else:
                a = xi
        k += 1
    print("Iteracao ", k , "| x = ", xi ,  "| f(x) = ", f(xi), "| b-a = ", b-a) 
    print("Dada a tolerancia ", tol)
    print("O valor mais aproximado é: ",xi)
else:
    print("Não há raiz no interva! ")           