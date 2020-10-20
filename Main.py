#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import import_ipynb
from configure import ConnType,InputType
import GamepadInput
import KeyboardInput
from Algo import Algo
from Actuate import Actuate

def main():
    
    val = input("Enter Connection Type: 0:KEYBOARD (DEFAULT)  1.JOYSTICK")
    print(val)
    if int(val)==1:
        print("if")
        Ci = GamepadInput.GamepadInput()
    else:
        print("else")
        Ci = KeyboardInput.KeyboardInput()
    
    alg = Algo()
    act = Actuate()
    
    while True:
        Ci.readInput()
        alg.run(Ci.getInput())

        dir=alg.get_dir()          
        spd=alg.get_speed()
        
        if not any ([dir,spd]):
            act.pinCleanup()
            break
        else:
            act.setDirection(alg.get_dir())
            act.setSpeed(alg.get_speed())
            
    
    

if __name__ == "__main__":
    print("hello")
    main()


# In[ ]:




