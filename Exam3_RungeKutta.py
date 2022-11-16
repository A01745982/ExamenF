# Ecuación diferencial
f= lambda x, y: x**2+y**2

# Función Algoritmo Runge-Kutta orden 4
def rk4(x0,y0,xf,h):
    while x0 <= xf:
        k1 = h*f(x0,y0)
        k2 = h*f(x0+(h/2), y0+(k1/2))
        k3 = h*f(x0+(h/2), y0+(k2/2))
        k4 = h*f(x0+h, y0+k3)
        k = (1/6)*(k1 + 2*k2 + 2*k3 + k4)
        y0 = y0+k
        x0 = x0+h
    return x0, y0

# Impresion de resultados
ans = (rk4(0,1,0.8,0.01))
print("Solución de ecuación diferencial y("+"%.2f"%ans[0]+"): ", "%.6f"%ans[1])