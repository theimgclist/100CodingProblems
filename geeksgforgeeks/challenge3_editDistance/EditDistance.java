/*
     Created by Avinash on 1st August, 2017
 */
import java.io.*;
import java.util.*;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.BufferedReader;
public class EditDistance 
{
	public static int editDistance;
	public static void main(String[] args) 
	{
        	BufferedReader read = new BufferedReader(new InputStreamReader(System.in));
		String word1, word2;
		try
		{
			System.out.print("Enter first string : "); 
			word1 = read.readLine();
			System.out.print("Enter second string : ");
			word2 = read.readLine();
			Helper link = new Helper();
			editDistance = link.editChallenge(word1, word2);
			
		}
		catch (IOException e)
		{
			e.printStackTrace();
		}
                System.out.println("The number of operations required to transform first string to second is : "+editDistance);
	}

}
class Helper
{

        public int editChallenge(String w1, String w2)
	{
		int len1 = w1.length();
		int len2 = w2.length();
		int i,j;
		if(len1 == 0)
			return len2;
		if(len2 == 0)
			return len1;	
		int[][] cache = new int[len1 + 1][len2 +1];
		for(i = 0 ; i <= len1; i++)
		{
			for( j = 0 ; j <= len2; j++)
			{
				if(i == 0)
					cache[i][j] = j;
				else if(j == 0)
					cache[i][j] = i;
				else if(w1.charAt(i - 1) == w2.charAt(j - 1))
					cache[i][j] = cache[i - 1][j - 1];
				else
					cache[i][j] = 1 + Math.min(cache[i][j-1], Math.min(cache[i - 1][j], cache[i - 1][j - 1]));
					
			}
		}
		return cache[len1][len2];	
        }
}
         
