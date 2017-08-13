# 15_comets
A simple python3 program to retrieve comet information from the internet; and display the 15 brightest comets currently in the night sky

"""
----------------------------------------------------------------------
Name:        Comet_table.py
Purpose:     To Download current data on comets from internet,
and display current Comet Information for the 15 brightest comets

Author: John Duchek, john.duchek@asemonline.org

Created:     October 27, 2014
Last Updated:  August 13, 2017
 
 Copyright:   (c) 2014-6 John Duchek
 Outline:
 1. goes on internet to minor planet center and downloads current comet data
 (http://www.minorplanetcenter.net/iau/Ephemerides/Comets/Soft03Cmt.txt)
 2. sorts data by magnitude
 3.  Displays data in tabular form based on user location and time. 
 
 Note: before using program, user needs to put in his location data and insure python3 
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
