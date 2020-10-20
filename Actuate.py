#!/usr/bin/env python
# coding: utf-8

# In[2]:


import RPi.GPIO as GPIO
import import_ipynb
import configure as cfg


# Setting GPIO to generate PWM signal
GPIO.setmode(GPIO.BCM)

GPIO.setup(cfg.P1in1,GPIO.OUT)
GPIO.setup(cfg.P1in2,GPIO.OUT)
GPIO.setup(cfg.P2in1,GPIO.OUT)
GPIO.setup(cfg.P2in2,GPIO.OUT)

GPIO.setup(cfg.en1,GPIO.OUT)
GPIO.setup(cfg.en2,GPIO.OUT)

GPIO.output(cfg.P1in1,GPIO.LOW)
GPIO.output(cfg.P1in2,GPIO.LOW)
GPIO.output(cfg.P2in1,GPIO.LOW)
GPIO.output(cfg.P2in2,GPIO.LOW)


class Actuate:

    def __init__(self):
        self.p1=GPIO.PWM(cfg.en1,1000)
        self.p2=GPIO.PWM(cfg.en2,1000)
        self.p1.start(25)
        self.p2.start(25)
    

    def setSpeed(self,dc):
        self.p1.ChangeDutyCycle(dc[0])
        self.p2.ChangeDutyCycle(dc[1])

    def setDirection(self, Dir):
        GPIO.output(cfg.P1in1,Dir[0])
        GPIO.output(cfg.P1in2,Dir[1])
        GPIO.output(cfg.P2in1,Dir[0])
        GPIO.output(cfg.P2in2,Dir[1])

    def pinCleanup(self):
        GPIO.cleanup()


# In[ ]:





# In[ ]:




