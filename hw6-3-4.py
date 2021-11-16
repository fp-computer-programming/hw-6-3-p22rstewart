# Author RTS 11/12/21
lst = list(input("Enter a list of #s or letters seprated by spaces: "))
anwser = input("Would you like the middle or end?: ")
if anwser == "end":
    lst.reverse()
    print(lst[0])
elif anwser == "middle":
    lst.reverse()
    lst.remove(lst[0])
    lst.reverse()
    lst.remove(lst[0])
    print(lst)

#lst_e = lst[::2]
#print(lst_e)
#lst1 = int(lst_e.count())
#lst2 = lst1 / 3
#mid = lst2 * 2
#end = lst2 * 3
#print(lst2)
#lst_1 = lst_e[:1]

#lst_e = (lst[:] % 2 == 0)
#print(lst_e)
