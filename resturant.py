from tkinter import*
import random
import tkinter.messagebox
from datetime import datetime
import time

def total():
	a1=int(food1.get())
        a2=int(food2.get())
	a3=int(food3.get())
	a4=int(food4.get())
	a5=int(food5.get())
	a6=int(food6.get())
	a7=int(food7.get())
	a8=int(food8.get())
	a9=int(food9.get())
	a10=int(food10.get())
	a11=int(food11.get())
	a12=int(food12.get())       
	x=(150*a1)+(50*a2)+(20*a3)+(70*a4)+(50*a5)+(30*a6)+(80*a7)+(40*a8)+(50*a9)+(40*a10)+(50*a11)+(30*a12)
	a=(2.5*x)/100
	b=x+a+a
	totalx.set(b)
	display.insert(END,'\t'+'      YOUR BILL'+'\n')
	display.insert(END,firstname.get()+middlename.get()+lastname.get()+'\n')
	display.insert(END,'Phone No. :-'+phoneno.get()+'\n')
	display.insert(END,'Email Id. :-'+email.get()+'\n')
	display.insert(END,'Order No. :-'+togo.get()+'\n')
	display.insert(END,'Date :-'+Date1.get()+'\n')
	display.insert(END,'Time :-'+Time1.get()+'\n')
	display.insert(END,'Pizza :-'+food1.get()+'\n')
	display.insert(END,'Burger :-'+food2.get()+'\n')
	display.insert(END,'Drink :-'+food3.get()+'\n')
	display.insert(END,'Pasta :-'+food4.get()+'\n')
	display.insert(END,'Wrap :-'+food5.get()+'\n')
	display.insert(END,'Fries :-'+food6.get()+'\n')
	display.insert(END,'Biryani :-'+food7.get()+'\n')
	display.insert(END,'Sandwich :-'+food8.get()+'\n')
	display.insert(END,'Noodels :-'+food9.get()+'\n')
	display.insert(END,'Milkshake :-'+food10.get()+'\n')
	display.insert(END,'Icecream :-'+food11.get()+'\n')
	display.insert(END,'Spring Roll :-'+food12.get()+'\n')
	display.insert(END,'\t'+'        Thankyou'+'\n')

root = Tk()
root.title("your bill")
root.geometry("1890x900+0+0")
root.config(background="black") 

firstname = StringVar()
middlename = StringVar()
lastname = StringVar()
phoneno = StringVar()
alterno = StringVar()
email = StringVar()
add1 = StringVar()
add2 = StringVar()
add3 = StringVar()
add4 = StringVar()
pin = StringVar()
country = StringVar()
id = StringVar()
payment = StringVar()


middlename.set(" ")
lastname.set(" ")
phoneno.set(" ")
alterno.set(" ")
email.set(" ")
add1.set(" ")
add2.set(" ")
add3.set(" ")
add4.set(" ")
pin.set(" ")
country.set(" ")
id.set(" ")
payment.set(" ")

togo = StringVar()
coupon = StringVar()

togo.set(random.randint(1569, 999999))
coupon.set(random.randint(1569565, 99999999999))


food1 = StringVar()
food2 = StringVar()
food3 = StringVar()
food4 = StringVar()
food5 = StringVar()
food6 = StringVar()
food7 = StringVar()
food8 = StringVar()
food9 = StringVar()
food10 = StringVar()
food11 = StringVar()
food12 = StringVar()
totalx = StringVar()


food1.set(0) 
food2.set(0) 
food3.set(0) 
food4.set(0) 
food5.set(0) 
food6.set(0) 
food7.set(0) 
food8.set(0) 
food9.set(0) 
food10.set(0) 
food11.set(0) 
food12.set(0) 


