# Windows WSL Configuring VSCode
For Windows WSL users, we need to connect to WSL first before installation the extensions.

## Windows WSL Connecting to VSCode
We can connect to WSL in VScode using the `Connect to` in the `Welcome Page` and select `WSL`. 

![alt text](../assets/installation/connect_to.png)

and select `WSL`

![alt text](../assets/installation/top_panel.png)

Alternatively, you can also click on the lower left corner of the screen.

![alt text](../assets/installation/LR_corner_no_conn.png)

Select `WSL` at the top panel. The WSL extension will be installed automatically for the first time. After that please wait for WSL to launched in VSCode.

Once WSL is launched, you should see your lower right corner as shown:

![alt text](../assets/installation/LR_corner_conn_wsl.png)

## Installing Python Extension in WSL 
We need to install extension in WSL/Ubuntu.

First make sure that we are connected to WSL as shown 

![alt text](../assets/installation/LR_corner_conn_wsl.png)

Go to the `Extensions` tab, search for the following extensions in the marketplace and install them:

- Python
- Jupyter
- Colab

Please make sure the extension are installed under `WSL:UBUNTU` instead of `LOCAL`

[Video: Connect WSL in VSCode](https://drive.google.com/file/d/1BbKKiy_VsBnEd8Y8Ar89zBSHpC_3w-4V/view?usp=drive_link)


#### Windows User: Alternative Way to Connect VSCode to WSL
There is an alternative way to connect WSL to VSCode with the command line interface (CLI). Using the CLI method, the entire home folder is opened in VSCode. You don’t need to open each GitHub folder individually. While this saves time by eliminating the need to constantly open and close repositories, it also comes with a trade‑off: you lose the isolation that separate repositories normally provide.

Here is the process to connect WSL with VSCode using command:

1. Launch `WSL`.
2. At `WSL`, use the following command and VSCode will be launched.

```bash
code .
```