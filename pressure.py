#pressure
kp = float(input("Enter pressure in kiloPascal: "))
psi =   0.145038*kp
mmHg = 7.5006*kp
atm = 0.00986923*kp

print(f"PSI:{psi} || mm of Hg:{mmHg} || ATM:{atm}")