ab= Frame(root,bg="red",bd=20,relief=RIDGE)
ab.grid()
ab1=Frame(ab,bd=10,width=1890,height=100,padx=10,bg="black",relief=RIDGE)
ab1.grid(row=0, column=0, columnspan=4)
ab2=Frame(ab,bd=10,width=630,height=815,padx=10,bg="black",relief=RIDGE)
ab2.grid(row=1, column=0)
ab3=Frame(ab,bd=10,width=630,height=815,padx=10,bg="black",relief=RIDGE)
ab3.grid(row=1, column=1)
ab4=Frame(ab,bd=10,width=630,height=800,bg="black",relief=RIDGE)
ab4.grid(row=1, column=2)
ab5=Frame(ab4,bd=10,width=620,height=635,padx=10,bg="black",relief=RIDGE)
ab5.grid(row=0, column=0)
ab6=Frame(ab4,bd=10,width=620,height=190,padx=10,bg="black",relief=RIDGE)
ab6.grid(row=1, column=0)

Date1 = StringVar()
Time1 = StringVar()
Date1.set(time.strftime("%d/%m/%Y"))
Time1.set(time.strftime("%H:%M:%S"))

dt= Label(ab1,textvariable=Date1,font=('monospace',20,'bold'),width=30,pady=9,bd=5,bg="black",fg="green").grid(row=0, column=0)
dt1= Label(ab1,text="THE HACKER'S CAFE",font=('FontAwesome',45,'bold'),width=20,pady=9,bd=5,bg="black",fg="red").grid(row=0, column=1,columnspan=2)
dt2= Label(ab1,textvariable=Time1,font=('monospace',20,'bold'),width=30,pady=9,bd=5,bg="black",fg="green").grid(row=0, column=3)

total=Button(ab6,text="TOTAL",font=('FontAwesome',25,'bold'),command=total,width=20,height=2,pady=9,bd=5,bg="yellow",fg="red").grid(row=0, column=0)

display=Text(ab5,width=35,height=20,pady=7,bd=3,font=('monospace',20,'bold'))
display.grid(row=0,column=0)

info0=Label(ab2,font=('FontAwesome',35,'bold'),bg="black",fg="green",text="Customer Information").grid(row=0,column=0,columnspan=2)

info1=Label(ab2,font=('monospace',20,'bold'),text="first Name :- ",bg="black",fg="green").grid(row=1,column=0)
info_det1=Entry(ab2,textvariable=firstname,font=('FontAwesome',30,'bold'),width=10,bg="orange",fg="black")
info_det1.grid(row=1,column=1)

info2=Label(ab2,font=('monospace',20,'bold'),text="middle Name :- ",bg="black",fg="green").grid(row=2,column=0)
info_det2=Entry(ab2,textvariable=middlename,font=('FontAwesome',30,'bold'),width=10,bg="orange",fg="black")
info_det2.grid(row=2,column=1)

info3=Label(ab2,font=('monospace',20,'bold'),text="last Name :- ",bg="black",fg="green").grid(row=3,column=0)
info_det3=Entry(ab2,textvariable=lastname,font=('FontAwesome',30,'bold'),width=10,bg="orange",fg="black")
info_det3.grid(row=3,column=1)

info4=Label(ab2,font=('monospace',20,'bold'),text="Phone No. :- ",bg="black",fg="green").grid(row=4,column=0)
info_det4=Entry(ab2,textvariable=phoneno,font=('FontAwesome',30,'bold'),width=10,bg="orange",fg="black")
info_det4.grid(row=4,column=1)

info5=Label(ab2,font=('monospace',20,'bold'),text="Alternet No. :- ",bg="black",fg="green").grid(row=5,column=0)
info_det5=Entry(ab2,textvariable=alterno,font=('FontAwesome',30,'bold'),width=10,bg="orange",fg="black")
info_det5.grid(row=5,column=1)

info6=Label(ab2,font=('monospace',20,'bold'),text="Email id :- ",bg="black",fg="green").grid(row=6,column=0)
info_det6=Entry(ab2,textvariable=email,font=('FontAwesome',30,'bold'),width=10,bg="orange",fg="black")
info_det6.grid(row=6,column=1)

info7=Label(ab2,font=('monospace',20,'bold'),text="Address line 1 :- ",bg="black",fg="green").grid(row=7,column=0)
info_det7=Entry(ab2,textvariable=add1,font=('FontAwesome',30,'bold'),width=10,bg="orange",fg="black")
info_det7.grid(row=7,column=1)

