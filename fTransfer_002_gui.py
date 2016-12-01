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

import fTransfer_002_main
import fTransfer_002_func


def load_gui(self):
        

    #<Buttons>=============================================================================================================================
    self.srcBrowseBtn = tk.Button(self.master, text = 'Browse', width = 6, command=lambda: varS.set(fTransfer_002_func.browseSrcFile(self)))
    self.srcBrowseBtn.grid(row = 2, column = 0, columnspan = 4, padx = (10,0), pady = (0,0), sticky = 'nesw')

    self.dstBrowseBtn = tk.Button(self.master, text = 'Browse', width = 6, command=lambda: varD.set(fTransfer_002_func.browseDstFile(self)))
    self.dstBrowseBtn.grid(row = 2, column = 6, columnspan = 4, padx = (0,10), pady = (0,0), sticky = 'nesw')

    self.copyBtn = tk.Button(self.master, text = 'Copy', width = 6, command=lambda: fTransfer_002_func.dailyTransfer(self))
    self.copyBtn.grid(row = 5, column = 4, padx = (10,10), pady = (10,0), sticky = 'nesw')
    #</Buttons>==========================================================================


    #<Labels>===================================================
    self.labelSrc = tk.Label(self.master, text = 'Source Folder')
    self.labelSrc.grid(row = 0, column = 0, padx = (10,0), pady = (10,0), sticky = 'nw')

    self.labelDst = tk.Label(self.master, text = 'Destination Folder')
    self.labelDst.grid(row = 0, column = 6, padx = (0,10), pady = (10,0), sticky = 'nw')

    self.labelTimeTransfer = tk.Label(self.master, text = 'Time of Last File Transfer')
    self.labelTimeTransfer.grid(row = 3, column = 3, padx = (0,10), pady = (10,0), sticky = 'nw')
    #</Labels>==================================================================================


    #<Entries>===========================================================
    varS = StringVar()
    self.entrySrc = tk.Entry(self.master, textvariable = varS, width = 38)
    self.entrySrc.grid(row = 1, column = 0, columnspan = 4, padx=(10,0), pady=(0,0), sticky = 'nesw')

    varD = StringVar()
    self.entryDst = tk.Entry(self.master, textvariable = varD, width = 38)
    self.entryDst.grid(row = 1, column = 6, columnspan = 4, padx=(0,10), pady=(0,0), sticky = 'nesw')

    varT = StringVar()
    self.entryTimeTransfer = tk.Entry(self.master, textvariable = varT, width = 38)
    self.entryTimeTransfer.grid(row = 4, column = 3, columnspan = 4, padx=(0,10), pady=(0,0), sticky = 'nesw')    
    #</Entries>==============================================================================================


    fTransfer_002_func.create_db(self)
    fTransfer_002_func.newDayTransfer(self)



   
if __name__ == "__main__":
    pass
