def isPalindrome(input_string):
    if input_string[::-1] == input_string:
        return True
    else:
        return False
    
print(f"'Palindrome' is a Palindrome : {isPalindrome('Palindrome')}")
print(f"'level' is a Palindrome : {isPalindrome('level')}")