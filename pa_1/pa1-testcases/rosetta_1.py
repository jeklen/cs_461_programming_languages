# 对于有向无环图
# v表示顶点: v = ['a', 'b', 'c', 'd', 'e']
# e表示有向边: e = [('a','b'),('a','d'),('b','c'),('d','c'),('d','e'),('e','c')
import sys

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
    #for t in tmp:
    t = min(tmp)
    for i in range(len(e)):
        if t in e[i]:
            e[i] = 'toDel'
    if e:
        eset = set(e)
        if ('toDel' in eset):
            eset.remove('toDel')
        e[:] = list(eset)
    if v:
        v.remove(t)
    return t

def topoSort(v, e):
    result = []
    while True:
        nodes = indegree0(v, e)
        if nodes == None:
            break
        if nodes == -1:
            print("there's a circle")
            return None
        result.append(nodes)
    return result

lines = sys.__stdin__.readlines()
lines_set = set(lines)
v = list(lines_set)
e = []
for i in range(len(lines)//2):
    first = lines[2 * i]
    second = lines[2 * i + 1]
    e.append((second, first))
#e = [('a', 'b'), ('a', 'd'), ('b', 'c'), ('d', 'c'), ('d', 'e'), ('e', 'c')]
res = topoSort(v, e)
#print(res)
for line in res:
    sys.stdout.write(line)
    sys.stdout.flush()
