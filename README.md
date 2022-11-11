# Cli Utils

These utils are meant for Unix based systems like GNU/Linux and MacOS.
Written in Python using the Click module.

1. Workspace
    Opens and auto-runs scripts, applications and websites when `workspace` is executed. 
    
# Installation
    
* Clone the directory with:  
    `$ git clone https://github.com/chess10kp/cli-tools.git` (HTTPS)  
    `$ git clone git@github.com:chess10kp/cli-tools.git` (SSH)
* Make sure pip is installed with:  
        `# apt update && sudo apt install python3-pip && pip3 --version` (Ubuntu)
        `# pacman -S paru && paru -S python-pip && pip --version` (Arch Linux)  
* cd into the directiory of the util you want to use for example,   
    `$ cd workspace`
* Install the package with:  
    `pip install -e .`  


### Additional Setup

##### Workspace
1. `sudo nano ~/.bashrc` (or zsh equivalent) {Optional}
2. Add `alias workspace=<Whatever you want to call it>` 
3. Add website urls to `urls.txt`
4. Add application paths (usually `/usr/bin/<app_name>`) to `apps.txt`
5. Add scripts to `scripts.txt`
6. Optional (autostart): 
```$ touch ~/.config/autostart/filename.sh <br> $ sudo nano ~/.config/autostart/filename.sh```
Type `workspace` 
