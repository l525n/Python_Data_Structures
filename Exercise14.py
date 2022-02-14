nr1 = list(range(15))
nr2 = ["apple", "Mango", "Cherry", "Strawberry"]
nr3 = list(range(10))
print(nr1)
print(nr2)
print(nr3)

removal1 = int(input("Enter the index of the item you want to remove from list nr1: "))
nr1.remove(nr1[removal1])

removal2 = int(input("Enter the index of the item you want to remove from list nr2: "))
nr2.remove(nr2[removal2])

removal3 = int(input("Enter the index of the item you want to remove from list nr3: "))
nr3.remove(nr3[removal3])
print(nr1)
print(nr2)
print(nr3)
