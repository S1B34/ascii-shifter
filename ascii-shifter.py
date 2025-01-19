import os

def encrypt_decrypt(content, key, mode='encrypt'):
    """
    Encrypt or decrypt the content based on the mode.
    :param content: Text to process
    :param key: Numeric key for encryption/decryption
    :param mode: 'encrypt' or 'decrypt'
    :return: Processed text
    """
    result = ''
    key = key % 10  # Limit the key to a single-digit value
    if mode == 'decrypt':
        key = -key  # Reverse the shift for decryption
    
    for letter in content:
        num = ord(letter)
        num += key
        result += chr(num)
    
    return result


def get_valid_filename():
    """
    Prompt the user to enter a valid file name until the file exists.
    :return: Valid file name
    """
    while True:
        fname = input('Enter the file name: ')
        if os.path.isfile(fname):
            return fname
        print(f"Error: The file '{fname}' does not exist. Please try again.")


def get_valid_key():
    """
    Prompt the user to enter a valid numeric key.
    :return: Valid integer key
    """
    while True:
        try:
            return int(input('Enter the key (numeric): '))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def main():
    print("File Encryption/Decryption Tool")
    print("1. Encrypt")
    print("2. Decrypt")
    
    # Credit Note
    print("\nThis tool was developed by S1B34. Enjoy using it!\n")
    
    # Get user choice
    while True:
        choice = input("Choose an option (1 or 2): ").strip()
        if choice in ('1', '2'):
            break
        print("Invalid choice. Please select 1 for Encrypt or 2 for Decrypt.")
    
    mode = 'encrypt' if choice == '1' else 'decrypt'
    
    # Get valid file name and key
    fname = get_valid_filename()
    key = get_valid_key()

    # Read content from the file
    with open(fname, 'r') as fp:
        content = fp.read()

    # Process content (encrypt or decrypt)
    new_content = encrypt_decrypt(content, key, mode)

    # Write the processed content back to the file
    with open(fname, 'w') as fp:
        fp.write(new_content)
    
    action = "encrypted" if mode == 'encrypt' else "decrypted"
    print(f"File '{fname}' has been successfully {action}.")
    print("\n-- Program Complete --\n")

# Run the script
if __name__ == "__main__":
    main()
