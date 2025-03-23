# To find if the given number is prime or not
num = int(input("Enter a number "))

if num<=1:
    print("num is not prime")
else:
    i=2
    while i<=num:
        x=num%i
        if x==0:
            print("num is not prime")
            break
        else:
            i=i+1
