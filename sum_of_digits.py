#sum of digits
num = int(input("Enter a 4 digit no. : "))
s=0
n = num%10
q = num//10
s += n
n = q%10
q = q//10
s += n
n = q%10
q = q//10
s += n+q

print("Sum of digits: ",s)