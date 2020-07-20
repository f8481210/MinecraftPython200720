# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 15:51:09 2020

@author: User
"""


from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x,y,z = mc.player.getTilePos()

mc.setBlock(x+1,y,z,57)
mc.setBlock(x-1,y,z,57)
mc.setBlock(x,y,z+1,57)
mc.setBlock(x,y,z-1,57)
mc.setBlock(x+1,y,z+1,57)
mc.setBlock(x-1,y,z+1,57)
mc.setBlock(x+1,y,z-1,57)
mc.setBlock(x-1,y,z-1,57)