# Author RTS 11/12/21
lst = list(input("Enter a list of numbers: "))
lst2 = lst.copy()
lst2.sort()
if lst == lst2:
    print("The list is sorted")
else:
    print("The list is not sorted")
