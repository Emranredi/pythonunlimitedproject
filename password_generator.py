#Password Generator Project
import random
from cryptography.fernet import Fernet
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# i = 0
# password_letters = ""
# for i in range (nr_letters):
#     password_letters= password_letters +random.choice(letters)

# i = 0
# password_numbers = ""
# for i in range (nr_letters):
#     password_numbers= password_numbers +random.choice(numbers)

# i = 0
# password_symbols = ""
# for i in range (nr_letters):
#     password_symbols= password_symbols +random.choice(symbols)

# print(password_letters + password_numbers + password_symbols)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P


def write_key():
       key = Fernet.generate_key()
       with open("key.txt", "wb") as key_file:
           key_file.write(key)
#    # Call the function to generate the key



i = 0
password_letters = ""
for i in range (nr_letters):
    password_letters= password_letters +random.choice(letters)

i = 0
password_numbers = ""
for i in range (nr_numbers):
    password_numbers= password_numbers +random.choice(numbers)

i = 0
password_symbols = ""
for i in range (nr_symbols):
    password_symbols= password_symbols +random.choice(symbols)
    if password_symbols == "":
        password_symbols = "!"
    elif password_numbers == "@":
        print("Please use a correct choice for symbols.")


password = password_letters + password_numbers + password_symbols
password = list(password)
#password = random.shuffle(password)
random.shuffle(password)






def pas_updter():
    pass_upd=input("You want to add more characters to your or change it password.")
    if pass_upd.lower() == 'yes':
        print("Please run the program again to generate a new password.")
    else:
        print("Thank you for using the password generator.")
        return

def pass_evalut():
    if len(password) < 12:
        print("Your password is weak.")
    elif len(password) < 16:
        print("Your password is moderate.")
    else:
        print("Your password is strong.")

    pass_upd=input("You want to add more characters to your or change it password.")
    if pass_upd.lower() == 'yes':
        print("Please run the program again to generate a new password.")
        pas_updter()
    else:
        print("Thank you for using the password generator.")
        return
    
 
pass_evalut()
password = ''.join(password)
write_key()
print(f"The hard mode password is {password}")










import random
import string
from cryptography.fernet import Fernet

def write_key(file_path="key.key"):
    """Generate and save a symmetric encryption key."""
    key = Fernet.generate_key()
    with open(file_path, "wb") as key_file:
        key_file.write(key)
    print(f"Encryption key generated and saved to '{file_path}'")
    return key

def load_key(file_path="key.key"):
    """Load symmetric encryption key from file."""
    try:
        with open(file_path, "rb") as key_file:
            key = key_file.read()
        return key
    except FileNotFoundError:
        print("Encryption key not found. Generating a new one.")
        return write_key(file_path)

def get_characters(char_set_name, count):
    """Return a random string of length 'count' from character set."""
    if count <= 0:
        return ""
    char_sets = {
        "letters": string.ascii_letters,
        "numbers": string.digits,
        "symbols": "!#$%&()*+"
    }
    chars = random.choices(char_sets[char_set_name], k=count)
    return "".join(chars)

def evaluate_password_strength(password):
    """Evaluate password strength based on length and character variety."""
    length = len(password)
    categories = [
        any(c.islower() for c in password),
        any(c.isupper() for c in password),
        any(c.isdigit() for c in password),
        any(c in "!#$%&()*+" for c in password)
    ]
    variety = sum(categories)

    if length >= 16 and variety == 4:
        return "STRONG"
    elif length >= 12 and variety >= 3:
        return "MODERATE"
    else:
        return "WEAK"

def generate_password(nr_letters, nr_symbols, nr_numbers):
    """Generate a randomized password string."""
    password_chars = (
        get_characters("letters", nr_letters) +
        get_characters("symbols", nr_symbols) +
        get_characters("numbers", nr_numbers)
    )
    password_list = list(password_chars)
    random.shuffle(password_list)
    return "".join(password_list)

def encrypt_password(password, key):
    """Encrypt the password using Fernet symmetric encryption."""
    fernet = Fernet(key)
    encrypted = fernet.encrypt(password.encode())
    return encrypted.decode()

def main():
    print("=== PyPassword Generator ===")

    # Load or generate encryption key upfront
    key = load_key()

    while True:
        try:
            nr_letters = int(input("How many letters would you like in your password? (0-64): "))
            nr_symbols = int(input("How many symbols would you like? (0-32): "))
            nr_numbers = int(input("How many numbers would you like? (0-32): "))
        except ValueError:
            print("Please enter valid integer values.")
            continue

        if nr_letters < 0 or nr_letters > 64 or nr_symbols < 0 or nr_symbols > 32 or nr_numbers < 0 or nr_numbers > 32:
            print("Please enter valid counts within allowed ranges.")
            continue

        if nr_letters + nr_symbols + nr_numbers == 0:
            print("Password length cannot be zero. Please enter positive counts.")
            continue

        password = generate_password(nr_letters, nr_symbols, nr_numbers)
        strength = evaluate_password_strength(password)

        encrypted_password = encrypt_password(password, key)

        print(f"\nGenerated password: {password}")
        print(f"Password strength: {strength}")
        print(f"Encrypted password (safe to store): {encrypted_password}\n")

        regenerate = input("Generate a new password? (y/n): ").strip().lower()
        if regenerate != 'y':
            print("Thank you for using the password generator!")
            break

if __name__ == "__main__":
    main()
