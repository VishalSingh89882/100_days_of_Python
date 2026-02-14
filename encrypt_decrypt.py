alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
should_continue = True





def caesar(text, shift, encode_or_decode):
        output_text = ""
        if encode_or_decode == "decode":
                    shift *= -1
        for letters in text:
            if letters not in alphabet:
                output_text += letters
            else:
                shifted_index = (alphabet.index(letters) + shift) % 26
                output_text += alphabet[shifted_index]
    
        print(f"The {encode_or_decode}d text is {output_text}")


while should_continue:
     direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
     original_text = input("Type your message:\n").lower()
     original_shift = int(input("Type the shift number:\n"))
     caesar(text=original_text, shift=original_shift, encode_or_decode=direction)
     restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
     if restart == "no":
        should_continue = False
        print("Goodbye")

    


