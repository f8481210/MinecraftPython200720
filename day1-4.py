from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

x,y,z = mc.player.getTilePos()

x = x + 100
mc.player.setTilePos(x,y,z)
time.sleep(5)

x = x + 100
mc.player.setTilePos(x,y,z)
time.sleep(5)

x = x + 100
mc.player.setTilePos(x,y,z)