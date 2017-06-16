>0-what-is-my-pid
>1-list_your_processes
>2-show_your_bash_pid
>3-show_your_bash_pid_made_easy
>4-to_infinity_and_beyond
>5-kill_me_now
>6-kill_me_now_made_easy
>7-highlander
>8-beheaded_process
>9-process_and_pid_file
>10-manage_my_process
>11-zombie.c
>12-screencast_unix_signal
 
<li><a href="http://www.linfo.org/pid.html">Linux PID</a></li>
<li><a href="http://www.thegeekstuff.com/2012/03/linux-processes-environment/">Linux process</a></li>
<li><p><a href="http://www.thegeekstuff.com/2012/03/linux-signals-fundamentals/">Linux signal</a></p></li>
<li><p>man: <code>ps</code>, <code>pgrep</code>, <code>pkill</code>, <code>kill</code>, <code>exit</code></p></li>
<li><p>help: <code>trap</code></p></li>
<p>For those who want to know more and learn about all signals, check out <a href="http://www.computerhope.com/unix/signals.htm">this article</a>.</p>
<p>At the end of this project you are expected to be able to explain, <strong>without the help of Google</strong>:</p>
<li>What is a PID</li>
<li>What is a process</li>
<li>How to find a process PID</li>
<li>How to kill a process</li>
<li>What is a signal</li>
<li>What are the 2 signals that cannot be ignored</li>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be interpreted on Ubuntu 14.04 LTS</li>
<li>All your files should end with a new line</li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>All your Bash script files must be executable</li>
<li>Your Bash script must pass <code>Shellcheck</code> (version <code>0.3.3-1~ubuntu14.04.1</code> via <code>apt-get</code>) without any error</li>
<li>The first line of all your Bash scripts should be exactly <code>#!/usr/bin/env bash</code></li>
<li>The second line of all your Bash scripts should be a comment explaining what is the script doing</li>
    <p>Write a Bash script that displays its PID.</p>
	        <li>GitHub repository: <code>holberton-system_engineering-devops</code></li>
		        <li>Directory: <code>0x05-processes_and_signals</code></li>
			        <li>File: <code>0-what-is-my-pid</code></li>
    <p>Write a Bash script that displays a list of currently running processes.</p>
<p>Requirements:</p>
<li>Must show all processes, for all users, including those which might not have a TTY</li>
<li>Display a user-oriented format</li>
<li>Show process hierarchy</li>
	        <li>GitHub repository: <code>holberton-system_engineering-devops</code></li>
		        <li>Directory: <code>0x05-processes_and_signals</code></li>
			        <li>File: <code>1-list_your_processes</code></li>
    <p>Using your previous exercise command, write a Bash script that displays line containing the <code>bash</code> word, this allowing you to easily get the PID of your Bash process</p>
<p>Requirements:</p>
<li>You cannot use <code>pgrep</code></li>
<li>The third line of your script must be <code># shellcheck disable=SC2009</code> (for more info about ignoring <code>shellcheck</code> error <a href="https://github.com/koalaman/shellcheck/wiki/Ignore">here</a>)</li>
<p>Here we can see that my Bash PID is <code>4404</code>.</p>
	        <li>GitHub repository: <code>holberton-system_engineering-devops</code></li>
		        <li>Directory: <code>0x05-processes_and_signals</code></li>
			        <li>File: <code>2-show_your_bash_pid</code></li>
    <p>Write a Bash script that displays the PID, along with the process name, of processes which name contains the word <code>bash</code>.</p>
<p>Requirements:</p>
<li>You cannot use <code>ps</code></li>
<p>Here we can see that: </p>
<li>For the first iteration: <code>bash</code> PID is <code>4404</code> and that the <code>3-show_your_bash_pid_made_easy</code> script PID is <code>4555</code></li>
<li>For the second iteration: <code>bash</code> PID is <code>4404</code> and that the <code>3-show_your_bash_pid_made_easy</code> script PID is <code>4557</code></li>
	        <li>GitHub repository: <code>holberton-system_engineering-devops</code></li>
		        <li>Directory: <code>0x05-processes_and_signals</code></li>
			        <li>File: <code>3-show_your_bash_pid_made_easy</code></li>
    <p>Write a Bash script that displays <code>To infinity and beyond</code> indefinitely. </p>
<p>Requirements:</p>
<li>In between each iteration of the loop, add a <code>sleep 2</code></li>
<p>Note that I <code>ctrl+c</code> (killed) the Bash script in the example.</p>
	        <li>GitHub repository: <code>holberton-system_engineering-devops</code></li>
		        <li>Directory: <code>0x05-processes_and_signals</code></li>
			        <li>File: <code>4-to_infinity_and_beyond</code></li>
    <p>We killed our <code>4-to_infinity_and_beyond</code> process using <code>ctrl+c</code> in the previous task, there is actually another way to do this.</p>
