from tkinter import *
root=Tk()
root.title("simple cal using tkinter")
e=Entry(root,width=50,borderwidth=5)
e.grid(row=0,column=0,columnspan=3,padx=30,pady=50)
# for entering a num
def b_click(num):
    curr=e.get()
    e.delete(0,END)
    e.insert(0,str(curr)+str(num))
def b_add():
#     save the first number 
    first_num=e.get()
    e.delete(0,END)
    global math
    math="add"
    global f_num
    f_num=first_num
    
def b_sub():
    first_num=e.get()
    e.delete(0,END)
    global math
    math="sub"
    global f_num
    f_num=first_num
def b_mul():
    first_num=e.get()
    e.delete(0,END)
    global math
    math="mul"
    global f_num
    f_num=first_num
def b_div():
    first_num=e.get()
    e.delete(0,END)
    global math
    math="div"
    global f_num
    f_num=first_num
def b_equal():
    second_num=e.get()
    e.delete(0,END)
    if math=="add":
        e.insert(0,str(f_num)+"  +  "+str(second_num)+" = "+str(int(f_num)+int(second_num)))
    elif math=="sub":
        e.insert(0,str(f_num)+"  -  "+str(second_num)+" = "+str(int(f_num)-int(second_num)))
    elif math=="mul":
        e.insert(0,str(f_num)+"  *  "+str(second_num)+" = "+str(int(f_num)*int(second_num)))
    elif math=="div":
        e.insert(0,str(f_num)+"  /  "+str(second_num)+" = "+str(int(f_num)/int(second_num)))
# for clear the input
def b_clear():
    e.delete(0,END)
# define buttons
b_0=Button(root,text="0",padx=50,pady=30,command=lambda:b_click(0))
b_1=Button(root,text="1",padx=50,pady=30,command=lambda:b_click(1))
b_2=Button(root,text="2",padx=60,pady=30,command=lambda:b_click(2))
b_3=Button(root,text="3",padx=50,pady=30,command=lambda:b_click(3))
b_4=Button(root,text="4",padx=50,pady=30,command=lambda:b_click(4))
b_5=Button(root,text="5",padx=60,pady=30,command=lambda:b_click(5))
b_6=Button(root,text="6",padx=50,pady=30,command=lambda:b_click(6))
b_7=Button(root,text="7",padx=50,pady=30,command=lambda:b_click(7))
b_8=Button(root,text="8",padx=60,pady=30,command=lambda:b_click(8))
b_9=Button(root,text="9",padx=50,pady=30,command=lambda:b_click(9))
b_plus=Button(root,text="+",padx=50.47,pady=30,command=b_add)
b_minus=Button(root,text="-",padx=52,pady=30,command=b_sub)
b_star=Button(root,text="*",padx=52,pady=30,command=b_mul)
b_divide=Button(root,text="/",padx=52,pady=30,command=b_div)
b_clear=Button(root,text="clear",padx=50,pady=30,command=b_clear)
b_equal=Button(root,text="=",padx=50,pady=30,command=b_equal)
# put the buttons
b_0.grid(row=4,column=0)

b_1.grid(row=3,column=0)
b_2.grid(row=3,column=1)
b_3.grid(row=3,column=2)

b_4.grid(row=2,column=0)
b_5.grid(row=2,column=1)
b_6.grid(row=2,column=2)

b_7.grid(row=1,column=0)
b_8.grid(row=1,column=1)
b_9.grid(row=1,column=2)
b_plus.grid(row=1,column=3)
b_minus.grid(row=2,column=3)
b_star.grid(row=3,column=3)
b_divide.grid(row=4,column=3)
b_clear.grid(row=4,column=1)
b_equal.grid(row=4,column=2)
root.mainloop()
