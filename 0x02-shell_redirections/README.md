#Project 0x02. Shell, I/O Redirections and filters
##Description
This project builds upon previous knowledge with the introduction of [I/O Redirections](http://linuxcommand.org/lc3_lts0070.php) and [Special Characters](http://mywiki.wooledge.org/BashGuide/SpecialCharacters).

New commands introduced in this project include:
`echo`, `cat`, `head`, `tail`, `find`, `wc`, `sort`, `uniq`, `grep`, `tr`, `rev`, `cut`

#### 0. Hello World
Write a script that prints “Hello, World”, followed by a new line to the standard output.
#### 1. Confused smiley
Write a script that displays a confused smiley "(Ôo)'.
#### 2. Let's display a file mandatory

Display the content of the /etc/passwd file.
#### 3. What about 2? mandatory
4. Last lines of a file mandatory
Display the content of /etc/passwd and /etc/hosts
#### 4. Last lines of a file mandatory

Display the last 10 lines of /etc/passwd
#### 5. I'd prefer the first ones actually mandatory
Display the first 10 lines of /etc/passwd
#### 6. Line #2 mandatory

Write a script that displays the third line of the file iacta.
#### 7. It is a good file that cuts iron without making a noise mandatory

Write a shell script that creates a file named exactly \*\\'"Holberton School"\'\\*$\?\*\*\*\*\*:) containing the text Holberton School ending by a new line.
#### 8. Save current state of directory mandatory

Write a script that writes into the file ls_cwd_content the result of the command ls -la. If the file ls_cwd_content already exists, it should be overwritten. If the file ls_cwd_content does not exist, create it.
#### 9. Duplicate last line mandatory

Write a script that duplicates the last line of the file iacta

The file iacta will be in the working directory
#### 10. No more javascript mandatory

Write a script that deletes all the regular files (not the directories) with a .js extension that are present in the current directory and all its subfolders.
#### 11. Don't just count your directories, make your directories count mandatory

Write a script that counts the number of directories and sub-directories in the current directory.

The current and parent directories should not be taken into account
Hidden directories should be counted
#### 12. What’s new mandatory

Create a script that displays the 10 newest files in the current directory.
#### 13. Being unique is better than being perfect mandatory

Create a scripts that takes a list of words as input and prints only words that appear exactly once.
#### 14. It must be in that file mandatory

Display lines containing the pattern "root" from the file /etc/passwd
#### 14. It must be in that file mandatory

Display lines containing the pattern "root" from the file /etc/passwd
#### 15. Count that word mandatory

Display the number of lines that contain the pattern "bin" in the file /etc/passwd
#### 16. What's next? mandatory

Display lines containing the pattern "root" and 3 lines after them in the file /etc/passwd.
#### 17. I hate bins mandatory

Display all the lines in the file /etc/passwd that do not contain the pattern "bin".
#### 18. Letters only please mandatory

Display all lines of the file /etc/ssh/sshd_config starting with a letter.
#### 19. A to Z mandatory

Replace all characters A and c from input to Z and e respectively.
#### 20. Without C, you would live in hiago mandatory

Create a script that removes all letters c and C from input.
#### 21. esreveR mandatory

Write a script that reverse its input.

#### 22. DJ Cut Killer mandatory

Write a script that displays all users and their home directories, sorted by users.

Based on the the /etc/passwd file
