#usr/bin/env python3

if ! command -v pip &> /dev/null
then
    echo "pip is not installed, type "
    echo "sudo pacman -S python-pip"
    exit
fi

python3 /home/nitin/projects_HQ/python/cli-tools/workspace/workspace.py

