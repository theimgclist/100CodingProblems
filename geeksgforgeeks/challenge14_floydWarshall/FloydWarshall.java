/*
	Created by Avinash on 4th Dec, 2017
*/
import java.io.*;
import java.util.*;
import java.lang.*;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.BufferedReader;

public class FloydWarshall
{
	//public static int output = 0;
	final static int INF = 99999;
	public static void main(String[] args)
	{
		BufferedReader read = new BufferedReader(new InputStreamReader(System.in));
		int places = 0;
		int[][] distance;
		int[][] shortestPath = new int[10][10]; //taking max places as 10
		try
		{
			System.out.print("Enter the number of places : ");
			places = Integer.parseInt(read.readLine());
			distance = new int[places][places];
			for(int i = 0; i < places; i++)
			{
				for(int j = 0; j < places; j++)
				{
					distance[i][j] = Integer.parseInt(read.readLine());
					if(i == j)
					{
						distance[i][j] = 0;
						continue;
					}
					if(distance[i][j] == 0)
						distance[i][j] = 99999; 	
					
				}
			}
			Helper link = new Helper();
			shortestPath = link.findShortestPaths(places,distance);
		
		}
		catch(IOException e)
		{
			e.printStackTrace();
		}
		System.out.println("The shortest paths for all places : ");
		for(int i = 0; i < places; i++)
		{
			for(int j = 0; j < places; j++)
			{
				if(shortestPath[i][j] == INF)
					System.out.print("INF ");
				else
					System.out.print(shortestPath[i][j]+" ");
			}
			System.out.println();
		}
	}
}
class Helper
{
	public int[][] findShortestPaths(int n, int[][] distance)
	{
		int[][] dist;
		dist = Arrays.copyOf(distance,distance.length);
		for(int k = 0; k < n; k++)//picking each intermediate place
		{
			for(int i = 0; i < n; i++)//picking the source
			{
				for(int j = 0; j < n; j++)//picking the destination
				{
					if(dist[i][j] > dist[i][k] + dist[k][j] )
						dist[i][j] = dist[i][k]+dist[k][j];
				}
			}
		}
		return dist;
	}
}	
			
	
						