info8=Label(ab2,font=('monospace',20,'bold'),text="Address line 2:- ",bg="black",fg="green").grid(row=8,column=0)
info_det8=Entry(ab2,textvariable=add2,font=('FontAwesome',30,'bold'),width=10,bg="orange",fg="black")
info_det8.grid(row=8,column=1)

info9=Label(ab2,font=('monospace',20,'bold'),text="Address line 3:- ",bg="black",fg="green").grid(row=9,column=0)
info_det9=Entry(ab2,textvariable=add3,font=('FontAwesome',30,'bold'),width=10,bg="orange",fg="black")
info_det9.grid(row=9,column=1)

info10=Label(ab2,font=('monospace',20,'bold'),text="Address line 4 :- ",bg="black",fg="green").grid(row=10,column=0)
info_det10=Entry(ab2,textvariable=add4,font=('FontAwesome',30,'bold'),width=10,bg="orange",fg="black")
info_det10.grid(row=10,column=1)

info11=Label(ab2,font=('monospace',20,'bold'),text="PIN :- ",bg="black",fg="green").grid(row=11,column=0)
info_det11=Entry(ab2,textvariable=pin,font=('FontAwesome',30,'bold'),width=10,bg="orange",fg="black")
info_det11.grid(row=11,column=1)

info12=Label(ab2,font=('monospace',20,'bold'),text="Country :- ",bg="black",fg="green").grid(row=12,column=0)
info_det12=Entry(ab2,textvariable=country,font=('FontAwesome',30,'bold'),width=10,bg="orange",fg="black")
info_det12.grid(row=12,column=1)

info13=Label(ab2,font=('monospace',20,'bold'),text="ID Proof :- ",bg="black",fg="green").grid(row=13,column=0)
info_det13=Entry(ab2,textvariable=id,font=('FontAwesome',30,'bold'),width=10,bg="orange",fg="black")
info_det13.grid(row=13,column=1)

info14=Label(ab2,font=('monospace',20,'bold'),text="Payment by :- ",bg="black",fg="green").grid(row=14,column=0)
info_det14=Entry(ab2,textvariable=payment,font=('FontAwesome',30,'bold'),width=10,bg="orange",fg="black")
info_det14.grid(row=14,column=1)

info15=Label(ab2,font=('monospace',20,'bold'),text="Order No. :- ",bg="black",fg="green").grid(row=15,column=0)
info_det15=Entry(ab2,textvariable=togo,font=('FontAwesome',30,'bold'),width=10,bg="orange",fg="black")
info_det15.grid(row=15,column=1)

info16=Label(ab2,font=('monospace',20,'bold'),text="coupon :- ",bg="black",fg="green").grid(row=16,column=0)
info_det16=Entry(ab2,textvariable=coupon,font=('FontAwesome',30,'bold'),width=10,bg="orange",fg="black")
info_det16.grid(row=16,column=1)

ord0=Label(ab3,font=('FontAwesome',45,'bold'),bg="black",fg="green",text="MENU").grid(row=0,column=0,columnspan=2)

ord1=Label(ab3,font=('monospace',20,'bold'),text="Pizza X 150 :- ",bg="black",fg="green").grid(row=1,column=0)
ord_det1=Entry(ab3,textvariable=food1,font=('FontAwesome',30,'bold'),width=10,bg="orange",fg="black")
ord_det1.grid(row=1,column=1)

ord2=Label(ab3,font=('monospace',20,'bold'),text="Burger X 50 :- ",bg="black",fg="green").grid(row=2,column=0)
ord_det2=Entry(ab3,textvariable=food2,font=('FontAwesome',30,'bold'),width=10,bg="orange",fg="black")
ord_det2.grid(row=2,column=1)

ord3=Label(ab3,font=('monospace',20,'bold'),text="Drink X 20 :- ",bg="black",fg="green").grid(row=3,column=0)
ord_det3=Entry(ab3,textvariable=food3,font=('FontAwesome',30,'bold'),width=10,bg="orange",fg="black")
ord_det3.grid(row=3,column=1)

