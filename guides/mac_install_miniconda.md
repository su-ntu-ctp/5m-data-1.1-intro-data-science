# Install Miniconda in Mac

In the official website, you can screen down to quick setup and follow the command line installation instructions. We have collated the commands as follows:

Step 1 : Make a miniconda directory in home directory:
```bash
mkdir -p ~/miniconda3
```

Step 2 : Download the software
```bash
curl https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-arm64.sh -o ~/miniconda3/miniconda.sh
```

Step 3 : Install the software 
```bash
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
```

Step 4 : Remove the software
```bash
rm ~/miniconda3/miniconda.sh
```

Step 5 : Activate conda
```bash
source ~/miniconda3/bin/activate
```

You may need to close terminal and open again

Step 6 : Initialized conda
```bash
conda init --all
```