<p>Write a Bash script that kills <code>4-to_infinity_and_beyond</code> process.</p>
<p>Requirements:</p>
<li>You must use <code>kill</code></li>
<p>Terminal #0</p>
<p>Terminal #1</p>
<p>I opened 2 terminals in this example, started by running my <code>4-to_infinity_and_beyond</code> Bash script in terminal #0 and then moved on terminal #1 to run <code>5-kill_me_now</code>. We can then see in terminal #0 that my process has been terminated.</p>
	        <li>GitHub repository: <code>holberton-system_engineering-devops</code></li>
		        <li>Directory: <code>0x05-processes_and_signals</code></li>
			        <li>File: <code>5-kill_me_now</code></li>
    <p>Write a Bash script that kills <code>4-to_infinity_and_beyond</code> process.</p>
<p>Requirements:</p>
<li>You cannot use <code>kill</code> or <code>killall</code></li>
<p>Terminal #0</p>
<p>Terminal #1</p>
<p>I opened 2 terminals in this example, started by running my <code>4-to_infinity_and_beyond</code> Bash script in terminal #0 and then moved on terminal #1 to run <code>6-kill_me_now_made_easy</code>. We can then see in terminal #0 that my process has been terminated.</p>
	        <li>GitHub repository: <code>holberton-system_engineering-devops</code></li>
		        <li>Directory: <code>0x05-processes_and_signals</code></li>
			        <li>File: <code>6-kill_me_now_made_easy</code></li>
    <p>Write a Bash script that displays: </p>
<li><code>To infinity and beyond</code> indefinitely</li>
<li>With a <code>sleep 2</code> in between each iteration</li>
<li><code>I am invincible!!!</code> when receiving a <code>SIGTERM</code> signal</li>
<p>Make a copy of your <code>6-kill_me_now_made_easy</code> script, name it <code>67-kill_me_now_made_easy</code>,  that kills the <code>7-highlander</code> process instead of the <code>4-to_infinity_and_beyond</code> one.</p>
<p>Terminal #0</p>
<p>Terminal #1</p>
<p>I started <code>7-highlander</code> in Terminal #0 and then run <code>67-kill_me_now_made_easy</code> in terminal #1, for every iteration we can see <code>I am invincible!!!</code> appearing in terminal #0.</p>
	        <li>GitHub repository: <code>holberton-system_engineering-devops</code></li>
		        <li>Directory: <code>0x05-processes_and_signals</code></li>
			        <li>File: <code>7-highlander</code></li>
    <p>Write a Bash script that kills the process <code>7-highlander</code>.</p>
<p>Terminal #0</p>
<p>Terminal #1</p>
<p>I started <code>7-highlander</code> in Terminal #0 and then run <code>8-beheaded_process</code> in terminal #1 and we can see that the <code>7-highlander</code> has been killed.</p>
	        <li>GitHub repository: <code>holberton-system_engineering-devops</code></li>
		        <li>Directory: <code>0x05-processes_and_signals</code></li>
			        <li>File: <code>8-beheaded_process</code></li>
    <p>Write a Bash script that: </p>
<li>Creates the file <code>/var/run/holbertonscript.pid</code> containing its PID</li>
<li>Displays <code>To infinity and beyond</code> indefinitely</li>
<li>Displays <code>I hate the kill command</code> when receiving a SIGTERM signal</li>
<li>Displays <code>Y U no love me?!</code> when receiving a SIGINT signal</li>
<li>Deletes the file <code>/var/run/holbertonscript.pid</code> and terminate itself when receiving a SIGQUIT or SIGTERM signal</li>
<p><img src="http://i.imgur.com/m363Nha.jpg" alt="&quot;Y U no love me?!&quot; picture"></p>
<p>Executing the <code>9-process_and_pid_file</code> script and killing it with <code>ctrl+c</code>.</p>
<p>Terminal #0</p>
<p>Terminal #1</p>
<p>Starting <code>9-process_and_pid_file</code> in the terminal #0 and then killing it in the terminal #1.</p>
	        <li>GitHub repository: <code>holberton-system_engineering-devops</code></li>
		        <li>Directory: <code>0x05-processes_and_signals</code></li>
			        <li>File: <code>9-process_and_pid_file</code></li>
    <p><img src="http://i.imgur.com/o9q0iPA.jpg" alt="Priest stopping data center with /etc/init.d/DEAMON STOP"></p>
