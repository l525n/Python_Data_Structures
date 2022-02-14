range1 = int(input("Choose length of list: "))
nr1 = list(range(range1))
endpoint = int(input("Enter endpoint number: "))
nr2 = nr1[:endpoint]
startpoint = int(input("Enter starting number: "))
nr3 = nr1[startpoint:]
skip1 = int(input("Enter skipping number: "))
nr4 = nr1[startpoint::skip1]
skip2 = int(input("Enter second skipping number: "))
nr5 = nr1[:endpoint:skip2]
print(nr1)
print(nr2)
print(nr3)
print(nr4)
print(nr5)
