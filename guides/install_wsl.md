# Install WSL for Windows user

There are 2 processes in installing WSL. Both processes use the same command.
- First process is to install the system component mainly `Virtual Machine Platform`. You need to reboot the PC after installation of the system component.
- The second process is to install the Linux operating system. We will be using the default `Ubuntu`



## Install WSL System Component
We need to run the following command from **Windows Powershell as administrator**. 

```bash
wsl --install
```

The resulting screen, should be similar to below:
![assets/wsl/wsl1.png](../assets/wsl/wsl1.png)

> **Please note that the screen may varies according to different version of Windows. For Window 10 users, you may see 2 components installed instead of 1.**

After installation, we need to **reboot the PC**.

You can check the component installed using `Turn Windows Features on or off` app. You can find the app by searching `features` from the search bar.

The component is checked

![assets/wsl/wsl_component.png](../assets/wsl/wsl_component.png)

Note:
> **For newer PC, we will be using WSL2 which only need one system component `Virtual Machine Platform`.**
>**For Windows 10 user, we might need additional system component `Windows Subsystem for Linux`. Therefor you may see 2 component checked.** 

![alt text](../assets/wsl/wsl_2_component.PNG)

## Install Linux:Ubuntu
After the PC is rebooted, launch **Windows Powershell as administrator**. 

```bash
wsl --install
```

You should have similar setup screen as shown below:
![assets/wsl/wsl2.png](../assets/wsl/wsl2.png)

> **Note: You will be asked to setup your Linux account with a username and password. If you have successfully setup the Linux account and password, then the installation is considered as successful.**



## Update Ubuntu

We also use the following command to update Linux system:
```bash
sudo apt-get update
sudo apt-get upgrade
```
The first command is to get the update information from Ubuntu. See the quote from Google:

> The `sudo apt-get update` command, run in a Linux terminal, refreshes your system's local package index by downloading the latest package information from software repositories. This allows your system to recognize new versions of software or new packages that have been added to the repositories, but it does not actually install or upgrade any software;

Use the following command to get the latest package information:
```bash
sudo apt-get update
```

Sample update screen:
![assets/wsl/aptget_update.png](../assets/wsl/aptget_update.png)


To run the actual update, use the following command

```bash
sudo apt-get upgrade
```

It should be something similar below:
![assets/wsl/aptget_upgrade.png](../assets/wsl/aptget_upgrade.png)

## Troubleshoot WSL 

- If there is problem with WSL component installation, you can checked and uncheck the component `Virtual Machine Platform`. 

![assets/wsl/wsl_component.png](../assets/wsl/wsl_component.png)

- For older system, you may need to check and uncheck 2 components: `Virtual Machine Platform` and `Windows Subsystem for Linux`.

![assets/wsl/wsl_2_component.PNG](../assets/wsl/wsl_2_component.PNG)

- Alternatively, we can also user system component repair by going to `Settings` -> `Apps` -> `Installed Apps`, scroll down to related settings and select  `System Components`. Next, look for `Windows Subsystem for Linux` and click `Advanced options`. You can choose to `repair` or `reset` WSL.

![assets/wsl/component_repair.png](../assets/wsl/component_repair.png)

- Sometimes, the system will prompt for auto-repair during installation as shown below:

![assets/wsl/wsl_start_error.png](../assets/wsl/wsl_start_error.png)








