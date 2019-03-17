import sys
from tkinter import *
def table():
	for x in range(1,11):
	  m=int(text_input.get())
	  textDisplay.insert(END,(x), '\t',"x","\t",(m),'\t','=','\t',(x*m))
	  textDisplay.insert(END,'\n\n')



multiply=Tk()
multiply.title("Multiplication Table")
multiply.resizable(0,0)
text_input = StringVar()
lable= Label(multiply, text="Multiplication Table", font=('monospace',25,'bold'),bg='black',fg='green').grid(row=0,column=0)
textinput = Entry(multiply, textvariable = text_input,bd=6, font=('monospace',25,'bold'),bg="light blue").grid(row=1,column=0)
textDisplay = Text(multiply, width=30,height=22,bg="black",bd=16,fg="green",font=("monospace",15,"bold"))
textDisplay.grid(row=2,column=0)
btntable= Button(multiply,padx=20,pady=20,bd=8,fg="red",bg="black", font=('arial',25,'italic'),text="multiply",command=table,width=10).grid(row=3,column=0)
multiply.mainloop()
