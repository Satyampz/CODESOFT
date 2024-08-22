import random
import string

def generate_password(length , complexity):
    if complexity == "1":
        characters = string.ascii_letters
    elif complexity == "2":
        characters = string.ascii_letters + string.digits + string.punctuation  
    else:
        print("Invalid Data")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Strong Password Generator")
    try:
        length = int(input("Enter the length of password: "))
    except ValueError:
        print("Invalid input")
        return

    complexity = input("Choose complexity level(1: Letters, 2: Letters + Digits + Symbols): ")

    password = generate_password(length , complexity)

    if password:
        print("Generated Password:", password)
        print(" Password Generated Successfully !!!")
   
if __name__ == "__main__":
    main()
    exit()
    