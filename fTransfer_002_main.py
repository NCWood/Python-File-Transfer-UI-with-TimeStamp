#=========================================================#
# Python 3.5.2                                            #
#                                                         #
# Create UI that will allow user to choose folders/files  #
# and copy them to destination folder.                    #
#                                                         #
# Author: Nicholas Wood (nicholas.cameron.wood@gmail.com) #     
#                                                         #
#======================={nWc}=============================#


from tkinter import *
import tkinter as tk

import fTransfer_002_func
import fTransfer_002_gui



class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, *kwargs)

        self.master = master
        self.master.minsize(555,200)
        self.master.maxsize(555,200)

        fTransfer_002_func.centerWindow(self,555,200)
        self.master.title("Home Office File Transfer")

        self.master.protocol("WM_DELETE_WINDOW", lambda: fTransfer_002_func.askQuit(self))
        arg = self.master

        fTransfer_002_gui.load_gui(self)






if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
