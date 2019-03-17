
from tkinter import *
   
expression = "" 
  
  

def press(num): 
   
    global expression 
  
   
    expression = expression + str(num) 
  
   
    equation.set(expression) 
  
  

def equalpress(): 
    
    try: 
  
        global expression 
  
        total = str(eval(expression)) 
  
        equation.set(total) 
  
       
        expression = "" 
  
    except: 
  
        equation.set(" error ") 
        expression = "" 
  
  

def clear(): 
    global expression 
    expression = "" 
    equation.set("") 
  
  

if __name__ == "__main__": 

    
    gui = Tk() 
  
   
    gui.configure(background="black") 
  
    # set the title of GUI window 
    gui.title("Amit's Calculator") 
  
    equation = StringVar() 
  
   
    expression_field = Entry(gui, textvariable=equation) 
  
   
    expression_field.grid(columnspan=10,ipadx=245,ipady=20) 
  
    equation.set('enter your expression') 
  
    button1 = Button(gui, text=' 1 ',font=("monospace",15,"bold"), fg='green', bg='black',command=lambda: press(1), height=5, width=17) 
    button1.grid(row=2, column=0) 
    
    button2 = Button(gui, text=' 2 ', font=("monospace",15,"bold"),fg='green', bg='black',command=lambda: press(2), height=5, width=17) 
    button2.grid(row=2, column=1) 
  
    button3 = Button(gui, text=' 3 ', font=("monospace",15,"bold"),fg='green', bg='black', command=lambda: press(3), height=5, width=17) 
    button3.grid(row=2, column=2) 
  
    button4 = Button(gui, text=' 4 ',font=("monospace",15,"bold"), fg='green', bg='black', command=lambda: press(4), height=5, width=17) 
    button4.grid(row=3, column=0) 
  
    button5 = Button(gui, text=' 5 ',font=("monospace",15,"bold"), fg='green', bg='black', command=lambda: press(5), height=5, width=17) 
    button5.grid(row=3, column=1) 
  
    button6 = Button(gui, text=' 6 ',font=("monospace",15,"bold"), fg='green', bg='black',command=lambda: press(6), height=5, width=17) 
    button6.grid(row=3, column=2) 
  
    button7 = Button(gui, text=' 7 ',font=("monospace",15,"bold"), fg='green', bg='black',command=lambda: press(7), height=5, width=17) 
    button7.grid(row=4, column=0) 
  
    button8 = Button(gui, text=' 8 ',font=("monospace",15,"bold"), fg='green', bg='black',command=lambda: press(8), height=5, width=17) 
    button8.grid(row=4, column=1) 
  
    button9 = Button(gui, text=' 9 ', font=("monospace",15,"bold"),fg='green', bg='black', 
                     command=lambda: press(9), height=5, width=17) 
    button9.grid(row=4, column=2) 
  
    button0 = Button(gui, text=' 0 ',font=("monospace",15,"bold"), fg='green', bg='black', 
                     command=lambda: press(0), height=5, width=17) 
    button0.grid(row=5, column=0) 
  
    plus = Button(gui, text=' + ',font=("monospace",15,"bold"), fg='green', bg='black', 
                  command=lambda: press("+"), height=5, width=17) 
    plus.grid(row=2, column=3) 
  
    minus = Button(gui, text=' - ', font=("monospace",15,"bold"),fg='green', bg='black', 
                   command=lambda: press("-"), height=5, width=17) 
    minus.grid(row=3, column=3) 
  
    multiply = Button(gui, text=' * ', font=("monospace",15,"bold"),fg='green', bg='black', 
                      command=lambda: press("*"), height=5, width=17) 
    multiply.grid(row=4, column=3) 
  
    divide = Button(gui, text=' / ', font=("monospace",15,"bold"),fg='green', bg='black', 
                    command=lambda: press("/"), height=5, width=17) 
    divide.grid(row=5, column=3) 
  
    equal = Button(gui, text=' = ', font=("monospace",15,"bold"),fg='green', bg='black', 
                   command=equalpress, height=5, width=17) 
    equal.grid(row=5, column=2) 
  
    clear = Button(gui, text='Clear',font=("monospace",15,"bold"), fg='green', bg='black', 
                   command=clear, height=5, width=17) 
    clear.grid(row=5, column='1') 
    
    gui.mainloop() 
