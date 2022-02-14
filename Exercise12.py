nr1 = list(range(10))
range1 = int(input("Enter a number: "))
if range1 > len(nr1) - 1:
    range1b = int(input("Enter a smaller number: "))
    if range1b > len(nr1) - 1:
        range2 = len(nr1) - 1
        print(nr1[2:range2])
    else:
        print(nr1[2:range1b])
else:
    print(nr1[2:range1])

nr2 = ["Berlin", "Hamburg", "Freiburg", "Dresden"]
range3 = int(input("Enter another number: "))
if range3 > len(nr2) - 1:
    range3b = int(input("Enter a smaller number: "))
    if range3b > len(nr2) - 1:
        range4 = len(nr2) - 1
        print(nr2[2:range4])
    else:
        print(nr2[2:range3b])
else:
    print(nr2[2:range3])
