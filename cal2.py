
from tkinter import *

cal = Tk()
cal.title("Cosmo Calculator")
cal.resizable(0,0)
operator=""
inputvar= StringVar()

def click(numbers):
	global operator
	operator=operator+str(numbers)
	inputvar.set(operator)	

def clearinputfield():
	global operator
	operator=""
	inputvar.set("")	

def calculate():
	global operator
	sumup=str(eval(operator))
	inputvar.set(sumup)
	operator=""
		
def button(no,r,c): Button(cal,padx=25,bd=3,fg="black",font=('arial',20,'bold'),text=no,command=lambda:click(no),bg="#2e3436",foreground="white").grid(row=r,column=c,pady=5)		
	
def clearandequal(no,r,c):
	if no == "C": Button(cal,padx=25,bd=3,fg="black",font=('Arial',20,'bold'),text=no,command=clearinputfield,bg="#2e3436" ,foreground="#6ada34").grid(row=r,column=c)
	else:Button(cal,padx=25,bd=3,fg="black",font=('Arial',20,'bold'),text=no,command=calculate,bg="#2e3436",foreground="#6ada34").grid(row=r,column=c)

inputDisplay = Entry(cal,font=('ARIAL',20,'bold'),textvariable=inputvar,bd=5,insertwidth=4,bg="#2e3436",justify='right',foreground="white", disabledbackground='#2e3436',state='disabled').grid(columnspan=4, padx=10, pady=10,ipady=15)

btn7=button(7,1,0)
btn8=button(8,1,1)
btn9=button(9,1,2)
add=button("+",1,3)

btn6=button(6,2,0)
btn5=button(5,2,1)
btn4=button(4,2,2)
sub=button("-",2,3)

btn1=button(1,3,0)
btn2=button(2,3,1)
btn3=button(3,3,2)
mul=button("*",3,3)

clr=clearandequal("C",4,0)
zero=button(0,4,1)
eql=clearandequal("=",4,2)
div=button("/",4,3)

cal.mainloop()

