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

### Run Karen on Raspberry Pi 2 or 3 using Raspbian
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
    chmod +x ./install.sh
    sudo -H ./install.sh
    ```
1. Change directory to PCKaren.
1. Start PCKaren by running `python __main__.py`
1. Karen should now respond to your requests. ("How are you?, Tell me a joke., etc.)
1. If you ever need to stop the program use "CTRL-SHIFT-\".

### How to Create Suites

Suites are the best way to add your own, custom functions into the Assistant framework.

There are only a few requirements for suites to be imported and used-

1. "#suite.file" (without the quotes) must be the first line of code in your .py file (This feature will come later with an automatic search function)
1. There must be a method that is the same as the file name + "Method". (ie. DefaultSuite - def DefaultSuiteMethod())
1. When a command has been successfully heard based on the suite- the method MUST return True. If not, return false, so it will look for other commands from other suites.
1. All methods that use the Assistant class functions must pass the assistant as a parameter to the function, as well as the SuiteMethod() (For now)

To hook your method into the program, use the __main__.py included with the repository as an example. 

Add your suite to the sendCommands method in __main__.py similarly as DefaultSuiteMethod is used.

The following methods can be used in your custom Suites via the Assistant class:

* Listen() - Starts the assistant- causes it to begin listening for it's name and exceuting voice commands based on imported suites or ChatBot
* Speak(text) - "text" will be the value that your Assistant replies
* playSound(audiofile) - "audiofile" being the .mp3 file to play located in the main directory (unless specified)

Other methods are currently internal, however there are variables that you can use to customize and read from your assistant:

* Assistant.intent - Extracted intent from given command via Wit.Ai (in progress)
* Assistant.userCommand - Raw command recognized by Google Speech (currently)
* Assistant.name - TBA
* Assistant.location - TBA
* Assistant.voice - TBA


### Change Log
* 7-5-17
    * KAREN is currently running on the Pi, installation instructions to be uploaded to GitHub 

* 8-28-17
   * General improvements, KAREN works best on Ubuntu 16.04 at the moment.
   * Split up into PiKaren and PCKaren for better organization.
   * ElijahCommands added. Framework for custom functions to be added
   * Added installation instructions.
   
* 9-6-17
   * Karen now responds when hearing the word "Karen"
   * General code cleanup- added white space
   * Needs speed improvement

* 9-27-17
   * Added method to add suites for custom functions.
   * Added start and stop mp3s for listening routine.

* 10-21-17
   * Made small command identification improvements
   * Added Karen's more formal introduction
