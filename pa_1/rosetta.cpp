#include <iostream>
#include <list>
#include <queue>
using namespace std;

/*****************类声明********************/
class Graph
{
    int V;              //顶点个数
    list<int> *adj;     //邻接表
    queue<int> q;       //维护一个入度为0的顶点的集合
    int* indegree       //记录每个顶点的入度
public:
    Graph(int V);       //构造函数
    ~Graph();           //析构函数
    void addEdge(int v, int w); //添加边
    bool topological_sort();    //拓扑排序
};

/***************类定义*********************/
Graph::Graph(int V)
{
    this->V = V;
    adj = new list<int>[V];
}
