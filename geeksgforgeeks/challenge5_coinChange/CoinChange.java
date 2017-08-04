/*
     Created by Avinash on 4th August, 2017
 */
import java.io.*;
import java.util.*;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.BufferedReader;
public class CoinChange 
{
	public static int coinChangeWays;
	public static void main(String[] args) 
	{
        	BufferedReader read = new BufferedReader(new InputStreamReader(System.in));
		int amount;
		int coins, denominations[];
		try
		{    
	        	System.out.print("Enter the amount : ");
	        	amount = Integer.parseInt(read.readLine());
	        	System.out.print("Enter the number of denominations : ");
	        	coins = Integer.parseInt(read.readLine());
	        	denominations = new int[coins];
	        	System.out.print("Enter the denominations : ");
	        	for(int i = 0; i < coins; i++)
	        		denominations[i] = Integer.parseInt(read.readLine());
			Helper link = new Helper();
			coinChangeWays = link.coinChange(amount, coins, denominations);
			
		}
		catch (IOException e)
		{
			e.printStackTrace();
		}
                System.out.println("The number of ways to get the change is : "+coinChangeWays);
	}

}
class Helper
{

        public int coinChange(int n, int m, int[] d)
	{
		int[][] t = new int[m][n+1];
		int include_coin, exclude_coin;
 		for(int i = 0; i < m; i++)
 			t[i][0] = 1;
 		for(int i = 0; i < m; i++)
 		{
 			for( int j = 1; j < n+1; j++)
 			{
 				include_coin  = ( j - d[i] >= 0) ? t[i][j - d[i]] : 0;
 				exclude_coin = (i >= 1) ? t[i-1][j] : 0;
 				t[i][j] = include_coin + exclude_coin;
 			}
 		}
 		return t[m-1][n];	
	}				
}
         
