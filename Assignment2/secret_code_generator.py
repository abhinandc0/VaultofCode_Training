
#Function to encode text by using the Unicode value of letters
def encode_text(text,shift):
    encoded_text = ""
    for char in text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            encoded_char = chr((ord(char) - offset + shift) %26 + offset)
            encoded_text += encoded_char
        else:
            encoded_text += char
    return encoded_text

#Function to decode already encoded text, by utilising encode_text function
def decode_text(text,shift):
    return encode_text(text,-shift)
    #negative symbol is used to convert shift



#Function to use the app. Main function is called when the program is executed,
# which uses other functions
def main():
    print("\n Welcome to Secret Code Generator")
    action = input("Enter your choice, \n 1. Encode message \n 2. Decode message \n")

    if action == "1":
        text = input("Enter message to Encode: \n")
        shift = int(input("Enter shift number: \n"))
        encoded_text = encode_text(text,shift)
        print(f"Encoded text: {encoded_text}")
    elif action == "2":
        text = input("Enter message to Decode: \n")
        shift = int(input("Enter shift number: \n"))
        decoded_text = decode_text(text,shift)
        print(f"Decoded text: {decoded_text}")
    else:
        print("Invalid Input...\nExiting SGC")

main()

