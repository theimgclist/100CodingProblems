/*
    Created by Avinash on 21st Sept, 2017
*/
import java.io.*;
import java.util.*;
public class Knapsack
{
	public static int output;
	public static void main(String[] args)
	{
		BufferedReader read = new BufferedReader(new InputStreamReader(System.in));
		int k_w, n,capacity = 0;
		int[] i_w, i_v;
		try
		{
		System.out.println("Enter the weight of the knapsack : ");
		k_w = Integer.parseInt(read.readLine());
		System.out.print("Enter the number of items : ");
		n = Integer.parseInt(read.readLine());
		i_w = new int[n];
		System.out.print("Enter the weights of items : ");
		for(int i = 0; i < n; i++)
			i_w[i] = Integer.parseInt(read.readLine());
		i_v = new int[n];
		System.out.print("Enter the values of each item : ");
		for(int i = 0; i < n; i++)
			i_v[i] = Integer.parseInt(read.readLine());
		Helper link = new Helper();	
		capacity = link.knapsack(k_w, n, i_w, i_v);
		}
		catch(IOException e)
		{
			e.printStackTrace();
		}
		System.out.print("The value of items in knapsack is "+capacity);
	}
}

class Helper
{
	public int knapsack_recursion(int k_w, int n, int[] i_w, int[] i_v)
	{
		if(n == 0 || k_w == 0)
			return 0;
		else if(i_w[n-1] > k_w)
			return knapsack_recursion(k_w, n-1, i_w, i_v);
		else
			return Math.max(i_v[n-1] + knapsack_recursion(k_w - i_w[n-1], n-1, i_w, i_v),
					knapsack_recursion(k_w,n-1,i_w,i_v));
	}

	public int knapsack(int k_w, int n, int[] i_w, int[] i_v)
	{
		int cache[][] = new int[n+1][k_w+1];
		for(int i = 0; i < n+1; i++)
		{
			for(int j = 0; j < k_w+1; j++)
			{
				if(i == 0 || j == 0)
					cache[i][j] = 0;
				else if(i_w[i-1] <= j)
					cache[i][j] = Math.max(i_v[i-1] + cache[i-1][j - i_w[i-1]],cache[i-1][j]);
				else
					cache[i][j] = cache[i-1][j];
			}
		}
		return cache[n][k_w];
	}
}	                    	
			