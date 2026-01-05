# Conda Installation Verification
In this guide we want to confirm if our conda environment is setup properly. 

Step 0 : Launch VSCode. (Windows users please make sure you are connected to WSL)

Step 1 : Open the folder of lesson 1.1 which you have clone to your PC. Alternatively, you can also use command:
```bash
cd 5m-data-1.1-intro-data-science
```

Step 2 : Open the terminal in VSCode by clicking `...` > `Terminal` > `New Terminal` to open a new terminal windows

Step 3 : Run  the command `ls` to look for 2 files. They are `environment.yml` and `create_db_data.py`. Proceed if you can find the 2 files.

Step 4 : Run the following command to create the environment. Type `yes` to confirm installation.
```bash
conda env create -f environment.yml
```

Step 5 : Once completed run `conda env list` to confirm that you have the env `ddb` in addition to `base`.
```bash
conda env list
```

Step 6 : Run the command:
```bash
conda activate ddb
```

Step 7 : Run the command:
```bash
python create_db_data.py
```

If you can complete all steps without error then your conda installation is good.