def check_palindrome():
    user_input = input("Enter a string: ")
    if user_input == user_input[::-1]:
        print("Yes, it is a palindrome")
    else:
        print("No, it is not a palindrome")

# Call the function
check_palindrome()