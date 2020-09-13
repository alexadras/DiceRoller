import tkinter as tk
from random import randint

def color_default():
    btn_plus["fg"] = "black" 
    btn_plus["bg"] = "light gray"

def roll():
#no label
    r = randint(1,num_lados)
    if r == num_lados:
        lbl_valor["fg"] = "green"
    elif r == 1:
        lbl_valor["fg"] = "red"
    else:
        lbl_valor["fg"] = "black"
        
    lbl_valor["text"] = f'{ r }'

#no button plus
    btn_plus["text"] = "+"
    color_default()

def increase():
    v = int(lbl_valor["text"])
    lbl_valor["text"] = f'{v +1 }'
    lbl_valor["fg"] = "yellow"
    lbl_valor["bg"] = "gray"
    
    text = btn_plus["text"].replace("+","")
    if text != "":
        num = int(text)
    else:
        num = int( text + "0" )
    
    btn_plus["text"] = f'+{num + 1}'
    btn_plus["fg"] = "yellow"
    btn_plus["bg"] = "gray" 
    
#dados
num_lados = 6 # nuemros de lados do dado

def defaultColor():
    btn_d4["bg"] = "light gray"
    btn_d6["bg"] = "light gray"
    btn_d8["bg"] = "light gray"
    btn_d10["bg"] = "light gray"
    btn_d12["bg"] = "light gray"
    btn_d20["bg"] = "light gray"

def d4():
   global num_lados
   num_lados = 4
   roll()

   defaultColor()
   btn_d4["bg"] = "gray"
    
def d6():
    global num_lados
    num_lados = 6
    roll()

    defaultColor()
    btn_d6["bg"] = "gray"
    
def d8():
    global num_lados
    num_lados = 8
    roll()

    defaultColor()
    btn_d8["bg"] = "gray"
   
    
def d10():
    global num_lados
    num_lados = 10
    roll()

    defaultColor()
    btn_d10["bg"] = "gray" 
    
def d12():
    global num_lados
    num_lados = 12
    roll()

    defaultColor()
    btn_d12["bg"] = "gray" 
    
def d20():
    global num_lados
    num_lados = 20
    roll()

    defaultColor()
    btn_d20["bg"] = "gray"
  

#Programa 
win = tk.Tk()
win.title("Dice roller")

frm_control = tk.Frame(master=win)
frm_control.rowconfigure(0, minsize = 100, weight = 1)
frm_control.columnconfigure([0,1,2], minsize = 100, weight = 1)

btn_roll = tk.Button( master=frm_control, text = "roll", command=roll)
btn_roll["bg"] = "light gray"
btn_roll.grid( row=0, column=0, sticky="nsew")

lbl_valor = tk.Label(master=frm_control, text="0", font = "ariel 30 normal")
lbl_valor["bg"] = "gray"
lbl_valor.grid(row=0, column=1, sticky="nsew" )

btn_plus = tk.Button( master=frm_control , text = "+", command=increase)
color_default()
btn_plus.grid( row=0, column=2, sticky="nsew" )

#dicTips
frm_dicTips = tk.Frame(master=win)
frm_dicTips.rowconfigure(0, minsize = 50, weight = 1)
frm_dicTips.columnconfigure([0,1,2,3,4,5], minsize = 50, weight = 1)

btn_d4 = tk.Button( master=frm_dicTips , text = "d4", command=d4)
btn_d4["bg"] = "light gray"
btn_d4.grid(row = 0, column=0, sticky="nsew" )

btn_d6 = tk.Button( master=frm_dicTips , text = "d6", command=d6)
btn_d6["bg"] = "gray"
btn_d6.grid(row=0, column=1, sticky="nsew" )

btn_d8 = tk.Button( master=frm_dicTips , text = "d8", command=d8)
btn_d8["bg"] = "light gray"
btn_d8.grid(row=0, column=2, sticky="nsew" )

btn_d10 = tk.Button( master=frm_dicTips , text = "d10", command=d10)
btn_d10["bg"] = "light gray"
btn_d10.grid(row=0, column=3, sticky="nsew" )

btn_d12 = tk.Button( master=frm_dicTips , text = "d12", command=d12)
btn_d12["bg"] = "light gray"
btn_d12.grid(row=0, column=4, sticky="nsew" )

btn_d20 = tk.Button( master=frm_dicTips , text = "d20", command=d20)
btn_d20["bg"] = "light gray"
btn_d20.grid(row=0, column=5, sticky="nsew" )
    
#show conatiner 
frm_control.pack()
frm_dicTips.pack()
win.mainloop()
