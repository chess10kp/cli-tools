# Cli Utils

These utils are meant for Unix based systems like GNU/Linux and MacOS.
Written in Python using the Click module.

1. Workspace
    Opens and auto-runs scripts, applications and websites when `workspace` is executed. 
    
# Installation
    
* Clone the directory with: 
    `$ git clone https://github.com/chess10kp/cli-tools.git` (HTTPS)
    `$ git clone git@github.com:chess10kp/cli-tools.git` (SSH)
* Change the executable permissions of exec.sh for each util with:
    `$ chmod +x workspace/<utilname>/exec.sh`
* Follow additional setup for each tool below


### Additional Setup:

##### Workspace
1. `sudo nano ~/.bashrc` (or zsh equivalent)
2. Add `alias workspace=. ~/<PATH TO WORKSPACE FOLDER>/workspace/exec.sh` 
3. Add website urls to `urls.txt`
4. Add application paths (usually `/usr/bin/app`) to `apps.txt`
5. Add scripts to `scripts.txt`
6. Optional: `$ cp -r ~/<PATH TO WORKSPACE FOLDER>/workspace ~/.config/autostart`
