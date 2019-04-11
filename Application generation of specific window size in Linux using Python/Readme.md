1. Install Python
```	
	sudo apt-get update
	
	sudo apt-get install python2.7
```
2. install both xdotool and wmctrl
```
	sudo apt-get install wmctrl
		
	sudo apt-get install xdotool
```
3. Create a new file named bin at root location in Linux
```
	cd ~
	mkdir bin
```
Then copy the file 'setwindow' in this bin folder

4. If you just created ~bin, run: 
```
	source ~/.profile
```

5. Then copy file named 'align.py' at a new folder where you wish to run the program. 
Assuming we are going to copy the file on Desktop
```
	cd ~/Desktop
	Copy file at this location. 
```

6. So our 'align.py' is at 'Desktop/' location and now we will change permissions inorder to run the file
```
	chmod u+x align.py
```

7. Now you can run the script by passing input parameters

8. How to run: 
```	
	python [script_file_name] -w [desired_width] -h [desired_height]
	                           OR
	python [script_file_name] --width [desired_width] --height [desired_height]
```

9. Inputs allowed:
	i) ``` python align.py -w -h ```
		Takes the current system's screen resoultion, and then auto aligns 20 windows
	ii) ```python align.py -w 100 -h 100```
	     Will create 20 command prompt windows based on the input parameters of width = 100 and height = 100
    iii)``` python align.py -w 100 -h 200```
    	  If suppose screen resoulution is out of bounds for creating 20 windows based on given inputs, then give error and exit!
    iv) ```python align.py -d```
    	   Help mode On. Provides details on how to use the function