<p>Read:</p>
<li><a href="http://bashitout.com/2013/05/18/Ampersands-on-the-command-line.html">&amp;</a></li>
<li><a href="http://www.ghacks.net/2009/04/04/get-to-know-linux-the-etcinitd-directory/">init.d</a></li>
<li><a href="https://en.wikipedia.org/wiki/Daemon_(computing)">Daemon</a></li>
<li><a href="http://wiki.bash-hackers.org/scripting/posparams">Positional parameters</a></li>
<p>man: <code>sudo</code></p>
<p>Programs that are detached from the terminal and running in the background are called daemons or processes, need to be managed. The general minimum set of instructions is: <code>start</code>, <code>restart</code> and <code>stop</code>. The most popular way of doing so on Unix system is to use the init scripts.</p>
<p>Write a <code>manage_my_process</code> Bash script that: </p>
<li>Indefinitely writes <code>I am alive!</code> to the file <code>/tmp/my_process</code></li>
<li>In between every <code>I am alive!</code> message, the program should pause for 2 seconds</li>
<p>Write Bash (init) script <code>10-manage_my_process</code> that manages <code>manage_my_process</code></p>
<p>Requirements:</p>
<li>When passing the argument <code>start</code>:
<li>Starts <code>manage_my_process</code></li>
<li>Creates a file containing its PID in <code>/var/run/my_process.pid</code></li>
<li>Displays <code>manage_my_process started</code></li>
<li>When passing the argument <code>stop</code>:
<li>Stops <code>manage_my_process</code><br></li>
<li>Deletes the file  <code>/var/run/my_process.pid</code></li>
<li>Displays <code>manage_my_process stopped</code></li>
<li>When passing the argument <code>restart</code>
<li>Stops <code>manage_my_process</code><br></li>
<li>Deletes the file  <code>/var/run/my_process.pid</code></li>
<li>Starts <code>manage_my_process</code></li>
<li>Creates a file containing its PID in <code>/var/run/my_process.pid</code></li>
<li>Displays <code>manage_my_process restarted</code></li>
<li>Displays <code>Usage: manage_my_process {start|stop|restart}</code> if any other argument or no argument is passed</li>
<p>Note that this init script is far from being perfect (but good enough for the sake of manipulating process and PID file), for example we do not handle the case where we check if a process is already running when doing <code>./10-manage_my_process start</code>, in our case it will simply create a new process instead of saying that it is already started.</p>
	        <li>GitHub repository: <code>holberton-system_engineering-devops</code></li>
		        <li>Directory: <code>0x05-processes_and_signals</code></li>
			        <li>File: <code>10-manage_my_process</code></li>
    <p><a href="http://fineartamerica.com/featured/zombie-seahorse-lauren-b.html"><img src="http://i.imgur.com/C6mO7b3.jpg" alt="Zombie searhose"></a></p>
<p>Read <a href="https://zombieprocess.wordpress.com/what-is-a-zombie-process/">what a zombie process is</a>.</p>
<p>Write a C program that creates 5 zombie processes.</p>
<p>Requirements:</p>
<li>For every zombie process created, it displays <code>Zombie process created, PID: ZOMBIE_PID</code></li>
<li>Your code should use the Betty style. It will be checked using <code>betty-style.pl</code> and <code>betty-doc.pl</code></li>
<li>When you code is done creating the parent process and the zombies, use the function bellow</li>
<p>Example:</p>
<p>Terminal #0</p>
<p>Terminal #1</p>
<p>In Terminal #0, I start by compiling <code>11-zombie.c</code> and executing <code>zombie</code> which creates 5 zombie processes.
	        <li>GitHub repository: <code>holberton-system_engineering-devops</code></li>
		        <li>Directory: <code>0x05-processes_and_signals</code></li>
			        <li>File: <code>11-zombie.c</code></li>
    <p>Now that you master signals, what about sharing your knowledge?</p>
<p>Create a screencast where you live-code a task of your choice from this project or even a mix of them.</p>
<p>Requirements:</p>
<li>Step by step video</li>
<li>Two minutes of above</li>
<li>Done in English</li>
<li>Published to Youtube</li>
<p>While you are free to choose the recording system to record the screencast, I highly recommend <a href="https://screencast-o-matic.com">screencast-o-matic</a>.</p>
<p>Once you are done, please share the Youtube URL in your answer file and below.</p>
<p>We&#39;ll be watching you!</p>
<p><img src="https://media.giphy.com/media/l0MYEI1kqBRBrpEdO/giphy.gif" alt="eating popcorn and being impressed"></p>
	        <li>GitHub repository: <code>holberton-system_engineering-devops</code></li>
		        <li>Directory: <code>0x05-processes_and_signals</code></li>
			        <li>File: <code>12-screencast_unix_signal</code></li>
					          <p>Unless stated, all your projects will be auto-corrected with Ubuntu 14.04 LTS.</p>
