# Consideracion de nodos
nodes = '12345678'
num_nodes = len(nodes)

# Matriz de conexiones 8 nodos [8x8]
#    1  2  3  4  5  6  7  8
M = [
    [0, 1, 2, 0, 0, 0, 0, 0],
    [0, 0, 1, 5, 2, 0, 0, 0],
    [0, 0, 0, 2, 1, 4, 0, 0],
    [0, 0, 0, 0, 3, 6, 8, 0],
    [0, 0, 0, 0, 0, 3, 7, 0],
    [0, 0, 0, 0, 0, 0, 5, 2],
    [0, 0, 0, 0, 0, 0, 0, 6],
    [0, 0, 0, 0, 0, 0, 0, 0],
]

# Distancia menor y ruta para cada nodo
best = [[0, 0, 0]] * num_nodes

for j in range(1, num_nodes):
    pos = []
    for i in range(num_nodes):
        if M[i][j] != 0:
            dst = best[i][0] + M[i][j]
            pos.append([dst, nodes[i], nodes[j]])
    best[j] = min(pos)

last = best[-1]
actual_node = s_route = last[2]

# Ruta hasta el último nodo
while actual_node != '1':
    p = last[1]
    for q in best:
        if q[2] == p:
            s_route = q[2]+'-'+s_route
            last = q
    actual_node = last[1]
s_route = '1-'+s_route

# Impresion de resultados
print("Ruta más corta: ", s_route)
print("Distancia total: ", best[-1][0], "unidades")