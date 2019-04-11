#!/usr/bin/python

import sys, getopt
import gtk, pygtk
import os


screen_width = 0
screen_height = 0
rows = 5
columns = 4
finalcmd = ''

def main(argv):
   input_width = 0
   input_height = 0  
   global finalcmd

   try:
      opts, args = getopt.getopt(argv,"dw:h:",["width=","height="])
   except getopt.GetoptError:
      print 'Error in getting the arguments'
      sys.exit(2)

   for opt, arg in opts:
      if opt == '-d':
         print 'Debug called! Help Mode On! Pass the parameters w and h to generate window of specific size!'  #Help mode ON
         
         sys.exit()
      elif opt in ("-w", "--width"):
         input_width = arg
      elif opt in ("-h", "--height"):
         input_height = arg

   print 'Input Width given is ', input_width
   print 'Input Height given is ',input_height

   
   window = gtk.Window() 
   screen = window.get_screen() #Get screen resolution based on the current system
   screen_width = screen.get_width()
   screen_height = screen.get_height()
   print "Screen width = " + str(screen.get_width()) + ", Screen height = " + str(screen.get_height())


   if input_width == '-h':
	      print 'Input not provided. Taking default values based on screen resolution'
        input_width = int(screen_width/4)
        input_height = int(screen_height/5)
	

   input_width = int(input_width)
   input_height = int(input_height)
   

   if (input_width is None) or  (input_height is None):
	     print 'Input not provided. Taking default values based on screen resolution'
 	     input_width = screen_width/4
	     input_height = screen_height/5


   if ((input_width * 4) > screen_width) or ((input_height * 5) > screen_height):
	     print 'Height or Width out of bounds. Please specify parameters correctly based on the resolution of your device'
	     print 'Current device has maximum width resolution = ', screen_width
	     print 'Current device has maximum height resolution = ', screen_height
	     print 'If you wish to use current device screen resolution, please do not pass any input values in the command line  arguments'
	     sys.exit(2)
    
   startx = 0
   starty = 0
   finalx = 0
   finaly = 0

   for i in range(5):
       for j in range(4):
           finalx = startx + input_width 
	         finaly = starty + input_height
	         generate(startx,starty)
           startx = finalx
       
       startx = 0
       starty = starty + input_height
   finalcmd =  finalcmd[0:len(finalcmd)-3]
   
   print finalcmd
   os.system(finalcmd)


def generate(startx,starty):
    global finalcmd
    newstr = ""
    newstr = "setwindow gnome-terminal " +str(startx)+ " " + str(starty) + " " + str(25) + " " + str(20)
    finalcmd = finalcmd + newstr + str(" && ")
  # os.system(s)


if __name__ == "__main__":
   main(sys.argv[1:])







