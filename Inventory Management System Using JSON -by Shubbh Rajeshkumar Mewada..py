import json
import os
import sys
import datetime
from tabulate import tabulate

clear = lambda : os.system('cls')

lines = lambda : print('-'*120)

tab = lambda : print('\t'*5,end='')

empty = lambda : print('\n')

with open(r'C:\Users\NND\PycharmProjects\pythonProject\venv\DataSet.json') as data:

    json_str = data.read()

pyt_data = json.loads(json_str)
data.close()

order = {}

stocks={}

for i in pyt_data:

    for j in pyt_data[i]:

       for k in pyt_data[i][j]:

            key= pyt_data[i][j][k][2]

            value= [k,pyt_data[i][j][k][0],pyt_data[i][j][k][1],pyt_data[i][j][k][2],i,j]

            stocks.update({key:value})

def head():

    while True:

        tab()
        print("!!!We have Everthing that you're looking for!!!")
        empty()

        print('Press 1 for Bakery Products.\n')
        print('Press 2 for Dairy Products.\n')
        print('Press 3 for Fruits and Vegetables.\n')
        print('Press 4 if you want to exit.\n')

        n=int(input())

        if n==1:

            menu('Bakery Products')
            break

        elif n==2:

            menu('Dairy Products')
            break

        elif n==3:

            menu('Fruits And Vegetables')
            break

        elif n==4:

            break

def delitem():

    global order,stocks

    n=int(input('Please Enter the Item Number which you want to Remove: '))

    print(f'Deleting {stocks[n][0]} having quantity {order[n]}.')
    del order[n]

def payment(order1):

    global stocks,order

    print("So here is/are your Orders:")

    header=['Item Number','Item','Price','Quantity','Total '+u"\u20B9"]
    l=[]
    total=0

    for i in order1.keys():

        m=[]
        pyt_data[stocks[i][4]][stocks[i][5]][stocks[i][0]][1]-=order1[i]
        m.append(i)
        m.append(stocks[i][0].title())
        m.append(stocks[i][1])
        m.append(order1[i])
        m.append(u"\u20B9"+str(stocks[i][1]*order1[i]))
        l.append(m)
        total+=stocks[i][1]*order1[i]

    l.append(['NET TOTAL','---->','---->','---->', "\u20B9"+str(total)])
    print(tabulate(l, header, tablefmt="fancy_grid"))
    empty()

    n=input('Do you want to Add or Remove any Item??(Y/N): ').title()

    if n=='Y':

        print('Press 1 to Add New Items.')
        print('Press 2 to Delete New Items.')

        ch=int(input())

        if ch==1:

            head()
            payment(order)

        else:

            delitem()
            payment(order)

    else:

        mobile = int(input('Please Enter your Mobile Number to proceed for Payment: '))

        while len(str(mobile)) != 10:

            print("Please Enter Mobile Number in Proper Format!")
            print("Try Again!")
            mobile = int(input('Please Enter your Mobile Number to proceed for Payment: '))

        json_obj=json.dumps(pyt_data,indent=2)

        with open(r'C:\Users\NND\PycharmProjects\pythonProject\venv\DataSet.json','w') as data:

            data.write(json_obj)
            data.close()

        with open(r"C:\Users\NND\PycharmProjects\pythonProject\venv\Sales.json","r") as sales:

            sales_data= sales.read()
            sales.close()

        sales_data1=json.loads(sales_data)

        str1=str(datetime.datetime.now())[:11]

        if str1 in sales_data1.keys():

            sales_data1[str1].append({"Mobile": mobile, "Items": [[stocks[i][0],order[i]] for i in order.keys()], "Total": total})

        else:

            sales_data1[str1]=[]
            sales_data1[str1].append({"Mobile": mobile, "Items": [[stocks[i][0],order[i]] for i in order.keys()], "Total": total})

        json_obj = json.dumps(sales_data1, indent=2)

        with open(r'C:\Users\NND\PycharmProjects\pythonProject\venv\Sales.json','w') as file:

            file.write(json_obj)
            file.close()

        order={}

        sys.exit('Thank You for Shopping with us,Please Visit Again!!!!')

def menu(category):

    global order,stocks

    print(category.title())
    empty()

    header=['Item Number','Item','Price']

    for i in pyt_data[category]:

        print(i)

        l = []

        for k in pyt_data[category][i]:

            l.append([pyt_data[category][i][k][2],k.title(),u"\u20B9"+str(pyt_data[category][i][k][0])])

        print(tabulate(l, header, tablefmt="fancy_grid"))
        empty()

    print("Enter the Item Number of all the products that you want to purchase, Type Quit to Exit.")

    while True:

        try:

            key=int(input("Enter Item Number: "))
            value=int(input("Enter Quantity: "))

            while value > pyt_data[stocks[key][4]][stocks[key][5]][stocks[key][0]][1] or value<0 :

                print(f'Sorry!!, Stock does not contain {value} quantity of {stocks[key][0].title()}.')
                print(f'In Stock Quantity of {stocks[key][0].title()} is {pyt_data[stocks[key][4]][stocks[key][5]][stocks[key][0]][1]}.')
                value = int(input("Enter Quantity: "))

        except:

            break

        order.update({key:value})

    empty()
    tab()

    n=input("Want to Add Something??\nWould you like to Explore our Other Categories??(Y/N): ").capitalize()

    if n=='Y':
        head()

    else:
        print('Proceeding Towards Payment.....')
        payment(order)

clear()

tab()
lines()

print('!!!Welcome to Inventory Management System!!!')

lines()
head()
