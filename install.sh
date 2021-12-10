#!/usr/bin/env bash
#
# Note: Script to install requirements for 'download-vspc-mgmt-agents.py' on Ubuntu 20.04

# ensuring sudo access
if [[ "$EUID" = 0 ]]; then
    echo "(1) already root"
else
    sudo -k # make sure to ask for password on next sudo
    if sudo true; then
        echo "(2) correct password"
    else
        echo "(3) wrong password"
        exit 1
    fi
fi

# installing requirements
sudo apt update
sudo apt install firefox software-properties-common -y
sudo add-apt-repository ppa:deadsnakes/ppa -y
sudo apt update
sudo apt install python3.9 -y
wget https://github.com/mozilla/geckodriver/releases/download/v0.30.0/geckodriver-v0.30.0-linux64.tar.gz
tar -xvzf geckodriver*
sudo mv geckodriver /usr/bin/geckodriver 
sudo chown root:root /usr/bin/geckodriver
sudo chmod +x /usr/bin/geckodriver
python3.9 -m pip install -U selenium argparse
wget https://raw.githubusercontent.com/carceneaux/veeam-vspc-download-mgmt-agent/master/download-vspc-mgmt-agents.py
sudo chmod +x download-vspc-mgmt-agents.py
