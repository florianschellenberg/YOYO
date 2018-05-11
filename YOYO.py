# simple GUI
try:
    # for Python2
    from Tkinter import *   ## notice capitalized T in Tkinter 
except ImportError:
    # for Python3
    import tkinter
    from tkinter import *   ## notice lowercase 't' in tkinter here
    from tkinter import messagebox
# grid of 6x6



class Application(Frame):
    def __init__(self, master):
        Frame.__init__(self, master, relief=SUNKEN, bd=2)
        self.grid()
        self.create_Menue()
        self.create_playerButton()
        self.update_InfoField()
        self.title = Label(self, text="This is my Title", font=(18))
        self.title.grid(row = 0, column = 0, columnspan =4, sticky = N)
 
    def create_Menue(self):
        self.menubar = Menu(self)

        menu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="File", menu=menu)
        menu.add_command(label="New")

        menu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Edit", menu=menu)
        menu.add_command(label="Cut")
        menu.add_command(label="Copy")
        menu.add_command(label="Paste")
        try:
            self.master.config(menu=self.menubar)
        except AttributeError:
            # master is a toplevel window (Python 1.4/Tkinter 1.63)
            self.master.tk.call(master, "config", "-menu", self.menubar)            

    def create_playerButton(self):
        numPlayers = 4
        Playerbuttons = []
        count = 0
        for x in range(1,numPlayers+1):
            Playerbuttons.append(Button(self, text = ("Player "+str(x)),
                        command=lambda num=count: self.update_unreached(num),
                        activebackground="grey"))
#            self.Plybut.grid(row = x, column =2, sticky =W)
            Playerbuttons[count].grid(row = x, column =2, sticky =W)
            count += 1
        self.Playerbuttons=Playerbuttons
  
    def update_InfoField(self):
        self.textfield = Text(self)
        self.textfield.grid(row = 1, column = 0, columnspan =2, rowspan = 4, sticky = W)
        for x in range(0, 3):
             self.textfield.insert(0.0,  "We're on time %d\n" % (x))

    def update_unreached(self, num):
        # Hier wird das update durchgeführt, falls ein Spieler das Ziel nicht pünklich erreicht (Gelbe und Rote "Karte")
#        self.Plybut1["bg"] = 'yellow'
#        messagebox.showinfo("Information","We're in the update_unreached function")
        if self.Playerbuttons[num].config('bg') == 'red':
#            self.Playerbuttons[num].config(relief='raised')
            self.Playerbuttons[num].config(bg='grey')    
        elif self.Playerbuttons[num].config('bg') == 'yellow':
            self.Playerbuttons[num].config(bg='red')    
        else:
            self.Playerbuttons[num].config(bg='yellow')    

root = tkinter.Tk()

root.title("YOYO Endurance Test")
#root.geometry("600x600")
app = Application(root)

root.mainloop()
