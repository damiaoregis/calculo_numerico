import math
# Definir um intervalo [a,b] e a tolerancia
a = 1
b = 2
tol = 2e-2
k = 0
# Definir uma função
def f(x):
  f = x**7 -7
  return f
 

if f(a)* f(b) < 0:
    while (math.fabs(b-a)>tol) or math.fabs(b-a) > tol:
        xi = (a+b)/2
        print("Iteracao ", k , "| a = ", a , "| x = ", xi , "| b = ", b , "| f(a) = ",f(a),"| f(x) = ", f(xi), "| f(b) = ",f(b))
        if f(xi)== 0:
            print ("A raiz é : ",xi)
            break
        else:
            if f(a)* f(xi) < 0:
                b = xi
            else:
                a = xi
        k += 1
    print("Iteracao ", k , "| a = ", a , "| x = ", xi , "| b = ", b , "| f(a) = ",f(a),"| f(x) = ", f(xi), "| f(b) = ",f(b))
    print("Dada a tolerancia ", tol)
    print("O valor mais aproximado é: ",xi)
else:
    print("Não há raiz no interva! ")            