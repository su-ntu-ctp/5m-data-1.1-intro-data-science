# Lesson

## Brief

## Preparation

### Prerequisite knowledge for this program

Familarity with Python programming language, at an intermediate level. At least an understanding of and ability to code the following concepts:

- Variables
- Data types
- Operators
- Control structures
- Loops
- Built-in methods and functions
- Classes and objects

### Lesson Overview

This lesson contains a lot of software installations. Learners should expect hiccups and some waiting time while instructor is troubleshooting issues for other learners. 

---

## Part 1 - Introduction to data science and databases

Conceptual knowledge, refer to slides.

---

## Part 2 - Introduction to data science toolbox

To get started, we'll need to set up your environment with essential software applications that will allow you to run models and execute Python and SQL code.

One key aspect of this course is learning to use the Command Line Interface (CLI). The CLI is a powerful tool that data scientists and engineers use to interact with their computers and execute commands efficiently. Instead of clicking through a graphical user interface (GUI), you'll be typing commands into a text terminal application.

![CLI image](./assets/linux_terminal.png)

If you're new to the CLI, don't worry! While it might seem intimidating at first, using command-line tools will become second nature as you progress through the course. The CLI offers several advantages for data scientists:

- **Efficiency**: Executing commands quickly without navigating through menus
- **Automation**: Easily scripting repetitive tasks
- **Flexibility**: Accessing powerful tools and utilities

To help you get started with the CLI, here are some excellent online resources and tutorials:

- [Ubuntu CLI Tutorial](https://ubuntu.com/tutorials/command-line-for-beginners) - Linux command line for beginners from Ubuntu
- [Learning the Linux Shell](https://linuxcommand.org/lc3_learning_the_shell.php) - Part 1 of a comprehensive guide to the world of Linux.
- [Basic Linux Commands (video)](https://www.youtube.com/watch?v=7fs1i7TAMck) - One of the many, many Linux CLI tutorials you can find on YouTube

### Please refer to the [installation](./installation.md) file to install the required applications for this module.

---

## Part 3 - Python environments and git + github workflow

### Python environments

We can use conda to install different versions of Python. Conda also allows us to create and manage virtual environments for different projects. A `conda environment` is a self-contained virtual environment that contains its own Python installation and packages. This allows us to have different versions of Python and packages for different projects, without them conflicting with each other.

#### Get a list of conda environment in the system

```bash
conda env list
```

#### Create a conda environment

```bash
conda create -n <env_name> python=<python_version>
```

for example:

```bash
conda create -n myenv python=3.10
```

#### Activate a conda environment

```bash
conda activate <env_name>
```

#### Deactivate a conda environment

```bash
conda deactivate
```

#### Remove a conda environment

```bash
conda remove -n <env_name> --all
```

#### Install packages in a conda environment

```bash
conda install -n <env_name> <package_name>
```

or activate the environment first, then:

```bash
conda install <package_name>
```

to install multiple packages at once:

```bash
conda install <package_name_1> <package_name_2> <package_name_3>
```

#### Uninstall packages in a conda environment

```bash
conda uninstall -n <env_name> <package_name>
```

or activate the environment first, then:

```bash
conda uninstall <package_name>
```

#### Freeze dependencies

Freezing dependencies is the process of writing the dependencies of an environment to a file. This allows us to recreate the exact same environment for the application, with the exact same versions of packages.

Activate the environment first, then:

```bash
conda env export --no-builds > environment.yml
```

> Walk through the creation of an environment for this module

#### Recreate conda environment from environment.yml

```bash
conda env create -f environment.yml
```

#### Running python scripts in a conda environment

After activating the environment, run:

```bash
python <script_name.py>
```

### Git

Git is a version control system which allows us to track changes to our codes.

#### Create a git repository
You need to create an empty repository in the github with a repository name. In the local PC, create a folder with the same name as the repository name. Open the folder in VSCode, and launch a terminal:

```bash
git init
```

#### Add files to staging area

```bash
git add <file_name>
```

or add all files to staging area:

```bash
git add .
```

#### Commit changes

```bash
git commit -m "<commit_message>"
```

for example:

```bash
git commit -m "Initial commit"
```

#### Check status

```bash
git status
```

#### Check commit history

```bash
git log
```

#### Push changes to remote repository

```bash
git push
```

### Github

Github is a cloud-based hosting service for git repositories. It allows us to store our git repositories in the cloud, and collaborate with other developers.

#### Clone a git repository
Go to your desire repository, and forked a copy of the copy under your Github id. Go to the repository destination in the terminal and run the following command:

```bash
git clone <your_repo_url>
```

Then we can open the repo in VSCode.

#### Pull changes from remote repository

```bash
git pull
```

#### Push changes to remote repository

```bash
git push
```

> Walk through the forking of this repository and cloning of the forked repository to the local machine. Then attempt the 1st question of the assignment, and push the changes to the forked repository.
