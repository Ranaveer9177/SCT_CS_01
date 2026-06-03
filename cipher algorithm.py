def caesar_encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            # Handle uppercase and lowercase letters
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char

    return result


def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)


# User Input
message = input("Enter your message: ")
while True:
    try:
        shift = int(input("Enter shift value: "))
        break
    except ValueError:
        print("Please enter a valid integer for the shift value.")

# Encryption
encrypted = caesar_encrypt(message, shift)
print("\nEncrypted Message:", encrypted)

# Decryption
decrypted = caesar_decrypt(encrypted, shift)
print("Decrypted Message:", decrypted)