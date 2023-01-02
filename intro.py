# print("Hello ismail")
# name = input('what is your name')
# score = input('check grade')
# score = float(score)

# if score<40:
#     print(f'{name} you have F')

# elif score>=40 and score<50:
#     print(f'{name} you have D')

# elif score>=50 and score<60:
#     print(f'{name} you have C')

# elif score>=60 and score<70:
#     print(f'{name} you have B')

# elif score>=70 and score<=100:
#     print(f'{name} you have A')

# else:
#     print('score out of range pls input number between 0 and 100')

# hours = input('enter number of hours')

# hours1 = float(hours)

# rate = input('enter rate')

# rate1 = float(rate)
# grossPay=0
# if hours1<=40:
#     grossPay = hours1 * rate1
#     print(grossPay)
# elif hours1>40:
#     grossPay = hours1 * rate1
#     p = (hours1 - 40) * (rate1 * 1.5) 
#     print(grossPay + p)

# hours = input('enter number of hours')

# hours1 = float(hours)

# rate = input('enter rate')

# rate1 = float(rate)
# grossPay=0

# def computepay():
#     if hours1<=40:
#         grossPay = hours1 * rate1
#         return grossPay
#     elif hours1>40:
#         grossPay = hours1 * rate1
#         grossPay = hours1 * rate1
#         p = (hours1 - 40) * (rate1 * 0.5) 
#         return grossPay + p
# print(computepay())
# if  hours1<=40:
#     def computepay():
#         grossPay = hours1 * rate1
#         return grossPay

# elif hours1>40:
#     def computepay():
#         grossPay = hours1 * rate1
#         grossPay = hours1 * rate1
#         p = (hours1 - 40) * (rate1 * 0.5) 
#         return grossPay + p
# print(computepay())



    

# hrs = input("Enter Hours:")
# h = float(hrs)
# rate = input('enter rate')
# r=float(rate)
# if  hours1<=40:
#     def computepay():
#         grossPay = hours1 * rate1
#         return grossPay

# elif hours1>40:
#     def computepay():
#         grossPay = hours1 * rate1
#         grossPay = hours1 * rate1
#         p = (hours1 - 40) * (rate1 * 0.5) 
#         return grossPay + p
# p = computepay(h,r)

# def computepay(p):
# hours = input('enter number of hours')

# hours1 = float(hours)

# rate = input('enter rate')

# rate1 = float(rate)
# grossPay=0

# def computepay(hours1, rate1):
#     if hours1<=40:
#         grossPay = hours1 * rate1
#         return grossPay
#     elif hours1>40:
#         grossPay = hours1 * rate1
#         grossPay = hours1 * rate1
#         p = (hours1 - 40) * (rate1 * 0.5) 
#         return grossPay + p

# print(computepay(hours1,rate1)) 


 


# count=0
# ton=0
# while True:
#     num = input("Enter a number: ")
#     if num == "done":
#         break
#     # print(num)
#     try:
#         num=int(num)
#         count=count+1
#         ton=ton+num
#     except:
#         print("invalid input")
#         continue
# print(ton/count)

fname = input("Enter file name: ")
fh = open(fname)

lst =list()
count=0
for line in fh:                             #Loops through the file name ismail.txt and stores all text
    n = line.split()   
                     #This splits all the text in ismail.txt by the commas, thereby having just one word at a time 
    for i in n:
        count=count + 1
        print(i)
#         if i in lst: 
#             continue 
#         lst.append(i)
        
# print("\n", lst)      
# lst.sort()
# print("\n",lst, "\n")
# write output to a txt file
print(count)
with open('ans.txt','w') as f:
    f.write(str(count))




















