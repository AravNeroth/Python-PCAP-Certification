# Created by Arav Neroth on 07/02/2024

import random

alphabet = "abcdefghijklmnopqrstuvwxyz"

def check_message(mes: str) -> bool:
    # conditional checked if each letter in the message is lowercase and contains no special characters
    return all(letter.islower() for letter in mes) and mes.isalpha()

def encode_message(mes: str) -> str:
    # using a blank array, we take the first letter of the message and add it in.
    # then we add 3 random letters, and rinse and repeat. then we 'join' this array into an empty string,
    # which needs to happen as the type to be returned is a string
    encoded_parts = []

    for letter in mes: 
        encoded_parts.append(letter + random.choice(alphabet) + random.choice(alphabet) + random.choice(alphabet))

    return ''.join(encoded_parts)
    
def decode_message(encoded_mes: str) -> str:
    # since our encoded message is just the first letter every 4th place starting from 0
    # we can use python's handy feature of skipping past a certain number of places
    return encoded_mes[::4]

# default constructor 
def main():
    message = ""
    encoded_message = ""
    decoded_message = ""

# lazy while loop that will infinitly loop, with a 'break' ending the program
    while True:
        # very basic UI
        print("\nChoose '1' to encode a message")
        print("Choose '2' to decode a message")
        print("Choose '3' to print all messages")
        print("Choose '4' to exit")
        
        choice = input("Your Choice: ")

        if choice == '1':
            while True:
                print("* Message Cannot Contain Special Characters, Capitals, Or Numbers *")
                message = input("Message To Be Encrypted: ")

                if check_message(message):
                    encoded_message = encode_message(message)
                    print("Encoded Message: " + encoded_message)
                    break
                else:
                    print("Invalid message. Please try again.")
        
        elif choice == '2':
            if not encoded_message:
                print("No Encoded Message Stored. Please Encode One.")
            else:
                decoded_message = decode_message(encoded_message)
                print("Decoded Message: " + decoded_message)
        
        elif choice == '3':
            print("Original Message: " + message)
            print("Encoded Message: " + encoded_message)
            print("Decoded Message: " + decoded_message)
        
        elif choice == '4':
            break

        else:
            print("Invalid choice. Please select a valid option.")

    print("Message Manager Closed.") 




if __name__ == "__main__":
    main()
