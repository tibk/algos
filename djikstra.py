costs = [                                                                                                       
    [1, 1, 1, 10],
    [10, 10, 1, 10],
    [10, 10, 1, 10],
    [10, 10, 1, 1],
]


def get_neighbors(node, n):
    x, y = node
    neighbors = []
    if x < n - 1:
        neighbors += [(x + 1, y)]
    if y < n - 1:
        neighbors += [(x, y + 1)]
    # if x < n - 1 and y < n - 1:
    #     neighbors += [(x + 1, y + 1)]
    return neighbors


def get_travels(costs):

    n = len(costs)

    # init
    travels = [[(-1, []) for i in range(n)] for i in range(n)]
    travels[0][0] = costs[0][0], [(0, 0)]
    edges = [(0, 0)]

    while edges:
        new_edges = []
        for edge in edges:
            xe, ye = edge
            current_cost, current_path = travels[xe][ye]
            neighbors = get_neighbors(edge, n)
            for neighbor in neighbors:
                xn, yn = neighbor
                c = costs[xn][yn]
                c_tot, path = travels[xn][yn]
                if not(path) or current_cost + c < c_tot:
                    new_cost = current_cost + c
                    new_path = current_path + [(xn, yn)]
                    travels[xn][yn] = new_cost, new_path
                    new_edges.append(neighbor)
        edges = new_edges
    return travels


if __name__ == '__main__':
  for cost in costs:
    print(cost)
  travels = get_travels(costs)
  for travel in travels:
      print(travel)
