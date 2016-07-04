#!/usr/bin/Python
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.OUT)
GPIO.output(22,0)
time.sleep(5)
while True:
  pfad = "/sys/class/thermal/thermal_zone0/temp"
  in_file = open(pfad, "r")
  wert = in_file.read()
  in_file.close()
  if float(wert) >= 45000:
   GPIO.output(22,0)
   time.sleep(0.0146484375) #0.015625 :: 0.0078125 :: 0.00390625 :: 0.01953125 :: 0.0095262625 :: 0.0048828125 :: 0.00976525
  # print("off: "+str(float(wert)/1000))
   GPIO.output(22,1)
   time.sleep(0.029296875) # 0.03896484375 :: 0.0029296875 :: 0.0146484375 :: 0.019531250
  #print("on:  "+str(float(wert)/1000))
  elif float(wert) <= 43000:
   GPIO.output(22,1)
   time.sleep(5)
   print("kalt: "+str(float(wert)/1000))
   #205mA pro Luefter
   
