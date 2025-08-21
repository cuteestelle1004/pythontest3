principal=1000
rate=0.05
numyears=10
year=1
while year<=numyears:
    principal=principal*(1+rate)
    print(year,principal)
    year+=2