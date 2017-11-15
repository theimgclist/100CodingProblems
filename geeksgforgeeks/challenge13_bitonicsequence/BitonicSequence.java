/*
     Created by Avinash on 15th Nov, 2017
 */
import java.io.*;
import java.util.*;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.BufferedReader;
public class BitonicSequence 
{
	public static String theSequence = "";
	public static void main(String[] args) 
	{
        	BufferedReader read = new BufferedReader(new InputStreamReader(System.in));
		int n; // holds the number of elements in input data
		int[] data; // contains the actual data
		int bitonic = 0; // holds the length of longest increasing subsequence
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
                        bitonic = link.lenOfBitonicSeq(n,data); //calling the method that calculates the longest increasing subsequence
                        
		}
		catch (IOException e)
		{
			e.printStackTrace();
		}
                System.out.println("The length bitonic sequence for the given data of numbers is: "+bitonic);
                
	}

}
class Helper
{
	public int lenOfBitonicSeq(int n, int[] data)
	{
		int[] lisCount = new int[n]; // this array contains the lis for data at each index
		Arrays.fill(lisCount,1);
		int[] ldsCount = new int[n]; // this array contains the lds for data at each index
		Arrays.fill(ldsCount,1);
		int bitonic = 0;
		
		int lis = 0, position = -1;
		for(int i = 1; i < n; i++)  // picks each value from the data
         	{
         		for(int j = 0; j < i; j++)  // this array compares the value picked above with all the before items in the data
         		{
         			if(data[i] > data[j] && lisCount[i] < lisCount[j] + 1)      
         			{
         				lisCount[i] = 1 + lisCount[j];
         			}                                 
         		}
         	}

         	for(int i = n-2; i >= 0; i--)  // picks each value from the data
         	{
         		for(int j = n-1; j > i; j--)  // this array compares the value picked above with all the before items in the data
         		{
         			if(data[i] > data[j] && ldsCount[i] < ldsCount[j] + 1)      
         			{
         				ldsCount[i] = 1 + ldsCount[j];
         			}                                 
         		}
         	}
         	
         	bitonic = lisCount[0] + ldsCount[0] - 1;
         	for(int i = 1; i < n; i++)
         	{
         		if(lisCount[i] + ldsCount[i] - 1 > bitonic)
         			bitonic = lisCount[i] + ldsCount[i] - 1;
         	}
         		
                return bitonic;	

        }
	
}
         
