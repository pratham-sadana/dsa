def dfs(graph,node,visited=None):
    if visited == None:
        visited = []
    visited.append(node)
    print(node,end =" ")

    for i in graph[node]:
        if i not in visited:
            dfs(graph,i,visited)

graph = {
    'a':['b','c'],
    'b':['d','e'],
    'c':[],
    'd':[],
    'e':['f'],
    'f':['b','c']
}
dfs(graph,'a')
