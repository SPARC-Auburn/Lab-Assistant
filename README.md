# Lab-Assistant

### Project Overview
The puropse of this project is to create a virtual assistant to assist SPARC members.  The virtual assistant will be fully featured including abilities to help out in the lab to automating a home. It will include a system that allows for easy to use management of lab equipment and various administrative features.

### Karen's Forms
* Voice - Uses a microphone to take input from the user and speaks response back to user.
* Text - Uses the terminal to allow user to type commands and receive responses.
* Slack - Uses Slack messaging app to allow SPARC members to type commands and receive responses.

### Wishlist of Features
* Raspberry Pi Central Control w/ voice commands
* Remote Lab Door Unlock
* Remote Party Lights/LED Party Cubes
* Remote Camera Access (Door/3D Printer)
* Hour logging
* Tool signout
* TourBot(KAREN)

### Run Karen on PC or Raspberry Pi 2 or 3 using Debian Linux (Raspbian, Ubuntu, etc.)
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
1. Change directory to karen.
1. Plug in USB mic if computer does not have an integrated microphone.
1. Start Karen by running `python karen.py`
1. Karen should now respond to your requests. ("How are you?, Tell me a joke., etc.)
1. If you need to stop the program use "CTRL-SHIFT-\".

### Run Karen on PC using PyCharm (Windows, Ubuntu, etc.)
1. Install PyCharm Community Edition: https://www.jetbrains.com/pycharm/download/#section=windows
1. Install Python 2.7.13: https://www.python.org/downloads/release/python-2713/.  (Make sure that add to path is checked on Windows)
1. Clone directory into desired location using `git clone "https://github.com/SPARC-Auburn/Lab-Assistant"`
1. In PyCharm, press "File > New Project..."
1. Press "..." button and navigate to cloned directory. Press "OK" and "Create"
1. Press "File > Settings... > Project: Lab-Assistant > Project Interpreter"
1. Change the Project Interpreter to be "Python27/python.exe"
1. Press the green "+" button and add any Python libraries that are missing and press "OK".
1. Plug in USB mic if computer does not have an integrated microphone.
1. In the tree on the left, press "voice_karen.py".
1. Start PCKaren by running "python voice_karen.py" by right clicking in the center of the screen and pressing "Run voice_karen.py"
1. Karen should now respond to your requests. ("How are you?, Tell me a joke., etc.)
1. If you need to stop the program press the red square in the toolbar.

### How to Create Suites

Suites are the best way to add your own, custom functions into the Assistant framework.

There are only a few requirements for suites to be imported and used-

1. There must be a class that is the same as the file name in camel case notation. (ie. defaultsuite - class DefaultSuite)
1. The class must have an __init__ and checkcommand() function.  Use defaultsuite.py as a template.
1. Replace the "CLIENT_ACCESS_TOKEN" with the CLIENT_ACCESS_TOKEN from DialogFlow's corresponding agent.
1. Add additional recognition under the elif statement.

To hook your method into the program, import the suite in manage_suites.py like "from suites.newsuite import *"

Add your suite to the suites array to be included in the processing of commands.

### Current and Proposed Suites
1. Default - A collection of basic responses.
1. Lab - A collection of responses and functions pertaining to assisting users in the SPARC lab.
1. Home - A collection of responses and functions pertaining to home automation and light control.
1. Weather - A collection of responses and functions pertaining to processing weather commands.
1. Personal - A collection of functions pertaining to personal commands like reminders, time, and alarms.
1. Knowledge - A collection of functions to search Google, Bing, Wolfram Alpha, Wikipedia, or etc.
1. Fallback - A collection of fallback responses if previous suites did not catch.


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
   * Made small command identification improvements.
   * Added Karen's more formal introduction.

* 10-27-17
   * Various reformatting and refactoring changes.
   * Cleaned up code and squashed minor bugs.
   * Replaced pygame with pyglet to be compatible with 64 bit Windows.
   * Successfully ran on Windows through PyCharm and detailed instructions are in this readme above.

* 10-28-17
   * Fixed cross platform support. (Linux = Pygame; Windows/Mac = Pyglet)
   * Improved comments in program
   * Streamlined code
   * Added DialogFlow capabilities
   * Added lab and home suites

* 10-29-17
   * Restructured files to improve flexibility and make importing suites easier
   * Added text_karen
