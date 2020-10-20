#!/usr/bin/env python
# coding: utf-8

# In[1]:


import import_ipynb
import configure as cfg


# In[2]:


class Algo:
    
    def __init__(self):
        self.dir = cfg.Forward
        self.speed=cfg.DSpeed
        self.curr_speed = cfg.OSpeed

    def run(self, x):
        if any(self.curr_speed):
            self.speed = self.curr_speed
        if x==cfg.InputType.START: 
                self.dir = cfg.Forward
                self.speed = cfg.OSpeed
                
        elif x==cfg.InputType.FORWARD:
                self.dir = cfg.Forward
                
        elif x==cfg.InputType.BACKWARD:
                self.dir = cfg.Backward
                
        elif x==cfg.InputType.LOWSPEED:
                self.speed = cfg.LSpeed
                self.curr_speed = self.speed

        elif x==cfg.InputType.MEDIUMSPEED:
                self.speed = cfg.MSpeed
                self.curr_speed = self.speed

        elif x==cfg.InputType.HIGHSPEED:
                self.speed = cfg.HSpeed
                self.curr_speed = self.speed

        elif x==cfg.InputType.STOP:
                self.dir = cfg.Stop
                
        elif x==cfg.InputType.RIGHT:
                self.curr_speed = self.speed
                self.speed = [0, self.curr_speed[1]]
                
        elif x==cfg.InputType.LEFT:
                self.curr_speed = self.speed
                self.speed = [self.curr_speed[0],0]
        
        elif x==cfg.InputType.PAUSE:
                self.speed = cfg.DSpeed

        elif x==cfg.InputType.EXIT:
            self.dir=None
            self.speed=None

        else:
            print("<<<  wrong data  >>>")
            print("please enter the defined data to continue.....")
      
        
    def get_dir(self):
        print(self.dir)
        return self.dir
    
    def get_speed(self):
        print(self.speed)
        return self.speed


# In[ ]:




