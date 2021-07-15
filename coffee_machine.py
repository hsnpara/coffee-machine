# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 19:55:07 2017

@author: Hasan PARA
ID:240201046
"""
coffee_list=["Espresso","Cappuccino","Americano","Macchiato","Mocha","Filter","Turkish"]
price_list=[5.50,7.75,7.25,9.50,9.25,5.75,6]
size_list=["Tall","Grande","Venti"]
size_price_list=[0,1,1.5]
revenues=0
cup_counter=0
price=0
customer_counter=0
"""to detect  10th customer"""
while True:    
    coffee=input("What would you like to drink?")
    coffee=coffee.title()
    if coffee=="X":
        break
    """if we enter x to coffee the loop will stop"""
            
    while coffee not in coffee_list:
        
        coffee=input("You entered wrong word to order.Please enter order again! ")
        coffee=coffee.title()
        """check coffee if entered string does not exist in coffee list we ask again user to enter another order with loop"""
    for i in range(len(coffee_list)):
        
        if coffee==coffee_list[i]:
            price=price_list[i]
            """find coffee in coffee list and corresponding price to coffee"""
    size=0
    size_price=0
    if coffee=="Turkish":
        size="Tall"
    while coffee!="Turkish":
        size=input("Which size would you like to drink?")
        size=size.title()       
        """if entered turkish to coffee interpreterdo not enter the loop to detect size and price which corresponding to size"""
        while size not in size_list:
            size=input("You entered wrong word to size.Please enter size again! ")
            size=size.title()
            """check size in size list if entered size does not exist in size list ask again user to enter correct size"""
        if size!=0:
            break
    for a in range(len(size_list)):
        if size==size_list[a]:
            size_price=size_price_list[a]
            """detect which size correspond which price increment"""
    cup_number=input("How many cup would you like to buy?")
    while cup_number.isdigit()==False:
        cup_number=input("You did not entered an integer.Please enter integer! ")
        """check the entered input if it is an integer if the input is not an integer ask user to enter again  """
    customer_counter+=1
    cup_number=float(cup_number)
    price=(price+size_price)*cup_number
    if price>20:
        price=price*(9/10)
    if customer_counter%10==0:
        price=0
        print("You ordered ",cup_number,size," of ",coffee," Congratulations!!!You are 10th customer that's why you do not need pay any bill.")
    else:
        print("You ordered ",cup_number,size," of ",coffee," your bill is ",price," TL.")
    revenues=revenues+price
    cup_counter=cup_counter+cup_number
print("We bought ",cup_counter," cup and earned ",revenues," TL")





















