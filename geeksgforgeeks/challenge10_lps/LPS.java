/*
    Created by Avinash on 9th November, 2017
*/
import java.io.*;
import java.util.*;
public class LPS
{
	public static int output;
	public static void main(String[] args)
	{
		BufferedReader read = new BufferedReader(new InputStreamReader(System.in));
		String data;
		int lps = 0;
		try
		{
		System.out.println("Enter the string : ");
		data = read.readLine();
		Helper link = new Helper();	
		lps = link.findLPSDP(data.toCharArray(),0,data.length()-1);
		}
		catch(IOException e)
		{
			e.printStackTrace();
		}
		System.out.print("The length of longest palindromic sequence is "+lps);
	}
}

class Helper
{
	public int findLPSRec(char[] data, int i, int j)
	{
		if( i == j)
			return 1;
		if(data[i] == data[j] && i + 1 == j)
			return 2;
		if(data[i] == data[j])
			return 2 + findLPSRec(data, i + 1, j - 1);
		return Math.max(findLPSRec(data, i, j - 1), findLPSRec(data, i + 1, j));	
	}

	public int findLPSDP(char[] data, int x, int y)
	 {
	 	int n = data.length;
	 	int cache[][] = new int[n][n];
	 	for(int i = 0; i < n; i++) // for all subsequences of length 1, LPS is 1
	 		cache[i][i] = 1;
	 	for(int sub = 2; sub <= n; sub++) //We now check for sequences of length 2,3,4..n
	 	{
	 		for(int i = 0; i < n - sub + 1; i++)
	 		{
	 			int j = i + sub - 1;
	 			if(data[i] == data[j] && sub == 2)
	 				cache[i][j] = 2;
	 			else if(data[i] == data[j])
	 				cache[i][j] = 2 + cache[i+1][j-1];
	 			else
	 				cache[i][j] = Math.max(cache[i+1][j], cache[i][j-1]);
	 		}
	 	}
	 	return cache[0][n-1];		
	}
  	
}	                    	
			