#CI
p = float(input("Enter deposited amount:"))

for t in range(1,4):
    amt = p + (1+0.04)**t
    amt = round(amt,2)
    print(f"Amount after {t} years is: {amt}")