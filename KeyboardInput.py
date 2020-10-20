#!/usr/bin/env python
# coding: utf-8

# In[2]:


import import_ipynb
from configure import ConnType,InputType

class KeyboardInput():
    def __init__(self):
        #CarInput.__init__(self)
        self.key=None
        print("Keyboard Chosen")
        print("The default speed & direction of motor is LOW & Forward.....")
        print("c-continue s-stop f-forward b-backward l-low m-medium h-high e-exit")
        print("Press C to start")
        print("\n") 
    
    def readInput(self):
        print("please enter a value: ")
        self.mapInput(input())
        
    def getInput(self):
        return self.key
    
    def getConnType(self):
        return self.type
    
    def mapInput(self,value):
        if value=='c':
            self.key = InputType.START
        elif value=='f':
            self.key = InputType.FORWARD
        elif value=='b':
            self.key = InputType.BACKWARD
        elif value=='r':
            self.key = InputType.RIGHT
        elif value=='i':
            self.key = InputType.LEFT
        elif value=='l':
            self.key = InputType.LOWSPEED
        elif value=='m':
            self.key = InputType.MEDIUMSPEED
        elif value=='h':
            self.key = InputType.HIGHSPEED
        elif value=='s':
            self.key = InputType.STOP
        elif value=='p':
            self.key = InputType.PAUSE
        elif value=='e':
            self.key = InputType.EXIT
        else:
            self.key = None


# In[ ]:





# In[ ]:




