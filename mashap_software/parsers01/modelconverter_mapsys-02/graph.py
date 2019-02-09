import copy

def topological_sorting(dependencies, effects):
    deps = copy.deepcopy(dependencies)
    L = []
    S = find_independent_vars(deps)
    while S != set([]):
        ind = S.pop()
        L.append(ind)
        for dep in effects[ind]:
            deps[dep].remove(ind)
            if not deps[dep]:
                S.add(dep)
    return L

White, Grey, Black = range(3)

def contains_cycle(graph):
    from mert import ipdb
    ipdb.set_trace()
    colors = dict([(vertex, White) for vertex in graph.keys()])
    for vertex in graph.keys():
        if colors[vertex] == White:
            cycle = visit(graph, vertex, colors) 
            if cycle:
                cycle.append(vertex)
                return cycle
    return []

def visit(graph, vertex, colors):
    colors[vertex] = Grey
    cycle = []
    for end_vertex in graph[vertex]:
        if colors[end_vertex] == Grey:
            return [end_vertex]
        elif colors[end_vertex] == White:
            cycle = visit(graph, end_vertex, colors)
            if cycle:
                cycle.append(end_vertex)
                return cycle
    colors[vertex] = Black
    return cycle

def find_independent_vars(dependencies):
    return set([name for (name, value) in dependencies.items() if not value])
