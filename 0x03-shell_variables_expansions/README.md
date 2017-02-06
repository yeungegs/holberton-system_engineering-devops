#Project 0x03. Shell, init files, variables and expansions
##Description
This project builds upon previous knowledge with the introduction of [Expansions](http://linuxcommand.org/lc3_lts0080.php), [Shell Arithmetic](https://www.gnu.org/software/bash/manual/html_node/Shell-Arithmetic.html), [Variables](http://tldp.org/LDP/Bash-Beginners-Guide/html/sect_03_02.html), [Shell initialization files](http://tldp.org/LDP/Bash-Beginners-Guide/html/sect_03_01.html) and [The alias Command](http://www.linfo.org/alias.html).

New commands introduced in this project include:
`printenv`, `set`, `unset`, `export`, `alias`, `unalias`, `.`, `source`, `printf`

####0.`<o>`
Create a script that creates an alias.
- Name: `ls`
- Value: `rm *`

####1. Hello you
Create a script that prints `hello user`, where user is the current Linux user.
####2. The path to success is to take massive, determined action
Add `/action` to the `PATH`. `/action` should be the last directory the shell looks into when looking for a program.
####3. If the path be beautiful, let us not ask where it leads
Create a script that counts the number of directories in the `PATH`.
####4. Global variables
Create a script that lists environment variables.
####5. Local variables
Create a script that lists all local variables and environment variables, and functions.
####6. Local variable
Create a script that creates a new local variable.
Name: `BETTY`
Value: `Holberton`
####7. Global variable
Create a script that creates a new global variable.
Name: `HOLBERTON`
Value: `Betty`
####8. Every addition to true knowledge is an addition to human power
Write a script that prints the result of the addition of 128 with the value stored in the environment variable `TRUEKNOWLEDGE`, followed by a new line.
####9. Divide and rule
Write a script that prints the result of `POWER` divided by `DIVIDE`, followed by a new line.
`POWER` and `DIVIDE` are environment variables
####10. Love is anterior to life, posterior to death, initial of creation, and the exponent of breath
Write a script that displays the result of `BREATH` to the power `LOVE`
- `BREATH` and `LOVE` are environment variables
- The script should display the result, followed by a new line

####11. There are 10 types of people in the world -- Those who understand binary, and those who don't
Write a script that converts a number from base 2 to base 10.
- The number in base 2 is stored in the environment variable `BINARY`
- The script should display the number in base 10, followed by a new line

####12. Combination
Create a script that prints all possible combinations of two letters, except `oo`.
- Letters are lower cases, from `a` to `z`
- One combinaison per line
- The output should be alpha ordered, starting with `aa`
- Do not print `oo`
- Your script file should contain maximum 64 characters

####13. Floats
Write a script that prints a number with two decimal places.
The number will be stored in the environment variable `NUM`.
####14. Decimal to Hexadecimal
Write a script that converts a number from base 10 to base 16.
- The number in base 10 is stored in the environment variable `DECIMAL`
- The script should display the number in base 16, followed by a new line
