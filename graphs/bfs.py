from collections import deque

adj_list = []
distance = []
pred = []

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
    global adj_list, distance, pred
    n_nodes, n_edges = map(int, input().split())
    adj_list = [[] for _ in range(n_nodes)]
    distance = [None for _ in range(n_nodes)] # initially it is none for every node
    pred = [None for _ in range(n_nodes)]

    for _ in range(n_edges):
        a, b = map(int, input().split())
        adj_list[a].append(b)
        adj_list[b].append(a)

    bfs(0)
    for node in range(n_nodes):
        print(f"{node} -> {distance[node]}")
        path = []
        current_node = node
        while current_node != 0:
            path.append(current_node)
            current_node = pred[current_node]
        path.append(0)
        path.reverse()
        print(f"{node} -> {path}")


if __name__ == '__main__':
    main()