import random
import numpy
import copy

class Graph:

    """n表示图中点的个数，m表示图中边的个数"""
    def __init__(self, n, m, directed=True, connected='weak', loop=False):
        if directed==True and connected=='weak' and loop==False:
            self.n = n
            self.m = m
            self.matr = numpy.zeros((n, n))
            self.topo = list(range(n))
            random.shuffle(self.topo)
            self.RandomGenerTopoEdges(m-(n-1))
            weak_connected = self.CheckWeakConnectivity()
            if not weak_connected:
                self.RandomGenerTopoEdges(n-1)
            else:
                count = 0
                for i in range(n-1):
                    if self.matr[self.topo[i]][self.topo[i+1]]!=1:
                        self.matr[self.topo[i]][self.topo[i+1]]=1
                        count = count+1
                self.RandomGenerTopoEdges(n-1-count)
            self.edges = list()
            for i in range(n):
                for j in range(n):
                    if self.matr[i][j]==1:
                        e = (i, j)
                        self.edges.append(e)
                
    """检查图的弱连通性"""
    def CheckWeakConnectivity(self):
        temp = copy.deepcopy(self.matr)
        for i in range(self.n):
            for j in range(self.n):
                if temp[i][j]==1:
                    temp[j][i]=1
                elif temp[j][i]==1:
                    temp[i][j]=1
        for i in range(self.n-1):
            if i==0:
                result = temp.dot(temp)
            else:
                result = result.dot(temp)
        for i in range(self.n):
            for j in range(self.n):
                if result[i][j]==0 and i!=j:
                    return False
        return True

    """在图中随机生成edge_num条边"""
    def RandomGenerTopoEdges(self, edge_num):
        for i in range(edge_num):
                mid = random.randint(1, self.n-2)
                st = random.randint(0, mid)
                end = random.randint(mid+1, self.n-1)
                while self.matr[self.topo[st]][self.topo[end]] != 0:
                    mid = random.randint(1, self.n-2)
                    st = random.randint(0, mid)
                    end = random.randint(mid+1, self.n-1)
                self.matr[self.topo[st]][self.topo[end]] = 1

    """以字符串返回第i条边的信息"""
    def GetEdge(self, i, trim=True):
        if trim:
            return str(self.edges[i][0]+1)+" "+str(self.edges[i][1]+1)
        else:
            return str(self.edges[i][0])+" "+str(self.edges[i][1])

