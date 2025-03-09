from tkinter import *

class Application(Frame):
    def __init__ (self, master):
        super (Application, self).__init__(master)
        self.grid()
        self.bttn_clicks = 0
        self.create_widget()

    def create_widget(self):
        self.bttn = Button(self)
        self.bttn["text"] = "Total Clicks:\t 0"
        self.bttn["command"] = self.update_count
        self.bttn.grid()

    def update_count(self):
        self.bttn_clicks += 1
        self.bttn.configure(text = "Total Clicks:\t" + str(self.bttn_clicks))

root = Tk()
root.title("Click Counter")
root.geometry("600x300")

app = Application(root)
root.mainloop()