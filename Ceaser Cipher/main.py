alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g',
    'h', 'i', 'j', 'k', 'l', 'm', 'n',
    'o', 'p', 'q', 'r', 's', 't', 'u',
    'v', 'w', 'x', 'y', 'z'
]

def ceaser(original_text, shift_amount, encode_or_decode):
    output_text = ""
    
    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text:
        if letter not in alphabet:
            output_text += letter
        else:
            shifted_position = alphabet.index(letter) + shift_amount

            # to solve the problem if we get out of the list when we shift
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]

    print(f"Here is the result: {output_text}")

# to ask the user if he want to restart the program
should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    ceaser(text, shift, direction)

    restart = input("Type 'yes' if you want to go again, Otherwise type 'no'\n").lower()
    if restart == "no":
        print("Goodbye")
        should_continue = False
