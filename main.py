import json,random
import tkinter as tk
from tkinter import messagebox
setting = open("setting.json","r")
settings = json.loads(setting.read())
print(settings)
win = tk.Tk()
win.title("random")
win.geometry("400x400")
win.config(bg=settings["background-color"])
a = []
used = open("used.json","r")
a = json.loads(used.read())
value = ""
if len(a) > 0:
    value = a[random.randint(0,len(a) - 1)]
    a.remove(value)
    used.close()
    used = open("used.json","w")
    used.write(json.dumps(a))
    used.close()
else:
    used = open("used.json","w")
    tag = open("tag.json","r")
    used.write(tag.read())
    used.close()
    tag.close()
def pressed():
    global value,used,a
    if len(a) > 0:
        value = a[random.randint(0,len(a) - 1)]
        a.remove(value)
        used.close()
        used = open("used.json","w")
        used.write(json.dumps(a))
        used.close()
        lb.config(text=str(value))
    else:
        used = open("used.json","w")
        tag = open("tag.json","r")
        used.write(tag.read())
        used.close()
        tag.close()
        used = open("used.json","r")
        a = json.loads(used.read())
        value = a[random.randint(0,len(a) - 1)]
        a.remove(value)
        used.close()
        used = open("used.json","w")
        used.write(json.dumps(a))
        used.close()
        lb.config(text=str(value))
def reset():
    global used,value,a
    used = open("used.json","w")
    tag = open("tag.json","r")
    used.write(tag.read())
    used.close()
    tag.close()
    messagebox.showinfo("Reset", "Reset successful")
lb = tk.Label(text=value,bg=settings["background-color"],fg=settings["text-color"],font=("Arial",20))
lb.pack()
button = tk.Button(text="random",command=pressed,height=2,width=10)
button.pack()
button2 = tk.Button(text="reset",command=reset,height=2,width=10)
button2.pack()
win.mainloop()