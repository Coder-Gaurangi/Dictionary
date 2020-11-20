from tkinter import *
import json
from difflib import get_close_matches

#################Function Definitions
def nearmatch(user_data, keys):
    return get_close_matches(user_data,keys)


def printer_func(data, items):
    t1.delete(1.0, END)
    for value in items:
        t1.insert(END, value + '\n')

def data_check(user_data, keys, data1):
    if user_data in keys:
        item1 = data1[user_data]
        printer_func(user_data, item1)
        return 1
    elif user_data.title() in keys:
        item1 = data1[user_data.title()]
        printer_func(user_data.title(), item1)
        return 1
    elif user_data.upper() in keys:
        item1 = data1[user_data.upper()]
        printer_func(user_data.upper(), item1)
        return 1
    elif user_data.lower() in keys:
        item1 = data1[user_data.lower()]
        printer_func(user_data.lower(), item1)
        return 1
    else:
        return 0

def get_dict_value(user_data, keys, data1):
    if data_check(user_data,keys,data1):
            user_data = "/exit"
    else:
        closematch = nearmatch(user_data,keys)
        if len(closematch) > 0:
            t1.delete(1.0, END)
            t1.insert(END, "Did you mean one of these:"  + '\n')
            for value in closematch:
                t1.insert(END, value + '\n')
        else:
            t1.delete(1.0, END)
            t1.insert(END, "Word does not exist in language" + '\n')

def get_val_from_Screen():
    data1 = json.load(open("data.json"))
    keys = data1.keys()
    get_dict_value(user_value.get(),keys, data1)

############# Main Function

root=Tk()
root.geometry('900x600+300+100')
root.configure(bg='powder blue')            #background colour set to white
root.title('DICTIONARY')

fontLabel = Label(root,text='welcome to DICTIONARY',font=('algerian',40,'italic bold'),bg='powder blue',fg='blue')
fontLabel.place(x=130, y=10)                #alignment of heading

user_value = StringVar()
wordEntry = Entry(root,font=('airal',20),bd=8,textvariable=user_value)              #entry box
wordEntry.place(x=280,y=160)
btn=Button(root,text='finding meaning',command=get_val_from_Screen)
btn.place(x=385,y=220)

t12 = Label(root, text=" Definition(s):",font=('airal',20,'italic bold'),fg='blue',bg='powder blue')
t12.place(x=100,y=270)
t1=Text(root, height=30, width=90)
t1.place(x=100,y=310)

root.mainloop()