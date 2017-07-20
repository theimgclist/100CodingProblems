/*
     Created by Avinash on 20th July, 2017
 */
import java.io.*;
import java.util.*;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.BufferedReader;
public class fibonacci 
{

	static int memo[]; // instead of declaring the array size with some value, we can do it after taking the input, to save space
        public static void main(String[] args) 
	{
        	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int nth_term = 0,result = 0;
		try
		{       nth_term = Integer.parseInt(br.readLine());
			memo = new int[nth_term]; //array size declared here
			Arrays.fill(memo,-1);
		//	result = nth_fib_number_memoization(nth_term-1);
			result = nth_fib_number_tabulation(nth_term);
		
		}
		catch (IOException e)
		{
			e.printStackTrace();
		}
                System.out.println("The "+nth_term+"th term in Fibonacci series is "+result);
	}

        public static int nth_fib_number_memoization(int n)
	{
		if(memo[n] == -1)
         	{
         		if(n <= 1)
         			memo[n] = n;
         		else
         			memo[n] = nth_fib_number_memoization(n-1) + nth_fib_number_memoization(n-2);
         	}
         	return memo[n];	

        }
	public static int nth_fib_number_tabulation(int n)
	{
		int table[] = new int[n];
		table[0] = 0;
		table[1] = 1;
		for(int i = 2; i < n; i++)
		{
			table[i] = table[i-1] + table[i-2];
		}
		return table[n-1];
	}
}
         
