#!/usr/bin/env python
# coding: utf-8

# In[1]:


import import_ipynb
import Gamepad
from configure import ConnType,InputType


class GamepadInput():
    
    def __init__(self):
        self.key=None
        print("Gamepad Chosen")
        self.Gp=Gamepad.Gamepad()
        if not Gamepad.available():
            print("Connect your Gamepad")
            while not Gamepad.available():
                time.sleep(1)
                print("Waiting for Connection!!!")
        print("Gamepad Connected")
        
    def readInput(self):
        print("Press 'START' button to continue")
        e,i,v=self.Gp.getNextEvent(self)
        self.mapInput(e,i,v)
    
    def getInput(self):
        return self.key
    
    def getConnType(self):
        return self.type
        

    def mapInput(self,event,index,value):
        if value==0.0 or value=='False':
            self.key = InputType.PAUSE
        else:
            if event=='AXIS':
                if index==4 :
                    if value==1.0:
                        self.key = InputType.RIGHT
                    else:
                        self.key = InputType.LEFT
                elif index==5:
                    if value==1:
                        self.key = InputType.BACKWARD
                    else:
                        self.key = InputType.FORWARD
            elif event=='BUTTON':
                if index==9:
                    self.key = InputType.START
                elif index==0:
                    self.key = InputType.STOP
                elif index==1:
                    self.key = InputType.LOWSPEED
                elif index==2:
                    self.key = InputType.MEDIUMSPEED
                elif index==3:
                    self.key = InputType.HIGHSPEED
                elif index==8:
                    self.key = InputType.EXIT
                else:
                    self.key = InputType.STOP
        


# In[ ]:




