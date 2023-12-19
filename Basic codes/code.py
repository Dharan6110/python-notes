# num = int(input("enter a number :   "))
# fact = 1
# for i in range (1,num):
#     fact += fact*i
# print(f"The factorial of {num} is {fact}")
    
# word = input("Enter the palindrome  ")
# if word[::-1]== word:
#     print("Given string is Palindrome")
# else:
#     print("Given string is not Palindrome")

num = int(input("enter a number :   "))
a,b = 0,1
for i in range(2,num):
    c=a+b
    a,b = b,c
    print(c,end=" ")


