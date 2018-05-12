from random import *
from numpy import *

class graph:

    """n表示图中点的个数，m表示图中边的个数"""
    def __init__(self, n, m, directed=True, connected='weak', loop=False):
        if directed==True and connected=='weak' and loop==False:
            self.matr = numpy.zeros(n, n)
            print('yes')
            print(self.matr)
            topo = range(n)
            random.shuffle(topo)
            self.RandomGenerTopoEdges(m-(n-1))
            weak_connected = self.CheckWeakConnectivity()
            print(self.matr)
            print(weak_connected)
            if not weak_connected:
                self.RandomGenerTopoEdges(n-1)
            #else:
                
    """检查图的弱连通性"""
    def CheckWeakConnectivity():
        temp = copy.deepcopy(self.matr)
        for i in range(n):
            for j in range(n):
                if temp[i][j]==1:
                    temp[j][i]=1
                elif temp[j][i]==1:
                    temp[i][j]=1
        for i in range(n-1):
            if i==0:
                result = temp.dot(temp)
            else:
                result = result.dot(temp)
        for i in range(n):
            for j in range(n):
                if result[i][j]==0 and i!=j:
                    return False
        return True

    """在图中随机生成edge_num条边"""
    def RandomGenerTopoEdges(edge_num):
        for i in range(0, edge_num):
                mid = random.randint(2, n-1)
                st = random.randint(0, mid)
                end = random.randint(mid+1, n-1)
                if self.matr[topo[st]][topo[end]] == 0:
                    self.matr[topo[st]][topo[end]] = 1
                else:
                    i=i-1


g = graph(5, 10)

