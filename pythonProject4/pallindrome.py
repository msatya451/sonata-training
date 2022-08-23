def  palindrome(number):
    reversed_number=number[::-1]
    if(reversed_number==number):
        return "palindrome"
number=input("enter a number:")
print(palindrome(number))