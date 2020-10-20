#!/usr/bin/env python
# coding: utf-8

# In[1]:


import RPi.GPIO as GPIO
from enum import Enum

class ConnType(Enum):
    
    KEYBOARD=0
    JOYSTICK=1
    
class InputType(Enum):
    START=0
    FORWARD=1
    BACKWARD=2
    RIGHT=3
    LEFT=4
    LOWSPEED=5
    HIGHSPEED=6
    MEDIUMSPEED=7
    PAUSE=8
    STOP=9
    EXIT=-1


# P1 - PWM signal configuration for Pin1
P1in1 = 24
P1in2 = 23
en1 = 25
# P2 - PWM signal configuration for Pin2
P2in1 = 5
P2in2 = 6
en2 = 13

Forward = [GPIO.HIGH, GPIO.LOW]
Backward = [GPIO.LOW, GPIO.HIGH]
Stop = [GPIO.LOW,GPIO.LOW]

DSpeed=[25, 25] #default speed
LSpeed=[25, 25]
MSpeed=[50, 50]
HSpeed=[75, 75]
OSpeed=[0, 0]


# In[ ]:




