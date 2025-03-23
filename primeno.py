
# num = int(input("Enter a number "))


# if num<=1:
#     print("num is not prime")
# else:
#     i=2
#     while i<=num:
#         x=num%i
#         if x==0:
#             print("num is not prime")
#             break
#         else:
#             i=i+1


# num = [34, 12, 54, 23, 75, 34, 11]    
      
# def prime_number(number):  
#     condition = 0  
#     iteration = 2  
#     while iteration <= number / 2:  
#         if number % iteration == 0:  
#             condition = 1  
#             break  
#         iteration = iteration + 1  
    
#     if condition == 0:  
#         print(f"{number} is a PRIME number")  
#     else:  
#         print(f"{number} is not a PRIME number")  

# # prime_number(num)  

# for i in range(2,num-1):
#     if num % i == 0:
#         print("not prime")
#         break
# else:
#     print("prime")

#more questions#
#code to add two arrays using for loop

# from array import *
# a = array('i',[1,2,3,4])
# b = array('i',[4,5,6,7])
# for k in range(len(a)):
#     print(a[k],b[k])
# for e in range(len(a)):
#     a[e]=a[e]+b[e]

# for k in range(len(a)):
#     print(a[k],end=",")


# WAC to find the maximum value from an array 'or' #find the second largest number in the array
# from array import *

# arr = array('i',[84,649,400,82,48,129,900,6])

# def largest_in_the_array(arr):
#     first = -1
#     for i in range(len(arr)):
#         if arr[i]>first:
#             first=arr[i]
#     return first

# print(largest_in_the_array(arr))

# #noe for the second largest

# from array import *

# arr = array('i',[12, 35, 1, 10, 34, 1])


# def largest_in_the_array(arr):
#     first,second = arr[0],arr[0]
#     for i in range(len(arr)):
#         if arr[i]>=first:
#             first=arr[i]

#     return first
# # why not sort and find < may also work

# print(largest_in_the_array(arr))

# code is good but does not sastify the requirements
    

# # input in array 
# arr = array("i",[])
# n = int(input("enter length of the array: "))
# for i in range(n):
#     x = int(input("enter array element array: "))
#     arr.append(x)

# print(arr)

# val = int(input(""))
# k=0
# for e in arr:
#     if val==k:
#      print(k)
#      break
#     k +=1

# print(arr.index(val))

#to convert post fix expression to infix no function

from array import*
exppression = input("enter the expression")
arr = array("u",[])
arr.append[exppression[0]]

print(arr)


