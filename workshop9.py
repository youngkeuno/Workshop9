from graphics import*
from time import*
from random import*

new_list=[]
states=open("states.csv", "r")
for line in states:
	new_line=line.split(",")
	x1=new_line[0]
	x2=new_line[1]
	x3=int(new_line[2])
	x4=int(new_line[3])
	y=[x1,x2,x3,x4]
	new_list.append(y)

y=len(new_list)-1

#This is going to be a function that generates random states from our list of states. It then gets the population of each state and represents them as circles in a window where the area of the window is the total population of the country. Each state is given a circle of a certain color. The program will tell you what color is what state. Obviously the larger the population, the larger the circles will be, and the smaller the populations, the smaller the circles will be. 

def random_state_population_graphic():
	r1=1
	r2=2
	r3=3
	r4=3
	while r1==r2 or r1==r3 or r1==r4 or r2==r3 or r2==r4 or r3==r4:
		r1=randint(0,y)
		r2=randint(0,y)
		r3=randint(0,y)
		r4=randint(0,y)
	y1=new_list[r1][0]
	y2=new_list[r2][0]
	y3=new_list[r3][0]
	y4=new_list[r4][0]
	print("our first state is " + y1 +" which will be green in our graphic")
	print("our second state is " + y2+" which will be blue in our graphic")
	print("our third state is " + y3+" which will be red in our graphic")
	print("our fourth state is " + y4+" which will be purple in our graphic")
	win = GraphWin("My Program", 1000, 1000)
	total_pop=0
	for x in new_list:
		total_pop=total_pop+x[3]
	t=total_pop
	p1=new_list[r1][3]
	p2=new_list[r2][3]
	p3=new_list[r3][3]
	p4=new_list[r4][3]
	x1=p1/t
	x2=p2/t
	x3=p3/t
	x4=p4/t
	a1=1000000*x1
	a2=1000000*x2
	a3=1000000*x3
	a4=1000000*x4
	pi=3.14159265358979323846264338327950288419716939937510582097494459230781640628
	rd1=(a1/pi)**(.5)
	rd2=(a2/pi)**(.5)
	rd3=(a3/pi)**(.5)
	rd4=(a4/pi)**(.5)
	circle1=Circle(Point(250,250), rd1)
	circle2=Circle(Point(250,750), rd2)
	circle3=Circle(Point(750,250), rd3)
	circle4=Circle(Point(750,750), rd4)
	circle1.setFill("green")
	circle2.setFill("blue")
	circle3.setFill("red")
	circle4.setFill("purple")
	circle1.draw(win)
	circle2.draw(win)
	circle3.draw(win)
	circle4.draw(win)
	
random_state_population_graphic()

#This function does the same thing as the last, except now we get to choose the states. The states must be spelled properly for it to work. They're all capitalized, and spaces must be included for state names that have two parts like "New York". 

def states(s1,s2,s3,s4):
	for x in new_list:
		if x[0]==s1:
			r1=x
		else:
			y=0
	for x in new_list:
		if x[0]==s2:
			r2=x
		else:
			y=0
	for x in new_list:
		if x[0]==s3:
			r3=x
		else:
			y=0
	for x in new_list:
		if x[0]==s4:
			r4=x
		else:
			y=0
	y1=r1[0]
	y2=r2[0]
	y3=r3[0]
	y4=r4[0]
	print("our first state is " + y1 +" which will be green in our graphic")
	print("our second state is " + y2+" which will be blue in our graphic")
	print("our third state is " + y3+" which will be red in our graphic")
	print("our fourth state is " + y4+" which will be purple in our graphic")
	win = GraphWin("My Program", 1000, 1000)
	total_pop=0
	for x in new_list:
		total_pop=total_pop+x[3]
	t=total_pop
	p1=r1[3]
	p2=r2[3]
	p3=r3[3]
	p4=r4[3]
	x1=p1/t
	x2=p2/t
	x3=p3/t
	x4=p4/t
	a1=1000000*x1
	a2=1000000*x2
	a3=1000000*x3
	a4=1000000*x4
	pi=3.14159265358979323846264338327950288419716939937510582097494459230781640628
	rd1=(a1/pi)**(.5)
	rd2=(a2/pi)**(.5)
	rd3=(a3/pi)**(.5)
	rd4=(a4/pi)**(.5)
	circle1=Circle(Point(250,250), rd1)
	circle2=Circle(Point(250,750), rd2)
	circle3=Circle(Point(750,250), rd3)
	circle4=Circle(Point(750,750), rd4)
	circle1.setFill("green")
	circle2.setFill("blue")
	circle3.setFill("red")
	circle4.setFill("purple")
	circle1.draw(win)
	circle2.draw(win)
	circle3.draw(win)
	circle4.draw(win)

states("California","New York","Texas","Florida")

input("press a key to continue")
