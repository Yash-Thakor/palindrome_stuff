word = input("Enter a word: ")
l1 = list(word)
rev = l1.reverse()
word2 = ''.join(l1)
if word == word2:
    print("The word is a palindrome.")
else:
    print("The word is not a palindrome.")