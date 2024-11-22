from tkinter import *
from tkinter import filedialog as f
from tkvideo import *
from glob import glob
import shutil
import cv2
import pygame 
import PIL 
import os


#                                                           hover image is not transpirt 
#                                                                                                                           settings 
#                                                           grid to button on off for backgraond videos
#                                                                                                                           honver for home 
#                                                                                                                           using cv2 dynamic background chnge with hover 1
#                                                                                                                           1---go back to home---1 
#                                                                   consol icons 
#                                                                                                                           link funkstion user config mai edit ho jaega
#                                                                                                                     theam selector button
#                                                                                                                           hover sound in ps5()                                                                                                                           scrol for grid x and y axis
# add func 
# movement atomate
# 
#                                                                                                                           xbox controler works using pygame.joystic  
#  
#  
#       
# 

width=1920
hight=1080

main_theam=0


show=False

w=Tk()
w.title("GAME LAUNCHER")
w.iconbitmap("main.ico")
w.attributes('-fullscreen',True)

global back_video
back_video=glob("Artworks/main background theam/*.mp4")

pygame.mixer.init()
pygame.joystick.init()


joystat=pygame.joystick.get_count()

if joystat==1:
    joy=pygame.joystick.Joystick(0)
else:
    joy=pygame.joystick.Joystick



def load_set():
    global main_theam,catch_og
    file =open("user_config.txt")
    data=True
    catch=""
    a=1
    while data:
        data=file.readline()
        if "theam" in data:
            print("yes its present in line no =",a)
            catch=data 
            break
        a=a+1

    catch_og=catch
    catch=catch.replace("theam = ","")    

    main_theam=int(catch)
    main_theam=main_theam-1

    
    file.close()



def reset():
    global fr
    fr=cv2.VideoCapture(back_video[main_theam])
    lab.pack()
    lab.place(x=-2,y=-2)
    video()
   
load_set()
 
def video():
    global photo,ps5_val
    ret,fram = fr.read() # this is the raw form 
    if not ret:
       
       print("end")
       reset()
       return
        #fr=cv2.VideoCapture("bfile.mp4")
        #video()
    ocap=cv2.cvtColor(fram,cv2.COLOR_BGR2RGB) # now this will give coloor   
    cap=PIL.Image.fromarray(ocap)
    photo = PIL.ImageTk.PhotoImage(image=cap)
    #print("heloo") 
    
    

   # jright=joy.get_button(5)
    if joystat==1: 
        jcros=joy.get_button(0)
        jcircle=joy.get_button(1)

        jleft=joy.get_hat(0)
        jright=joy.get_hat(0)
        jup=joy.get_hat(0)
        jdown=joy.get_hat(0)

        if jcircle==1:
            w.event_generate('<<circle>>')
        if jcros==1:
            w.event_generate('<<cros>>')
        if jright==(1,0):
            w.event_generate('<<jright>>')
            #print("cross is pressed")
        if jleft==(-1,0):
            w.event_generate('<<jleft>>')
   #         print("left is pressed")
        if jup==(0,1):
            w.event_generate('<<jup>>')
   #         print("left is pressed")
        if jdown==(0,-1):
            w.event_generate('<<jdown>>')
   #         print("left is pressed")

    
    
    


    lab.photo=photo
    lab.configure(image=photo)    

    lab.after(2,video)

def find_event():
    
    pass

