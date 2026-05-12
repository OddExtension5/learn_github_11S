# program to calculate change
c  = int(input("Enter no. of cents: "))
toon = c//200
c = c%200
loon = c//100
c = c%100
quart = c//25
c = c%25
dime = c//10
c = c%10
nick = c//5
c = c%5
pen = c//1

print(f"Toonies:{toon} Loonies:{loon} Quarter:{quart} Dime:{dime} Nickel:{nick} Penny:{pen}")