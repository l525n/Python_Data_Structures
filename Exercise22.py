set1 = int(input("Enter the lenght of the first set: "))
Set1 = set(range(set1))
print(Set1)
print("After using pop() method:")
print(Set1.pop())  # can be put directly to print
print("")

set2 = int(input("Enter the lenght of the second set: "))
Set2 = set(range(set2))
print(Set2)
print("After using remove(2) method:")
Set2.remove(2)  # cannot be put directly to print, if so returns None
print(Set2)
print("")

set3 = int(input("Enter the lenght of the third set: "))
Set3 = set(range(set3))
print(Set3)
print("After using add(100) method:")
Set3.add(100)  # cannot be put directly to print, if so returns None
print(Set3)
print("")

set4 = int(input("Enter the lenght of the forth set: "))
Set4 = set(range(set4))
print(Set4)
print("")

duplicates = {1, 2, 2, 3, 4, 5, 5, 6, 6, 7}
print("After duplicate removal:")
print(duplicates)  # duplicates are removed due to the set-brackets in previous
# line