def ps1():
    global lab,fr

    print("its me ps1")
    ps1scn=Canvas(width=1920,height=1080,background="pink")
    lab=Label()
    ps1scn.create_window(-2,-2,anchor=NW,window=lab)   
    
    fr.open(back_video[main_theam])
    
    ps1scn.pack()
    ps1scn.place(x=0,y=0)
    
    
    rom=os.listdir("rom\PS1")
    rom_path=os.listdir("rom\PS1")
    png_path=os.listdir("rom\PS1")
    
    grid_button=Button(text='view',background="yellow")
    grid_button.pack()
    grid_button.place(x=0,y=0)
    global prev_x
    global prev_y
    global png,img_btn

    prev_x=0
    prev_y=0

    a=0
    while a<len(rom):
        rom_path[a]="rom/PS1/"
        png_path[a]="rom/PS1/"
        
        a=a+1

    def fun (game): #yeh game function ek int lega or us no. ke game ko chalega 
        tem='core\ePSXe190\ePSXe.exe -nogui -loadiso '
        tem=tem+rom_path[game]
      #  print(tem)
        os.popen(tem)
    def scan(): #yeh rom path banega 
    #    print(len(rom))
        a=0
        while a<len(rom):
        
            rom_path[a]=rom_path[a]+rom[a]+"/"+rom[a]+".cue"
            png_path[a]=png_path[a]+rom[a]+"/"+rom[a]+".png"
            a=a+1        
    a=0                                                                                                                                                                                     
    while a<len(rom):

        print(rom_path[a]+"\n")
        print(png_path[a]+"\n")
        a=a+1

    def right(event):
        hover_sound()
        x=388
        y=35
        global prev_x    
        global prev_y
        #print("this is right x "+str(prev_x))
        #print("this is right y "+str(prev_y))
        if prev_x<width-600:   
            hov_img.place(x=x+prev_x,y=y+prev_y)
            #print(hov_img.place_info())
            prev_x=prev_x+x-8
        
    def left(event):
        hover_sound()
        global prev_x
        global prev_y
        #print("this is left x "+str(prev_x))
        #print("this is left y "+str(prev_y))
        x=388
        y=35
        if prev_x>370:   #kam hoga tho left zdaaa jaega and vice versa
        
            hov_img.place(x=prev_x-x+16,y=y+prev_y)
            #print(hov_img.place_info())
            prev_x=prev_x-x+8
        
        arr=hov_img.place_info()
        background_video(arr)


    def down(event):
        hover_sound()
        global prev_x
        global prev_y
        #print("this is down x "+str(prev_x))
        #print("this is down y "+str(prev_y))
        x=8
        y=520
        if prev_y==0:
            hov_img.place(x=prev_x+x,y=prev_y+y)
            #print(hov_img.place_info())
            prev_y=prev_y+y-35
        arr=hov_img.place_info()
        background_video(arr)
        

    def up(event):
        hover_sound()
        global prev_x
        global prev_y
        #print("this is up x "+str(prev_x))
        #print("this is up y "+str(prev_y))
        x=8
        y=35
        if prev_y<=520:
         hov_img.place(x=prev_x+x,y=y)
         prev_y=0
        arr=hov_img.place_info()
        background_video(arr)
        
    
    def enter(event):

        arr=hov_img.place_info()
        if  arr['x']=='8'and arr['y']=='35':
            fun(0)
        if  arr['x']=='388'and arr['y']=='35':  # 1 is nope
            fun(1)
        if  arr['x']=='768'and arr['y']=='35':
            fun(2)
        if  arr['x']=='1148'and arr['y']=='35': # 3 is nope
            fun(3)
        if  arr['x']=='1528'and arr['y']=='35':
            fun(4)
        if  arr['x']=='8'and arr['y']=='520':
            fun(5)
        if  arr['x']=='388'and arr['y']=='520':
            fun(6)
        if  arr['x']=='768'and arr['y']=='520':
            fun(7)
        if  arr['x']=='1148'and arr['y']=='520':
            fun(8)
        if  arr['x']=='1528'and arr['y']=='520':
            fun(9)
     #   print(arr['x'],arr['y'])
    scan()

    img_btn=[] 
    for a in range(len(rom)):
        p=PhotoImage(file=png_path[a])
        img_btn.append(p) 

    png=PhotoImage(file="hover.png")
    
    hov_img=Label(image=png,bd=0)
    hov_img.pack()

    hov_img.place(x=8,y=35)
    
    global button
    button=[]
    for a in range(len(rom)):
        b= Button(image=img_btn[a],command=lambda a=a:fun(a),borderwidth=0)
        b.pack()
        button.append(b)
    #button[0].place(x=50,y=50)    for button placement
    ###############################################################################
    d=0                                                                           #
    h=0
    temp=0
    a=0
    for a in range(len(rom)):
        if(d>width-100):
            h=h+480
            d=0 
            temp=0
        button[a].place(x=20+d,y=50+h)                                            #
                                                                                  #
        d=380*(temp+1)                                                            #
        temp=temp+1                                                               #
    ###############################################################################
    
    
