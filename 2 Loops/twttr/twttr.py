# calling the main function
def main():
# Asking for the user input
    user_str=input("Input: ")
# Calling the function to remove vowels
    rev_vowels(user_str)
# Defining the function to remove vowels
def rev_vowels(user_str):
    vowels="aAeEiIoOuU"
    user_str1=""
# checking if vowels is in the string
    for i in user_str:
        if i not in vowels:
# vowel not present then other characters wil store on new string
            user_str1=user_str1+i
        else:
            pass
    print(user_str1)
main()
