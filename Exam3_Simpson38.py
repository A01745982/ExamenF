# Declaración de función f(x)
f= lambda x: 1 / ((x**2) + (1/10))

# Función Regla de Simpson 3/8 Compuesta
def simp38c(a,b,n,f):
    if n%3!=0:
        return "'n' debe ser múltiplo de 3"
    h=(b-a)/n
    suma=f(a)+f(b)
    for i in range(1,n):
        if i%3==0:
            suma+=2*f(a+i*h)
        else:
            suma+=3*f(a+i*h)
    return suma*(3*h/8)

# Impresion de resultados
print("Aproximación de resultado: ", simp38c(0,2,90,f))