# 
#    player=tkvideo(ps1scn,"bfile2.mp4",lblVideo,loop=1,size=(1920,1080))
#    player.play()
    def ext(event):
        ps1scn.destroy()   
        global lab
        #lab=""
        home(None) 
    

    w.bind('<Right>',right)
    w.bind('<<jright>>',right)

    w.bind('<Up>',up)
    w.bind('<<jup>>',up)

    
    w.bind('<Down>',down)
    w.bind('<<jdown>>',down)
   
    w.bind('<Left>',left)
    w.bind('<<jleft>>',left)
    
    w.bind('<Return>',enter)    
    w.bind('<<cros>>',enter)    
      
    w.bind('<BackSpace>',ext)
    w.bind('<<circle>>',ext)
 
    #print("main looop")

b_play=True
def setings():


  f=Canvas(w,width=650,height=600,bg="grey")
  
  f.pack()
  f.place(x=1600,y=750)
  
  lab1=Label(f,text="Resalution =",font="bold 20",bg="grey",fg="white")
  lab1.pack()
  lab1.place(x=10,y=50)
 
 
  lab2=Label(f,text="Main theam =",font="bold 20",bg="grey",fg="white")
  lab2.pack()
  lab2.place(x=10,y=120)
 
  pos=135
  t=35
  
  select=IntVar()

  select.set(2)
  
  
  def theam(value):
    global main_theam    
    main_theam=value-1
    fr.open(back_video[value-1])
    file=open("user_config.txt","r")
    data=file.read()
    file.close()
    main_theam=main_theam+1
    

    arr="theam = "+str(main_theam)+"\n"
    data=data.replace(catch_og,arr)
    
    file=open("user_config.txt","w")
    print(catch_og)
    print(arr)
    file.write(data)
    file.close()
    print("save done done donme")

  but1=Radiobutton(text="theam 1",variable=select,value=1,command=lambda:theam(select.get()))
  f.create_window(250,pos,window=but1)

  but2=Radiobutton(text="theam 2",value=2,variable=select,command=lambda:theam(select.get()))
  f.create_window(250,pos+t,window=but2)
  
  but3=Radiobutton(text="theam 3",value=3,variable=select,command=lambda:theam(select.get()))
  f.create_window(250,pos+t*2,window=but3)  

  but4=Radiobutton(text="theam 4",value=4,variable=select,command=lambda:theam(select.get()))
  f.create_window(250,pos+t*3,window=but4)  
  
  but5=Radiobutton(text="theam 5",value=5,variable=select,command=lambda:theam(select.get()))
  f.create_window(250,pos+t*4,window=but5)

  but6=Radiobutton(text="theam 6",value=6,variable=select,command=lambda:theam(select.get()))
  f.create_window(250,pos+t*5,window=but6)
  
  print(select.get())
  lab.place(x=-2,y=-2)
  #bt=Button(f,image=png,bg="red",command=lambda:print("asAS"))
  #bt.pack()
  #bt.place(x=10,y=200)
  
  click=StringVar()
  click.set("1920 x 1080")
  opt=OptionMenu(f,click,"1280 x 720","1920 x 1080","2048 x 3840",)
  opt.pack()
  opt.place(x=200,y=55)


  def ext(event):
    f.destroy()
    home(None)
  w.bind('<BackSpace>',ext)
      
def background_video(val):
        global b_play

        if b_play==True:
            if val==1:
                fr.open("Artworks\ps5\god of war\god of war.mp4")

            if val==2:
                fr.open("Artworks\ps5\horizon  forbiden west\Horizon Forbidden West - Announcement Trailer _ PS5-(1080p).mp4")

            if val==3:
                fr.open("Artworks\ps5\last of us part 1\last of us part 1.mp4")

            if val==4:
                fr.open("Artworks\ps5\\ratchat clank\Ratchet & Clank_ Rift Apart – Launch Trailer I PS5-(1080p).mp4")

            if val==5:
                fr.open("Artworks\ps5\miles morals\Marvel’s Spider-Man_ Miles Morales Launch Trailer I PS5, PS4-(1080p).mp4")

            if val==6:
                fr.open("Artworks\\ps5\\uncharted\\Uncharted_ Legacy of Thieves Collection – Launch Trailer _ PS5-(1080p60).mp4")

            if val==7:
                fr.open("Artworks\ps5\marvel spiderman\Marvel’s Spider-Man Remastered _ PC Launch Trailer-(1080p60).mp4")

            if val==8:
                fr.open("Artworks\\ps5\\days gone\\Days Gone – Story Trailer _ PS4-(1080p).mp4")


            

