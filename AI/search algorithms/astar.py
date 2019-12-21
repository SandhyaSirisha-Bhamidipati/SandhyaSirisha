def a_star(graph, start, dest):
    
    frontier = PriorityQueue()

    h = build_heuristic_dict()

    frontier.insert([(start, 0)], 0)
    explored = set()

    while not frontier.is_empty():

        path = frontier.remove()

        node = path[-1][0]
        g_cost = path[-1][1]
        explored.add(node)

        if node == dest:
            return [x for x, y in path]

        for neighbor, distance in graph[node]:
            cumulative_cost = g_cost + distance
            f_cost = cumulative_cost + heuristic(neighbor, h)
            new_path = path + [(neighbor, cumulative_cost)]

            if neighbor not in explored:
                frontier.insert(new_path, f_cost)

            elif neighbor in frontier._queue:
                frontier.insert(new_path, f_cost)
                print(path)
    return False




