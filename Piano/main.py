import tkinter as tk
from pyo import *
import os
import time
import threading


def playsound(fq):
    harmonics=5
    s = Server(nchnls=2, sr=44100, duplex=0).boot().start()

    f = Adsr(attack=.02, decay=.5, sustain=0.3, release=1, dur=2)
    a = Sine(freq=fq, mul=f)
    for i in range(0,harmonics+1):
        a+=Sine(freq=fq*i, mul=f*0.2)
    a.out()
    f.play()
    time.sleep(0.3)
    s.stop()



def displayblock(array):
    os.system('clear')
    for i in range(10, 0, -1):
        for j in array:
            if i <= j:
                print(chr(0x2593)*6, end='')
            else:
                print('       ', end='')
        time.sleep(0)
        print()


keystatus = False

data = [0]*10

keys = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'semicolon']
deltime=0
def keydown(event):
    global origin
    origin=time.time()
    key = event.keysym
    keystatus = True
    data = [0]*10

    while keystatus is True:
        if key in keys:
            k = keys.index(key)
            data[k] = 8
            displayblock(data)
            playsound(200+(k)*101.9)

        keystatus = root.bind('<ButtonRelease-1>', keyup)


def keyup(event):
    keystatus = False


root = tk.Tk()
root.title("key sense!")
root.bind('<KeyPress>', keydown)

root.mainloop()

