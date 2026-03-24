from art import logo
from string import ascii_lowercase

print(logo)

def encrypt_decrypt(shift, direction, message):
    cipher = ""
    if direction == "encode" or direction == "decode":    
        for i in message:
            if direction == "encode":
                shifted_index = alphabet.index(i) + shift
            else:
                shifted_index = alphabet.index(i) - shift
            shifted_index %= len(alphabet)
            cipher+=alphabet[shifted_index]
        print(f"Your {direction}d message is {cipher}")
    else:
        print("Enter valid option.")


exit = False

while not exit:
    alphabet = list(ascii_lowercase)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
    message = input("Type your message: ").lower()
    shift = int(input("Type the shift number: "))

    encrypt_decrypt(shift, direction, message)

    proceed_choice = input("Proceed with the ceaser cipher? (Type yes to proceed and no to quit): ")
    if proceed_choice == "yes":
        exit = False
    else:
        exit = True
