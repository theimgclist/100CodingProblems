/*
     Created by Avinash on 2nd August, 2017
 */
import java.io.*;
import java.util.*;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.BufferedReader;
public class MinCostPath 
{
/*
 * Some basic rules while coding in Programming Contests:
 * Try to follow at least 80% of them
	Correctness
		- final declaration for required data types
		- avoid Object creation 
		- Scanner slows down, use InputReader
		- avoid too many static functions
		- check the boundaries of loop variables, where to include last element and where to skip
		- start with base cases and returning results for base cases wherever possible
			
	Efficiency
		- use library functions as much as possible		
		- assertEquals("RESULT", functionToCall())
	Debugging-ability
		- avoid too many global variables 
		- Separate logic from meta-processing
		- variable/function pneumonics must make sense
 * 
 */
	public static int minCost;
	public static void main(String[] args) 
	{
        	BufferedReader read = new BufferedReader(new InputStreamReader(System.in));
		int m,n,x,y;
		int[][] cost;
		try
		{      
			System.out.print("Enter the dimensions of the cost matrix : ");
			m = Integer.parseInt(read.readLine());
			n = Integer.parseInt(read.readLine());
			cost = new int[m][n];
			System.out.print("Enter the costs : ");
			for(int i = 0; i < m; i++)
			{
				for(int j = 0; j < n; j++)
				{
					cost[i][j] = Integer.parseInt(read.readLine());
				}
			}
			System.out.print("Enter the X and Y coordinates of destination : ");
			x = Integer.parseInt(read.readLine());
			y = Integer.parseInt(read.readLine());
			Helper link = new Helper();
			minCost = link.minCostPath(cost,x,y);
			
		}
		catch (IOException e)
		{
			e.printStackTrace();
		}
                System.out.println("The minimum cost it takes is : "+minCost);
	}

}
class Helper
{

        public int minCostPath(int[][] cost, int x, int y)
	{
		int[][] cache = new int[x+1][y+1];
		for(int i = 0; i <= x; i++)
		{
			for(int j = 0; j <= y; j++)
			{
				if(i == 0 && j == 0)
					cache[i][j] = cost[i][j];
				else if(i == 0)
					cache[i][j] = cache[i][j-1] + cost[i][j];
				else if(j == 0)
					cache[i][j] = cache[i-1][j] + cost[i][j];
				else
					cache[i][j] = cost[i][j] + Math.min(cache[i-1][j], (Math.min(cache[i-1][j-1], cache[i][j-1])));
			}
		}
		return cache[x][y];	
        }
}   
