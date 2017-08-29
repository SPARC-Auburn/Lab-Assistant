# Lab-Assistant

### Project Overview
The puropse of this project is to bring a system that allows for easy to use management of lab equipment and various administrative features.

### Wishlist of Features
* Raspberry Pi Central Control w/ voice commands
* Remote Lab Door Unlock
* Remote Party Lights/LED Party Cubes
* Remote Camera Access (Door/3D Printer)
* Hour logging
* Tool signout
* TourBot(KAREN)

### Run PCKaren on Raspberry Pi 2 or 3 using Ubuntu MATE
1. Load image of Ubuntu MATE on 6GB+ micro SD card from https://ubuntu-mate.org/raspberry-pi/
1. Run Ubuntu MATE on Pi and complete setup.
1. Make sure installation is updated by running the following commands (This may take a long while):
    ```
    sudo apt-get update
    sudo apt-get upgrade
    sudo -H pip install --upgrade pip
    ```
1. Clone directory into desired location using `git clone "https://github.com/SPARC-Auburn/Lab-Assistant"`
1. Run installation script using: 
    ```
    cd PCKaren
    chmod +x ./install.sh
    sudo -H ./install.sh
    ```
1. Start PCKaren by running `python Listen.py`

### Run PCKaren on Raspberry Pi 2 or 3 using Raspbian
1. Load image of Rasbian on 6GB+ micro SD card
1. Run Raspbian on Pi and complete setup.
1. Make sure installation is updated by running the following commands (This may take a long while):
    ```
    sudo apt-get update
    sudo apt-get upgrade
    sudo -H pip install --upgrade pip
    ```
1. Clone directory into desired location using `git clone "https://github.com/SPARC-Auburn/Lab-Assistant"`
1. Run installation script using: 
    ```
    cd PCKaren
    chmod +x ./install.sh
    sudo -H ./install.sh
    ```
1. Start PCKaren by running `python Listen.py`

### Change Log
* 7-5-17
    * KAREN is currently running on the Pi, installation instructions to be uploaded to GitHub 

* 8-28-17
   * General improvements, KAREN works best on Ubuntu 16.04 at the moment.
   * Split up into PiKaren and PCKaren for better organization.
   * ElijahCommands added. Framework for custom functions to be added
   * Added installation instructions.
