# Created by Avinash on 6th Dec, 2017

def process() :
	places = int(input("Enter the number of places "))
	dist = [[0 for i in range(places)]for j in range(places)]
	print("Enter the distances");
	for i in range(places):
		
		for j in range(places):
			dist[i][j] = int(input())
			if i == j :
				dist[i][j] = 0
				continue
			if dist[i][j] == 0 :
				dist[i][j] = 99999
			
		
	shortestDistance = floydWarshall(places, dist)
	
	for i in range(places):
		temp = []
		for j in range(places):
			if shortestDistance[i][j] == 99999 :
				temp.append("INF ")
			else  :
				temp.append(shortestDistance[i][j])
				 
		print(temp)
def floydWarshall(n,distance):
	dist = [[0 for i in range(n)]for j in range(n)]
	
	for i in range(n):
		
		for j in range(n):
			dist[i][j] = distance[i][j]
			

	for k in range(n):
		for i in range(n):
			for j in range(n):
				if dist[i][j] > dist[i][k] + dist[k][j] :
					dist[i][j] = dist[i][k] + dist[k][j]
	return dist	
			

if __name__ == "__main__":
	process()
	