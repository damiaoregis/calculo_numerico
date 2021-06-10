import math
# Definir um intervalo 
tol = 5e-4
x0 = 0.5
k = 0
xi = 0
# Definir uma função

def f(x):
  f = (x**3) - 9*x +3 
  return f

# funçao de iteraçao
def g(x):
  g = (x**3)/9 +1/3
  return g

while math.fabs(f(xi)) > tol or math.fabs(xi-x0) > tol:
    xi = x0 
    print("Iteracao ", k , "| x =", xi ,"| g(x) =",g(xi),"| f(x) =", f(g(xi))) 
    k+=1
    xi=g(x0) 
    x0=xi 
print("Iteracao ", k , "| x =", xi ,"| g(x) =",g(xi),"| f(x) =", f(g(xi))) 
print("Dada a tolerancia ", tol)
print("O valor mais aproximado é: ",xi)