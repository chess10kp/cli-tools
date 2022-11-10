#usr/bin/env python3

if ! command -v pip &> /dev/null
then
    echo "pip is not installed, type "
    echo "sudo pacman -S python-pip"
    exit
fi

dir=$(cd -P -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd -P)

python3 ${dir}/workspace.py

