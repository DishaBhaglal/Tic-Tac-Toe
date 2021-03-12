from tkinter import*

root=Tk()

root.title("Tic Tac Toe")
root.resizable(width=False,height=False)
root.configure(bg='DodgerBlue2')

zeroPhoto = PhotoImage(file="zero.png")
crossPhoto = PhotoImage(file="cross.png")
whitePhoto = PhotoImage(file="white.png")
winPhoto = PhotoImage(file="winner.gif")
tiePhoto = PhotoImage(file="tie.png")

click = [True, True, True, True, True, True, True, True, True]

x=0
lst=["","","","","","","","",""]

b1 = Button(root,image = whitePhoto,command=lambda:play(1))
b1.grid(row=2,column=0)

b2 = Button(root,image = whitePhoto,command=lambda:play(2))
b2.grid(row=2,column=1)

b3 = Button(root,image = whitePhoto,command=lambda:play(3))
b3.grid(row=2,column=2)

b4 = Button(root,image = whitePhoto,command=lambda:play(4))
b4.grid(row=3,column=0)

b5 = Button(root,image = whitePhoto,command=lambda:play(5))
b5.grid(row=3,column=1)

b6 = Button(root,image = whitePhoto,command=lambda:play(6))
b6.grid(row=3,column=2)

b7 = Button(root,image = whitePhoto,command=lambda:play(7))
b7.grid(row=4,column=0)

b8 = Button(root,image = whitePhoto,command=lambda:play(8))
b8.grid(row=4,column=1)

b9 = Button(root,image = whitePhoto,command=lambda:play(9))
b9.grid(row=4,column=2)


main = Label(root, text="Tic.Tac.Toe ", font=("Verdana",16,"bold"), pady=15, bg='DodgerBlue2', fg='white')
main.grid(row=0,column=0,columnspan=3)

