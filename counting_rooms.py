import sys

adj_list = []
visited = []
maze = []

# depth-first search
def dfs(node: int):
    visited[node] = True 
    for neighbor in adj_list[node]:
        if not visited[neighbor]:
            dfs(neighbor)

def count_components(n: int, m: int):
    global adj_list, visited
    
    n_nodes = n * m
    
    count_connected_components = 0
    for node in range(n_nodes):
        row, col = node // m, node % m 
        if maze[row][col] == '#':
            continue 
        if not visited[node]:
            count_connected_components += 1
            dfs(node)
    return count_connected_components

moves_list = [
    (-1, 0), # UP
    (1, 0), # DOWN
    (0, -1), # LEFT
    (0, 1) # RIGHT 
]

def main():
    global adj_list, visited , maze 
    
    n, m = map(int, input().split())
    for _ in range(n):
        row = input()
        maze.append(row)
    
    n_nodes = n * m 
    adj_list = [[] for _ in range(n_nodes)]
    visited = [False for _ in range(n_nodes)]
    
    for row in range(n):
        for col in range(m):
            if maze[row][col] == '#':
                continue 
            node = row * m + col 
            for delta_row, delta_col in moves_list:
                neighbor_row = row + delta_row 
                neighbor_col = col + delta_col 
                if 0 <= neighbor_row < n and 0 <= neighbor_col < m and maze[neighbor_row][neighbor_col] != '#':
                    # if i don't leave the grid and the neighboring is a free cell (not a wall)
                    neighbor = neighbor_row * m + neighbor_col 
                
                    adj_list[node].append(neighbor) # only considering the pair (node, neighbor)
                    # because the symmetric pair will be considered later in the code when row,col correspond to neighbor
            
    print(count_components(n, m))
    
    
if __name__ == '__main__':
    sys.setrecursionlimit(10**9)
    main()
