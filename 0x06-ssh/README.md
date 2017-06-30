[![Holberton logo](https://www.holbertonschool.com/assets/holberton-logo-1cc451260ca3cd297def53f2250a9794810667c7ca7b5fa5879a569a457bf16f.png)](https://www.holbertonschool.com/)
# 0x06. SSH

### Author: Elaine Yeung [<img src="https://user-images.githubusercontent.com/23224088/27935507-4e614b68-6260-11e7-8b20-d0352ef3ff53.png" height="18px"/>](https://twitter.com/egsy) 

## Synopsis
This project introduces the concepts of **server management** in software development.

### At the end of this project stuents should be able to explain to anyone, **without the help of Google**:
*   What is a server
*   Where server usually live
*   What is SSH
*   How to create an SSH RSA key pair
*   How to connect to a remote host using an SSH RSA key pair

### Resources
Read:

*   [What is a (physical) server - text](https://en.wikipedia.org/wiki/Server_(computing)#Hardware_requirement)
*   [What is a (physical) server - video](https://www.youtube.com/watch?v=B1ANfsDyjeA)
*   [SSH essentials](https://www.digitalocean.com/community/tutorials/ssh-essentials-working-with-ssh-servers-clients-and-keys)

man: `ssh`, `ssh-keygen`, `env`

### Project Requirements
#### Bash 
*   Allowed editors: `vi`, `vim`, `emacs`
*   All your files will be interpreted on Ubuntu 14.04 LTS
*   All your files should end with a new line
*   A `README.md` file, at the root of the folder of the project, is mandatory
*   All your Bash script files must be executable
*   The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`
*   The second line of all your Bash scripts should be a comment explaining what is the script doing

The advantage of using `#!/usr/bin/env bash` instead of `/bin/bash` for instance is that it will make your script portable for different OS where Bash might be in a different location.

## Project Breakdown
Task # | Type | Short description | File name and link |
---: | --- | --- | --- |
0 | **Mandatory** | <p>Write a Bash script that uses <code>ssh</code> to connect to your server using the private key <code>~/.ssh/holberton</code> with the user <code>ubuntu</code>.</p><p>Requirements:</p><ul><li>Only use <code>ssh</code> single-character flags</li><li>You cannot use <code>-l</code></li><li>Do not need to handle the case of a private key protected by a passphrase</li></ul> | File: [0-use_a_private_key](./0-use_a_private_key)
1 | **Mandatory** | <p>Write a Bash script that creates a RSA key pair.</p><p>Requirements:</p><ul><li>Name of the created private key must be <code>holberton</code></li><li>Number of bits in the created key to be created 4096</li><li>The created key must be protected by a passphrase</li></ul> | File: [1-create_ssh_key_pair](./1-create_ssh_key_pair)
2 | **Mandatory** | <p>Your Ubuntu Vagrant machine has an SSH configuration file for the local SSH client, let&#39;s configure it to our needs so that you can connect to a server without typing a password.    Share your SSH client configuration in your answer file.</p><p>Requirements:</p><ul><li>Your SSH client configuration must be configured to use the private key <code>~/.ssh/holberton</code></li><li>Your SSH client configuration must be configured to refuse to authenticate using a password</li></ul> | File: [2-ssh_config](./2-ssh_config)


