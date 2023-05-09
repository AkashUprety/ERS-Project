import tkinter
from tkinter import*
from tkinter import ttk
from tkinter.ttk import Progressbar
import os
t=tkinter.Tk()
t.geometry('800x450+250+150')
t.configure(bg='white')
t.resizable(False,False)

txt=Label(t,text='Enquiry',bg='white',fg='light green',font=('arial',45,'bold'))
txt.place(x=10,y=10)

txt2=Label(t,text='Registration',bg='white',fg='light green',font=('arial',45,'bold'))
txt2.place(x=40,y=95)

txt3=Label(t,text='System',bg='white',fg='light green',font=('arial',45,'bold'))
txt3.place(x=180,y=190)


img=PhotoImage(file='Ers.png')
Label(t,image=img,bg='white').place(x=480,y=-5)

Progress_label=Label(t,text="Loading.....",font=("Trebuchet Ms",13,"bold"),fg='green',bg='white')
Progress_label.place(x=300,y=350)

progress=ttk.Style()
progress. theme_use('clam')
progress.configure("red.Horizontal.TProgressbar",background="green")
progress=Progressbar(t,orient=HORIZONTAL,length=780,mode='determinate',style="red.Horizontal.TProgressbar")
progress.place(x=10,y=380)

def top():
    t.withdraw()
    os.system("python log.py")
    t.destroy()
i=0

def load():
    global i
    if i<=20:
        txt0='Loading....'+(str(5*i)+'%')
        Progress_label.config(text=txt0)
        Progress_label.after(600,load)
        progress['value']=5*i
        i +=1
        
    else:
        top()

load()
t.mainloop()