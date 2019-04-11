### Description

The main aim of the project to create a number of subprocesses, based on the given input parameters by the user. 

Suppose you wish to create 6 new terminals of a particular size and of specific window size, you can do it using my application
The command line argument is: 

```
python align.py -d [help_mode] -w [width] -h [height] -r [no of rows] -c [no of columns] -a [application name]
```
   OR
```
python align.py --debug [help_mode] --width [width] --height [height] --rows [no of rows] --columns [no of columns] --application [application name]
```

1. All the arguments mentioned above are optional arguments. You may or may not pass the arguments

2. You can provide any combination of number of rows, columns and width and height(in pixels) and application named to be spawned. 

3. The result is n(=rows*columns) number of new applications are spawned up based on given input

### Installation Steps 
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
	python [script_file_name] -d [help_mode] -w [width] -h [height] -r [no of rows] -c [no of columns] -a [application name]
                           OR
	python [script_file_name] --debug [help_mode] --width [width] --height [height] --rows [no of rows] --columns [no of columns] --application [application name]
```

#### Test Cases
i) No parameters passed: 
    
``` python align.py -w -h ```
	
Takes the current system's screen resoultion, and then auto aligns 20 windows
![Image 1] (https://github.com/jaytorasakar8/Personal-Projects/blob/master/Application%20generation%20of%20specific%20window%20size%20in%20Linux%20using%20Python/Output%20Screenshots/1.PNG)

	
ii) Only Width and height(in pixels) passed

```python align.py -w 100 -h 100```
	
Will create 20 command prompt windows(default values) based on the given width = 100 and height = 100
![Image] (https://github.com/jaytorasakar8/Personal-Projects/blob/master/Application%20generation%20of%20specific%20window%20size%20in%20Linux%20using%20Python/Output%20Screenshots/2.PNG)

iii) Input passed is out of bounds

``` python align.py -w 100 -h 200```

If suppose screen resoulution is out of bounds for creating 20 windows based on given inputs, then give error and exit!
![Image] (https://github.com/jaytorasakar8/Personal-Projects/blob/master/Application%20generation%20of%20specific%20window%20size%20in%20Linux%20using%20Python/Output%20Screenshots/3.PNG)
    
iv) Get help regarding the application

```python align.py -d```
    
Help mode On. Provides details on how to use the program
![Image] (https://github.com/jaytorasakar8/Personal-Projects/blob/master/Application%20generation%20of%20specific%20window%20size%20in%20Linux%20using%20Python/Output%20Screenshots/4.PNG)

v) Only number of rows and columns passed

```python align.py -r 3 -c 4```

Creates a total of 12 new terminals, using the current device's screen resolution
![Image] (https://github.com/jaytorasakar8/Personal-Projects/blob/master/Application%20generation%20of%20specific%20window%20size%20in%20Linux%20using%20Python/Output%20Screenshots/5.PNG)

vi) Number of rows, columns, and height, width is passed

``` python align.py -w 100 -h 200 -r 3 -c 4```

Creates a total of 12(3 * 4) new terminals, of each of 100 * 200 pixels dimensions
![Image] (https://github.com/jaytorasakar8/Personal-Projects/blob/master/Application%20generation%20of%20specific%20window%20size%20in%20Linux%20using%20Python/Output%20Screenshots/6.PNG)

vii) When all parameters are passed

``` python align.py -w 100 -h 200 -r 1 -c 2 -a gedit```

Creates a total of 2 new Gedit process window of dimension = 100 * 200 px	
![Image] (https://github.com/jaytorasakar8/Personal-Projects/blob/master/Application%20generation%20of%20specific%20window%20size%20in%20Linux%20using%20Python/Output%20Screenshots/7.PNG)
