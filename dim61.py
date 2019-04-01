from Tkinter import *
import re
import ftplib
from ftplib import FTP
from time import sleep
import os,threading
import re,time,sys
from datetime import datetime
filename="" 
v=""
myarray=[]
myarray2=[]
myarray3=[]
t=""
val={}
Time1=""
sample=r"User.(.*).Password.(.*).Filename.(.*).Backuptime.(.*)"
p=open("Backupdetails.txt","r")
lines=p.readlines()
        
def backup1():
        
        while True:      
           for filename in myarray:    
              sleep(5) 
              print filename
              p=os.path.basename(os.path.normpath(filename))
              print p
                  with open(filename,"r") as k:
                  p=os.path.basename(os.path.normpath(filename))
                  t = str(datetime.now().replace(second=0, microsecond=0))
                  ftp.storlines("STOR "+p+t,k)
                  print "perfect"
def backup2():
    try:    
        while True:
           for filename in myarray2:
               sleep(10)
               with open(filename,"r") as k:
                  p=os.path.basename(os.path.normpath(filename))
                  t = str(datetime.now().replace(second=0, microsecond=0))
                  ftp.storlines("STOR "+p+t,k)
                  print "perfect"
    except:
            print "<Error>:Cannot make Days Backup....Some Error has occured"
def backup3():
     try:   
       while True:    
           for filename in myarray3:
              sleep(15) 
              with open(filename,"r") as k:
                  t =str(datetime.now().replace(second=0, microsecond=0))    
                  p=os.path.basename(os.path.normpath(filename))       
                  ftp.storlines("STOR "+p+t,k)
                  print "perfect"
     except:
             print "<Error>:Cannot make Weeks Backup....Some Error has occured"
def backup4():
     try:   
        
        while True:     
           v = str(datetime.time(datetime.now()).replace(second=0, microsecond=0))
           for i in val :
              if val[i] == v :
                with open(i,"r") as k:
                  t =str(datetime.now().replace(second=0, microsecond=0))      
                  ftp.storlines("STOR "+i+t,k)
                  print i
                  print "Hour perfect"
                  sleep(10)
     except:
             print "<Error>:Cannot make Timely Backup....Some Error has occured"
             
             
for line in lines:
     match=re.search(sample,line,re.M|re.I)
     if match!=None:
            a=str(match.group(1))
            b=str(match.group(2))
            try:
              q=str(os.system('hostname -I'))
              ftp=ftplib.FTP(q)
              ftp.login(a,b)
              filename=match.group(3)
              print "login successfull"
            except:
              print "<Error>:Login Error"      
            Time1=match.group(4).rstrip()
            try:
              if Time1.rstrip()=="minutes":
                 myarray.append(filename)
               
              else:
                  if Time1.rstrip()=="days":
                      myarray2.append(filename)
                  else :
                     if Time1.rstrip()=="weeks":
                       myarray3.append(filename)   
                     else:
                       q=os.path.basename(os.path.normpath(filename))          
                       val[q]=Time1.rstrip()
            except:
                      print "<Error>:Appending error"
 
           

if __name__=="__main__":

      
        t1=threading.Thread(target=backup1)
        t2=threading.Thread(target=backup2)
        t3=threading.Thread(target=backup3)
        t4=threading.Thread(target=backup4)
        
     
        t1.start()
        t2.start()
        t3.start()
        t4.start()

     
        t1.join()
        t2.join()
        t3.join()
        t4.join()

       
       

