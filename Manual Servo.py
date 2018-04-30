import time, pantilthat
from tkinter import *
from tkinter import ttk

# this set the inicial position for servos
pantilthat.idle_timeout(0.5)
pantilthat.pan(90)
pantilthat.tilt(-90)

root = Tk()

def window(main):
    main.title('Manual Servo')
    main.update_idletasks()
    width = 800 # main.winfo_width()
    height = 480 # main.winfo_height()
    x = (main.winfo_screenwidth() // 2 ) - (width // 2)
    y = (main.winfo_screenheight() // 2) - (height // 2)
    main.geometry('{}x{}+{}+{}'.format(width, height, x, y))
window(root)


def servoPan_neg(event):
    a = pantilthat.get_pan()-1
    print(a)
    pantilthat.pan(a)

def servoPan_pos(event):
    b = pantilthat.get_pan()+1
    print(b)
    pantilthat.pan(b)

def servoTilt_neg(event):
    c = pantilthat.get_tilt()-1
    print(c)
    pantilthat.tilt(c)

def servoTilt_pos(event):
    d = pantilthat.get_tilt()+1
    print(d)
    pantilthat.tilt(d)


label_1 = Label(root, text="Pos Pan Servo -:")
entry_1 = Entry(root)
label_1.grid(row=0, sticky=E)
label_2 = Label(root, text="Pos Pan Servo +:")
entry_2 = Entry(root)
label_2.grid(row=1, sticky=E)
label_3 = Label(root, text="Pos Tilt Servo -:")
entry_3 = Entry(root)
label_3.grid(row=2, sticky=E)
label_4 = Label(root, text="Pos Tilt Servo +:")
entry_4 = Entry(root)
label_4.grid(row=3, sticky=E)

entry_1.bind("<Return>", servoPan_neg)
entry_1.grid(row=0, column=1)
entry_2.bind("<Return>", servoPan_pos)
entry_2.grid(row=1, column=1)
entry_3.bind("<Return>", servoTilt_neg)
entry_3.grid(row=2, column=1)
entry_4.bind("<Return>", servoTilt_pos)
entry_4.grid(row=3, column=1)


root.mainloop()
