/*
    Created by Avinash on 11th November, 2017
*/
import java.io.*;
import java.util.*;
public class CuttingRod
{
	public static int output;
	public static void main(String[] args)
	{
		BufferedReader read = new BufferedReader(new InputStreamReader(System.in));
		int maxPrice = 0;
		try
		{
		System.out.println("Enter the length of rod : ");
		int rodLength;
        	rodLength = Integer.parseInt(read.readLine());
        	int[] price = new int[rodLength];
        	System.out.print("Enter the price of different lenghts of rod: ");
        	for(int i = 0; i < rodLength; i++)
        		price[i] = Integer.parseInt(read.readLine());
        	Helper link = new Helper();
        	maxPrice = link.findMaxPriceDP(price,rodLength);
		}
		catch(IOException e)
		{
			e.printStackTrace();
		}
		System.out.print("The maximum price that can be obtained is " +maxPrice);
	}
}

class Helper
{
        public int findMaxPrice(int[] price, int length)
	{
		if(length <= 0)
			return 0;
		int max = Integer.MIN_VALUE;
		for(int i = 0; i < length; i++)
			max = Math.max(max, price[i] + findMaxPrice(price, length - i - 1));
		return max;
	}
        
        public int findMaxPriceDP(int[] price, int length)
	{
		
		int cache[] = new int[length+1];
		int maxPrice = -1;;
		for(int i = 1; i <= length; i++)
		{
			int max = Integer.MIN_VALUE;
			for(int j = 0; j < i; j++)
			{
				maxPrice= Math.max(maxPrice, price[j] + cache[i - j - 1]);		
				cache[i] = maxPrice;
			 }
		 }
		 return cache[length];
	}
  	
}	                    	
			