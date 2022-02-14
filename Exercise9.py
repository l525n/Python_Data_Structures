Range1 = int(input("Enter starting number: "))
Range2 = int(input("Enter ending number: "))
Nr1 = list(range(Range1, Range2))
print(Nr1)
print(len(Nr1))
length2 = int(input("Enter length: "))
Nr2 = list(range(length2))
print(Nr2)
print(len(Nr2))
length3 = int(input("Enter length of list: "))
Nr3 = list(range(length3))
print(Nr3)
print(len(Nr3))


Nr4 = list(
    range(
        int(input("Enter starting number: ")),
        int(input("Enter ending number: ")),
        int(input("Enter Increment: ")),
    )
)
print(Nr4)