def play(num):
	global x,mylist,b1,b2,b3,b4,b5,b6,b7,b8,b9,tryButton,click
	
	if num==10:
		turnLabel = Label(root, text="O's turn", font=("Helvetica",14,"bold"), pady=5, bg='DodgerBlue2', fg='white')
		turnLabel.grid(row=1, column=0,columnspan=3)


	if (lst.count("o")+lst.count("x"))==9:
			tieLabel = Label(root, text="It's a tie", font=("Helvetica",14,"bold"), pady=5, bg='DodgerBlue2', fg='white')
			tieLabel.grid(row=5, column=0)
			tie_Label = Label(root, image=tiePhoto)
			tie_Label.grid(row=5, column=1, columnspan=2)
			no_use()	
	
	if num==1 and click[0]==True:
		if x%2==0:
			b1.configure(image = zeroPhoto)
			lst[0]="o"
			click[0]=False
			xturn()
		else:
			b1.configure(image = crossPhoto)
			lst[0]="x"
			click[0]=False
			oturn()
	elif num==2 and click[1]==True:
		if x%2==0:
			b2.configure(image = zeroPhoto)
			lst[1]="o"
			click[1]=False
			xturn()
		else:
			b2.configure(image = crossPhoto) 
			lst[1]="x"
			click[1]=False
			oturn()
	elif num==3 and click[2]==True:
		if x%2==0:
			b3.configure(image = zeroPhoto)
			lst[2]="o"
			click[2]=False
			xturn()
		else:
			b3.configure(image = crossPhoto)	
			lst[2]="x"
			click[2]=False
			oturn()
	elif num==4 and click[3]==True:
		if x%2==0:
			b4.configure(image = zeroPhoto)
			lst[3]="o"
			click[3]=False
			xturn()
		else:
			b4.configure(image = crossPhoto)
			lst[3]="x"
			click[3]=False
			oturn()	
	elif num==5 and click[4]==True:
		if x%2==0:
			b5.configure(image = zeroPhoto)
			lst[4]="o"
			click[4]=False
			xturn()
		else:
			b5.configure(image = crossPhoto)	
			lst[4]="x"
			click[4]=False
			oturn()
	elif num==6 and click[5]==True:
		if x%2==0:
			b6.configure(image = zeroPhoto)
			lst[5]="o"
			click[5]=False
			xturn()
		else:
			b6.configure(image = crossPhoto)	
			lst[5]="x"
			click[5]=False
			oturn()	
	elif num==7 and click[6]==True:
		if x%2==0:
			b7.configure(image = zeroPhoto)
			lst[6]="o"
			click[6]=False
			xturn()
		else:
			b7.configure(image = crossPhoto)
			lst[6]="x"
			click[6]=False
			oturn()
	elif num==8 and click[7]==True:
		if x%2==0:
			b8.configure(image = zeroPhoto)
			lst[7]="o"
			click[7]=False
			xturn()
		else:
			b8.configure(image = crossPhoto)
			lst[7]="x"
			click[7]=False
			oturn()
	elif num==9 and click[8]==True:
		if x%2==0:
			b9.configure(image = zeroPhoto)
			lst[8]="o"
			click[8]=False
			xturn()
		else:
			b9.configure(image = crossPhoto)
			lst[8]="x"
			click[8]=False
			oturn()

	if lst.count("o")>=3:
		if ((lst[0]=="o" and lst[1]=="o" and lst[2]=="o") or (lst[3]=="o" and lst[4]=="o" and lst[5]=="o") 
		or (lst[6]=="o" and lst[7]=="o" and lst[8]=="o") or (lst[0]=="o" and lst[3]=="o" and lst[6]=="o")
		or (lst[1]=="o" and lst[4]=="o" and lst[7]=="o") or (lst[2]=="o" and lst[5]=="o" and lst[8]=="o")
		or (lst[0]=="o" and lst[4]=="o" and lst[8]=="o") or (lst[2]=="o" and lst[4]=="o" and lst[6]=="o")):
			winLabel = Label(root, text="O won", font=("Helvetica",14,"bold"), pady=5, bg='DodgerBlue2', fg='white')
			winLabel.grid(row=5, column=0)
			winnerLabel = Label(root, image=winPhoto)
			winnerLabel.grid(row=5, column=1, columnspan=2)
			no_use()
			return
		elif ((lst[0]=="x" and lst[1]=="x" and lst[2]=="x") or (lst[3]=="x" and lst[4]=="x" and lst[5]=="x") 
		or (lst[6]=="x" and lst[7]=="x" and lst[8]=="x") or (lst[0]=="x" and lst[3]=="x" and lst[6]=="x")
		or (lst[1]=="x" and lst[4]=="x" and lst[7]=="x") or (lst[2]=="x" and lst[5]=="x" and lst[8]=="x")
		or (lst[0]=="x" and lst[4]=="x" and lst[8]=="x") or (lst[2]=="x" and lst[4]=="x" and lst[6]=="x")):
			winLabel = Label(root, text="X won", font=("Helvetica",14,"bold"), pady=5, bg='DodgerBlue2', fg='white' )
			winLabel.grid(row=5, column=0)
			winnerLabel = Label(root, image=winPhoto)
			winnerLabel.grid(row=5, column=1, columnspan=2)	
			no_use()
			return
	
	if num!=10:
		x=x+1			
			
def oturn():
	turnLabel = Label(root, text="O's turn", font=("Helvetica",14,"bold"), pady=5, bg='DodgerBlue2', fg='white')
	turnLabel.grid(row=1, column=0,columnspan=3)

def xturn():
	turnLabel = Label(root, text="X's turn", font=("Helvetica",14,"bold"), pady=5, bg='DodgerBlue2', fg='white')
	turnLabel.grid(row=1, column=0,columnspan=3)		

def no_use():
	b1.config(state="disabled")
	b2.config(state="disabled")
	b3.config(state="disabled")
	b4.config(state="disabled")
	b5.config(state="disabled")
	b6.config(state="disabled")
	b7.config(state="disabled")
	b8.config(state="disabled")
	b9.config(state="disabled")

play(10)

root.mainloop()
