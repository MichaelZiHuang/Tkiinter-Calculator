from tkinter import *
from math import sin, cos, tan

class MyFirstGui:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        #Grid.rowconfigure(master, 0, weight=1)
        #Grid.rowconfigure(master, 1, weight=1)
        #Grid.rowconfigure(master, 2, weight=1)
        #Grid.columnconfigure(master, 0, weight=1)
        #Grid.columnconfigure(master, 1, weight=1)
        #Grid.columnconfigure(master, 2, weight=1)

        self.val = "0"
        self.total_label_text = StringVar()
        self.total_label_text.set(self.val)

        self.input = Entry(master, text=self.total_label_text, width=5)
        self.input.grid(row=0, columnspan=3, sticky=W+E)

        self.total = Label(master, textvariable=self.total_label_text)
        #self.total.grid(row=0, columnspan=3, sticky=W+E)
        """
        for i in range(1, 10):
            #for j in range(1, 4):
            self.i = Button(master, text=i, width=4)
        for i in range(0, 3):
            self.i.pack()
        """
        self.Zero = Button(master, text="0", command=lambda: self.update("0"), width=4)
        self.One = Button(master, text="1", command=lambda: self.update("1"), width=4)
        self.Two = Button(master, text="2", command=lambda: self.update("2"))
        self.Three = Button(master, text="3", command=lambda: self.update("3"),width=4)
        self.Four = Button(master, text="4", command=lambda: self.update("4"), width=4)
        self.Five = Button(master, text="5", command=lambda: self.update("5"),width=4)
        self.Six = Button(master, text="6", command=lambda: self.update("6"))
        self.Seven = Button(master, text="7", command=lambda: self.update("7"),width=4)
        self.Eight = Button(master, text="8", command=lambda: self.update("8"))
        self.Nine = Button(master, text="9", command=lambda: self.update("9"))

        self.Sub = Button(master, text="-", command=lambda: self.update("-"))
        self.Plus = Button(master, text="+", command=lambda: self.update("+"))
        self.Div = Button(master, text="/", command=lambda: self.update("/"))
        self.Mult = Button(master, text="*", command=lambda: self.update("*"))

        self.Equal = Button(master, text="Enter", command=lambda: self.evaulate())
        self.Clear = Button(master, text="Clear", command=lambda: self.total_label_text.set("0"))
        #self.total.grid(row=0, columnspan=3, sticky=W+E)
       
        self.Zero.grid(row=4, column=1, sticky=W+E)
        self.One.grid(row=3, sticky=W+E)
        self.Two.grid(row=3, column=1, sticky=W+E)
        self.Three.grid(row=3, column=2, sticky=W+E)
        self.Four.grid(row=2, column=0, sticky=W+E)
        self.Five.grid(row=2, column=1, sticky=W+E)
        self.Six.grid(row=2, column=2, sticky=W+E)
        self.Seven.grid(row=1, column=0, sticky=W+E)
        self.Eight.grid(row=1, column=1, sticky=W+E)
        self.Nine.grid(row=1, column=2, sticky=W+E)

        self.Mult.grid(row=0, column=4, sticky=N+S)
        self.Sub.grid(row=1, column=4, sticky=N+S)
        self.Plus.grid(row=2, column=4, sticky=N+S)
        self.Div.grid(row=3, column=4, sticky=N+S)

        self.Equal.grid(row=4, column=4, sticky=W+E)
        self.Clear.grid(row=5, column=4, sticky=W+E)

        #self.label = Label(master, text="")
        #self.label.grid(columnspan=3, sticky=SE)
          
    def evaulate(self):
        try:
            self.total_label_text.set(eval(self.total_label_text.get()))
        except (ZeroDivisionError, SyntaxError) as e:
            self.total_label_text.set("0")
        
        

    def update(self, method):
        if(self.total_label_text.get() is "0"):
            self.total_label_text.set(method)
        else:
            self.total_label_text.set(self.total_label_text.get()+method)

    def callback(self):
        print("Hey call")
    

root = Tk()
my_gui = MyFirstGui(root)
root.mainloop()

