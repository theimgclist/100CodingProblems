/*
     Created by Avinash on 25th July, 2017
 */
import java.io.*;
import java.util.*;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.BufferedReader;
public class LIS 
{
	public static String theSequence = "";
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
                        lis = link.calculate_LIS(data); //calling the method that calculates the longest increasing subsequence
                        
		}
		catch (IOException e)
		{
			e.printStackTrace();
		}
                System.out.println("The length of longest increasing subsequence for the given data of numbers is: "+lis);
                System.out.println("The longest increasing subsequence is: "+theSequence);
	}

}
class Helper
{
	public int calculate_LIS(int[] n)
	{
		int[] lisCount = new int[n.length]; // this array contains the lis for data at each index
		for(int i = 0; i < n.length; i++)  // picks each value from the data
         	{
         		int max = -1;
         		for(int j = 0; j < i; j++)  // this array compares the value picked above with all the before items in the data
         		{
         			if(n[i] > n[j])      
         			{
         				if(max == -1 || max < lisCount[j] + 1)
         					max = 1 + lisCount[j];
         			 }                                 
         		}
         	  	 if(max == -1)
         	 		max = 1;
         	 	lisCount[i] = max;	
         	 }
         	 int lis = -1;
         	 int position = -1;
         	 for(int i =0; i < lisCount.length; i++)
         	 {
         	 	if(lisCount[i] > lis)
         	 	{
         	 		lis = lisCount[i];
         	 		position = i;
         	 	}
         	 }
         	 String theSequence = n[position]+ " ";
         	 int result = lis-1;
         	 for(int i = position - 1; i >= 0; i--)
         	 {
         	 	if(lisCount[i] == result)
         	 	{
         	 		theSequence = n[i] + " "+theSequence;
         	 		result--;
         	 	}
         	  }
         	  LIS.theSequence = theSequence;
         	  return lis;	

        }
	
}
         
