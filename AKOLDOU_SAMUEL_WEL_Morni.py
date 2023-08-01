# Day 3
# Basic operators and expression( input and output operators)
# arithmethmic operator
# +, _ ,* ,/, % ,operators
# /n  newline
# //  divide , quotein without remainder 
 # ** exponnation operators 

# Addition 
x = 50 + 50
print(x)
# subtraction
y = 40 - 50
print (y)
# multiplication
z = 20 * 30
print(z)
# modulus
m = 60 % 20
print(m)
 # Exponnetial
n = 10 ** 2
print (n)
 # divide
p = 50 // 3
print(p)
 # divide 
t = 80 / 3
print(t)
# Examles on comparison operator
a = 40
b = 20
if a > b:
    print("a is greater than b")
    print(a > b)

m = 12
n = 100
if  m >= n:
    print('m is not greater or equal to n')
print(m >= n)
cars = {"BMW"," JEEP" "V8"}
if 'BMW' in cars:
    print("BMW is in the list of cars")
    print("JEEP" in cars)
    print ("V8" in cars)
    # Identity operators
    x = 50
    y = 50
    print(x is y)
    print(x is not y)
    print(x == y)
    print(x!= y)
    print( x < y)
    print( x <= y)
    # Bitwise operators
    # Bitwise AND ('&')
    # Bitwise OR ('|')
    # Bitwise XOR ('^')
    # Bitwise left shift ()
    # Bitwise right shift ()

    # Example
    a = 10
    b = 20
    print(a & b)

    #  ASSIGMENT 1
    # create a simple calculator program with a GUI Interface 
    # make the title of the calcuator program with your name ( add, subtract, multiple and divide)
    # learn tkinder 
    import tkinter
    from tkinter import *

    first_number=second_number=None

    def get_digit(digit):
       current = result_label['text']
       new = current + str(digit)
    result_label.config(text=new)

    def clear():
       result_label.config(text='')

    def get_operator(op):
        global first_number, operator
    first_number = int(result_label['text'])
    operator = op
    result_label.config(text='')

    def get_result():
        global first_number,second_number,operator
        second_number = result_label['text']
        
        if operator == '+':
            result_label.config(text=str(first_number + second_number))
        elif operator == '_':
            result_label.config(text=str(first_number - second_number))
        elif opearator == '*':
            result_label.config(text=str(first_number * second_number))
        else :
        if second_number == 0:
            result_label.config(text="Error")
                    else:
                result_label.config(text=str(round(first_number / second_number,2)))



    root = Tk()
    root.title ("AKOLDOU SAMUEL WEL")
    root.geometry("280x380")
    root.resizable(0,0)
    root.configure(bg="black")

    result_label = Label(root,text=0,bg='black',fg='white')
    result_label.grid(row=0,column=0,columnspan= 5 pady=(50,25) sticky='w')
    result_label.config(font=('verdana',30,'bold'))
    








btn1 = Button(root,text='1',bg ='#00a65a',fg ='white',width=5, height=2,command=lambda :get_digit(1) )
btn1.grid(row=3, column=0)
btn1.config(font=('verdana',14 ))


btn2 = Button(root,text='2',bg ='#00a65a',fg ='white',width=5, height=2,command=lambda :get_digit(2))
btn2.grid(row=3, column=1)
btn2.config(font=('verdana',14 ))

btn3 = Button(root,text='3',bg ='#00a65a',fg ='white',width=5, height=2,command=lambda :get_digit(3))
btn3.grid(row=3, column=2)
btn3.config(font=('verdana',14 ))

btn4 = Button(root,text='4',bg ='#00a65a',fg ='white',width=5, height=2,command=lambda :get_digit(4),)
btn4.grid(row=2, column= 0)
btn4.config(font=('verdan3a',14 ))

btn5 = Button(root,text='5',bg ='#00a65a',fg ='white',width=5, height=2 ,command=lambda :get_digit(5),)
btn5.grid(row=2, column=1)
btn5.config(font=('verdana',14 ))

btn6 = Button(root,text='6',bg ='#00a65a',fg ='white',width=5, height=2,command=lambda :get_digit(6),)
btn6.grid(row=2, column=2)
btn6.config(font=('verdana',14 ))

btn7 = Button(root,text='7',bg ='#00a65a',fg ='white',width=5, height=2,command=lambda :get_digit(7))
btn7.grid(row=1, column=0)
btn7.config(font=('verdana',14 ))

btn_clr = Button(root,text='C',bg ='#00a65a',fg ='white',width=5, height=2,command=lambda :clear())
btn_clr.grid(row=4, column=0)
btn_clr.config(font=('verdana',14 ))

btn0 = Button(root,text='0',bg ='#00a65a',fg ='white',width=5, height=2,command=lambda :get_digit(0))
btn0.grid(row=4, column=1)
btn0.config(font=('verdana',14 ))

btn_equals = Button(root,text='=',bg ='#00a65a',fg ='white',width=5, height=2,command=get_result)
btn_equals.grid(row=4, column=2)
btn_equals.config(font=('verdana',14 ))

btn_div = Button(root,text='/',bg ='#00a65a',fg ='white',width=5, height=2,command=lambda :get_operator('/'))
btn_div.grid(row=4, column=3)
btn_div.config(font=('verdana',14 ))

btn8 = Button(root,text='8',bg ='#00a65a',fg ='white',width=5, height=2,command=lambda :get_digit(8),)
btn8.grid(row=1, column=1)
btn8.config(font=('verdana',14 ))

btn9 = Button(root,text='9',bg ='#00a65a',fg ='white',width=5, height=2,command=lambda :get_digit(9))
btn9.grid(row=1, column=2)
btn9.config(font=('verdana',14 ))

btn0 = Button(root,text='0',bg ='#00a65a',fg ='white',width=5, height=2,command=lambda :get_digit(0))
btn0.grid(row=4, column=1)
btn0.config(font=('verdana',14 ))

btn_add = Button(root,text='+',bg ='#00a65a',fg ='white',width=5, height=2,command=lambda :get_operator('+'),)
btn_add.grid(row=1, column=3)
btn_add.config(font=('verdana',14 ))

btn_sub = Button(root,text='_',bg ='#00a65a',fg ='white',width=5, height=2,command=lambda :get_operator('_'),)
btn_sub.grid(row=2, column=3)
btn_sub.config(font=('verdana',14 ))

btn_multiply = Button(root,text='*',bg ='#00a65a',fg ='white',width=5, height=2,command=lambda :get_operator('*'))
btn_multiply.grid(row=3, column=3)
btn_multiply.config(font=('verdana',14 ))






























































root.mainloop()