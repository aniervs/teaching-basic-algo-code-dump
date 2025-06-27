# row, col -> node = row * m + col
# node -> row = node // m, col = node % m
from collections import deque

adj_list = []
pred = []
distance = []

moves_list = [
    (-1, 0), # UP
    (1, 0), # DOWN
    (0, -1), # LEFT
    (0, 1), # RIGHT
]

def bfs(source: int):
    # breadth-first search
    Q = deque()
    Q.append(source)
    distance[source] = 0
    while len(Q) > 0:
        node = Q.popleft()
        for neighbour in adj_list[node]:
            if distance[neighbour] is None:
                distance[neighbour] = distance[node] + 1
                pred[neighbour] = node
                Q.append(neighbour)

def main():
    global adj_list, pred, distance

    n, m = map(int, input().split())
    labyrinth = []
    for _ in range(n):
        row = input()
        labyrinth.append(row)

    n_nodes = n * m

    adj_list = [[] for _ in range(n_nodes)]
    pred = [None for _ in range(n_nodes)]
    distance = [None for _ in range(n_nodes)]

    for row in range(n):
        for col in range(m):
            if labyrinth[row][col] == '#': # a wall
                continue
            node = row * m + col
            if labyrinth[row][col] == 'A':
                source_node = node
            elif labyrinth[row][col] == 'B':
                target_node = node
            for delta_row, delta_col in moves_list:
                neighbor_row = row + delta_row
                neighbor_col = col + delta_col
                if 0 <= neighbor_row < n and 0 <= neighbor_col < m and labyrinth[neighbor_row][neighbor_col] != '#':
                    neighbor_node = neighbor_row * m + neighbor_col
                    adj_list[node].append(neighbor_node)

    bfs(source_node)
    path = []
    current_node = target_node
    while current_node != source_node:
        path.append(current_node)
        current_node = pred[current_node]
    path.append(source_node)
    path.reverse()

    path = [(node // m, node % m) for node in path]
    moves_sequence = ""
    for i in range(len(path) - 1):
        # comparing path[i] with path[i + 1]
        if path[i + 1][0] == path[i][0] + 1: # the row increased by 1 -> DOWN
            moves_sequence += 'D'
        elif path[i + 1][0] == path[i][0] - 1: # the row decreased by 1 -> UP
            moves_sequence += 'U'
        elif path[i + 1][1] == path[i][1] + 1: # the column increased by 1 -> RIGHT
            moves_sequence += 'R'
        else: # otherwise, the column decreased by 1 -> LEFT
            moves_sequence += 'L'

    # print(path)
    print(moves_sequence)

if __name__ == '__main__':
    main()