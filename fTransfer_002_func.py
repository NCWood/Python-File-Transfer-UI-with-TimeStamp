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
import shutil
import os
from os import path
import datetime
from datetime import datetime, date, time, timedelta
import sqlite3

import fTransfer_002_main
import fTransfer_002_gui

# yesterday
aDayOld = datetime.now() - timedelta(hours = 24)


#============================
def centerWindow(self, w, h):                                                    
    # get screen width and height                                                 
    screen_width = self.master.winfo_screenwidth()                                
    screen_height = self.master.winfo_screenheight()                              
    # calculate x and y coords to center app                                      
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo


def askQuit(self):
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        self.master.destroy()
        os._exit(0)
#============================


        
#CreateDatabase====
def create_db(self):
    conn = sqlite3.connect('fileTransferTime.db')
    with conn:
        cur = conn.cursor()
        cur.execute("""CREATE TABLE if not exists tbl_transferTime( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_copyTime TEXT );""")
        conn.commit()
    conn.close()
#===============



#File Selection and Copy====================================================================
def browseSrcFile(self):
    self.fSrc = filedialog.askdirectory(initialdir="/",title='Please select a source folder')
    print ('Source File: ', self.fSrc)
    return self.fSrc
 
    

def browseDstFile(self):
    self.fDst = filedialog.askdirectory(initialdir="/",title='Please select a destination folder')
    print ('Destination File: ', self.fDst)
    return self.fDst



def dailyTransfer(self):
    for root, dirs, files in os.walk(self.fSrc):
        for txtfile in files:
            path = os.path.join(root, txtfile)
            st = os.stat(path)
            mtime = datetime.fromtimestamp(st.st_mtime)
            ctime = datetime.fromtimestamp(st.st_ctime)
            if mtime > aDayOld and txtfile.endswith('.txt'):
                shutil.copy(os.path.join(self.fSrc, txtfile), os.path.join(self.fDst, txtfile))
            elif ctime > aDayOld and txtfile.endswith('.txt'): 
                shutil.copy(os.path.join(self.fSrc, txtfile), os.path.join(self.fDst, txtfile))
        timeClicked = datetime.now()
        addToTable(self)
    print('Files successfully copied!')
    print(timeClicked)
#===========================================================================================


#DB insertions and retrievals===============================================================
def addToTable(self):
    timeClicked = datetime.now()
    conn = sqlite3.connect('fileTransferTime.db')
    with conn:
        cur = conn.cursor()
        cur.execute("""INSERT INTO tbl_transferTime (col_copyTime) VALUES (?)""", [timeClicked])
        self.entryTimeTransfer.insert(END, timeClicked)
        conn.commit()
    conn.close()


    
def newDayTransfer(self):
    self.entryTimeTransfer.delete(0,END)
    conn = sqlite3.connect('fileTransferTime.db')
    cursor = conn.cursor()
    cursor.execute("""SELECT col_copyTime FROM tbl_transferTime WHERE ID = (SELECT MAX(ID) FROM tbl_transferTime)""")
    lastTime = cursor.fetchone()
    print (lastTime)
    self.entryTimeTransfer.insert(0, str(lastTime))        
    conn.close()    
#==================================================

    




if __name__ == "__main__":
    pass
                
