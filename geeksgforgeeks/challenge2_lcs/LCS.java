/*
     Created by Avinash on 30th July, 2017
 */
import java.io.*;
import java.util.*;
import java.lang.*;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.BufferedReader;
public class LCS 
{
	public static String theSequence = "";
	public static void main(String[] args) 
	{
        	BufferedReader read = new BufferedReader(new InputStreamReader(System.in));
		String data1, data2; // contains the actual data
		int lcs = 0; // holds the length of longest common subsequence
		int i = 0; // loop control variable
		try
		{       
			System.out.print("Enter the first sequence : ");
			data1 = read.readLine();
			System.out.print("Enter the second sequence : ");
			data2 = read.readLine();
                        Helper link = new Helper();
                        lcs = link.calculate_LCS(data1, data2); //calling the method that calculates the longest common subsequence
                }
		catch (IOException e)
		{
			e.printStackTrace();
		}
                System.out.println("The length of longest common subsequence is : "+lcs);
                System.out.print("The longest common subsequence is : "+theSequence);
	}

}
class Helper
{

	public int calculate_LCS(String s1, String s2)
	{
		int len1, len2,length;
		len1 = s1.length();
		len2 = s2.length();
		int[][] lcs = new int[len1 + 1][len2 + 1]; // this array contains the lcs
		for(int i = 0; i <= len1; i++) 
         	{
         		for(int j = 0; j <= len2; j++)  
         		{
         			if( i == 0 || j == 0)
         				lcs[i][j] = 0;
         			else if(s1.charAt(i-1) == s2.charAt(j-1))
         				lcs[i][j] = 1 + lcs[i-1][j-1];
         			else
         				lcs[i][j] = Math.max(lcs[i-1][j], lcs[i][j-1]);
         		}
         	}
         	length = lcs[len1][len2];
         	char[] sequence = new char[length + 1];
         	sequence[length] = '\0';
         	int i = len1, j = len2;
         	while(i > 0 && j > 0)
         	{
         		if(s1.charAt(i - 1) == s2.charAt(j - 1))
         		{
         			sequence[length - 1] = s1.charAt(i - 1);		
         			i--;
         			j--;
         			length--;
         		}
         		else if(lcs[i-1][j] > lcs[i][j-1])
         			i--;
         		else
         			j--;
         	}
         	LCS.theSequence = new String(sequence);	
                return lcs[len1][len2];
	}
}	
         
