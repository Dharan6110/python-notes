# To know given number is complex or not

# a=eval(input("Enter value: "))
# if type(a)== float:
#     print("it is float")
# else:
#     print("Not float")

# to know whether given str in 5 letter or not
# s = input("Enter string: ")
# if len(s) == 5:
#     print("Exact 5 letters word")
# else:
#     print("NOt a 5 letters word")

# whether 2 digit or not
# a=int(input())
# if 10 <= a <=99:
#     print('2 - Digit')

# last value of list is string 
# 1,2,3,4,'DHARAN'
# a = eval(input("Enter the list : "))
# if type(a[-1])==str:
#     print("String")
    
# input_list = input("Enter the list separated by spaces: ").split()
# if input_list and isinstance(input_list[-1], str):
#     print("The last element is a string.")
# else:
#     print("The last element is not a string or the list is empty.")

# a = input("Eter the string :")
# b = input("Eter the string :")
# if len(a) == len(b):
#     print(f"{a} * {b} = ",len(a)*len(b))

# if a==b[::-1] :
#     print(a+b)


# check data is single value data typr or Multiple value data type
# Svdt = int,float,bool,complex
# Mvdt = str,list,tuple,dict,set
# data = eval(input("Enter the data :"))
# if (type(data)) in [int,str,float,complex,bool]:
#     print("single value data type")
# else:
#     print("Multiple value data type")

# check data is Capital or not
# char = input("Ennter the string:")
# if 'A'<= char <= 'Z':
#     print("Capital")
# else:
#     print("Not capital")

# try:
#     a = eval(input("Enter the list : "))
#     if type(a[-1])==str and len(a[-1])>=5:
#         print("String")
# except Exception as e:
#     print("Not valid iput")


# whether homogenous or heterogenous 
# a=[1,'Dharan']
# if type(a[0]) == type(a[1]):
#     print("Homogenous")
# else:
#     print("Heterogenous")

# Highest among 5 numbers
# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# num3 = int(input("Enter the third number: "))
# num4 = int(input("Enter the fourth number: "))
# num5 = int(input("Enter the fifth number: "))
# highest_number = max(num1, num2, num3, num4, num5)
# print(f"The highest number among {num1}, {num2}, {num3}, {num4}, and {num5} is: {highest_number}")
    
# a=[12,45,2,33,74,76]
# a.sort()
# print(a)
# print(max(a))
# print(min(a)) 


# num= int(input("enter the value :"))
# if num%5 ==0:
#     if num%2 ==0:
#         print("even")
#     else:
#         print("Odd")
# else:
#     print("Not divisilbe by 5")
 
#  Find vowel or consonant
# char = input("enter the char :")
# if 'A'<=char <= 'Z' or 'a' <= char <='z':
#     if char in 'AEIOUaeiou':
#         print("Vowel")
#     else: print("consanant")
# else:
#     print("Enter alpabet from A to Z or a to z")

# create login id with email and password
# email = 'bdnr91@gmail.com'
# Password = 'Dharan'
# user_id = input("Enter the mail : ")
# Password_id= input("Enter the Password :")
# if email==user_id:
#     if Password==Password_id:
#         print("Welcome to Email..!")
#     else:
#         print("Enter valid Password")
# else:
#     print("Invalid User ID")


# i=1
# while i<=10:
#     print(i,end='')
#     i+=1

# i=1
# while i<=10:
#     print(i**2,end=' ')
#     i+=1
# i=1
# while i<=10:
#     print(i**3,end=' ')
#     i+=1

# i=1
# while i<=10:
#     print(f"3 x { i}  =  ",i*3)
#     i+=1

# m=1
# n = int(input(" enter n :"))
# while m<=n:
#     if m%5 == 0:
#         print(m,end=' ')
#     m += 1

# Sum of "n" natural numbers
# i= 1
# num = int(input("enter a num :"))
# sum = 0
# while i<=num:
#     sum+=i
#     i+=1
# print(sum)

# Prodct of n natural numbers
# i= 1
# num = int(input("enter a num :"))
# Product = 1
# while i<=num:
#     Product*=i
#     i+=1
# print(Product)

# Reverse a number
# num = int(input("Enter num"))
# rev = 0
# while num>0:
#     rem= num%10
#     rev = (rev * 10 ) +rem
#     num //= 10
# # print(rev)

# #Palidnrome of number
# num=int(input("Enter the number:___"))
# rev=0
# temp=num
# while temp!=0:
#     rem = temp%10
#     rev=rev*10+rem
#     temp= temp//10
# if num==rev:
#     print("Palindrome")
# else:
#     print("Not Palindrome")   
    
# REVERSE A GIVEN STRING
# a=input("ENter a string:_________")
# revstr=""
# i=len(a)-1
# while i>=0:
#     revstr=revstr+a[i]
#     i-=1
# print(revstr)
# Define a string

# my_string = "Hello, World!"
# reversed_string = my_string[::-1]
# print(reversed_string)

# na = input("Enter :__")
# rev = na[::-1]
# print(rev)
# if na==rev:
#     print(f"{na} is Palindrome")
# else:
#     print(f"{na} is not palindrome")


#  # Strong number program
 
# a=int(input("Enter the Value:____"))
# temp = a
# sum=0
# while a!=0:
#     rem=a%10
#     fact=1
#     for i in range(1,rem+1):
#         fact*=i
#     sum=sum+fact
#     a=a//10

# if (temp==sum):
#     print(f"{temp} is Strong number")
# else:
#     print(f"{temp} is Not Strong Number")

# # Armstrong or not
# num = int(input("Enter Value: "))
# temp1, temp2,count, sum = num, num,0, 0
# while num != 0:
#     count += 1
#     num = num // 10
# while temp1 != 0:
#     rem = temp1 % 10
#     sum += rem**count
#     temp1 = temp1 // 10
# if sum == temp2:
#     print(f"{temp2} is an Armstrong number")
# else:
#     print(f"{temp2} is not an Armstrong number")


#                OR

# num = int(input("Enter a number: "))
# num_str = str(num)
# num_digits = len(num_str)
# sum_of_digits = sum(int(digit) ** num_digits for digit in num_str)

# if sum_of_digits == num:
#     print(f"{num} is an Armstrong number.")
# else:
#     print(f"{num} is not an Armstrong number.")


# Binary to Decimal
# binary_num = "1101"
# decimal_num = int(binary_num, 2)
# print("Decimal:", decimal_num)

# num = int(input("Eter the number:___"))
# temp=num
# sum=0
# while num!=0:
#     rem = num%10
#     fact=1
#     for i in range(1,rem+1):
#         fact*=i
#     sum=sum+fact
#     num=num//10
# if (sum==temp):
#     print(f"{temp} is strong number")
# else:
#     print(f"{temp} is not strong number")