ord4=Label(ab3,font=('monospace',20,'bold'),text="Pasta X 70 :- ",bg="black",fg="green").grid(row=4,column=0)
ord_det4=Entry(ab3,textvariable=food4,font=('FontAwesome',30,'bold'),width=10,bg="orange",fg="black")
ord_det4.grid(row=4,column=1)

ord5=Label(ab3,font=('monospace',20,'bold'),text="Wrap X 50 :- ",bg="black",fg="green").grid(row=5,column=0)
ord_det5=Entry(ab3,textvariable=food5,font=('FontAwesome',30,'bold'),width=10,bg="orange",fg="black")
ord_det5.grid(row=5,column=1)

ord6=Label(ab3,font=('monospace',20,'bold'),text="Fries X 30 :- ",bg="black",fg="green").grid(row=6,column=0)
ord_det6=Entry(ab3,textvariable=food6,font=('FontAwesome',30,'bold'),width=10,bg="orange",fg="black")
ord_det6.grid(row=6,column=1)

ord7=Label(ab3,font=('monospace',20,'bold'),text="Biryani X 80 :- ",bg="black",fg="green").grid(row=7,column=0)
ord_det7=Entry(ab3,textvariable=food7,font=('FontAwesome',30,'bold'),width=10,bg="orange",fg="black")
ord_det7.grid(row=7,column=1)

ord8=Label(ab3,font=('monospace',20,'bold'),text="Sandwich X 40 :- ",bg="black",fg="green").grid(row=8,column=0)
ord_det8=Entry(ab3,textvariable=food8,font=('FontAwesome',30,'bold'),width=10,bg="orange",fg="black")
ord_det8.grid(row=8,column=1)

ord9=Label(ab3,font=('monospace',20,'bold'),text="Noodels X 50 :- ",bg="black",fg="green").grid(row=9,column=0)
ord_det9=Entry(ab3,textvariable=food9,font=('FontAwesome',30,'bold'),width=10,bg="orange",fg="black")
ord_det9.grid(row=9,column=1)

ord10=Label(ab3,font=('monospace',20,'bold'),text="MilkShake X 40 :- ",bg="black",fg="green").grid(row=10,column=0)
ord_det10=Entry(ab3,textvariable=food10,font=('FontAwesome',30,'bold'),width=10,bg="orange",fg="black")
ord_det10.grid(row=10,column=1)

ord11=Label(ab3,font=('monospace',20,'bold'),text="Icecream X 50 :- ",bg="black",fg="green").grid(row=11,column=0)
ord_det11=Entry(ab3,textvariable=food11,font=('FontAwesome',30,'bold'),width=10,bg="orange",fg="black")
ord_det11.grid(row=11,column=1)

ord12=Label(ab3,font=('monospace',20,'bold'),text="Spring Roll X 30 :- ",bg="black",fg="green").grid(row=12,column=0)
ord_det12=Entry(ab3,textvariable=food12,font=('FontAwesome',30,'bold'),width=10,bg="orange",fg="black")
ord_det12.grid(row=12,column=1)

ord13=Label(ab3,font=('FontAwesome',40,'bold'),text="TAX  &  TOTAL ",bg="black",fg="green")
ord13.grid(row=13,column=0,columnspan=2)

ord14=Label(ab3,font=('monospace',20,'bold'),text="GST",bg="black",fg="green").grid(row=14,column=0)
ord_det14=Label(ab3,font=('FontAwesome',20,'bold'),text="2.5%",width=10,bg="black",fg="red")
ord_det14.grid(row=14,column=1)

ord15=Label(ab3,font=('monospace',20,'bold'),text="CGST",bg="black",fg="green").grid(row=15,column=0)
ord_det15=Label(ab3,font=('FontAwesome',20,'bold'),text="2.5%",width=15,bg="black",fg="red")
ord_det15.grid(row=15,column=1)

ord16=Label(ab3,font=('monospace',20,'bold'),text="Total ",bg="black",fg="green").grid(row=16,column=0)
ord_det16=Entry(ab3,textvariable=totalx,font=('FontAwesome',30,'bold'),width=10,bg="white",fg="black")
ord_det16.grid(row=16,column=1)

root.mainloop()