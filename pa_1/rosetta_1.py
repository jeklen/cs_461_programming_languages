# 对于有向无环图
# v表示顶点: v = ['a', 'b', 'c', 'd', 'e']
# e表示有向边: e = [('a','b'),('a','d'),('b','c'),('d','c'),('d','e'),('e','c')
def indegree0(v, e):
    if v==[]:
        return None
    tmp = v[:]
    # tmp中剩下来的是入度为0的顶点
    for i in e:
        if i[1] in tmp:
            tmp.remove(i[1])
    if tmp == []:
        return -1

    # 只要是包含了这个入度为0的顶点的都可以删掉
    for t in tmp:
        for i in range(len(e)):
            if t in e[i]:
                e[i] = 'toDel'
    if e:
        eset = set(e)
        eset.remove('toDel')
        e[:] = list(eset)
    if v:
        for t in tmp:
            v.remove(t)
    return tmp

def topoSort(v, e):
    result = []
    while True:
        nodes = indegree0(v, e)
        if nodes == None:
            break
        if nodes == -1:
            print("there's a circle")
            return None
        result.extend(nodes)
    return result

v = ['a', 'b', 'c', 'd', 'e']
e = [('a', 'b'), ('a', 'd'), ('b', 'c'), ('d', 'c'), ('d', 'e'), ('e', 'c')]
res = topoSort(v, e)
print(res)
