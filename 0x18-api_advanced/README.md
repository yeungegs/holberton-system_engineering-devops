0-subs.py
1-top_ten.py
2-recurse.py
100-count.py
<!-- Task Body -->
  <p>Write a function that queries the Reddit API (https://www.reddit.com/dev/api/) and returns the number of subscribers (not active users, total subscribers) for a given subreddit. If an invalid subreddit is given, the function should return 0.</p>

<p>Hint: No authentication is necessary for most features of the Reddit API. If you&#39;re getting errors related to Too Many Requests, ensure you&#39;re setting a custom User-Agent.</p>

<p>Requirements:</p>

<ul>
<li>Prototype: <code>def number_of_subscribers(subreddit)</code></li>
<li>If not a valid subreddit, return 0.</li>
<li>NOTE: Invalid subreddits may return a redirect to search results. Ensure that you are not following redirects.</li>
</ul>

<!-- Task Body -->
  <p>Write a function that queries the Reddit API (https://www.reddit.com/dev/api/) and prints the titles of the first 10 hot posts listed for a given subreddit.</p>

<p>Requirements:</p>

<ul>
<li>Prototype: <code>def top_ten(subreddit)</code></li>
<li>If not a valid subreddit, print None.</li>
<li>NOTE: Invalid subreddits may return a redirect to search results. Ensure that you are not following redirects.</li>
</ul>

<!-- Task Body -->
  <p>Write a <em>recursive function</em> that queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit. If no results are found for the given subreddit, the function should return None.</p>

<p>Hint: The Reddit API uses pagination for separating pages of responses.</p>

<p>Requirements:</p>

<ul>
<li>Prototype: <code>def recurse(subreddit, hot_list=[])</code></li>
<li>Note: You may change the prototype, but it must be able to be called with just a subreddit supplied. AKA you can add a counter, but it must work without supplying a starting value in the main.</li>
<li>If not a valid subreddit, return None.</li>
<li>NOTE: Invalid subreddits may return a redirect to search results. Ensure that you are not following redirects.</li>
</ul>

<p>Your code will NOT pass if you are using a loop and not recursively calling the function! This /can/ be done with a loop but the point is to use a recursive function. :)</p>

<!-- Task Body -->
  <p>Write a <em>recursive function</em> that queries the Reddit API, parses the title of all hot articles, and prints a sorted count of given keywords (case-insensitive, delimited by spaces. Javascript should count as javascript, but java should not).</p>

<p>Requirements:</p>

<ul>
<li>Prototype: <code>def count_words(subreddit, word_list)</code></li>
<li>Note: You may change the prototype, but it must be able to be called with just a subreddit supplied and a list of keywords. AKA you can add a counter or anything else, but the function must work without supplying a starting value in the main.</li>
<li>Results should be printed in descending order, by the count, not the title. Words with no matches should be skipped and not printed.</li>
<li>Results are based on the number of times a keyword appears, not titles it appears in. &#39;java java java&#39; counts as 3 separate occurences of java.</li>
<li>To make life easier, &#39;java.&#39; or &#39;java!&#39; or &#39;java_&#39; should not count as &#39;java&#39;</li>
<li>If no posts match or the subreddit is invalid, print a newline.</li>
<li>NOTE: Invalid subreddits may return a redirect to search results. Ensure that you are NOT following redirects.</li>
</ul>

<p>Your code will NOT pass if you are using a loop and not recursively calling the function! This /can/ be done with a loop but the point is to use a recursive function. :)</p>

[![Holberton logo](https://www.holbertonschool.com/assets/holberton-logo-1cc451260ca3cd297def53f2250a9794810667c7ca7b5fa5879a569a457bf16f.png)](https://www.holbertonschool.com/)
# NAME OF PROJECT

### Author: Elaine Yeung [<img src="https://user-images.githubusercontent.com/23224088/27935507-4e614b68-6260-11e7-8b20-d0352ef3ff53.png" height="18px"/>](https://twitter.com/egsy) 

## Synopsis
This project introduces **INSERT DESCRIPTION HERE**

### At the end of this project students should be able to explain to anyone, **without the help of Google**:

### Resources

### Project Requirements
-   Allowed editors: `vi`, `vim`, `emacs`
-   All your Bash script files will be interpreted on Ubuntu 14.04 LTS
-   All your files should end with a new line
-   A `README.md` file, at the root of the folder of the project, is mandatory
-   All your Bash script files must be executable
-   Your Bash script must pass `shellcheck` without any error
-   The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`
-   The second line of all your Bash scripts should be a comment explaining what is the script doing

The advantage of using `#!/usr/bin/env bash` instead of `/bin/bash` for instance is that it will make your script portable for different OS where Bash might be in a different location.

## Project Breakdown
Task # | Type | Short description | File name and link |
---: | --- | --- | --- |
0 | **Mandatory** | | 
1 | **Mandatory** | | 
2 | **Mandatory** | | 
3 | **Mandatory** | | 
4 | **Mandatory** | | 
5 | **Mandatory** | | 

