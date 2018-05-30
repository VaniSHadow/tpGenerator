#! -*- coding: utf8 -*-

from Graph import *
from TPGenerator import *

g = 'DAG'
path = r"D:\Workspace\python3\tpGenerator\test"
file_name = "test"
exe_name = "ttest.exe"
gener = TPGenerator()
gener.GenerateTP(path, file_name, exe_name, g, node_num=100, edge_num=500)
