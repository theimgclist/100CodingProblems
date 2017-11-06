/*
    Created by Avinash on 6th November, 2017
*/
import java.io.*;
import java.util.*;
public class EggDropping
{
	public static int output;
	public static void main(String[] args)
	{
		BufferedReader read = new BufferedReader(new InputStreamReader(System.in));
		int n,k,threshold = 0;
		try
		{
		System.out.println("Enter number of eggs : ");
		n = Integer.parseInt(read.readLine());
		System.out.print("Enter number of floors : ");
		k = Integer.parseInt(read.readLine());
		Helper link = new Helper();	
		threshold = link.eggsThresholdFloorCache(n,k);
		}
		catch(IOException e)
		{
			e.printStackTrace();
		}
		System.out.print("The threshold floor for eggs is "+threshold);
	}
}

class Helper
{
	public int eggsThresholdFloor(int eggs, int floors)
	{
		if(floors == 0 || floors == 1)
        		return floors;
        	if(eggs == 1)
        		return floors;
       		int min = Integer.MAX_VALUE, threshold;
      		for(int k = 1; k <= floors; k++)
        	{
        		threshold = Math.max(eggsThresholdFloor(eggs-1, k-1), eggsThresholdFloor(eggs, floors - k));
        		if(threshold < min)
        			min = threshold;
        	}
        	return min + 1;
        		
	}

	public int eggsThresholdFloorCache(int eggs, int floors)
	{
		int cache[][] = new int[eggs+1][floors+1];
		int temp;
		for(int i = 1; i <= eggs; i++)
		{
			cache[i][0] = 0;
			cache[i][1] = 1;	
	        }
	        for(int i = 1; i <= floors; i++)
	        {
	        	cache[1][i] = i;
	        }
	        for(int i = 2; i <= eggs; i++)
	        {
	        	for(int j = 2; j <= floors; j++)
	        	{
	        		cache[i][j] = Integer.MAX_VALUE;
	        		for(int x = 1; x <= j; x++)
	        		{
	        			temp = 1 + Math.max(cache[i-1][x-1], cache[i][j-x]);
	        			if(temp < cache[i][j])
	        				cache[i][j] = temp;
	        		}
	        	}
	        }
	        return cache[eggs][floors];	
	        	
	}
  	
}	                    	
			