def home(event):
    print("its me home")

    show=True

    
    #global but
    

    #lab=Label() 
    
    pos=150

    #png.place(x=35,y=30)

    global fr,lab
    global png_ps1,png_ps5,png,ps5_val
    global home_hover
    home_hover=0
    ps5_val=False

   # fr=cv2.VideoCapture("Artworks\\main background theam\\2bfile.mp4")         

    frame=Canvas(bg="#1B1B1B",height=hight,width=width)
    png_ps1=PhotoImage(file="Artworks\\consoles\\ps1.png")
    
    lab=Label()
    frame.create_window(0,0,anchor=NW,window=lab)
   
    frame.pack(fill="both",expand=True)
    frame.place(x=-2,y=-2)
  #  video()

    #png_hover=Frame(background="orange",height=300,width=350)
    

    #image=cv2.imread(r"Artworks\\consoles\\ps1.png",1)
    
    png_ps5=PhotoImage(file="Artworks\\consoles\\ps5.png")
    
    but1=Label(image=png_ps5)

    but=Label(image=png_ps1) # bad mai label bana denge agaar moue use nahi karna hoga tho
    frame.create_window(150,pos+350,window=but)
    frame.create_window(150,pos,window=but1)
    #lab.pack()
    #lab.place(x=0,y=0)


    #png_hover.pack()
    #png_hover.place(x=40,y=50)

    #but.pack()
    #but.place(x=50,y=50)

    
    but3=Button(text="Pc GAMES", font="bold 30",height=5,background="green" )
    
    frame.create_window(150,pos+700,window=but3)
    # but3.pack()
    # but3.place(x=pos*2,y=50)
#
    # but4=Button(text="PC GAMES", font="bold 30",height=5,background="gold" )
    # but4.pack()
    # but4.place(x=pos*3,y=50)
#
    # 
    but2=Label(text="settings", font="bold 30",height=2)
     #but2.pack()
    frame.create_window(1850,1050,window=but2)
    #but2.place(x=1750,y=950)
   
    wmark=Label(text="CREATED BY CYBORGZONE", font="bold 80",bg="black",fg="red")
    frame.create_window(1100,500,window=wmark)
    
     
    global prev_x
    prev_x=0
    
    def right1(event):
            global home_hover
            print(home_hover)
            hover_sound()
            nomsat() 
            but2.configure(background="red")
            home_hover=4
            return        
    def left1(event):
        global home_hover
        print(home_hover)
        hover_sound()
        nomsat()
        but.configure(bd=10)
        home_hover=2
        return
    def up(event):
        global home_hover
        hover_sound()
        if home_hover==2:
            nomsat()
            but1.configure(bd=10)
            home_hover=1
            print("succes")
            return
        hover_sound()
        if home_hover==3:
            nomsat()
            but.configure(bd=10)
            home_hover=2
            print("succes")
            return

    def nomsat():
        but.configure(bd=0)        
        but1.configure(bd=0)        
        but2.configure(background="white")        
        
        but3.configure(background="green")        

    def down(event):
        global home_hover
        hover_sound()
        if home_hover==0:
            nomsat()
            but1.configure(bd=10)
            home_hover=1
            print("succes")
            return
    
        if home_hover==1:
            nomsat()
            but.configure(bd=10)
            home_hover=2
            print("succes")
            return
        
        if home_hover==2:
            nomsat()
            but3.configure(background="white")
            home_hover=3
            print("succes")
            return

    def enter1(event):
        global lab  
        
        if home_hover==1:
            frame.destroy()
            ps5()       
        if home_hover==2:
            frame.destroy()
            ps1()    
        if home_hover==3:
            frame.destroy()
            pc_games()
        if home_hover==4:
            frame.destroy()
            setings()
                
                
           
        #reset()
        #arr=png.place_info()
        ###print(arr['x'])
        ##
        #if arr['x']=='35':
        ##    png.place(x=1950,y=0)
        #    ps1()       
        #            #    
        #if arr['x']=='1485':
        #    png.place(x=1950,y=0)
            #   pcgames()
        
    
    def qu(NONE):
        w.quit()
        
    w.bind('<Right>',right1)
    w.bind('<<jright>>',right1)
    
    w.bind('<Left>',left1)
    w.bind('<Return>',enter1)    
    w.bind('<<cros>>',enter1)    
    
    w.bind('<Up>',up)    
    w.bind('<<jup>>',up)
   
    w.bind('<Down>',down)    
    w.bind('<<jdown>>',down)
    #w.bind('<<circle>>',qu)

    



