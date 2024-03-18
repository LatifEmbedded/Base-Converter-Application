from tkinter import*
import tkinter as tk
from tkinter import ttk
def function(from_base, to_base) :
    try :
        number =int(Number.get(), from_base)
        if to_base == 10 :
            result.delete(0, END)
            number = str(number)
            result.insert(END, number)
        elif to_base == 2 :
            result.delete(0, END)
            number = bin(number)
            number = str(number)
            result.insert(END, number)
        elif to_base == 8 :
            result.delete(0, END)
            number = oct(number)
            number = str(number)
            result.insert(END, number)
        elif to_base == 16 :
            result.delete(0, END)
            number = hex(number)
            number = str(number)
            result.insert(END, number)
    except :
        Number.delete(0, END)
        Number.config(background = 'RED')       
        Number.insert(END, '_ERROR_')
        Number.after(1000, cleaRing)
def desTro(event = None) :
    wndw.destroy()
def cleaRing() :
    Number.config(background = 'white')
    Number.delete(0, END)
def CheckTo(string) :
    if string == "Hexadecimal" : 
        return True, 16
    elif string == "Octal" : 
        return True, 8
    elif string == "Binary" : 
        return True, 2
    elif string == "Decimal": 
        return True, 10
    else :
        return False, "nothing"
def check(string) :
    if string == "Hexadecimal" : 
        return True, 16
    elif string == "Octal" : 
        return True, 8
    elif string == "Binary" : 
        return True, 2
    elif string == "Decimal": 
        return True, 10
    else :
        return False, "nothing"
def ClearEntry(event = None) :
    Number.delete(0, END)
    result.delete(0, END)
    combobox.delete(0, END)
    combobox_1.delete(0, END)
def gets(event = None) :
    global base_from, base_to
    base_from = combobox.get()
    base_to = combobox_1.get()
def OK(event = None) :
    state, from_base = check(base_from)
    stt, to_base = CheckTo(base_to)
    function(from_base, to_base)
wndw = Tk()
wndw.configure(background = 'grey')
wndw.minsize(300, 300)
wndw.maxsize(300, 300)
wndw.resizable(False, False)
wndw.title('Base Converter')
lists = ["Hexadecimal", "Octal", "Decimal", "Binary"]
text = Label(wndw, text = 'Number', background = 'grey', fg = 'black').place(x = 20, y = 30)
Number = Entry(wndw, width = 25, justify = CENTER)
Number.place(x = 100, y = 30)
text = Label(wndw, text = 'From Base', background = 'grey', fg = 'black').place(x = 20, y = 70)
combobox = ttk.Combobox(wndw, values = lists, width = 22)
combobox.place(x = 100, y = 70)
text = Label(wndw, text = 'To Base', background = 'grey', fg = 'black').place(x = 20, y = 110)
combobox_1 = ttk.Combobox(wndw, values = lists, width = 22)
combobox_1.place(x = 100, y = 110)
text = Label(wndw, text = 'Result', background = 'grey', fg = 'black').place(x = 20, y = 150)
result = Entry(wndw, width = 25, justify=  CENTER)
result.place(x = 100, y = 150)
ok_button = Button(wndw, text = 'OK', background = 'grey', fg = 'white', activebackground = 'grey', activeforeground = 'white', width = 5, height = 1, command = OK).place(x = 100, y = 190)
clear_button = Button(wndw, text = 'CLEAR', background = 'grey', fg = 'white', activebackground = 'grey', activeforeground = 'white', width = 5, height = 1, command = ClearEntry).place(x = 210, y = 190)
wndw.bind('<Return>', OK)
menu_bar = Menu(wndw)
wndw.config(menu = menu_bar)
file = Menu(menu_bar, tearoff = 0)
file.add_command(label = 'Exit', command = desTro)
menu_bar.add_cascade(label = 'File', menu = file)
wndw.bind('<Control-e>', desTro)
wndw.bind('<Control-c>', ClearEntry)
combobox.bind("<<ComboboxSelected>>", gets)
combobox_1.bind("<<ComboboxSelected>>", gets)
base_from = 0
base_to = 0
wndw.mainloop()