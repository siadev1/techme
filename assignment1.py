# from random import randint

# def computepay():
#     hours = input('enter number of hours')
    
#     hours1 = float(hours)

#     rate = input('enter rate')
    
#     rate1 = float(rate)

#     if hours1<=40:
#         grossPay = hours1 * rate1
#         print(grossPay)
#     elif hours1>40:
#         grossPay = hours1 * rate1
#         grossPay = hours1 * rate1
#         p = (hours1 - 40) * (rate1 * 0.5) 
#         print("your pay is",grossPay + p)

# # print(computepay())

# def grade():
#     grade = randint(1,100)
#     print(grade)
#     if grade<40:
#         print("You score F")

#     elif grade>=40 and grade<50:
#         print("You score D")

#     elif grade>=50 and grade<60:
#         print("You score C")

#     elif grade>=60 and grade<70:
#         print("You score B")

#     elif grade>=70 and grade<=100:
#         print("You score A")

#     else:
#         print('score out of range pls input number between 0 and 100')
# i = 0
# name = input("Pls enter your name")
# while i<=3:
#     print(f'Welcome {name} what would you like to do today?')
#     print("1. Compute pay") 
#     print("2. Check Score")
#     print("3. Exit Program")
#     m=int(input('Enter a number'))
#     match m:
#         case 1: 
#             computepay()

#         case 2:
#             grade()
#             rand = randint(1,100)
            

#         case 3:
#             break
#         case _:
#             print('pls input number within the the range')
# print(f"GoodBye {name}")
max= None
min= None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    # print(num)
    try:
        num1=int(num)
        check=num1
        # max=num1
        # min=num1
    except:
        print("invalid input")
        continue
        
    if max is None:
        
        max=check
        
    if min is None:
        min=check
    
    if check>=max :
        max=check
    
    elif check<=min:
        min=check
    
print("Maximum", max)
print("Minimum", min)
    
    # else:
    #     min=check
        

    # if min is None and check<max :
    #     min=check
    #     # print("hi")


