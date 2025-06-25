def calculate_age():
    name = input("Enter your name: ")
    birth_year = int(input("Enter your birth year (e.g., 2003): "))
    current_year = 2025
    age = current_year - birth_year
    print(f"Thank you {name} \n, your age is {age}.")

# Call the function
calculate_age()