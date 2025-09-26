# WSL

## Basic Linux Command

- Display the current path of your directory
```bash
pwd
```

- List non-hidden files and folders of the current directory
```bash
ls
```

- List all files and folders of the current directory including hidden files and folders
```bash
ls -al
```

- Navigate to a folder
```bash
cd /home/dsai/my_projects
```

- Navigate to previous folder
```bash
cd ..
```


### Connection to WSL in VSCode





# Git and GitHub
For every new lesson, fork + clone the lesson repository (repo).
For a new lesson, fork the repo (one time only).
Go to the NTU repository, e.g. https://github.com/su-ntu-ctp/5m-data-1.1-intro-data-science.
Click on the Fork button at the top of the repo page.
Create a new fork by confirming the name (for example Dave) of your new repo, e.g. dave/5m-data-1.1-intro-data-science.
Clone the repo to your local PC
Go to your local Terminal window (WSL users: check for $ prompt).
Type pwd to check your working directory. Othewise, use cd to change to the correct directory.
Type git clone https://github.com/dave/5m-data-1.1-intro-data-science.
Change to your cloned directory with the cd, e.g.  cd 5m-data-1.1-intro-data-science.
Update changes from NTU repo
Go to the your forked repo, e.g. https://github.com/dave/5m-data-1.1-intro-data-science.
Click on Sync fork button on the repo home page to update your repo with the new content from the NTU repo. If there are no changes, you will see a message "The branch is not behind the upstream"---nothing to update.
Go to your local Terminal window and change to your cloned directory e.g.  cd 5m-data-1.1-intro-data-science.
Type git pull to download the new changes from your personal forked repository.


How to access GitHub repos from VSCode
You can access your GitHub repos directly from VSCode. 

https://code.visualstudio.com/docs/sourcecontrol/intro-to-git#_pushing-and-pulling-remote-changes

https://code.visualstudio.com/docs/sourcecontrol/intro-to-git#_open-a-git-repository


https://discord.com/channels/1165846570177150996/1393771280364208138