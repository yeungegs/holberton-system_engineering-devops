#!/usr/bin/python3
import requests



def count_words(subreddit, word_list):
    """script that queries Reddit API then parses the title of all hot articles
    Must be recursive
    Results should be printed in descending order, by the count, not the title. Words with no matches should be skipped and not printed.
    Results are based on the number of times a keyword appears, not titles it appears in. 'java java java' counts as 3 separate occurences of java.
    To make life easier, 'java.' or 'java!' or 'java_' should not count as 'java'
    Hints:
        Ensure that you are NOT following redirects.
        Your code will NOT pass if you are using a loop and not recursively calling the function!
        This /can/ be done with a loop but the point is to use a recursive function. :)
    Returns:
        sorted count of given keywords
               case-insensitive
               delimited by spaces.
                         exampleJavascript should count as javascript, but java should not).
        If no posts match or the subreddit is invalid, print a newline.
   """


    
