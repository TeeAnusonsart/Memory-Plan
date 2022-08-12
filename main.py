import tkinter as tk
from tkinter import*
from tkcalendar import Calendar
from tkcalendar import DateEntry
import pickle
import datetime as dt
from datetime import datetime

try: 
    with open('data.dat', 'rb') as file:
        data=pickle.load(file)
    with open('info.dat', 'rb') as file:
        infos=pickle.load(file)
except:
    data = []
    infos = []

dl=[]
alert_date=[]


today = dt.datetime.now()
window = tk.Tk()
window.title("Futureplan")
window.minsize(width=700,height=600)

cal = Calendar(window, selectmode = 'day',
               year = today.year, month = today.month,
               day = today.day,bordercolor="red",background="#BF3EFF"
               ,normalbackground="#FFBBFF", headersbackground="#EE6AA7"
               ,weekendbackground="#FFBBFF",selectbackground="red"
               ,disabledselect="black",date_pattern=('y,m,dd'))


cal.pack(pady = 50,fill="both",ipady="50")


for i in data:
    dates = dt.datetime(i[0], i[1], i[2])
    cal.calevent_create(dates,"", tags="hu")
    cal.tag_config("hu", background="violet")


    
def grad_date():
    getdate=cal.get_date()
    info=text_input.get()
    dl=list(map(lambda x:int(x),getdate.split(","))) 
    dates = dt.date(dl[0], dl[1], dl[2])
    cal.calevent_create(dates,"", tags="hu")
    cal.tag_config("hu", background="violet")
    data.append(dl)
    infos.append(info)
    with open('data.dat', 'wb') as file:
        pickle.dump(data, file)
    with open('info.dat', 'wb') as file:
        pickle.dump(infos,file)

def get_info():
    getdate=cal.get_date()
    x=list(map(lambda x:int(x),getdate.split(","))) 
    for i in range(len(data)):
        if x==data[i]:
            date.config(text=infos[i]+" deadline "+getdate)
        else :
            date.config(text=" none ")

def remove_info():
    getdate=cal.get_date()
    x=list(map(lambda x:int(x),getdate.split(","))) 
    dates = dt.date(x[0], x[1], x[2])
    cal.calevent_create(dates,"", tags="hi")
    cal.tag_config("hi", background="#FFBBFF",foreground="black")
    for i in range(len(data)):
        if x==data[i]:
            del data[i]
            with open('data.dat', 'wb') as file:
                pickle.dump(data, file)

text= tk.Label(master=window,text="ป้อนงานของคุณ : ")
text.pack()


text_input= tk.Entry(master=window)
text_input.pack(ipady="10",ipadx="20")

button = tk.Button(master = window, text="Get Date" ,command = grad_date).pack(pady = 20)
show_info_button=tk.Button(master = window, text="Get info" ,command = get_info).pack(pady = 20)
remove_button=tk.Button(master = window, text="Remove info" ,command = remove_info).pack(pady = 20)
date = Label(window, text = "")
date.pack(pady = 20)


window.mainloop()
