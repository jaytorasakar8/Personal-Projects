#!/usr/bin/python

import sys, getopt
import gtk, pygtk
import os
import commands

screen_width = 0
screen_height = 0
partition_x_percent = 25  #default when columns = 4
partition_y_percent = 20  #default when rows = 5
finalcmd = ''
application = ''


def main(argv):
   input_width = 0
   input_height = 0
   input_rows = 0
   input_columns = 0
   global partition_x_percent
   global partition_y_percent 
   global finalcmd
   global application

   try:
      opts, args = getopt.getopt(argv,"dr:c:w:h:a:",["rows=", "columns=", "width=","height=", "application="])
      
   except getopt.GetoptError:
      print "args", argv
      print 'Error in getting the arguments. Please pass the correct arguments'
      sys.exit(2)

   for opt, arg in opts:
      if opt == '-d':
         print 'Debug called. Help mode ON'
         print 'Pass the parameters w and h inorder to generate window size of specified resolution'
         print 'python align.py -r [rows] -c [columns] -w [width] -h [height] -a [application name]'
         print 'OR'
         print 'python align.py --rows [rows] --columns [columns] --width [width] --height [height] --application [application]'
         sys.exit()

      elif opt in ("-r", "--rows"):
         input_rows = arg
      elif opt in ("-c", "--columns"):
         input_columns = arg	
      elif opt in ("-w", "--width"):
         input_width = arg
      elif opt in ("-h", "--height"):
         input_height = arg
      elif opt in ("-a", "--application"):
         application = arg         


   print 'Rows given is ', input_rows
   print 'Columns given is ',input_columns
   print 'Width given is ', input_width
   print 'Height given is ',input_height
   print 'Application is', application
   
   window = gtk.Window()
   screen = window.get_screen()
   screen_width = screen.get_width()
   screen_height = screen.get_height()
   print "Screen Width = " + str(screen.get_width()) + ", Screen Height = " + str(screen.get_height())

   #Case if no input parameters are given. E.g: python align.py
   if input_rows == 0 and input_columns == 0 and input_width == 0 and input_height == 0 and application == '':
      print 'No Input parameters provided. Taking default values!'
      print 'Creating 20 new terminals of 5 rows and 4 columns using current screen resolution'
      input_rows = int(5)
      input_columns = int(4)
      input_width = screen_width/4
      input_height = screen_height/5
      application = 'gnome-terminal'

   #Incase rows have not been specified. Eg: python align.py -r -c 
   if input_rows == '-c':
      print 'Input Rows not provided. Taking default values of 5 rows and 4 columns'
      input_rows = int(5)
      input_columns = int(4)
   
   if (input_rows is None or input_rows == 0):
      input_rows = int(5)
   if (input_columns is None or input_columns == 0):
      input_columns = int(4)
 
   #It could be a string or an integer, so converting it to int	
   input_rows = int(input_rows)
   input_columns = int(input_columns)
   
 
   if (input_rows <= 0) or (input_columns <=0):
       print 'Please specify correct input number of rows or columns'
       sys.exit(2)

   #Incase width and height is not specified Eg: python align.py -r -h
   if input_width == '-h':
       print 'Input not provided. Taking default values based on screen resolution'
       input_width = int(screen_width/4)
       input_height = int(screen_height/5)
	
   input_width = int(input_width)
   input_height = int(input_height)
   
   #input width or height is not provided, so taking default values
   if (input_width is None) or  (input_width == 0):
	  print 'Input width not provided. Taking default values based on screen resolution'
 	  input_width = screen_width/input_columns

   if (input_height is None) or (input_height == 0):
	  print 'Input height not provided. Taking defalut value based on screen resolution'
	  input_height = screen_height/input_rows

   #If application hasn't been given, so by default creating a terminal
   if application == '':
	  application = 'gnome-terminal'


   #Check if the given screen resolution is feasible or not
   if ((input_width * input_columns) > screen_width) or ((input_height * input_rows) > screen_height):
	  print 'Height or Width out of bounds. Please specify parameters correctly based on the resolution of your device'
	  print 'Current device has maximum width resolution = ', screen_width
	  print 'Current device has maximum height resolution = ', screen_height
	  print 'If you wish to use current device screen resolution, please do not pass any input values in the command line  arguments'
	  sys.exit(2)

   #Our setwindow script takes the inputs interms of % of the window size
   partition_x_percent = 100/input_columns
   partition_y_percent = 100/input_rows

   print 'Rows given is ', input_rows
   print 'Columns given is ',input_columns
   print 'Width given is ', input_width
   print 'Height given is ',input_height
   print 'Partition x: ', partition_x_percent 
   print 'Partition y: ', partition_y_percent    

   startx = 0
   starty = 0
   finalx = 0
   finaly = 0

   for i in range(input_rows):
       for j in range(input_columns):
           finalx = startx + input_width
           finaly = starty + input_height
           generate(startx,starty)
           startx = finalx
           #finalx = startx + ((partition_x_percent * screen_width)/100)
           #finaly = starty + ((partition_y_percent * screen_height)/100)

       startx = 0
       starty = starty + input_height
       #starty = starty + ((partition_y_percent * screen_height)/100)
   finalcmd =  finalcmd[0:len(finalcmd)-3]
   print finalcmd
   
   try:
       os.system(finalcmd)
   except:
       print "Something went wrong with the given input application name. Please provide correct parameters!"
       sys.exit(2)	
	


def generate(startx,starty):
    global finalcmd
    global partition_x_percent
    global partition_y_percent
    global application 

    newstr = ""
    newstr = "setwindow" + " " + application + " " +str(startx)+ " " + str(starty) + " " + str(partition_x_percent) + " " + str(partition_y_percent)
    finalcmd = finalcmd + newstr + str(" && ")
 


if __name__ == "__main__":
   main(sys.argv[1:])







