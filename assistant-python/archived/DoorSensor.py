#!/usr/bin/python
# speed of sound 1126 feet per second
#13512 inches per second 
# import time module
import time

# import gpio module
import RPi.GPIO as GPIO
# GPIO.setmode(GPIO.BOARD)

count = 0
#loop used to check values multiple times
while (count < 3):

   alpha = 0
   beta = 0
   gamma = 0
   delta = 0
   inch = 0
   cm = 0
   
   # set up gpio pin 11 as output
   GPIO.setup(11, GPIO.OUT)

   # Be sure there is no signal to parallax ping: pin 11, 0 = False
   GPIO.output(11, 0)
   time.sleep(0.00002)
   # send parallax ping a signal: pin 11, 1 = True
   GPIO.output(11, 1)
         
   time.sleep(0.00002)
   # set up gpio pin 11 as input
   GPIO.setup(11, GPIO.IN)

   # send parallax ping a signal: pin 11, 1 = True
   GPIO.input(11)

   # Start time
   alpha = time.time()

   while GPIO.input(11) == 1 and delta < 20:
      delta = delta + 1
   else:
      # Stop time
      beta = time.time()
      gamma = beta - alpha
      # print parallax ping value
      # calc for speed of sound at inches per second should be "correct"
      inch = 13512 * gamma
      #calc for speed at centimeters per second should be "correct"
      cm = 34320.48 * gamma
      #displays time, inches, cm should be the distance the object is from the device
      results = {
         'time':gamma,
         'inch':inch,
         'cm':cm,
         'counter':delta,
         'value':GPIO.input(11),
         'start':alpha,
         'end':beta
      }
      print results
      #print "Time: ", gamma
      #print "Inch: ", inch
      #print "CM: ", cm
      #increase count by 1
   count = count + 1
   # set up gpio pin 11 as output
   GPIO.setup(11, GPIO.OUT)

   # Be sure there is no signal to parallax ping: pin 11, 0 = False
   GPIO.output(11, 0)
   # Rest for a few seconds
   time.sleep(5)
