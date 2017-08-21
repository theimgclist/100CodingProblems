/*
     Created by Avinash on 21st Aug, 2017
 */
import java.io.*;
import java.util.*;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.BufferedReader;
public class MatrixMultiplication 
{

	public static int output;
	public static void main(String[] args) 
	{
        	BufferedReader read = new BufferedReader(new InputStreamReader(System.in));
		int p;
		int[] vector;
		try
		{       System.out.print("Enter the number of matrices: ");
			p = Integer.parseInt(read.readLine());
			vector = new int[p];
			System.out.print("Enter the dimension vector: ");
			for(int i = 0; i < p; i++)
				vector[i] = Integer.parseInt(read.readLine());
			Helper link = new Helper();
			output = link.numOfOperations(vector, vector.length);
			
		}
		catch (IOException e)
		{
			e.printStackTrace();
		}
                System.out.println("The minimum number of matrix multiplication operations needed = "+output);
	}

}
class Helper
{

        public int numOfOperations(int v[], int n)
	{
		int m[][] = new int[n][n];
		int i,j,k,l,q;
		for(i = 0; i < n; i++)
			m[i][i] = 0;
		for(l = 2; l < n; l++)
		{
			for(i = 1; i < n-l+1; i++)
			{
				j = i+l-1;
				m[i][j] = Integer.MAX_VALUE;
				for(k = i; k <= j-1; k++)
				{
					q = m[i][k] + m[k+1][j] + v[i-1]*v[k]*v[j];
					if( q < m[i][j] )
						m[i][j] = q;
				}
			}
		}
		return m[1][n-1];	
			
	}
	
}
         
