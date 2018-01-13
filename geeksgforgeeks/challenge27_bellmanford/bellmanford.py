"""
	Created by Avinash on 13th Jan 2018
"""
from collections import defaultdict
class Graph :
	def __init__(self,vertices) :
		self.V = vertices
		self.graph = []
	
	def addedge(self,u,v,w) :
		self.graph.append([u,v,w])
			
	def printarr(self,dist) :
		print("Vertex distance from source")
		for i in range(self.V) :
			print("%d \t\t %d" %(i,dist[i]))
	
	def Bellmanford(self, src) :
		dist = [float("Inf")] * self.V
		dist[src] = 0
	
		for i in range(self.V - 1):
			for u,v,w in self.graph :
				if(dist[u] != float("Inf") and dist[u] + w < dist[v]):
					dist[v] = dist[u] + w
		for u,v,w in self.graph :
			if(dist[u] != float("Inf") and dist[u] + w < dist[v]) :
				print("Graph contains negative weight  cycle")
				return
		self.printarr(dist)
	

if __name__ == "__main__" :	
	g = Graph(5)
	g.addedge(0,1,-1)
	g.addedge(0,2,4)
	g.addedge(1,2,3)
	g.addedge(1,3,2)
	g.addedge(1,4,2)
	g.addedge(3,2,5)
	g.addedge(3,1,1)
	g.addedge(4,3,-3) 
	g.Bellmanford(0)

	
	