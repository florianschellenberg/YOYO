# simple GUI
try:
    # for Python2
    from Tkinter import *   ## notice capitalized T in Tkinter 
except ImportError:
    # for Python3
    from tkinter import *   ## notice lowercase 't' in tkinter here

import time, winsound


class Application(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self. grid()
        self.create_widgets()
        self.button_clicks = 0
        
    def create_widgets(self):
        self.button1 = Button(self, text = "hello")
        self.button1["command"] = self.update_count
        self.button1.grid(row = 0, column =2, columnspan =2, sticky =W)

        self.button2 = Button(self)
        self.button2.grid(row = 1, column =1, sticky =W)
        self.button2.configure(text = "Play the Sound")
        self.button2["command"] = self.play_sound

        self.button3 = Button(self, text = "Play Sound with Pause")
        self.button3["command"] = self.play_sound_pause
        self.button3.grid(row = 1, column =2, columnspan =2, sticky =W)

        self.textfield = Text(self, wrap = WORD)
        self.textfield.grid(row = 16, column = 0, columnspan = 3, sticky = W)

    def update_count(self):
        self.button_clicks += 1
        self.button1["text"] = "Total Clicks: " + str(self.button_clicks)
        self.textfield.delete(0.0, END)
        self.textfield.insert(0.0, "Total Clicks: " + str(self.button_clicks))

    def play_sound(self):
        winsound.PlaySound('2.wav', winsound.SND_FILENAME)

    def play_sound_pause(self):
        print(time.time())
        Timer(2, sound(), ()).start()
       
    def sound(self):
        winsound.PlaySound('2.wav', winsound.SND_FILENAME)


root = Tk()

root.title("YOYO endurance test")
root.geometry("600x600")

app = Application(root)
# app.grid()

root.mainloop()
