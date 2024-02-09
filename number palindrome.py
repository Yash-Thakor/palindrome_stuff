num = int(input("Enter a number: "))
str1 = str(num)
l1 = list(str1)
rev = l1.reverse()
str2 = ''.join(l1)
if str1 == str2:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")