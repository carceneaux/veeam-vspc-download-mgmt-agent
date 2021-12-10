# veeam-vspc-download-mgmt-agent

The script in this project serves as a workaround for automating the download of the VSPC (Veeam Service Provider Console) Management Agent installation files for Windows, Linux, & MacOS operating systems.

The expectation is that this script can be installed on a single server and be used to download the VSPC Mgmt Agent install file saving it to a _shared location_. Then, the files can be leveraged by custom automation when performing unattended installs.

## 📗 Documentation

This project was tested using an Ubuntu 20.04 headless server (no GUI). While other operating systems should work, they have not been tested and might require minor changes.

### Requirements

* Veeam Service Provider Console v6
* [Python 3.9](https://www.python.org)
  * selenium
  * argparse
* [Mozilla Firefox](https://www.mozilla.org/en-US/firefox/new/)
* [GeckoDriver - WebDriver for Firefox](https://github.com/mozilla/geckodriver)

### Quick Install

The below command automates install of this project on the server in question. It was tested on Ubuntu 20.04.

```bash
usr/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/carceneaux/veeam-vspc-download-mgmt-agent/master/install.sh)"
```

### Manual Install

* Install Mozilla Firefox

```bash
sudo apt update
sudo apt install firefox
```

* Install GeckoDriver - WebDriver for Firefox

```bash
wget https://github.com/mozilla/geckodriver/releases/download/v0.30.0/geckodriver-v0.30.0-linux64.tar.gz
tar -xvzf geckodriver*
sudo mv geckodriver /usr/bin/geckodriver 
sudo chown root:root /usr/bin/geckodriver
sudo chmod +x /usr/bin/geckodriver
```

* Install Python 3.9

```bash
sudo apt install software-properties-common -y
sudo add-apt-repository ppa:deadsnakes/ppa -y
sudo apt update
sudo apt install python3.9 -y
```

* Download script and mark it as executable

```bash
wget https://raw.githubusercontent.com/carceneaux/veeam-vspc-download-mgmt-agent/master/download-vspc-mgmt-agents.py
sudo chmod +x download-vspc-mgmt-agents.py
```

## ✍ Contributions

We welcome contributions from the community! We encourage you to create [issues](https://github.com/carceneaux/veeam-vspc-download-mgmt-agent/issues/new/choose) for Bugs & Feature Requests and submit Pull Requests. For more detailed information, refer to our [Contributing Guide](CONTRIBUTING.md).

## 🤝🏾 License

* [MIT License](LICENSE)

## 🤔 Questions

If you have any questions or something is unclear, please don't hesitate to [create an issue](https://github.com/carceneaux/veeam-vspc-download-mgmt-agent/issues/new/choose) and let us know!
