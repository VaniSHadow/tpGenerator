from Graph import *

class TPGenerator:

    def GenerateTP(self, filepath, ty, count=10):
        self.path = filepath
        if ty == 'DAG':
            for i in range(1, count+1):
                n = random.randint(10, 20)
                m = random.randint(n-1, n*2)
                obj = Graph(n, m)
                f = open(filepath+str(i)+".in", "a")
                line = str(obj.n)+" "+str(obj.m)
                f.write(line+"\n")
                for j in range(obj.m):
                    line = obj.GetEdge(j)
                    f.write(line+"\n")
                f.close()
