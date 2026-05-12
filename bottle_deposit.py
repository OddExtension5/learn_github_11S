# bottle deposit
import locale
locale.setlocale(locale.LC_ALL,'')
a = int(input("No. of containers of volume 1L or less: "))
b = int(input("No. of containers of volume more than 1L: "))

r = 8*a+20*b
r = locale.currency(r , grouping=True)

print("Refund:",r)
