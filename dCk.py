from tkinter import *
import datetime
import os

def r_p(re_pa):
    try:
        base_p = sys._MEIPASS
    except Exception:
        base_p = os.path.abspath(".")

    return os.path.join(base_p, re_pa)  

def d_t():
    time = datetime.datetime.now()
    hti = time.strftime("%I")
    mti = time.strftime("%M")
    sti = time.strftime("%S")
    apti = time.strftime("%p")

    date = time.strftime("%d")
    month = time.strftime("%m")
    year = time.strftime("%y")
    day = time.strftime("%a") 

    ht.config(text=hti)
    mt.config(text=mti)
    st.config(text=sti)
    apt.config(text=apti)
    ht.after(200,d_t)

    dd.config(text=date)
    man.config(text=month)
    yt.config(text=year)
    dyt.config(text=day)


clock = Tk()
clock.title("Clock")
clock.geometry("900x500")
i = PhotoImage(file = r_p("c1.png"))
l = Label(image=i)
l.pack()


h = Label(clock,text="Hour", font= ("Time New Roman",17),fg="red",highlightbackground="#ee6b6e",highlightthickness=1)
h.place(x = 70,y = 160,height=30,width=80)

ht = Label(clock,text="Hour", font= ("Time New Roman",25,"bold"),fg="white",bg="red",highlightbackground="#f69697",highlightthickness=2)
ht.place(x = 70,y = 50,height=100,width=80)

m = Label(clock,text="Min", font= ("Time New Roman",17),fg="red",highlightbackground="#ee6b6e",highlightthickness=1)
m.place(x = 310,y = 160,height=30,width=80)

mt = Label(clock,text="Min", font= ("Time New Roman",25,"bold"),bg="red",fg="white",highlightbackground="#f69697",highlightthickness=2)
mt.place(x = 310,y = 50,height=100,width=80)

s = Label(clock,text="Sec", font= ("Time New Roman",17),fg="red",highlightbackground="#ee6b6e",highlightthickness=1)
s.place(x = 540,y = 160,height=30,width=80)

st = Label(clock,text="Sec", font= ("Time New Roman",25,"bold"),bg="red",fg="white",highlightbackground="#f69697",highlightthickness=2)
st.place(x = 540,y = 50,height=100,width=80)

ap = Label(clock,text="AM/PM", font= ("Time New Roman",16),fg="red",highlightbackground="#ee6b6e",highlightthickness=1)
ap.place(x = 750,y = 160,height=30,width=80)

apt = Label(clock,text="Am/Pm", font= ("Time New Roman",25,"bold"),bg ="red", fg="white",highlightbackground="#f69697",highlightthickness=2)
apt.place(x = 750,y = 50,height=100,width=80)

########for date ##########

d = Label(clock,text="Day", font= ("Time New Roman",17),fg="red",highlightbackground="#ee6b6e",highlightthickness=1)
d.place(x = 70,y = 410,height=30,width=80)

dd = Label(clock,text="Hour", font= ("Time New Roman",25,"bold"),fg="white",bg="red",highlightbackground="#f69697",highlightthickness=2)
dd.place(x = 70,y = 300,height=100,width=80)

ma = Label(clock,text="Month", font= ("Time New Roman",17),fg="red",highlightbackground="#ee6b6e",highlightthickness=1)
ma.place(x = 310,y = 410,height=30,width=80)

man = Label(clock,text="M", font= ("Time New Roman",25,"bold"),bg="red",fg="white",highlightbackground="#f69697",highlightthickness=2)
man.place(x = 310,y = 300,height=100,width=80)

y = Label(clock,text="Year", font= ("Time New Roman",17),fg="red",highlightbackground="#ee6b6e",highlightthickness=1)
y.place(x = 540,y = 410,height=30,width=80)

yt = Label(clock,text="Sec", font= ("Time New Roman",25,"bold"),bg="red",fg="white",highlightbackground="#f69697",highlightthickness=2)
yt.place(x = 540,y = 300,height=100,width=80)

dy = Label(clock,text="day", font= ("Time New Roman",17),fg="red",highlightbackground="#ee6b6e",highlightthickness=1)
dy.place(x = 750,y = 410,height=30,width=80)

dyt = Label(clock,text="Am/Pm", font= ("Time New Roman",25,"bold"),bg ="red", fg="white",highlightbackground="#f69697",highlightthickness=2)
dyt.place(x = 750,y = 300,height=100,width=80)

d_t()
clock.mainloop()