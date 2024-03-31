def main():
    # Prompt user to input a CamelCase string
    camel_case = input("Enter a CamelCase string: ")
    
    # Convert the CamelCase string to snake_case
    snake_case(camel_case)

def snake_case(camel_case):
    camel_case1 = ""
    for i in range(len(camel_case)):
        # Check if the character is uppercase
        if camel_case[i].isupper():
            # If uppercase, add underscore followed by lowercase version of the character
            camel_case1 += "_" + camel_case[i].lower()
        else:
            # If lowercase, add the character as it is
            camel_case1 += camel_case[i]
    # Print the snake_case version of the string (remove leading/trailing spaces)
    print(camel_case1.strip())

main()