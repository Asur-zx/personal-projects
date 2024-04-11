import tkinter as tk
from pyo import Server, Sine, Adsr
import threading
import time
import os

s = Server(nchnls=2, sr=44100, duplex=0).boot().start()

def playsound(fq):
    harmonics = 5

    f = Adsr(attack=0.02, decay=0.9, sustain=0.3, release=0, dur=2)

    a = Sine(freq=fq, mul=f)
    for i in range(1, harmonics + 1):
        a += Sine(freq=fq * i, mul=f * 0.1)

    a.out()

    f.play()

    time.sleep(1.3)


def displayblock(array):
    os.system('clear')
    for i in range(8, 0, -1):
        for j in array:
            if i <= j:
                print(chr(0x2593) * 6, end='')
            else:
                print('       ', end='')
        print()

keystatus = False
data = [0] * 8
keys = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k']
threads = []

def keydown(event):
    global keystatus

    key = event.keysym
    keystatus = True
    data = [0] * 8

    if key in keys:
        k = keys.index(key)
        frequency = 200 + (k) * 127.375

        data[k] = 8
        displayblock(data)

        thread = threading.Thread(target=playsound, args=(frequency,))
        threads.append(thread)
        thread.start()

def keyup(event):
    global keystatus
    keystatus = False

root = tk.Tk()
root.title("Key Sense!")

root.bind('<KeyPress>', keydown)
root.bind('<KeyRelease>', keyup)

root.mainloop()

for thread in threads:
    thread.join()

s.stop()
