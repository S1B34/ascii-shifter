# File Encryption/Decryption Tool

A simple Python-based tool for encrypting and decrypting text files using ASCII character shifts. This project is designed to help users protect their text-based data with a numeric key.

---

## Features
- Encrypt or decrypt text files with a numeric key.
- Supports simple ASCII-based encryption/decryption.
- User-friendly interface with prompts and validations.
- Handles file validation and error handling.

---

## How It Works
1. The script reads the content of a text file.
2. A numeric key is applied to shift the ASCII value of each character:
   - **Encryption**: Characters are shifted forward by the key.
   - **Decryption**: Characters are shifted backward by the key.
3. The processed content overwrites the original file.

---

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/S1B34/<repository-name>.git
   ```
2. Navigate to the project directory:
   ```bash
   cd <repository-name>
   ```
3. Ensure you have Python 3 installed.

---

## Usage
1. Run the script:
   ```bash
   python <script-name>.py
   ```
2. Follow the on-screen prompts:
   - Enter the name of the text file to encrypt or decrypt.
   - Choose between **encryption** or **decryption**.
   - Provide a numeric key.

Example:
```bash
Enter the file name: example.txt
Enter the key (numeric): 3
```

3. The file will be encrypted or decrypted based on your selection.

---

## Example
### Input File: `example.txt`
```
Hello World!
```

### Encrypt:
- Key: `3`
- Output File Content:
```
Khoor#Zruog$
```

### Decrypt:
- Key: `3`
- Output File Content:
```
Hello World!
```

---

## Limitations
- This tool uses a basic substitution cipher, which is not secure for sensitive or confidential data.
- Characters may fall outside the printable ASCII range depending on the key.

---

## Credits
This tool was developed by **S1B34**.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.
