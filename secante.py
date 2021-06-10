import math
# Definir as variaveis

x = 0
x0 = 0
x1 = 1
tol = 5e-4
k = 0
# Definir uma função
def f(x):
  f = x**3 - 9*x +3
  return f

xa1 = x0
x = x1
while math.fabs(f(x)) > tol  or math.fabs(x1-x0) > tol:
    if math.fabs(f(x)) < tol:
        print ("A raiz é : ",x)
        break
    else:
        xa2 = xa1
        print("Iteracao ", k , ", xi-1 = ", xa2,", xi= ", xa1, ", x = ", x, ",f(x) = ", f(x))
        xa1 = x
        x = xa1 - f(xa1)*(xa2 - xa1)/(f(xa2) - f(xa1))
        k += 1
print("Iteracao ", k , ", xi-1 = ", xa2,", xi= ", xa1, ", x = ", x, ",f(x) = ", f(x))
print("Dada a tolerancia ", tol)
print("O valor mais aproximado é: ",x)
            