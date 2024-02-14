def mailling_address():   
    #welcome user 
    #disply user mailling address
    #ask recipient name
    print('name: vaishnavi.s.shinde')
    #ask building name and number
    print('munsi appartment A/303')
    #ask street name
    print('nahur road mulund west')
    #ask city and state
    print('mumbai,Maharashtra')
    #ask pin code
    print('400080')


def welcome_user():
    #welcome user
    #ask user his or her name
    username=input("Enter your name here:")
    #greet user
    print ("Hello" ,username)


def area_of_room():   
    #show the area of room
    #ask user for value of room
    length=int(input('enter the length of the room:'))
    width=int(input('enter the width of the room:'))

    #the area of room
    area=length*width
    #display result
    print('the area of room is' ,area ,'squre feet')


def area_of_feild():    
    #the area of field
    #ask user to value of length and width
    length=int(input('enter the length of land:'))
    width=int(input('enter the width of land:'))

    #the area of acres
    area=length*width/43560
    #display result
    print('the area of field is' ,area, 'area')

def bottle_refund():   
    #the refund amount of collection bottle
    print('welcome to the refund calculator!')
    print('How much you want get back for recycling!')
    value_less=0.10
    value_more=0.25
    #ask user to enter value
    less=int(input('enter the number which is less than 1 litter:'))
    more=int(input('enter the number which is more than 1 litter:'))

    refund=value_less*less+value_more*more
    print('your recycling refund is' ,refund)

def tax_and_tip():    
    #tax and tip
    print('welcome to the friends meal calculator!')
    print('let me help you to find out the tax and tip for your happy meal!')
    tax_rate=0.10
    tip_rate=0.17
    #ask user to enter a cost
    cost=int(input('enter a cost of your happy meal:'))
    #calculate your cost
    tax=cost*tax_rate
    tip=cost*tip_rate
    total=cost+tax+tip
    #display the result
    print('the tax and tip your meal is:' ,tax)

def positive_integers():    
    #calculate the sum of first n positive integers
    #ask number to user
    n=int(input('enter a positive integer:'))

    #the sum
    sum=n*(n+1)/2

    #the result
    print('the sum of the first is:' ,n)
    print('positive ineger is' ,sum)

def widgest_gizmos():    
    #widgest and gizmos
    #ask user the value
    widget=0.075
    gizmos=0.112
    user_widget=int(input('enter the widget weighs:'))
    user_gizmos=int(input('enter the gizmos weighs:'))

    #the total
    total_weight=(widget*user_widget)+(gizmos*user_gizmos)
    #display result
    print('yess your total amount is:' ,total_weight)

def compound_interest():    
    #compund interest
    print('welcome to the compound interest calculator!')
    print('get ready to see your money!')
    print('this tool make you aa s fun!')
    #ask user to enter amount deposited
    user_deposit=int(input('please enter the amount deposited:'))
    interest=0.04
    n=int(input('enter the how many year you want here:'))
    #calculate the values
    for i in range(1,n+1):
        amount=(user_deposit*(1+interest/100)**i)
    print('yess your compound interest is:' ,amount)

def height_units():    
    #height units 
    #convert a height into feet and inches to centimeter
    per_ft=12
    per_in=2.54

    #ask the number to user
    print('enter your height:')
    feet=int(input('number of feet:'))
    inches=int(input('number of inches:'))

    #number of centimeters
    cm=(feet*per_ft + inches) * inches

    #display result
    print('your height is in inches is:' , cm)



def area_volume():    
    #finding the area and volume 
    print('welcome to the area and volume finding calculator:')
    import math

    #ask user for radius
    radius=int(input('enter the radius of circle:'))

    #calculate area and volume
    area=4 * math.pi * radius**2
    volume=(4/3) * math.pi * radius**3

    #display result
    print('area= %.4f.' % (area))
    print('volume=%.4f.' %(volume))

def distance_units():    
    #distance units
    print('welcome to the distance units calculator:')
    #ask user to enter a distance feet
    dis_feet=int(input('please enter your distance feet:'))

    #the distance in inches
    #1 feet=12 inches
    dis_inches=dis_feet * 12

    #the distance in yards
    #1 yard=3 feet
    dis_yard=dis_feet/3

    #the distance in miles
    #1 mile=5280 feet
    dis_mile=dis_feet/5280

    #display result
    print('your distance in inches is %.4f.' % (dis_inches))
    print('your distance in yards is %.4f.' % (dis_yard))
    print('your distance in mile is %.4f.' % (dis_mile))


def order_integers():    
    #the 3 integers
    #ask user for number
    a=int(input('enter the first number'))
    b=int(input('enter the second number'))
    c=int(input('enter the third number'))

    minimum=min (a,b,c)
    maximum=max(a,b,c)
    sec_value=a+b+c-minimum-maximum

    #display result
    print('yess! your sorted order is here:')
    print('' ,minimum)
    print('' ,sec_value)
    print('' ,maximum)
    

#importing tkinter library
import tkinter as tk

#creating a main window 
window=tk.Tk()

#change title
window.title('Vaishnavi shinde')

#size
window.geometry('730x500')

#lable
tk.Label(window,text='Python Projects',font=('Helvetica',24)).place(x=270,y=30)
tk.Label(window,text='Made By: Vaishnavi shinde',font=('Helvetica',12)).place(x=290,y=70)

#button
tk.Button(window,text='mailling address',command=mailling_address).place(x=50,y=130,width=200,height=40)
tk.Button(window,text='welcome user',command=welcome_user).place(x=280,y=130,width=200,height=40)
tk.Button(window,text='area of room',command=area_of_room).place(x=500,y=130,width=200,height=40)
tk.Button(window,text='area of feild',command=area_of_feild).place(x=50,y=180,width=200,height=40)
tk.Button(window,text='bottle refund',command=bottle_refund).place(x=280,y=180,width=200,height=40)
tk.Button(window,text='tax and tip',command=tax_and_tip).place(x=500,y=180,width=200,height=40)
tk.Button(window,text='positive integers',command=positive_integers).place(x=50,y=230,width=200,height=40)
tk.Button(window,text='widgest gizmos',command=widgest_gizmos).place(x=280,y=230,width=200,height=40)
tk.Button(window,text='compound interest',command=compound_interest).place(x=500,y=230,width=200,height=40)
tk.Button(window,text='height units',command=height_units).place(x=50,y=280,width=200,height=40)
tk.Button(window,text='area volume',command=area_volume).place(x=280,y=280,width=200,height=40)
tk.Button(window,text='distance units',command=distance_units).place(x=500,y=280,width=200,height=40)
tk.Button(window,text='order integers',command=order_integers).place(x=50,y=330,width=200,height=40)


#ye agar nai likhoge toh UI nai dikhega
window.mainloop()


# In[ ]:




