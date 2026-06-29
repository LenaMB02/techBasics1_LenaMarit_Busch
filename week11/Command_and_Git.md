## Terminal

Have you ever seen a hacking scene in a film, where lines of text are streaming in a magic black window? That's where we are going to explore now.

**Terminal** is one of the coolest place to interact with your computer. It is a text-based user interface that allows you to interact with a computer by typing **commands**. 

You can open the terminal window from your PyCharm. It is in principle the same as if you open the terminal window from your system, just the python version as well as environment are already configured for you.

Try typing the following command into your system terminal:

`python --version`

You shall be able to see something like `Python 3.12.11`, or the version of your default python installed on your laptop. 

In case you get `command not found: python`, try `python3 --version`. If `python3` works instead of `python` for you, you can just use `python3` instead of `python` in your general system environment. If both dont work for you, better stay with terminal inside PyCharm for now, or you need to [install Python manually](https://www.python.org/downloads/) for your system.

Now let's get to know our computer a bit more inside a terminal.

Depends on where you are accessing this terminal, you might see something like the following:

`(.venv) Mac:techBasics1 cqx931$`

`(.venv)` means the current environment you are using. Here `.venv` is the default python environment that comes with PyCharm. It can also have another name if you named it differently.
`.` means it is a hidden folder. A python virtual environment is a context in which you run Python code. It is a common and good practice in Python to set up a dedicated environment that is separated from your system. 
One of the reasons to do so is that if we mess up something, it won't influence the rest of the system. We will learn more about environment later in the next session.

`techBasics1` is your current location. If you are opening the terminal from PyCharm it shall show you "techBasics1_your_name" instead.

`cqx931` here is my username. You shall see your username here instead.

---

Here is a list of basic commands: 

**If you use PowerShell, the Windows alternatives are shown where the command differs.**

`cd` change the directory where you are currently locating in your system.

`cd ~` go to your home directory

`cd Desktop/techBasics1/week1` go to a particular location

`cd ../` go outside the current folder

`ls` list all the files in the current directory. (PowerShell: `dir`)

`ls -l` list all the files with more information. (PowerShell: `dir`)

`ls -A` for hidden files. (PowerShell: `dir -Force`)

`mkdir` make a new directory.

`touch <filename>` create a new empty file, inside the current directory. (PowerShell: `ni <filename>`. `ni` is a default alias for the `New-Item` command)

`rm <filename>` remove a file. (PowerShell: `ri <filename>`. `ri` is a default alias for the `Remove-Item` command)

`mv <source> <destination>` move a file from one location to another location. (PowerShell: `mi <source> <destination>`. `mi` is a default alias for the `Move-Item` command)

`cp <source> <destination>` create a copy of the file from the first location to the second location. (PowerShell: `ci <source> <destination>`. . `ci` is a default alias for the `Copy-Item` command)

`open` open up a directory in your finder (PowerShell: `ii`, it is a default alias for the `Invoke-Item` command)

`rmdir <directory>` remove a directory, but only if it's empty. (PowerShell: `ri <directory> -Recurse -Force` for non-empty directories)

`python my_file.py` runs a Python file

### Exercise 1
Create a `week11` folder inside your GitHub repository with command line ONLY

---

## Git & GitHub

We have been committing to our GitHub repository through PyCharm or the online interface. 
However, what these interfaces do are actually calling terminal commands in the back. 
Today we are going to learn what are actually happening behind the scene.

`git init` If you are starting fresh, you will first need to initialize a directory as a Git repository. Run this command inside the directory you are working on.

`git clone [url]` If you already created a repository on GitHub, or if you want to retrieve a Git repository from someone else.

`git status` show modified files in your working directory

`git add [file]` add a file to your next commit. For multiple files, separate file names with space.

`git add -A` add all changes to your next commit

`git commit [file] -m "[message]"` commit your staged content. For multiple files, separate file names with space.

`git log` check your commit history

`git help` check all available commands

`git remote -v` check your current git remote setup

`git remote add [alias] [url]` add a git URL as an alias

`git push` Push the local commit to the remote GitHub repository. By default, it pushes to origin/main

`git pull` fetch and merge commits from remote GitHub repository

`git reset HEAD^` reset the last commit

For more, check out this [cheat sheet for the most commonly used Git commands](https://education.github.com/git-cheat-sheet-education.pdf)

\* To be able to push directly to GitHub from command line, you will need a Personal Access Token. Please checkout [the following instructions](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-personal-access-token-classic) to generate a personal access token. 
The first time you try to push from command line, the terminal will ask you for password, paste this personal access token instead of your GitHub password.

### Exercise 2
- Try to do the following through command line:
  - git add the `code_study.md` file to your GitHub repository
  - git commit it with a message of your like
  - git push it to your GitHub repository online

Optional: You can even copy the file over to your GitHub repository from the class repository through command line, but you can also just drag it in the system UI.