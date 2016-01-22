
### python2.7 print something to file
	f = open('filename', 'a+')
	print >> f, 'something'
	f.flush() #flush memory to disk
	f.closed #check file closed or not
	f.close() #close file, release memory and the
	
### python open
if file is not exist, create a new file, same as without "+"， open file default mode is read.

	* 	f=open('filename', 'w')
	* 	f=open('filename', 'w+')
	* 	f=open('filename', 'a')
	* 	f=open('filename', 'a+')
	* 	f=open('filename')
	* 	f=open('filename', 'r')
	
if filename is not exist, will raise exception, so we usally: 

	with open('filename') as f:do something 
	to handle exception

we can also add multi mode, like behind:

	f=open('filename', 'a+r+w')
	if 'a' and 'w' all use, 'a' will ingore 'w'
	
### python read
	* f=open('filename')
	* f.read() # read all
	* f.readline() # read line by line
	* f.readlines() #get a list
	
	* f=open('filename', 'rb')
	* f.read(10) #read 10 byte per time


