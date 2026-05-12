# tax and tip
c = float(input("Enter cost of meal:"))
tax = 0.1*c
tip = 0.18*(c-tax)
grand = c+tax+tip

print("===============BILL==============")
print("TAX:", "%.2f"%tax)
print("TIP:", "%.2f"%tip)
print("GRAND TOTAL:","%.2f"%grand)
