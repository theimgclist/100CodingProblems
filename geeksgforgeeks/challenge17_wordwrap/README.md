[http://www.geeksforgeeks.org/dynamic-programming-set-18-word-wrap/]		
[https://stackoverflow.com/a/857770] -> This SO answer has a good approach.		
Start from the base testcase and code the solution for it.		
From there add more complex test cases.
They call this Test Driven Development TDD.
Line breaking, also known as word wrapping, is the process of breaking a section of text into lines,		
such that it will fit in the available width of a page, window or other display area.		
In text display, line wrap is the feature of continuing on a new line when a line is full,	
such that each line fits in the viewable window, allowing text to be read from top to bottom without any horizontal scrolling.		
One approach to solve this problem is by Greedy algorithm.	
Put as many words as possible in the first line and move to the next line.	
Using this approach, there will be fewer lines but chances are that the words are not wrapped/distributed uniformly across the display.		
```
SpaceLeft := LineWidth
for each Word in Text
    if (Width(Word) + SpaceWidth) > SpaceLeft
        insert line break before Word in Text
        SpaceLeft := LineWidth - Width(Word)
    else
        SpaceLeft := SpaceLeft - (Width(Word) + SpaceWidth)	
```	
[https://www.youtube.com/watch?v=RORuwHiblPc] -> This video by Tushar explains the DP approach really well.		
I was trying different cases. If any of the words length is greater than the width of display, that has to be handled.		
By initializing the text width size to length of the word with maximum length, this problem can be handled.		