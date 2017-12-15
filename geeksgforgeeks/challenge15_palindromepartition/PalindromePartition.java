/*
	Created by Avinash on 12th Dec, 2017
*/
import java.io.*;
import java.util.*;
import java.io.IOException;
import java.lang.*;

public class PalindromePartition
{
	public static void main(String[] args)
	{
		BufferedReader read = new BufferedReader(new InputStreamReader(System.in));
		String data;
		int n;
		int minSplits = 0;
		Boolean[][] isPal = new Boolean[100][100];
	        try
		{
			System.out.println("Enter the string ");
			data = read.readLine();
			n = data.length();
			Helper link = new Helper();
			isPal = link.palCheck(data);
			minSplits = link.palPartition(data,isPal);
		}
		catch(IOException e)
		{
			e.printStackTrace();
		}
		System.out.print("The minimum number of cuts required for palindrome partitioning is "+minSplits);
	}
}

class Helper
{
	public Boolean[][] palCheck(String data)
	{
		int n = data.length();
		Boolean[][] isPal = new Boolean[n][n];
		for(int i = 0; i < n; i++)
			isPal[i][i] = true; //all substrings of length 1 are palindromes

		for(int i = 0; i < n - 1; i++) // checking all substrings of len 2
		{
			if(data.charAt(i) == data.charAt(i+1))
				isPal[i][i+1] = true;
		}
		
		for(int l = 3; l <= n; l++) // taking each substring of length >= 2
		{
			for(int i = 0 ; i < n-l+1; i++) // starting index of each substring
			{
				int j = i+l-1; // ending index of each substring
				if(data.charAt(i) == data.charAt(j) && isPal[i+1][j-1] != null) // checking if current substring is a palindrome
					isPal[i][j] = true;
			}
		}
		return isPal;	
		
	}
	public int palPartition(String data, Boolean[][] isPal)
	{
		int n = data.length();
		int[] splits = new int[n];
		for(int i = 0; i < n; i++)
		{
			int min = Integer.MAX_VALUE;
			if(isPal[0][i] != null)
				splits[i] = 0;
			else
			{
				for(int j = 0; j < i; j++)
				{
					if(isPal[j+1][i] != null && min > splits[j] + 1)
						min = splits[j] + 1;
				}
				splits[i] = min;
			}
		}
		return splits[n-1];
	}
}	
	
		
			