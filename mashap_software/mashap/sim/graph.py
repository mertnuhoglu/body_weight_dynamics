import copy

def topological_sorting(dependencies, effects):
    if (find_missing_variables(dependencies) != {}) | (find_missing_variables(effects) != {}):
        raise KeyError, 'missing variables in dependencies: ' + find_missing_variables(dependencies).__str__() + ' or in effects: ' + find_missing_variables(effects).__str__()  
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

def find_missing_variables(graph):
    # finds variables that are in destinations (values) of dependencies or effects but not in
    # keys of them.
    result = []
    for vertex in graph.keys():
        for end_vertex in graph[vertex]:
            if end_vertex not in graph.keys():
                result.append((vertex,end_vertex))
    return dict(result)
    
def contains_cycle(graph):
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
