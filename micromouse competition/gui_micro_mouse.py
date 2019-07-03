
from tkinter import*
from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk
root=Tk()
frame=Frame(root,width=700 , height=400)
color= open('bin/color.txt','r').read()
frame.config(bg=color)
root.title("micromouse results")
frame.pack(fill="both",expand="yes" )


#_______________________helper functions____________________________
def sort(x):
    i=0
    while True:
        

        if i == len(x)-1:
            break
        if x[i][0]>x[i+1][0]:
            t1=x[i]
            t2=x[i+1]
            x[i]=t2
            x[i+1]=t1
            i=0

            

        if x[i][0]==x[i+1][0]:

            if x[i][1]>x[i+1][1]:
                t1=x[i]
                t2=x[i+1]
                x[i]=t2
                x[i+1]=t1
                i=0
                continue
        i+=1
    return x

                
#________________________right data ________________________________
frameright=tk.LabelFrame(frame,text="TOP RESULTS",width=230 , height=399,bg=color)
frameright.place(relx=0.66,rely=0)
frame_top10=Frame(frameright,width=200 , height=360,bg="black")
frame_top10.place(relx=0,rely=0)

                        
#________________________left data____________________________
frameleft=tk.LabelFrame(frame,text="COUNTER",width=450 , height=399,bg=color)
frameleft.place(relx=0.01,rely=0)



frame1=Frame(frameleft,width=350 , height=200,bg="black")
frame1.place(relx=0.1,rely=0)

frame_time=Frame(frameleft,width=350 , height=200,bg="black")
frame_time.place(relx=0.3,rely=0)
#------------------------micromouse--------------------------------------------
# This function is used to  
# display time on the label 
t=0
s=0
m=0
def new_time() :
    global t , s,m
    t=1
    s=0
    m=0
    time()
    
    
def time():
    if t==1 : 
        global s , m 
        string = '{}:{}'.format(m,s)
        lbl.config(text = string) 
        lbl.after(1000, time) 
        if s%60==0 and s!=0:
            s=0
            m+=1
        s+=1

# Styling the label widget so that clock 
# will look more attractive 
lbl = Label(frame_time, font = ('calibri', 80, 'bold'), 
            background = 'black', 
            foreground = 'white') 
  
# Placing clock at the centre 
# of the tkinter window 
lbl.pack(anchor='center') 



top10=Label(frame_top10, font = ('calibri', 20, 'bold'), 
            background = color, 
            foreground = 'white') 
top10.pack(anchor='center') 

        
#------------------------buttons/sensors-----------------------------------------------
tops=[]
counter=0
def stop():
    global t,tops,counter
    t=0
    counter+=1
        

    tops.append([m,s,'@LAP({})'.format(counter)])
    if len(tops)!=1:
        
        tops=sort(tops)
        print(tops)
    lbl.config(text = '0:0') 
    res=''
    for t in tops:
        res+='{}:{} {}\n'.format(t[0],t[1],t[2])
    top10.config(text = res) 
    
    
    
MyButton3 = Button(frameleft, text="stop", width=10, command=stop,fg='blue')
MyButton3.place(relx=.4, rely=.85)


MyButton4 = Button(frameleft, text="start", width=10, command=new_time,fg='blue')
MyButton4   .place(relx=.2, rely=.85)



#--------------------------statusbar--------------------------------------------

status = Label(root,text= 'Micromouse competition',bd=3,relief=SUNKEN, anchor=W)#bd is  boarder , rellief , anchore to the w 'west'
status.pack(side=BOTTOM,fill=X)





#------------------------------------------------------

menu=Menu(root)
root.config(menu=menu)# means that i am configuring a menu called menu
#--------------------------------
submenu=Menu(menu)

options=Menu(menu)
menu.add_cascade(label='options',menu=options)

options.add_command(label='redo')
#---------------------------------------------
edit=Menu(menu)
menu.add_cascade(label='edit',menu=edit)

edit.add_command(label='redo')
#---------------------------------------------
def black():
      color="black"
      guifile=open('bin/color.txt','w')
      guifile.write(color)
      guifile.close()
      frame.config(bg="black")
      frameright.config(bg=color)
      frameleft.config(bg=color)
      frame_top10.config(bg=color)
          
def red():
      color="red"
      guifile=open('bin/color.txt','w')
      guifile.write(color)
      guifile.close()
      frame.config(bg="red")
      frameright.config(bg=color)
      frameleft.config(bg=color)
      frame_top10.config(bg=color)

def white():
      color="white"
      guifile=open('bin/color.txt','w')
      guifile.write(color)
      guifile.close()
      frame.config(bg="white")
      frameright.config(bg=color)
      frameleft.config(bg=color)
      frame_top10.config(bg=color)

def gray():
      color="gray"
      guifile=open('bin/color.txt','w')
      guifile.write(color)
      guifile.close()
      frame.config(bg="gray")
      frameright.config(bg=color)
      frameleft.config(bg=color)
      frame_top10.config(bg=color)

def green():
      color="green"
      guifile=open('bin/color.txt','w')
      guifile.write(color)
      guifile.close()
      frame.config(bg="black")
      frameright.config(bg=color)
      frameleft.config(bg=color)
      frame_top10.config(bg=color)

menu.add_cascade(label='color',menu=submenu)
submenu.add_command(label='black',command=black)
submenu.add_command(label='red',command=red)
submenu.add_command(label='white',command=white)
submenu.add_command(label='green',command=green)
submenu.add_command(label='gray',command=gray)

#--------------------------------------

root.mainloop()
