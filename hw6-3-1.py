# Author RTS 11/12/21

w1 = list(input("Enter a word: "))
w2 = list(input("Enter another word: "))
w1.sort()
w2.sort()

if w1 == w2:
    print("The words are anagrams")
else:
    print("The words are not anagrams")