def hover_sound():
    pygame.mixer.music.load("effects\\play.mp3")
    pygame.mixer.music.play()

def ps5():
    print("its ps5")
    global fr,lab,back_png
    global game_png
    global lab_game_png
    global scr
    scr=0
     
    game_png=[]
    lab_game_png=[]
  
    ps5_len=os.listdir("Artworks/ps5/")
    ps5_game_path=[]
    back_png=PhotoImage()

    Ps5_can=Canvas(width=1920,height=1080,background="black")
    lab=Label()
    #fr.open("Artworks\\main background theam\\bfile.mp4")
    wmark=Label(text="CREATED BY CYBORGZONE", font="bold 80",bg="black",fg="red")
    
    Ps5_can.create_window(-2,-2,anchor=NW,window=lab)#
    
  #  Ps5_can.create_window(300,500,anchor=NW,window=wmark)#
    
    
    for a in range (8):
        ps5_game_path.append("Artworks/ps5/"+ps5_len[a]+"/"+ps5_len[a]+".png")
    
    for a in range (8):    
        p=PhotoImage(file=ps5_game_path[a])
        game_png.append(p)
    
         
    ps5_frame=Frame(width=265,height=265,bg="white")
    #ps5_frame.pack()
    
    Ps5_can.place(x=0,y=0)
    pos=300
    
    for a in range (len(ps5_len)):    
        
        l=Label(image=game_png[a],bd=1)
        l.pack()
        lab_game_png.append(l)


  #  d=0                                                                           #
  #  h=0
  #  temp=0
  #  a=0
  #  for a in range (8):    
  #      #if(d>width-100):
  #      #    h=h+480    <---------------------FOR PLACE THE INTEM DOWN AFTER LIMIT 
  #      #    d=0 
  #      #    temp=0
  #      lab_game_png[a].place(x=30+d,y=40+h)                                            #
  #                                                                                #
  #      d=290*(temp+1)                                                            #
  #      temp=temp+1                                                               #
  #  
    

    #for a in range(len(ps5_game_path)):
    #    arr=(lab_game_png[a].place_info())
    #    print("this is "+ps5_len[a]+"  x  y  :  "+ arr["x"])
   
    y=80

    lab_game_png[0].place(x=2060,y=y) #days gone   
           
    lab_game_png[1].place(x=30,y=y)   #god of war
    
    lab_game_png[2].place(x=320,y=y)   #horizon
    #
    lab_game_png[3].place(x=610,y=y)   # last of us
    #
