# Module 1 First-Time Software Installation

## Hardware Requirements
- Desktop/laptop computer running the latest version of macOS/Linux/Windows operating system (OS)
- Recommended 8GB onboard memory (RAM)
- Recommended 50GB available hard disk storage space (HDD/SSD)
- Webcam and microphone for online Zoom sessions

## Software Requirements

- WSL (for Windows users only)
- Visual Studio Code (VSCode) or any source code editor
- Git Command-Line Interface (CLI)
- GitHuB CLI 
- Conda/Miniconda
- DBeaver database viewer

## WSL for Windows

### *For Windows users only* - Windows Subsystem for Linux (WSL)

Windows users should install WSL which allows you to run Windows and Linux at the same time on a Windows machine. WSL allows you to install a Linux distribution (e.g. Ubuntu, OpenSUSE, Kali, Debian, etc.) and use Linux applications and utilities such as command-line (CLI) tools. 

Most software engineering and development tools are initially developed for Linux and then adapted for Windows. As a result, they often perform better on Linux. Although Windows versions of popular tools are widely available, we strongly recommend using the Linux version whenever possible for optimal performance.
You must be running Windows 11 or 10 version 2004 and higher. 

Follow the instructions [here](https://learn.microsoft.com/en-us/windows/wsl/install) to install Ubuntu on WSL.

## Visual Studio Code (VSCode)

You will need a code editor to write Python or SQL code in the course. VSCode is a popular source code editor used by developers for writing, debugging and editing code across various programminng languages. 

Download and install VSCode [here](https://code.visualstudio.com/download).

### Install the following vscode extensions

Go to the `Extensions` tab, search for the following extensions in the marketplace and install them:

- Python
- Jupyter

> Windows WSL users, install the Windows version as VSCode will work across both Windows and WSL environments.

## Git vs GitHub

Git and GitHub are two essential tools in software engineering. Git is a version control system that helps developers track changes in their code locally. GitHub is a web-based platform where developers can store and share their Git projects, facilitating collaboration and code management. Together, they enable a workflow where developers work on code locally with Git and then share it on GitHub for others to see, review, and contribute. This combination supports efficient collaboration, version control, and project management, making it indispensable for modern software engineering teams.

## Git CLI

We will be using Git extensively in this course and you will need to install the command line interface (CLI) application on your computer.

### Download and install Git CLI [here](https://git-scm.com/downloads).

> Windows WSL users, please follow instructions for Linux/Unix

## GitHub CLI

GitHub is not the same as Git! 😉

You will need to access your GitHub account from your computer and the GitHub CLI tool simplifies the process of authentication in order to allow Git to manage the files in your account, e.g. `git clone`, `git pull`, `git commit`. 

### Download and install GitHub CLI [here](https://github.com/cli/cli?tab=readme-ov-file#installation).

### TLDR; 

On Linux/WSL Ubuntu using APT package manager:

`sudo apt install gh`

On macOS using Homebrew:

`brew install gh`

### Setup your GitHub Credentials

You will need to authenticate your GitHub account to allow access your files in your repository. 

Type the following command:

`gh auth login`

Follow the on-creen instructions.

1. Select `GitHub.com` as your login account.

2. Select `HTTPS` as your preferred protocal.

3. Select `y` to authenticate Git with your GitHub credentials.

4. Select `Login with a web browser` to authenticate your account.

A one-time code (e.g. 1A23-B567) will be displayed on your terminal. 

Login to your GitHub account with your web browser. After you have logged into your GitHub account, key in the one-time code given earlier.

You should now be able to access your GitHub account using Git CLI commands from your local computer.

## Conda/Miniconda

Conda is a package and environment manager that we will be using throughout this program, to manage our Python packages and environments. Miniconda is a lightweight version of the Anaconda distribution, designed for users who prefer a minimal installation. It includes only the essentials: Python, conda (the package and environment manager), and their dependencies. Unlike Anaconda, which comes preloaded with hundreds of scientific packages, Miniconda allows you to install only the packages you need, making it more flexible and less resource-intensive.

### Download and install miniconda [here](https://www.anaconda.com/docs/getting-started/miniconda/main)

### Download and install miniconda [here](https://www.anaconda.com/docs/getting-started/miniconda/install#quickstart-install-instructions)

> Windows WSL users, please follow instructions for Linux/Unix

## DBeaver

We will be using DBeaver SQL client throughout this course to connect to databases and write SQL code. The free version is called DBeaver Community (dbeaver-ce).

### Download and install DBeaver Community [here](https://dbeaver.io/download/)

> Windows WSL users, please follow instructions for Linux/Unix.
>
> Use the Snap package manager `sudo snap install dbeaver-ce`



