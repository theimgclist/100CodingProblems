/*
     Created by Avinash on 14th Nov, 2017
 */
import java.io.*;
import java.util.*;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.BufferedReader;
public class SumOfLIS 
{
	public static String theSequence = "";
	public static int sum = 0;
	public static void main(String[] args) 
	{
        	BufferedReader read = new BufferedReader(new InputStreamReader(System.in));
		int n; // holds the number of elements in input data
		int[] data; // contains the actual data
		int lis = 0; // holds the length of longest increasing subsequence
		int i = 0; // loop control variable
		try
		{       
			System.out.println("Enter the number of elements in data :");
			n = Integer.parseInt(read.readLine());
			data = new int[n];
			System.out.println("Enter the actual terms ");
			for(i = 0; i < n; i++)
        			data[i] = Integer.parseInt(read.readLine());
                        Helper link = new Helper();
                        lis = link.calculate_sumOfLIS(n,data); //calling the method that calculates the longest increasing subsequence
                        
		}
		catch (IOException e)
		{
			e.printStackTrace();
		}
                System.out.println("The length of longest increasing subsequence for the given data of numbers is: "+lis);
                System.out.println("The longest increasing subsequence is: "+theSequence);
                System.out.println("The sum of the longest increasing subsequence is: "+sum);
	}

}
class Helper
{
	public int calculate_sumOfLIS(int n, int[] data)
	{
		int[] lisCount = new int[n]; // this array contains the lis for data at each index
		Arrays.fill(lisCount,1);
		int sumLIS[] = new int[n];
		for(int i = 0; i < n;i++)
			sumLIS[i] = data[i];
		int max_sum = 0;	
		int lis = 0, position = -1;
		for(int i = 1; i < n; i++)  // picks each value from the data
         	{
         		for(int j = 0; j < i; j++)  // this array compares the value picked above with all the before items in the data
         		{
         			if(data[i] > data[j] && lisCount[i] < lisCount[j] + 1) // calculates lis for each index      
         			{
         				lisCount[i] = 1 + lisCount[j];
         			}
         			if(data[i] > data[j] && sumLIS[i] < sumLIS[j] + data[i])  //calculates the sum of lis for each index
         			{
         				sumLIS[i] = sumLIS[j] + data[i];
         			}                               
         		}
         	}
         	for(int i = 0; i < n; i++)
         	{
              		if( lis < lisCount[i])
              		{
                 		lis = lisCount[i];
                 		position = i;
                 	}
                 	if(max_sum < sumLIS[i])
                 		max_sum = sumLIS[i];
                 		
                }	
        	String theSequence = data[position]+ " ";
         	int result = lis-1;
         	for(int i = position - 1; i >= 0; i--)
         	{
         		if(lisCount[i] == result)
         		{
         			theSequence = data[i] + " "+theSequence;
         	 		result--;
         	 	}
         	}
         	SumOfLIS.theSequence = theSequence;
         	SumOfLIS.sum = max_sum;
         	return lis;	

        }
	
}
         
