import tkinter as tk
import random
import datetime

now = datetime.datetime.now()
random.seed(now)

import fun_strings as fun_strings

def run():
    runoutput = (random.choice(fun_strings.RUN_STRINGS))
    print(runoutput)

def dare():
    dareoutput = (random.choice(fun_strings.DARE_STRINGS))
    print(dareoutput)

def truth():
    truthoutput = (random.choice(fun_strings.TRUTH_STRINGS))
    print(truthoutput)

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame, text="Truth", fg="green", command=truth)
button.pack(side=tk.LEFT)
DareButton = tk.Button(frame, text="Dare", command=dare)
DareButton.pack(side=tk.LEFT)
RunButton = tk.Button(frame, text="Run", command=run)
RunButton.pack(side=tk.LEFT)

root.mainloop()