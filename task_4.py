def bank():
    n = int(input("Type budget: "))
    years = int(input("Amount of year"))
    creditwibsotok = 1 / 10
    amountmoney = n * creditwibsotok
    i = 0
    while years > i:
        n += amountmoney
        i += 1

    print(round(n, 2))

print(bank())