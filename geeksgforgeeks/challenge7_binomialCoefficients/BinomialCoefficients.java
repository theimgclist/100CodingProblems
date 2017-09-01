/*
	Created by Avinash on 1st September, 2017
*/
import java.io.*;
import java.util.*;
import java.io.IOException;
public class BinomialCoefficients
{

	public static int output;
	public static void main(String[] args)
	{
		BufferedReader read = new BufferedReader(new InputStreamReader(System.in));
		int n,k;
		try
		{
			System.out.print("Enter the n value ");
			n = Integer.parseInt(read.readLine());
			System.out.print("Enter the k value ");
			k = Integer.parseInt(read.readLine());
			Helper link = new Helper();
			output = link.binomialCoeff(n,k);
		}
		catch(IOException e)
		{
			e.printStackTrace();
		}
		System.out.print("The binomial coefficient is "+output);
	}
}
class Helper
{
	public int binomialCoeff(int n, int k)
	{
		int c[][] = new int[n+1][k+1];
		int i,j;
		for(i = 0; i <= n; i++)
		{
			for(j = 0; j <= Math.min(i,k); j++)
			{
				if(j == 0 || j == i)
					c[i][j] = 1;
				else
					c[i][j] = c[i-1][j-1] + c[i-1][j];
			}
		}
		return c[n][k];
	}
}