#
#
#
    lab_game_png[4].place(x=1770,y=y)   #spiderman
    #
    lab_game_png[5].place(x=1190,y=y)   #
    #
    lab_game_png[6].place(x=900,y=y)   # ratchat clank
    #
    lab_game_png[7].place(x=1480,y=y)   #



    #Ps5_can.create_image(0,0,image=back_png)
    #Ps5_can.create_ima ge(150,150,image=game_png)
    global b_play 
        

    
    global hover_position
    hover_position=0

    def ext(event):
        Ps5_can.destroy()  
        global lab
        home(None) 
        
    def normstat():
        fr.open(back_video[main_theam])
        lab_game_png[0].configure(bd=1)
        lab_game_png[1].configure(bd=1)
        lab_game_png[2].configure(bd=1)
        lab_game_png[3].configure(bd=1)
        lab_game_png[4].configure(bd=1)
        lab_game_png[5].configure(bd=1)
        lab_game_png[6].configure(bd=1)
        lab_game_png[7].configure(bd=1)
        
    
    def goto(val):
        #print(hover_position)  
                
        arr=lab_game_png[val].place_info()

        pos_x=int(arr['x'])
        pos_y=int(arr['y'])
        ps5_frame.place(x=pos_x-6,y=pos_y-6)
    
    def right(event):
        global hover_position
        global scr

        hover_sound()
        if hover_position==0 and scr==0:
            goto(1)
            hover_position=1
            background_video(1)
            return
        
        if hover_position==1 and scr==0:
            goto(2)
            background_video(2)
            hover_position=2
            return
        
        if hover_position==2 and scr==0:
            goto(3)
            background_video(3)
            hover_position=3
            return
        
        if hover_position==3 and scr==0:
            goto(6)
            background_video(4)
            hover_position=4
            return
        
        if hover_position==4 and scr==0:
            goto(5)
            background_video(5)
            hover_position=5
            return
        
        
        if hover_position==5 and scr==0:
            goto(7)
            background_video(6)
            hover_position=6
            return
        
        if hover_position==6 and scr==0:
            hidescr()
            goto(4)
            background_video(7)
            hover_position=7
            return
        
        if hover_position==7 and scr==2:
            goto(0)
            background_video(8)
            hover_position=8
            return
        
        if hover_position==6 and scr==2:
            goto(4)
            background_video(7)
            hover_position=7
            return
        
        
        
        if hover_position==5 and scr==2:
            goto(7)
            background_video(6)
            hover_position=6
            return
        
        
        
        if hover_position==4 and scr==2:
            goto(5)
            background_video(5)
            hover_position=5
            return
        
    
    def hidescr():
     global scr
     
     
     if hover_position==6 and scr<=1 or hover_position==7 and scr<=1:
        scr=2
        lab_game_png[0].place(x=2060-pos-pos,y=y)   
        lab_game_png[1].place(x=30-pos-pos,y=y)   
        lab_game_png[2].place(x=320-pos-pos,y=y)   
        lab_game_png[3].place(x=610-pos-pos,y=y)   
        lab_game_png[4].place(x=1770-pos-pos,y=y)   
        lab_game_png[5].place(x=1190-pos-pos,y=y)   
        lab_game_png[6].place(x=900-pos-pos,y=y)   
        lab_game_png[7].place(x=1480-pos-pos,y=y)   
    
     
     
     if hover_position==4:
        scr=1
        lab_game_png[0].place(x=2060,y=y)   
        lab_game_png[1].place(x=30,y=y)   
        lab_game_png[2].place(x=320,y=y)   
        lab_game_png[3].place(x=610,y=y)   
        lab_game_png[4].place(x=1770,y=y)   
        lab_game_png[5].place(x=1190,y=y)   
        lab_game_png[6].place(x=900,y=y)   
        lab_game_png[7].place(x=1480,y=y)   



    def left(event):
      
        
        global hover_position
        global scr

        hover_sound()
        if hover_position==1 and scr==0:
            fr.open(back_video[main_theam])
            hover_position=0            
           
            ps5_frame.place(x=-350,y=y)
            return
        if hover_position==2 and scr==0:

            goto(1)
            hover_position=1
            background_video(1)
            return
        if hover_position==3 and scr==0:

            goto(2)
            hover_position=2
            background_video(2)
            return
        if hover_position==4 and scr==0:

            goto(3)
            background_video(3)
            hover_position=3
            return
        if hover_position==5 and scr==0:
            goto(6)
            background_video(4)
            hover_position=4
            return
        
        if hover_position==6 and scr==0:
            goto(5)
            background_video(5)
            hover_position=5
            return
        
        
        if hover_position==7 and scr==2:
            goto(7)
            background_video(6)
            hover_position=6
            return
        
        if hover_position==8 and scr==2:
            goto(4)
            background_video(7)
            hover_position=7
            return
    
     
        if hover_position==7 and scr==2:
            goto(6)
            background_video(6)
            hover_position=6
            return
        
        if hover_position==6 and scr==2:
            goto(5)
            background_video(5)
            hover_position=5
            return
        
        if hover_position==5 and scr==2:
            goto(6)
            background_video(4)
            hover_position=4
            return
        
        
        
        if hover_position==5 and scr==2:
            goto(6)
            background_video(4)
            hover_position=4
            return
        
        
        if hover_position==4 and scr==2:
            hidescr()
            scr=0
            goto(3)
            background_video(3)
            hover_position=3
            return
        
        


    w.bind('<Right>',right)
    w.bind('<<jright>>',right)    
    
    w.bind('<Left>',left)
    w.bind('<<jleft>>',left)

    w.bind('<BackSpace>',ext)
    w.bind('<<circle>>',ext)    

    w.bind('<space>',back_video_pause)
    

def add():
    #window.Tk(Toplevel)
    pass


