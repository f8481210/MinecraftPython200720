# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 11:32:40 2020

@author: User
"""


from mcpi.minecraft import Minecraft
mc = Minecraft.create()

print(mc.player.getTilePos())
print(mc.player.getPos())

x = 100.1135
y = 60.2356
z = 10.369
mc.player.setPos(x,y,z)