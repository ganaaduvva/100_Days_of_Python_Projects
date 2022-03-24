import logo_art

alphabet = [
    'a',
    'b',
    'c',
    'd',
    'e',
    'f',
    'g',
    'h',
    'i',
    'j',
    'k',
    'l',
    'm',
    'n',
    'o',
    'p',
    'q',
    'r',
    's',
    't',
    'u',
    'v',
    'w',
    'x',
    'y',
    'z',
    'a',
    'b',
    'c',
    'd',
    'e',
    'f',
    'g',
    'h',
    'i',
    'j',
    'k',
    'l',
    'm',
    'n',
    'o',
    'p',
    'q',
    'r',
    's',
    't',
    'u',
    'v',
    'w',
    'x',
    'y',
    'z'
]


def caesar(secure_text, shift_amount, cipher_direction):
    text_secured = ''
    if cipher_direction == 'decode':
        shift_amount *= -1
    for char in secure_text:
        if char in alphabet:
            index = alphabet.index(char)
            text_secured += alphabet[index + shift_amount]
        else:
            text_secured += char
    print(f"The {cipher_direction}d text is \"{text_secured}\"")


def starts():
    direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if shift > 26:
        shift = shift % 26
    caesar(secure_text=text, shift_amount=shift, cipher_direction=direction)


print(logo_art.logo)
starts()
repeat = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
while repeat != 'no':
    starts()
    repeat = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
print("Goodbye!!")
