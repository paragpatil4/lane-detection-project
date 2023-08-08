
#from tkinter import messagebox as ms
#import sqlite3
from PIL import ImageTk
import tkinter as tk
from PIL import Image, ImageTk

# main Class


root = tk.Tk()

#root.configure(background="grey")
#root.geometry("500x400")
#root.title("Login")

w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Lane And Curve Detection")

image2 = Image.open('img8.jpg')
image2 = image2.resize((1630, 1000), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0)  # , relwidth=1, relheight=1)
label_l1 = tk.Label(root, text="Lane And Curve Detection",font=("Times New Roman", 30, 'bold'),
                    background="brown", fg="white", width=70, height=1)
label_l1.place(x=0, y=0)


def log():
    from subprocess import call
    call(["python","cam.py"])

def obj():
    from subprocess import call
    call(["python","video-detection.py"])
    
def lane():
        from subprocess import call
        call(["python","laneDetectRansac.py"])
        
def window():
  root.destroy()

# button1 = tk.Button(root, text="Specific Object Detection", command=log, width=18, height=1,font=('times', 25, ' bold '), bg="hot pink", fg="white")
# button1.place(x=0, y=160)
button1 = tk.Button(root, text=" Object Detection", command=obj, width=18, height=1,font=('times', 25, ' bold '), bg="violet", fg="black")
button1.place(x=0, y=260)

button2 = tk.Button(root, text="Lane Detection",command=lane,width=18, height=1,font=('times', 25, ' bold '), bg="violet", fg="black")
button2.place(x=0, y=350)

root.mainloop()
