# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 15:26:37 2020

@author: User
"""

#題目:一次蓋10個
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x,y,z = mc.player.getTilePos()
i = 0
while i<=50 :
    mc.setBlock(x,y+i,z,169)
    i = i+1
