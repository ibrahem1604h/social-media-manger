from tkinter import*
import webview

app=Tk()
app.title("S.M.M")
app.geometry("1000x600+200+50")
app.iconbitmap("imag/li-ion_14984919.ico")
app.configure(bg="#636768")

title_en=Label(app,text="Sociala Media Manger",
             fg="black", bg="#347383",
             font=("Courier",16)
             )

title_en.pack(fill=X)
image=PhotoImage(file="imag/top-view-man-working-home.png")
image_lable=Label(app,image=image)

image_lable.place(x=240,y=80,width=700,height=400)

title_ar=Label(app,text=" تطبيق مواقع تواصل اجتماعي",
             fg="black", bg="#636768",
             font=("Courier",26,"bold")
             )
title_ar.place(x=320,y=520)

side=Frame(app,width=180,height=590,bg="#347383",bd=0,relief=GROOVE)
side.place(x=0,y=24)

side_titel1=Label(side,text="Ibrahim.io",bg="#347383",fg="black",font=("Courier",13,"bold"))
side_titel1.place(x=5,y=10)

user=PhotoImage(file="imag/user_187488.png")
face=PhotoImage(file="imag/facebook_5968764.png")
insta=PhotoImage(file="imag/instagram_2111463.png")
tiktok=PhotoImage(file="imag/tik-tok_4782345.png")
youtupe=PhotoImage(file="imag/youtube_4494485.png")
gethub=PhotoImage(file="imag/github_919847.png")
X=PhotoImage(file="imag/x (1).png")

def facebock():
    url="https://www.facebook.com/"
    webview.create_window(
    "YOUR ACCOUNT",
    url,
    width=815,
    height=560,
    resizable=False,
    x=390,y=120,
    zoomable=True
    )
    webview.start()

def inastgramg():
    url="https://www.instagram.com/"
    webview.create_window(
    "YOUR ACCOUNT",
    url,
    width=815,
    height=560,
    resizable=False,
    x=390,y=120,
    zoomable=True
    )
    webview.start()

def youtube():
    url="https://www.youtube.com/"
    webview.create_window(
    "YOUR ACCOUNT",
    url,
    width=815,
    height=560,
    resizable=False,
    x=390,y=120,
    zoomable=True
        
    )
    webview.start()
    
    
def tkitok():
    url="https://www.tiktok.com/"
    webview.create_window(
    "YOUR ACCOUNT",
    url,
    width=815,
    height=560,
    resizable=False,
    x=390,y=120,
    zoomable=True
    )
    webview.start()
    
def X_twitter():
    url="https://www.X.com/"
    webview.create_window(
    "YOUR ACCOUNT",
    url,
    width=815,
    height=560,
    resizable=False,
    x=390,y=120,
    zoomable=True
    )
    webview.start()
    
    
    
def github():
    url="https://github.com/"
    webview.create_window(
    "YOUR ACCOUNT",
    url,
    width=815,
    height=560,
    resizable=False,
    x=390,y=120,
    zoomable=True
    )
    webview.start()
    
    

profil=Button(side,text="IBRAHIM FISAL",
              image=user,
              cursor="hand2",
              bd=0,
              relief=RIDGE,
              compound=TOP,
              width=90,
              height=90,
              bg="#347383",
              )
profil.place(x=25,y=50)

side_titel2=Label(side,text="sociala app",bg="#347383",fg="black",font=("Courier",12,"bold"))
side_titel2.place(x=25,y=160)

face_buttom=Button(side,
                   text="Facebock",
                   bd=0,
                   image=face,
                   width=60,
                   height=60,
                   bg="#347383",
                   cursor="hand2",
                   compound=TOP,
                   relief=RIDGE,  
                   command=facebock,
                   )
face_buttom.place(x=20,y=180)

insta_buttom=Button(side,
                   text="Instagram",
                   bd=0,
                   image=insta,
                   width=60,
                   height=60,
                   bg="#347383",
                   cursor="hand2",
                   compound=TOP,
                   relief=RIDGE, 
                   command=inastgramg)
insta_buttom.place(x=20,y=245)

tiktok_buttom=Button(side,
                   text="Tik Tok",
                   bd=0,
                   image=tiktok,
                   width=60,
                   height=60,
                   bg="#347383",
                   cursor="hand2",
                   compound=TOP,
                   relief=RIDGE,     
                   command=tkitok)
tiktok_buttom.place(x=20,y=310)

youtupe_buttom=Button(side,
                   text="Youtube",
                   bd=0,
                   image=youtupe,
                   width=60,
                   height=60,
                   bg="#347383",
                   cursor="hand2",
                   compound=TOP,
                   relief=RIDGE, 
                   command=youtube)
youtupe_buttom.place(x=20,y=375)

gethub_buttom=Button(side,
                   text="GitHub",
                   bd=0,
                   image=gethub,
                   width=60,
                   height=60,
                   bg="#347383",
                   cursor="hand2",
                   compound=TOP,
                   relief=RIDGE,
                   command=github)
gethub_buttom.place(x=20,y=440)

twitter_buttom=Button(side,
                   text="X",
                   bd=0,
                   image=X,
                   width=60,
                   height=60,
                   bg="#347383",
                   cursor="hand2",
                   compound=TOP,
                   relief=RIDGE, 
                   command=X_twitter    
                   )
twitter_buttom.place(x=20,y=505)


app.mainloop()



