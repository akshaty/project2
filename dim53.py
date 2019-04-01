from Tkinter import *
import re
import ftplib
from ftplib import FTP
from time import sleep
import os,threading
import re,time 
from datetime import datetime
filename="" 
v=""
myarray=[]
myarray2=[]
myarray3=[]
t=time.ctime()
val={}
Time1=""
def save():
    p=e1.get()
    q=e2.get()
    r=e3.get()
    s=e4.get()
    T="User:"+p+" "+"Password:"+q+" "+"Filename:"+r+" "+"BackupTime:"+s
    f=open("Backupdetails.txt","a")
    f.write(T)
    f.write("\n")
    f.close()
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    #os.system("python /home/akshat/dim61.py")
    print "done"
window = Tk()
window.title("Info")
A=Label(window,text="Enter the User name")
B=Label(window,text="Enter the Password")
C=Label(window, text="Enter the filename")
D=Label(window,text="Enter the Backup time")

A.grid(row=0,column=0)
B.grid(row=1,column=0)
C.grid(row=2,column=0)
D.grid(row=3,column=0)
e1=Entry(window)
e2=Entry(window,show="*")
e3=Entry(window)
e4=Entry(window)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
e3.grid(row=2,column=1)
e4.grid(row=3,column=1)
Q=Button(window,text="Save",fg="Blue",command=save) 
W=Button(window,text="Quit",fg="Red",command=window.destroy)
W.grid(row=4, column=0)
Q.grid(row=4,column=2)
window.mainloop()
