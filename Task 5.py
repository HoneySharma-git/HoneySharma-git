###Task 5 ###

def fact(n):
    i=1
    for i in range(1,n):
        y = i * n
        i = i + 1
        n=y
    return y

x= int(input("Enter a number"))
y = fact(x)
print("Factorial of Number is:",y)
