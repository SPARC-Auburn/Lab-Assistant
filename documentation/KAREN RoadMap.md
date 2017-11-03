# KAREN RoadMap Updated:(8/30/2017)
## COMPLETED
### V1.0 (7/5/17)
* Initial upload
### V1.1 (8/28/17)
* Installation file added
### V1.2 (9/4/17)
* Siri-like approach to listening
* General code cleanup
  * -temporary removal of certain lab features
### V1.3 (9/9/17)
* Setup suites
* Framework for custom functions (ie. ElijahCommands)
### V1.4 (10/30/17)
* Integrated DialogAPI
* Code cleanup and commentation
* Added Text and Slack based Karen
## TO DO
### V1.5 (TBD)
* Framework for Bluetooth-Serial commands sent to Raspberry Pi
* Framework for Bluetooth-Serial commands sent to Arduino
* Framework for Wifi commands sent to Raspberry Pi
### V1.6 (TBD)
* LabCommands suite
  * Lab door unlock via remote Arduino
  * Party lights via remote Arduino
  * Hour Logging
  * Tool Signout
  * Lab Tour
  * Motion Camera capture ---- 1.5.5
### V1.7 (TBD)
* Touch screen interface via Raspberry Pi (PiKaren)
### V1.8 (TBD)
* HomeCommands suite
  * Weather
  * Time
  * Temperature
  * Lights
### V1.9 (TBD)
* PersonalCommands suite
  * Record information
  * Wakeup time (like Sleep Cycle)
  * Scheduler
  * Distance between locations
  * Google articles
  * Wikipedia articles
  * Play video
  * Play music


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

### Wishlist of Features
* Raspberry Pi Central Control w/ voice commands
* Remote Lab Door Unlock
* Remote Party Lights/LED Party Cubes
* Remote Camera Access (Door/3D Printer)
* Hour logging
* Tool signout
* TourBot(KAREN)