def pc_games():

    global lab,game_png,position
    position=0
    game_png=[]
    lab_game_png=[]
  
    pc_game_len=os.listdir("Artworks/pc_games/")
    pc_game_path=[]

    for a in range (len(pc_game_len)):
        pc_game_path.append("Artworks\\pc_games\\"+pc_game_len[a]+"\\")
    
    for a in range (len(pc_game_len)):    
        tem=pc_game_path[a]+"Untitled"+".png"
        p=PhotoImage(file=tem)
        
        game_png.append(p)
    
    print(pc_game_path)

    can=Canvas(width=width,height=hight,bg="black")
    lab=Label()
    but=Button(text="ADD",activebackground="red",command=add)
    #la=Label(image=game_png[0],bd=2)
    can.create_window(962,542,window=lab)
    can.create_window(1900,10,window=but)


    for a in range (len(pc_game_len)):    
        p=Label(image=game_png[a],bd=3)
        p.pack()
        lab_game_png.append(p)
    
    def defa_scr():
        
        for a in range (len(pc_game_len)):    
            lab_game_png[a].place(x=300*a+30,y=70)

    defa_scr()
    
    def scr():
        print("its the scroll")

        for a in range (6):    
            lab_game_png[a].place(x=30,y=70)
         
        a=6
        while a<len(pc_game_len):    
            lab_game_png[a].place(x=300*(a-5)+30,y=70)
            a+=1

    def right(event):
        global position
        #print("this pc leb right "+str(position))
        if position <len(pc_game_len):
            if position==6:
                print("its scroll")
                scr()
            lab_game_png[position-1].configure(bd=3)
            lab_game_png[position].configure(bd=10)
            hover_sound()
            position+=1
        #print("this pc leb right "+str(position))
        return
    
    def left(event):
        global position
        #print("this pc leb "+str(position))
        if position >1:
            if position==6:
                defa_scr()
            lab_game_png[position-1].configure(bd=3)
            lab_game_png[position-2].configure(bd=10)
            hover_sound()
            position-=1

        #print("this pc leb "+str(position))
        return

    def enter(event):  
        tem1=pc_game_path[position-1]+pc_game_len[position-1]+".lnk"
        print(tem1)
        os.popen(tem1)
        can.destroy
        print(pc_game_len[position-1]+" is playing")
       
    def ext(event):
        can.destroy()
        home(None)
    w.bind('<BackSpace>',ext)
 
    w.bind('<Right>',right)
    w.bind('<Left>',left)
    w.bind('<Return>',enter)
    
    can.pack()
    can.place(x=-2,y=-2)

def add():
    win=Tk()

    win.title("ADD FUNCTION")
    win.geometry("300x200")
    win.iconbitmap("main.ico")
    
    l=Label(win,text="Enter name ",font="bold 15")
    l.place(x=10,y=10)
    


    l1=Label(win,text="IMAGE FILE",font="bold 15")
    l1.place(x=10,y=60)
    
    l2=Label(win,text="EXE FILE",font="bold 15")
    l2.place(x=10,y=100)
    

    ent=Entry(win)
    ent.place(x=140,y=17)

    def chsf(a):
        global img_file
        global exe_file
        if a==1:
            img_file= f.askopenfilename()
            print(img_file)
            a=0
            return
        
        if a==2:
            exe_file= f.askopenfilename()
            print(exe_file)
            a=0
            return
    
    bu=Button(win,text="chose img file",command=lambda:chsf(1))
    bu.pack()
    bu.place(x=150,y=60)
    

    bu1=Button(win,text="chose exe file",command=lambda:chsf(2))
    bu1.pack()
    bu1.place(x=150,y=100)


    def done1():
        name=ent.get()
        
        game_path="Artworks\\pc_games\\"+name
        os.mkdir(path=game_path)        
 
        shutil.copy(img_file,game_path)
        
        tem=glob(game_path+"\\*.png")
        print(tem[0]) 
        os.popen("rename "+tem[0]+" "+"Untitled.png")

        win.destroy()

        
   
    but=Button(win,text="DONE",command=done1,activebackground="yellow")
    but.place(x=100,y=150)


def back_video_pause(event):
    global b_play
    if b_play==False:
        b_play=True
        return

    
    b_play=False 

fr=cv2.VideoCapture(back_video[main_theam])         
lab=Label()

video()
pc_games()
#home(None)

def qu(NONE):
    w.quit()


w.bind('<Escape>',qu)


if joystat==0:
    print("joystic not pressent "+str(joystat))
 
        #joy=pygame.joystick.Joystick(event.device_index)

#print(joy.get_numaxes())

find_event()



w.mainloop()


     