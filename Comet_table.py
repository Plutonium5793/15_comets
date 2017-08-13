#!/usr/bin/python3


"""
----------------------------------------------------------------------
Name:        Comet_table.py
Purpose:     To Download current data on comets from internet,
and display current Comet Information for the 15 brightest comets

Author: John Duchek, john.duchek@asemonline.org

Created:     October 27, 2014
Last Updated:  August 13, 2017
 
 
 Outline:
 1. goes on internet to minor planet center and downloads current comet data
 (http://www.minorplanetcenter.net/iau/Ephemerides/Comets/Soft03Cmt.txt)
 2. sorts data by magnitude
 3.  Displays data in tabular form based on user location and time. 
 
 Note: before using program, user needs to put in his location data and insure python 
 and all necessary modules are loaded.  program runs in python3 

 Version 0.30-convert gui to tkinter
 Version 0.20 
Program downloads current comet data from minor planet center,
Sorts file by magnitude of the objects,
Displays the 15 brightest comets currently in the sky.  
It requires pyephem for its calculations.
Created on Thu Oct  2 08:38:59 2014
# -*- coding: utf-8 -*-


"""
#!/usr/bin/python3
import tkinter as tk
from tkinter import ttk
from ephem import *
from string import *
import urllib.request

win=tk.Tk()
win.resizable(False, False)

urllib.request.urlretrieve('http://www.minorplanetcenter.net/iau/Ephemerides/Comets/Soft03Cmt.txt', 'Soft03Cmt.txt')


john=Observer()
# --------------   Choose Site    ------------------------
#john_timezone=-5 #Central Daylight Time
#site="Karamar, MO"
#john.long,john.lat,john.elev='-90.379025','38.47362',147.9  #longitude, latitude, elevation in meters
#-------------------- Site 2 ------------------------------
john_timezone=-6  #mountain Daylight time
site="Carrizozo, NM"
john.long,john.lat,john.elev='-105.77175','33.60763',1849
# --------------------------------------------------------
john.temp=15 #deg C
john.pressure=1010 #mB
john.date=now()
sun,moon=Sun(),Moon()

global item,name,mag,ra,dec,Constellation,altitude  

def partition(theList, start, end,name,ra,dec,Constellation,altitude):

        pivot = theList[end]    
        pivot1=name[end]
        pivot2=ra[end]
        pivot3=dec[end]
        pivot4=Constellation[end]
        pivot5=altitude[end]

        bottom = start-1                         # begin "outside"                           
        top = end                                # place other side for partitioning                            

        done = 0
        while not done:                             # begin                    
            while not done:                        
                bottom = bottom + 1                   

                if bottom == top:                   # has we reached the end?       
                    done = 1                        # if so, exit!    
                    break
                if theList[bottom] > pivot:         # move values '>' "above"
                    theList[top] = theList[bottom]
                    name[top]=name[bottom]
                    ra[top]=ra[bottom]
                    dec[top]=dec[bottom]
                    Constellation[top]=Constellation[bottom]
                    altitude[top]=altitude[bottom]
                    
                    break
                
            while not done:                        
                top = top-1                        
                
                if top == bottom:                   # if end is reached, exit!        
                    done = 1                       
                    break
                if theList[top] < pivot:            # do the opposite of the above      
                    theList[bottom] = theList[top]  # '<' are moved "below" 
                    name[bottom]=name[top]
                    ra[bottom]=ra[top]
                    dec[bottom]=dec[top]
                    Constellation[bottom]=Constellation[top]
                    altitude[bottom]=altitude[top]
                                    
                    break                          

        theList[top] = pivot 
        name[top]=pivot1
        ra[top]=pivot2
        dec[top]=pivot3
        Constellation[top]=pivot4
        altitude[top]=pivot5
        
        
        return top                              

def quicksort(theList, start, end,name,ra,dec,Constellation,altitude):
    if start < end:                             # verifies the list is not empty
        split = partition(theList, start, end,name,ra,dec,Constellation,altitude)      # partition the sublist
        quicksort(theList, start, split-1,name,ra,dec,Constellation,altitude)          # sort both halves.
        quicksort(theList, split+1, end,name,ra,dec,Constellation,altitude)            # recursion 
    else:
        return
    
f=open("Soft03Cmt.txt",'r')
        
name=[0]
mag=[0]
ra=[0]
dec=[0]
Constellation=[0]
altitude=[0]
while True:
    line=f.readline()
    if len(line)==0: #length 0 indicates EOF
        break
    if line[0:6]!='# From': #removes alternate lines

        comet=readdb(line)
        comet.compute(john)
        name.append(comet.name)
        mag.append(comet.mag)
        ra.append(comet.ra)
        dec.append(comet.dec)
        Constellation.append(constellation(comet)[1])
        altitude.append(comet.alt)
       # before sort by mag print name[-1], mag[-1]   

quicksort(mag,0,len(mag)-1,name,ra,dec,Constellation,altitude)
win.title("15 Brightest Comets of "+str(len(mag))+" at "+site)

data_frame=ttk.LabelFrame(win,text='15 Brightest Comets')        
data_frame.grid(column=6,row=16)        

ttk.Label(data_frame,text="Name").grid(column=0,row=0,sticky=tk.W,padx=5,pady=2)
ttk.Label(data_frame,text="Magnitude").grid(column=1,row=0,sticky=tk.W,padx=5,pady=2)
ttk.Label(data_frame,text="R. Ascension").grid(column=2,row=0,sticky=tk.W,padx=5,pady=2)
ttk.Label(data_frame,text="Declination").grid(column=3,row=0,padx=5,pady=5)
ttk.Label(data_frame,text="Constellation").grid(column=4,row=0,sticky=tk.W,padx=5,pady=2)
ttk.Label(data_frame,text="Altitude").grid(column=5,row=0,sticky=tk.W,padx=5,pady=5)

for item in range (1, 16):
    alt=str(altitude[item])
    alt_deg=alt.split(':')
    ttk.Label(data_frame,text= str(name[item])[0:35]).grid(column=0,row=item,sticky=tk.W,padx=5,pady=0)
    ttk.Label(data_frame,text= str(mag[item])[0:35]).grid(column=1,row=item,sticky=tk.W,padx=5,pady=0)
    ttk.Label(data_frame,text= str(ra[item])[0:35]).grid(column=2,row=item,sticky=tk.W,padx=5,pady=0)
    ttk.Label(data_frame,text= str(dec[item])[0:35]).grid(column=3,row=item,sticky=tk.W,padx=5,pady=0)
    ttk.Label(data_frame,text= str(Constellation[item])[0:35]).grid(column=4,row=item,sticky=tk.W,padx=5,pady=0)
    ttk.Label(data_frame,text= str(alt_deg[0])[0:35]).grid(column=5,row=item,sticky=tk.W,padx=5,pady=0)
    
    
 


win.mainloop()
#win = TableWindow()
#win.connect("delete-event", Gtk.main_quit)
#win.show_all()
#Gtk.main()
