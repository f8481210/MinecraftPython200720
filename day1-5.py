# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 14:39:27 2020

@author: User
"""


from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time
t = 0 
while True :
    t = t + 1
    mc.postToChat("這是第"+str(t)+"次")
    time.sleep(2)
