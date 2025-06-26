def process_texts():
    text1 = input("Enter first text: ")
    text2 = input("Enter second text: ")
    combined_text = text1 + text2
    char_list = list(combined_text)
    return char_list
  
    


# Call the function
result = process_texts()
print("Character list:", result)  # Optional: Display the list
print("Thank you for using my application")