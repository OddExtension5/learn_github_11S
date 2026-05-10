#bread
n = int(input("Enter no. of loaves: "))
price = 250*n
dis = 0.6*price
sp = price-dis

print(f"PRICE:{price:10.2f}")
print(f"DISCOUNT:{dis:7.2f}")
print(f"TOTAL:{sp:10.2f}")