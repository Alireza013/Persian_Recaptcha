"""write program to create re-captcha password with python
use libraries"""

# import useful libraries
from random import choice, randint
from captcha.image import ImageCaptcha
from tkinter import *
import string
import time

global c_text

# for gui window
root = Tk()
root.title("Re-Captcha")
canvas = Canvas(root, width=300, height=300)
canvas.pack()


# for create captcha
cap = ImageCaptcha(width=280, height=90)
ps = string.ascii_letters + string.digits
c_text = "".join(choice(ps) for w in range(randint(4, 5)))

cap.generate(c_text)
cap.write(c_text , "Pass.jpg")


# for show captcha
img = PhotoImage(file = "Pass.jpg")
canvas.create_image(20,20,anchor=NW, image=img)


# for textbox
txt = Entry(root)
canvas.create_window(150, 140, window=txt)

def change():
    global c_text
    c_text = "".join(choice(ps) for w in range(randint(4, 5)))

    cap.generate(c_text)
    cap.write(c_text, "Pass.jpg")
    img = PhotoImage(file="Pass.jpg")
    canvas.create_image(20,20,anchor=NW, image=img)
    canvas.mainloop()


Tries = 0 #number of tries
# check captcha
def check():
    global Tries
    if txt.get() == c_text:
        lbl["text"] = "!درسته"
        Tries = 0
        lbl["foreground"] = "green"
        lbl.place(x=120, y=195)
    elif len(txt.get()) == 0:
        lbl["text"] = "!لطفا کپچا را در کادر وارد کنید"
        lbl["foreground"] = "Black"
        lbl.place(x=50, y=195)
    else:
        Tries += 1
        lbl["text"] = (".غلطه! دوباره امتحان کن\n %i:تعداد تلاش"%(Tries))
        time.sleep(0.4)
        lbl["foreground"] = "red"
        lbl.place(x=60, y=195)
        change()

# for check captcha
btn = Button(root, text="! بررسی", command=check)
btn.place(x=80,y=160)

# for change captcha
btn_2 = Button(root, text="! تعویض کپچا", command=change)
btn_2.place(x=140, y=160)


# for label
lbl = Label(root, text=".کپچا را وارد کنید", font="irelham")
lbl.place(x=90, y=195)

# show box
mainloop()
# Codded by ALIREZA RAHIMI
