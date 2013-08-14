from Tkinter import *
import curses
import time

scrn = curses.initscr()
curses.noecho()
curses.cbreak()
scrn.keypad(1)
scrn.nodelay(1)

maplist = []

def clicker(event):
	xevent = event.x
	yevent = event.y
	for item in maplist:
		xitem = item[0]
		yitem = item[1]
		if xitem <= xevent < xitem + 20 and yitem <= yevent < yitem + 20:
			listposit = maplist.index(item)
			maplist.remove(item)
			squpdate = [xitem,yitem,1]
			maplist.insert(listposit,squpdate)

master = Tk()
master.attributes('-topmost', 1)
cvs = Canvas(master,width = 700,height = 700)
cvs.pack()
cvs.bind('<Button-1>',clicker)

xcounter = 0
while xcounter < 35:
	ycounter = 0
	while ycounter < 35:
		bigx = xcounter * 20
		bigy = ycounter * 20
		cvs.create_rectangle(bigx,bigy,bigx + 20,bigy +20,tag = 'block')
		mapitem = [bigx,bigy,0]
		maplist.append(mapitem)
		ycounter = ycounter + 1
	xcounter = xcounter + 1
done = False
while done == False:
	cvs.update()
	c = scrn.getch()
	if c== 32:
		done = True
	for thing in maplist:
		xthing = thing[0]
		ything = thing[1]
		life = thing[2]
		if life == 1:
			cvs.create_rectangle(xthing,ything,xthing+20,ything+20,fill = 'black')
		if life == 0:
			cvs.create_rectangle(xthing,ything,xthing+20,ything+20,fill = 'white')

while True:
	cvs.update()
	cvs.delete(ALL)
	neighborlist = []

	for thing in maplist:
		thingpoint = maplist.index(thing)
		neighbors = 0
		xposit = thing[0]
		yposit = thing[1]
		thinglife = thing[2]
		for item in maplist:
			xcoords = item[0]
			ycoords = item[1]
			itemlife = item[2]
			xtotal = xposit - xcoords
			ytotal = yposit - ycoords
			if -20 <= xtotal <= 20 and -20 <= ytotal <= 20 and itemlife == 1:
				neighbors = neighbors + 1
			elif xtotal < -21 and ytotal < -21:
				break
		neighborlist.append(neighbors)

	for thing in maplist:
		xthing = thing[0]
		ything = thing[1]
		life = thing[2]
		listposit = maplist.index(thing)
		neighbors = neighborlist[listposit]
		if life == 0 and neighbors == 3:
			living = 1
		elif life == 1:
			neighbors = neighbors - 1
			if neighbors >=4 or neighbors <=1:
				living = 0
			else:
				continue
		else:
			continue
		maplist.remove(thing)
		squpdate = [xthing,ything,living]
		maplist.insert(listposit,squpdate)

	for thing in maplist:
		xthing = thing[0]
		ything = thing[1]
		life = thing[2]
		if life == 1:
			cvs.create_rectangle(xthing,ything,xthing+20,ything+20,fill = 'black')
		if life == 0:
			cvs.create_rectangle(xthing,ything,xthing+20,ything+20,fill = 'white')


master.mainloop()
