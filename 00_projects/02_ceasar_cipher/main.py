from art import logo
from string import ascii_lowercase

print(logo)

alphabet = list(ascii_lowercase)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
message = input("Type your message: ").lower()
shift = int(input("Type the shift number: "))

def encrypt(shift, message):
    shifted_alphabets = alphabet[shift:]
    shifted_alphabets.extend(alphabet[:shift])
    encrypted_message = []
    for letter in message:
        encrypted_message.append(shifted_alphabets[alphabet.index(letter)])
    return "".join(encrypted_message)

def decrypt(shift, message):
    shifted_alphabets = alphabet[shift:]
    shifted_alphabets.extend(alphabet[:shift])
    decrypted_message = []
    for letter in message:
        decrypted_message.append( alphabet[shifted_alphabets.index(letter)] )
    return "".join(decrypted_message)

print(encrypt(100, "hello"))
# print(decrypt(10, "rovvy"))
print(len(alphabet))

if shift > len(alphabet):
    print(f"Enter shift number which is less than {len(alphabet)}")
elif direction != "encode" or direction != "decode":
    print("Enter a valid operation. eg 'encode' or 'decode")
else:
    if direction == "encode":
        encrypt(shift, message)
    else:
        decrypt(shift, message)

