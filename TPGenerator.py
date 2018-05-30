from Graph import *
import os

class TPGenerator:

	"""生成测试点"""
	def GenerateTP(self, path, file_name, exe_name, ty, count=10, node_num=100, edge_num=100, weight_limit=20):
		self.file_path = path + "\\" + file_name
		self.exe_path = path + "\\" + exe_name
		if ty == 'DAG':
			for i in range(1, count+1):
				n = random.randint(int(node_num/2), node_num)
				m = random.randint(n-1, min(n*2, edge_num))
				obj = Graph(n, m)
				input_filename = self.file_path + str(i) + ".in"
				output_filename = self.file_path + str(i) + ".out"
				f = open(input_filename, "w")
				line = str(obj.n)+" "+str(obj.m)
				f.write(line+"\n")
				for j in range(obj.m):
					line = obj.GetEdge(j)
					f.write(line+"\n")
				f.close()
				f = open(output_filename, "w")	#创建
				f.close()
				self.run(self.exe_path, input_filename, output_filename)
	
	"""从.in运行exe得到.out"""
	def run(self, exe_path, input_filename, output_filename):
		command = exe_path + "<" + input_filename + ">" + output_filename
		os.system(command)
