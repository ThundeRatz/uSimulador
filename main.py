#!/usr/bin/python
# -*- coding: utf-8 -*-

from maze import Maze, Mouse
from time import sleep, time
from floodfill import floodFill, fastRun

showReal = True
def main(): 

    if showReal:
        real = Maze(1, 1)
        memory = Maze(0, 1)
        ws = memory.inter.master.winfo_screenwidth() # width of the screen
        hs = memory.inter.master.winfo_screenheight() # height of the screen
        real.inter.master.geometry('%dx%d+%d+%d' % (660, 660, (ws/2), (hs-660)/2))
        memory.inter.master.geometry('%dx%d+%d+%d' % (660, 660, ((ws/2)-660), (hs-660)/2))        
    else:
        real = Maze(1)
        memory = Maze(0, 1)
        ws = memory.inter.master.winfo_screenwidth() # width of the screen
        hs = memory.inter.master.winfo_screenheight() # height of the screen
        memory.inter.master.geometry('%dx%d+%d+%d' % (660, 660, (ws-660)/2, (hs-660)/2))        
    t = time()
    while time() - t < 5:
        memory.update()
        real.update()

    floodFill(memory, real)
    print("\a")
    sleep(1)
    memory.setMouse([0,15])
    sleep(2)
    fastRun(memory)


    sleep(1)
    exit()

    while(1):
        memory.update()
        real.update() # Caso a GUI não esteja sendo constantemente atualizada, os botões não funcionam
        sleep(0.01)

main()
