import math
# Definir x e a tolerancia
x = 2
tol = 10**-7
k = 0
# Definir uma função
def f(x):
  f = math.log(x) -1
  return f

# Definir derivada numerica
def dnf(x): 
    dnf =1/x
    return dnf

while math.fabs(f(x)) > tol or math.fabs(x) > tol:
    if math.fabs(f(x)) <= tol:
        print ("A raiz é : ",x)
        break
    else:
        print("k = ", k , "| x = ", x,  "|f(x) = ", f(x))
        x = x-f(x)/dnf(x)
        k += 1
print("k = ", k , "| x = ", x,  "|f(x) = ", f(x))
print("Dada a tolerancia ", tol)
print("O valor mais aproximado é: ",x)
            