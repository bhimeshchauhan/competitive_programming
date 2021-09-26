def topological_sort(graph):
    output = []
    visited = {}
    for node, adjacencyList in graph.items():
        if node in visited:
            continue
        stack = [node]
        while len(stack) > 0:
            cur = stack[-1]
            neighbors = graph[cur]
            count = 0
            for neighbor in neighbors:
                if not neighbor in visited:
                    if neighbor in stack:
                        raise Exception("Found cycle")
                    stack.append(neighbor)
                    count += 1
            if count == 0:
                # Cannot move
                output.append(stack.pop(-1))
                visited[cur] = None

    return output