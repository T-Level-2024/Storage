import tkinter
from tkinter import ttk
root = tkinter.Tk()
gift_list = {}

def input_window():
    top=tkinter.Toplevel(root)
    top.geometry("150x50")
    top.title("Item input")
    tkinter.Label(top, text="Enter item:").pack(side=tkinter.TOP)
    item = tkinter.StringVar(top)
    text = tkinter.Entry(top, textvariable=item).pack(side=tkinter.TOP)
    def add_item(parameter):
        global gift_list
        try:
            gift_list[item.get()]
        except KeyError:
            gift_list[item.get()] = 1
        else:
            gift_list[item.get()] += 1
        finally:
            top.destroy()
    top.bind("<Return>", add_item)

def list_window():
    top=tkinter.Toplevel(root)
    top.geometry("250x500")
    top.title("Gift list")
    if gift_list == {}:
        return
    items = []
    i = 0
    for key, value in gift_list.items():
        print("{} - {}".format(key, value))
        items.insert(i, "{} - {}".format(key, value))
        i+=1
    listbox = tkinter.Listbox(top, width=250, height=500)
    listbox.pack(side=tkinter.TOP)
    listbox.insert(0, *items)

root.title("Santa Gift Tracker")
root.geometry("150x155")
root.minsize(200, 150)
tkinter.Label(root, text="Santa Gift Tracker").pack(side=tkinter.TOP)
tkinter.Button(root, text="Add item", command=input_window).pack(side=tkinter.TOP)
tkinter.Button(root,text="View list", command=list_window).pack(side=tkinter.TOP)
tkinter.Button(root, text="Quit", command=root.destroy).pack(side=tkinter.TOP)
root.mainloop()
