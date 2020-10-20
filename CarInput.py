#!/usr/bin/env python
# coding: utf-8

# In[1]:


#from abc import ABCMeta, abstractmethod
from configure import ConnType,InputType

class CarInput():
    
    def __init__(self):
        self.key=None
        
    def getInput(self):
        return self.key
    
    def getConnType(self):
        return self.type

