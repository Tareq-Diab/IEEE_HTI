
from tkinter import*
from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk
root=Tk()
frame=Frame(root,width=800 , height=600)
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



frame1=Frame(frameleft,width=350 , height=230,bg="black")
frame1.place(relx=0.1,rely=0)

frame_time=Frame(frameleft,width=350 , height=230,bg="black")
frame_time.place(relx=0.1,rely=0)



logos=tk.LabelFrame(frame,text="sponsers",width=800 , height=200,bg=color)
logos.place(relx=0.01,rely=0.68)

logoframe=Frame(logos,width=400 , height=200,bg=color)
logoframe.place(relx=0.01,rely=0.04)

photo2=Image.open("bin/ieee_logo.jpg")
width_org, height_org = photo2.size
photo2=photo2.resize((int(width_org*0.2), int(height_org*0.2)), Image.ANTIALIAS)
photo2 = ImageTk.PhotoImage(photo2)

label2 =Label(logoframe , image=photo2)

label2.place(relx=0.04,rely=0.04)


logoframe2=Frame(logos,width=400 , height=200,bg=color)
logoframe2.place(relx=0.6,rely=0.04)

photo1=Image.open("bin/logo2.png")
#width_org, height_org = photo1.size
photo1=photo1.resize((int(width_org*0.2), int(height_org*0.2)), Image.ANTIALIAS)
photo1 = ImageTk.PhotoImage(photo1)

logo2 =Label(logoframe2 , image=photo1)

logo2.place(relx=0.04,rely=0.04)

#------------------------micromouse--------------------------------------------

# This function is used to  
# display time on the label 

t=0
s=0
m=0
sg=0
mg=0
reset=0
def new_time() :
    global t , s,m,mg,tops
    tops=[]
    t=1
    s=0
    m=0
    sg=0
    mg=0
    time()
    team_time()
    
    
def time():
    global s , m ,reset
    if mg<=2 and reset == 1:
        s=0
        m=0
        reset=0
    if mg<2 : 
        
        string = 'Lap time {}:{}'.format(m,s)
        lbl.config(text = string) 
        lbl.after(1000, time) 
        if s%60==0 and s!=0:
            s=0
            m+=1
        s+=1


def team_time():
    global sg , mg ,teams_best_times , tops
    if mg<2 : 
        
        string = 'total time {}:{}'.format(mg,sg )
        lblg.config(text = string) 
        lblg.after(1000, team_time) 
        if sg%60==0 and sg!=0:
            sg=0
            mg+=1
        sg+=1
    else:
        teams_best_times[team_name.get()]=[tops[0][0],tops[0][1]]
        tops=[]
        show_teams_times()
        
        
def show_teams_times():
    
    res=''
    for n in teams_best_times:
        #res+='{}:{} {}\n'.format(t[0],t[1],t[2])
        res+='{} {}:{}\n'.format(n,teams_best_times[n][0],teams_best_times[n][1])
    top10.config(text = res)
    #label_best.config(text='Best time {}:{}'.format(tops[0][0],tops[0][1]))

    
    
        

# Styling the label widget so that clock 
# will look more attractive 
lbl = Label(frame_time, font = ('calibri', 30, 'bold'), 
            background = 'black', 
            foreground = 'white') 
lblg = Label(frame_time, font = ('calibri', 40, 'bold'), 
            background = 'black', 
            foreground = 'white') 
label_best = Label(frame_time, font = ('calibri', 30, 'bold'), 
            background = 'black', 
            foreground = 'white') 
# Placing clock at the centre 
# of the tkinter window 
lblg.place(relx=0.05,rely=0)
lbl.place(relx=0.05,rely=0.3)

label_best.place(relx=0.05,rely=0.6)




top10=Label(frame_top10, font = ('calibri', 20, 'bold'), 
            background = color, 
            foreground = 'white') 
top10.pack(anchor='center') 
#------------------------teams mangement----------------------------------------------
teams_best_times={}
team_name=tk.Entry(frameleft)
team_name.place(relx=0.1,rely=0.65)


        
#------------------------buttons/sensors-----------------------------------------------

tops=[]
counter=0
def stop():
    global t,tops,counter,reset
    reset=1
   
    
    counter+=1
    
        

    tops.append([m,s,'@LAP({})'.format(counter)])
    if len(tops)!=1:
        
        tops=sort(tops)
        print(tops)
    #lbl.config(text = '0:0') 
    label_best.config(text='Best time {}:{}'.format(tops[0][0],tops[0][1]))
    """
    res=''
    for t in tops:
        res+='{}:{} {}\n'.format(t[0],t[1],t[2])
    top10.config(text = res)
    

    """
    
    
MyButton3 = Button(frameleft, text="sensor pulse", width=10, command=stop,fg='blue')
MyButton3.place(relx=.4, rely=.85)


MyButton4 = Button(frameleft, text="New team is ready!", width=20, command=new_time,fg='blue')
MyButton4   .place(relx=0.45,rely=0.65)



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
